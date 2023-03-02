from django.shortcuts import render
from . import templates, static, util
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, FileResponse
from django.shortcuts import redirect
from .models import *
import json, csv, io, xlsxwriter, math, os
from django.db.models import Avg, Max, Min, Sum, Subquery, OuterRef, FloatField, CharField, IntegerField
from itertools import chain
from django.db.models.functions import Cast
import pandas as pd
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from capstone.settings import EMAIL_HOST_USER
from django.contrib import messages
from datetime import date, datetime
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template, render_to_string
from django.core.files.storage import FileSystemStorage

#Common variables
counties = util.get_data()["Counties"]
categories = util.get_data()["Categories"]
status = util.get_data()["Status"]
zones = util.get_data()["Zones"]
counties_dict = util.get_county()



# Create your views here.

def index(request):
    return render(request, "company/home.html")

def login_view(request):
    
    if request.method == "POST":
        n = request.POST.get('next', '')
        if n.rsplit('/', 1)[-1] == "login":
            n = reverse("company:index")
            
        #Authonticate the reseceived information
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(n) 
        else:
            return render(request, "company/login.html", {
                "message": "Invalid username and/or password."
            })

    return render(request, "company/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("company:login"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "company/register.html", {
                "message": "Passwords Don't match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "company/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("company:index"))

    return render(request, "company/register.html")

def products(request):
    products = Price.objects.all()
    suppliers = Supplier.objects.all()

    if request.method == "POST":
        #Collecting and Sorting Data
        rawdata = json.loads(request.body)
        newProduct = rawdata.get("newProduct")
        
        supplierId = int(newProduct.pop("supplier", None))
        price = int(newProduct.pop("productPrice", None))

        #Creating New Product
        new_product = Product(**newProduct)
        new_product.save()

        #Creating A price object
        supplier = suppliers.get(pk=supplierId)
        price = Price(price = price, product = new_product , supplier=supplier)
        price.save()

        response_data = {
            "message": "Product Stored Successfully.",
            "id": new_product.id
        }
        return JsonResponse(response_data, status=201)
    
    return render(request, "company/products.html",{
        #To display the products in reverse order, to place the recently added product on top
        "products": products[::-1],
        "suppliers": suppliers,
        "categories": categories
    })

def fetchItems(request):
    products = list(Product.objects.all().values())
    suppliers = list(Supplier.objects.all().values())
    jobs = list(Job.objects.all().values())
    prices = list(Price.objects.all().values())
    counties = json.dumps(counties_dict)
    data = json.dumps(util.get_data())

    response_data = {
        "products": products,
        "suppliers": suppliers,
        "jobs": jobs,
        "prices": prices,
        "counties": counties,
        "data": data
    }

    return JsonResponse(response_data, status=201)

def productDetail(request,id):
    products = Product.objects.all()
    if products.filter(pk=id).exists():
        product = Product.objects.get(pk=id)
        prices = product.productPrice.all()
        suppliers = Supplier.objects.all()
        
        if request.method == "GET":
            return render(request, "company/productdetails.html",{
                "product": product,
                "prices":prices,
                "suppliers": suppliers,
                "categories": categories
            })

        elif request.method == "PUT":
            data = json.loads(request.body)
            editedProduct = data.get("editedProduct")
            product.nameP = editedProduct["nameP"]
            product.brand = editedProduct["brand"]
            product.category = editedProduct["category"]
            product.weight = editedProduct["weight"]
            product.size = editedProduct["size"]
            product.description = editedProduct["description"]
            product.save()

            response_data = {
                "message": "Product Edited Successfully.",
                "id": product.id
            }
            return JsonResponse(response_data, status=201)

        else:
            id = json.loads(request.body)
            Product.objects.get(pk=id).delete()
            
            response_data = {
                "message": "Product Deleted."
            }
            return JsonResponse(response_data, status=201)
    else:
        return HttpResponse("Product Does Not exist")

def productPrice(request):
    if request.method == "POST":
        data = json.loads(request.body)
        newPrice = data.get("newPrice")
        product = Product.objects.get(pk=newPrice["product"])
        supplier = Supplier.objects.get(pk=newPrice["supplier"])
        price = Price(price = newPrice["price"], product = product , supplier=supplier)
        price.save()

        #Updating the corresponding supply items if any
        util.updateSupplies(price)
        

        response_data = {
            "message": "Price Added.",
            "id": price.id
        }
        return JsonResponse(response_data, status=201)
    elif request.method == "PUT":
        #Getting updated price
        data = json.loads(request.body)
        editPrice = int(data.get("editPrice"))
        priceId = int(data.get("priceId"))
        
        #Updating the price with the new value
        price = Price.objects.get(pk=priceId)
        price.price = editPrice
        price.save()

        #Updating the corresponding supply items if any
        util.updateSupplies(price)

        response_data = {
            "message": "Price Edited."
        }
        return JsonResponse(response_data, status=201)

    else:
        #Getting data from json
        data = json.loads(request.body)
        priceId = int(data.get("priceId"))
        
        #Getting the price to delete
        price = Price.objects.get(pk=priceId)
        product = price.product
        prices = product.productPrice.all()
        if prices.count()  > 1:
            #Updating the corresponding supply items if any
            util.updateSupplies(price)
            #Deleting the price
            price.delete()

            response_data = {
                "message": 1
            }
            return JsonResponse(response_data, status=201)
        else:
            response_data = {
                "message": 0
            }
            return JsonResponse(response_data, status=201)

def suppliers(request):
    suppliers = Supplier.objects.all()
    suppliers = suppliers.order_by("-id").all()

    #Paginating the suppliers
    paginator = Paginator(suppliers, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "company/suppliers.html",{
        # "suppliers" : suppliers
        "suppliers" : page_obj
    })

def supplierForm(request):
    if request.method == "POST":
        data = json.loads(request.body)
        newSupplier = data.get("newCompany")
        newSupplier.pop("county")
        new_supplier = Supplier(**newSupplier)
        new_supplier.save()
        
        response_data = {
            "message": "Supplier Added.",
            "id": new_supplier.id
        }
        return JsonResponse(response_data, status=201)
    else:
        return render(request, "company/companyForm.html", {
            "mode": "Supplier",
        })

def supplierDetail(request, id):
    supplier = Supplier.objects.get(pk=id)
    personnel = supplier.personnel.all() 
    products = Price.objects.filter(supplier=supplier)

    if request.method == "PUT":
        data = json.loads(request.body)
        ES = data.get("updateCompany")

        supplier.nameC = ES["nameC"]
        supplier.address = ES["address"]
        supplier.email = ES["email"]
        supplier.contact = ES["contact"]
        supplier.zone = ES["zone"]
        supplier.location = ES["location"]
        supplier.save()

        response_data = {
            "message": "Supplier Edited."
        }
        return JsonResponse(response_data, status=201)

    elif request.method == "DELETE":
        supplier.delete()

        response_data = {
            "message": "Supplier Deleted."
                
        }
        return JsonResponse(response_data, status=201)

    else:
        context = {
            "supplier": supplier,
            "personnel": personnel,
            "zones": zones,
            "products": products
        }

        return render(request, "company/supplierDetails.html", context)

def personnel(request):
    if request.method == "POST":
        data = json.loads(request.body)
        person = data.get("newPerson")

        name = person["name"]
        phone = person["phone"]
        email = person["email"]
        companyId = person["companyId"]

        company = Company.objects.get(pk=companyId)

        p = Personnel(nameC = name, contact=phone, email = email, company = company)
        p.save()

        response_data = {
            "message": "Personnel Successfully Added",
            "id": p.id
        }
        return JsonResponse(response_data, status=201)
    
    elif request.method == "PUT":
        data = json.loads(request.body)
        editperson = data.get("updatePerson")
        personId = data.get("personId")
        person = Personnel.objects.get(pk=personId)

        person.nameC = editperson["name"]
        person.contact = editperson["phone"]
        person.email = editperson['email']
        person.save()

        response_data ={
            "message": "Personnel Successfully Updated",
            "id": person.id
        }
        return JsonResponse(response_data, status=201)

    else:
        data = json.loads(request.body)
        personId = data.get("personId")
        Personnel.objects.get(pk=personId).delete()

        response_data ={
            "message": "Personnel Successfully Deleted"
        }
        return JsonResponse(response_data, status=201)


def clients(request):
    clients = Client.objects.all()
    clients = clients.order_by("-id").all()
    #Paginating the clients
    paginator = Paginator(clients, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "company/clients.html",{
        "clients": page_obj
    })

def clientForm(request):
    if request.method == "POST":
        data = json.loads(request.body)
        newClient = data.get("newCompany")
        newClient.pop("zone")
        new_Client = Client(**newClient)
        new_Client.save()
        
        response_data = {
            "message": "ClientAdded.",
            "id": new_Client.id
        }
        
        return JsonResponse(response_data, status=201)
    else:
        return render(request, "company/companyForm.html", {
            "mode": "Client",
            "counties": counties
        })

def clientDetail(request, id):
    client = Client.objects.get(pk=id)
    personnel = client.personnel.all()
    jobs = client.client.all()

    if request.method == "PUT":
        data = json.loads(request.body)
        editDetails = data.get("updateCompany")
        client.nameC = editDetails["nameC"]
        client.address = editDetails["address"]
        client.email = editDetails["email"]
        client.contact = editDetails["contact"]
        client.county = editDetails["county"]
        client.location = editDetails["location"]
        client.save()

        response_data = {
            "message": "Client Edited."
        }
        return JsonResponse(response_data, status=201)
    
    elif request.method == "DELETE":
        client.delete()

        response_data = {
            "message": "Client Deleted."
        }
        return JsonResponse(response_data, status=201)

    context = {
        "client": client,
        "personnel": personnel,
        "counties": counties,
        "jobs": jobs
    }

    return render(request, "company/clientDetails.html", context)

def jobs(request):
    if request.method == "POST":
        data = json.loads(request.body)
        j = data.get("newJob")
        client = Client.objects.get(pk = j["client"] )
        newJob = Job(code = j["code"], client = client)
        newJob.save()
        response_data = {
            "message": "Job Added.",
            "id": newJob.id
        }

        return JsonResponse(response_data, status=201)
    
    jobs = Job.objects.all()
    products = Price.objects.all()
    suppliers = Supplier.objects.all()
    clients = Client.objects.all()

    context = {
        "jobs": jobs[::-1],
        "products": products[::-1],
        "suppliers": suppliers,
        "clients": clients,
    }

    return render(request, "company/jobs.html", context)

@login_required(login_url="company:login")
def jobDetail(request, id):
    job = Job.objects.get(pk=id)
    supplies = job.jobItem.all()

    if request.method == "DELETE":
        job.delete()

        return JsonResponse({"message": "Job Deleted"}, status = 201)
    elif request.method == "PUT":
        data = json.loads(request.body)
        updated_status = data.get("status")
        current_status = job.status
        if status.index(str(updated_status)) > status.index(str(current_status)):
            job.status = updated_status
            job.save()
        return JsonResponse({"message": "Status Updated"}, status = 201)

    # if "message" not in request.session:
    #     request.session['message'] = ''
    # message = request.session['message']

    elif request.method == "POST":
        data = json.loads(request.body).get("data")
        value = data["value"]

        if data["type"] == "cheque":
            job.cheque = value
            job.save()
        else:
            job.lpo = value
            
            job.save()

            #Generating the notes 
            notes = Notes.objects.all()
            x = datetime.now()
            y = x.strftime("/%m/%Y")

            if notes:
                if not notes.filter(job = job).exists() :
                    last = notes.last()
                    sub1 = last.deliveryNo[3:-2]
                    if y == sub1:
                        sub2 = int(last.deliveryNo[-1]) + 1
                    else:
                        sub2 = 1
                    util.create_notes(job, y, sub2)
            else:
                util.create_notes(job, y, 1)

        return JsonResponse({"message": "Data Saved"}, status = 201)

    context = {
        "job": job, 
        "status": status,
        "supplies": supplies,
        #"message": message
    }

    return render(request, "company/jobDetails.html", context)

def supplies(request, id):
    if request.method == "POST":
        data = json.loads(request.body)
        newSupply = data.get("newSupply")

        product = Product.objects.get(pk = newSupply["product"])
        #Getting the min and max prices
        prices = Price.objects.filter(product = product)
        minBuying = prices.get(price = newSupply['minPrice'])
        maxBuying = prices.get(price = newSupply['maxPrice'])

        #Fetching the job instace
        job = Job.objects.get(pk = newSupply["job"] )

        new_supply = Supply(
            qty = newSupply["qty"],
            price = newSupply["price"],
            minBuying = minBuying,
            maxBuying = maxBuying,
            total = newSupply["total"],
            product = product,
            job = job,
        )
        new_supply.save()

        #Updating the job value
        util.updateJobValue(job)

        response_data = {
            "message": "Supply Added.",
            "jobValue": job.value
        }
        return JsonResponse(response_data, status=201)    

    elif request.method == "PUT":
        data = json.loads(request.body)
        editedSupply = data.get("editedSupply")
        s = Supply.objects.get(id=editedSupply["id"])
        s.qty = editedSupply['qty']
        s.price = editedSupply['price']
        s.total = editedSupply['total']
        s.save()

        #Update the jobvalue after edit
        util.updateJobValue(s.job)

        response_data = {
            "message": "Supply Edited."
        }
        return JsonResponse(response_data, status=201)

    else:
        s = Supply.objects.get(id=id)
        s.delete()

        #Update the job value after delete
        util.updateJobValue(s.job)

        response_data = {
            "message": "Supply Deleted.",
            "jobValue": s.job.value
        }
        return JsonResponse(response_data, status=201)




def getItems(request, type, id):
    job = Job.objects.get(pk=id)
    products = Product.objects.all()
    supplies = job.jobItem.all()
    notes = "" if not Notes.objects.filter(job=job).exists() else Notes.objects.get(job=job)
   
    #Variables to render to the html page
    context = {
        "job": job, 
        "supplies": supplies,
        "notes": notes,
    }

    #Joining the subqueries
    subquery1 = products.filter(id=OuterRef('product_id'))
    subquery2 = Price.objects.all().filter(id=OuterRef('minBuying_id'))
    combined = supplies.annotate(
        category = Cast(Subquery(subquery1.values('category')[:1]), output_field=IntegerField()),
        nameP = Cast(Subquery(subquery1.values('nameP')[:1]), output_field=CharField()),
        brand = Cast(Subquery(subquery1.values('brand')[:1]), output_field=CharField()),
        buying = Cast(Subquery(subquery2.values('price')[:1]), output_field=IntegerField()),
        supplier = Cast(Subquery(subquery2.values('supplier')[:1]), output_field=IntegerField()),
        bt = (Cast('qty',output_field=IntegerField()) * Cast('buying',output_field=IntegerField())),
    )
    
    if type == "print_rfq_csv":
       # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename = {job.code}.csv'
        writer = csv.writer(response)
        writer.writerow(["Product","brand","qty", "Buying","Selling", "Buying total", "Selling Total"])
        total_buying = 0
        total_selling = 0
        for s in supplies:
            writer.writerow([s.product.nameP, s.product.brand, s.qty, s.minBuying.price, s.price,(s.minBuying.price*s.qty), s.total])
            total_buying += (s.minBuying.price*s.qty)
            total_selling += s.total
        writer.writerow(["","","","","Grand Total", total_buying, total_selling, "Difference",(total_selling-total_buying)])
        return response 

    elif type == "check_analysis":
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = f'attachment; filename = {job.code}.xlsx'

        columns_heads = ["Product","brand","qty", "Buying","Selling", "Buying total", "Selling Total"]
        rows = combined.values_list('nameP', 'brand', 'qty', 'buying', 'price', 'bt', 'total')

        output = util.create_xlsx(combined, columns_heads, rows)
        
        response.write(output.getvalue())

        return response

    elif type == "invoice_request":
        
        suppliers_list = combined.values_list('supplier', flat=True).distinct() #This gives a value to get an object remove flat=True
        
        for i in suppliers_list:
            supplier = Supplier.objects.filter(id=i)
            items = combined.filter(supplier = (i))  
            columns_heads = ["Product","brand","qty", "Total","Price"]
            rows = combined.values_list('nameP', 'brand', 'qty')

            output = util.create_xlsx(items, columns_heads, rows)
            
            #Sending mail
            subject, from_email, to = 'Django Test', EMAIL_HOST_USER, supplier.values_list('email', flat=True)[0]
            text_content = 'Could you kindly furnish us with an invoice of the attached items.'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach('supplies.xlsx',output.getvalue(), 'application/vnd.ms-excel')
            msg.send()

        messages.success(request, 'Email Sent.')
        return redirect(reverse("company:jobDetail", kwargs={'id':id}))

    elif type == "print_rfq_pdf":
        a = [{"title":"RFQ", "body":"Quotation for RFQ"}]
        response = util.create_pdf(context, a)
        return response

    elif type == "print_DI":
        a = [{"title":"Invoice", "body":"Invoice"}, {"title":"Delivery", "body":"Delivery Note"}]
        response = util.create_pdf(context, a)
        return response

    elif type == "print_receipt":
        a = [{"title":"Receipt", "body":"Receipt"}]
        response = util.create_pdf(context, a)
        return response
