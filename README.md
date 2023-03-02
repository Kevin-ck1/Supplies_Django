# CS50 PROJECT

The project was created as a capstone project for CS50w - Web Programming with Python and JavaScript course, but apart from that it has real time uses. In short the project is a web application, that helps **Suppliers** to keep track of their products, supplies, suppliers and clients.

 ## Project Description/ Background

I got the inspiration of the project as I was helping my mother keep records in her supply's company. 

In Kenya most of the institutions that require steady supply of products employ a system of supplies popularly referred as **RFQs**.

**RFQs** (Request for Quotations) can be defined as a process wherein an enterprise asks a set of potential suppliers or service providers to submit their price quotations and stand a  chance to supply or provide goods or services. Once the enterprise  receives the price quotations, it can choose the vendor that best  matches its criteria for the goods or services.(https://www.gep.com/knowledge-bank/glossary/what-is-request-for-quotation)

RFQs are essential for businesses that require a consistent supply of products with set specifications and standard, every time. Therefore,  suppliers or service providers that are better organized usually have  higher chances to of creating a streamlined RFQ that offers the best  match the requirements of an enterprise, every time.

The  *RFQ Process* has various steps as listed below:

* Awarding of the RFQ - In this steps, an Institution (In our case - our client) sends an RFQ to the supplier (In this case us); or the Supplier can check the Clients bulletins for any available RFQs and request to be given a copy if any.  In this step the *RFQ* contains a list of items that the client requires.
* Filling of the RFQ - Once the RFQ is received, the Supplier should fill in the item prices as per their inventory, but in our case since the company deals with general products from different fields, the company does not keep stock of goods. Hence to fill in the prices we obtain the prices from our partner suppliers, whom we have worked with previously.
* Submitting of the RFQ - Once the RFQ is filled, it is submitted to the Client's tender box in a sealed hard-copy.
* Issuing of **LPO** - Once a supplier has won the bid, in respective with other bidders, the Supplier is issue with an **LPO (Local Purchase Order)** , which is a document to show proof of wining the supply bid and it also contains the final list of products to be purchased and the quantity required. Note that it also contains the prices as they were quoted in the RFQ.
* Buying and Delivering of the products - Once you receive the LPO, which acts as a security, we can buy the goods from our suppliers and transport them to the institutions. During delivery, the institution is to be issued with a **Delivery Note** and also **Invoice** for payment request.
* Payment - Once the goods have been verified and the invoice issued, payment is made to the Supplier(us) via cheque, and upon the cheque clearing, a **Receipt** is issued to the client.

The project therefore tries to make the above steps easier, with the project we cable of:

1. Feeding and keeping track of our suppliers details.
2. Feeding and keeping track of our clients(institutions) details.
3. Feeding and updating the products and its prices.
4. Preparing the RFQ prices and generating an RFQ pdf as the hardcopy.
5. Generating excel sheets for the use of comparison of the buying and selling prices of products in a particular job order(RFQ).
6. Updating the the RFQs products and quantity per per product with respect to the received RFQ.
7. Generating of Delivery Notes and  Invoice Notes with the delivery of the requested products, and the subsequent issuing of the Receipt after payment.



## Distinctiveness and Complexity

Below are some of the functions that make the application distinctive from others:

* With the application we are able to download data from the database into presentable format in the form of a `.csv` or `.xlsx` file.
* Also the application is able to render a HTML page with styling into a pdf document, which is downloadable. The pdf documents can also be merged.
* The application can also be used to send excel documents as email attachments to multiple entities at the same time. With excel contain different sets of data.
* With the application we are able to retrieve data from an external excel sheet, and save the data to be used in various parts of the application.
* As for complexity in styling, some pages of the application incorporate modal classes, for floating divs.

## Build Status
Development



## Tech/Framework used 

For the project the languages/frameworks used are as per directed in the CS50w requirements, which are ;

1. python 
2. Django - Python frame used as the backend of the application. Django templates were in help in the creating of the HTML pages.
3. HTML, CSS, JavaScript for the front end. Most of the styling for the project incorporated the use of Bootstrap classes.
4. mySql - As the database



## Requirements

Before starting up the project, some modules/library/applications are required. Note that the application was developed and tested using a windows machine, hence the below listed requirements are tailored to a *windows machine*.

* **python** - the latest version of python is required. As of the writing of this  document, the version used in the application is `Python 3.10.5`. 

* **pip** - As of writing, the version of pip used is `pip-22.2.2`. To ensure the latest version is installed `python -m pip install --upgrade pip`

* **Polymophic** - It simplifies using inherited models in Django. To install the module on the console run `pip install django-polymorphic`. We follow-up by adding the `polymorphic` key word into the `INSTALLED_APPS`, in the `settings.py` file in the root directory of the project.

  ```python
  INSTALLED_APPS = [
      'company',
      'polymorphic',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```



* **pandas** - Its a data analysis and manipulation tool. To install it on the console run `pip install pandas`

* **openpyxl** - It is a library to read or write excel files. To ensure functioning of pandas in extracting data from external excel file, ensure that the latest version of *openpyxl* is used. On the console run `pip install openpyxl`.

* **xlsxwriter** - It is a module used in the writing of worksheets in the format *.xlsx*. To install the latest module in the console run `pip install XlsxWriter`.

* **PyPDF2** - It is a pdf library used in the project for merging of pdf files. To install it, run `pip install PyPDF2`. Also to use the library ensure that **typing_extensions** are up to date, we do so by running `python -m pip install typing-extensions --upgrade`.

* **WeasyPrint** -  It used to turn HTML pages into pdf. To make weasyprint run on a windows machine.

  * Ensure latest python is installed

  * Download and install latest version of **GTKS installer** -  https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases

  * On the console run `python -m pip install weasyprint`

    For detailed instruction of *WeasyPrint*  installation visit https://doc.courtbouillon.org/weasyprint/stable/first_steps.html

* **App passwords** - It is a 16-digit passcode that gives a less secure app or device permission to access your Google Account. In this case it is used to grant Django the access of a gmail email account. To set up check https://support.google.com/accounts/answer/185833?hl=en

  The *gmail*  address together with the *app password* are then feed-in to the *settings.py* file. The *gmail address* as the `EMAIL_HOST_USER` and the *password* as the `EMAIL_HOST_PASSWORD`. An example of the Gmail_Email settings is as shown below:

  ```python
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_HOST = 'smtp.gmail.com'
  EMAIL_PORT = 587
  EMAIL_HOST_USER = 'kevin.dev254@gmail.com'
  EMAIL_HOST_PASSWORD = '16_digit passcode goes here'
  EMAIL_USE_TLS = True
  EMAIL_USE_SSL = False
  ```

  **Note** - For the purpose of submitting this project, the above code(i.e using google sever to send mail) is not used. But the code is available in the *settings.py* file, it is just commented out. To use it, uncomment the bit of code and use a *gmail* account with *app password* , with the *address* as the `EMAIL_HOST_USER` and the *password* as the `EMAIL_HOST_PASSWORD`.  While uncommenting the code, comment the section for `# Email Settings - local host` , which contains code that sends the mail through the local sever host.

## Running the Application

With all the requirements properly installed, run the below commands simultaneously in two separate consoles. 

* `python manage.py makemigrations` then `python manage.py migrate` - Note, install all the modules before caring out the migrations.

* `python manage.py runserver` - This opens a server an provides a link to that leads to the displayed app.
* `python -m smtpd -n -c DebuggingServer localhost:1025` - Opens up server for the sending of the attached email.

Note that the above commands are for running the app in development mode in a *windows machine*.

## Code Explanation

This section explains the functionality of the application by page, it also explain the contents of the files used in creating the pages' functionality.

With the initialization of the project, the standard Django files were created e.g the views.py, url.py, settings.py e.t.c, which contains some of the applications logic.

Apart from the Django files, two extra files folder, with respective contents, are included in the project. They include the **templates** folder which houses the *html templates* and the **static folder** which holds the static files i.e the JS files and the css files for the application. Also housed in the static folder is a **data** folder housing an excel sheet with some data which is imported as variables into the application.

In the explanation of the files, this documentation will explain part of the files code and functionality. Using the following criteria in explanation: - The functionality of the app will be described with the various pages of the application. In each page, this documentation will state the files used and description of the code that enables the page to properly render onto the browser.

### Common files

This are some of the files that are common throughout the application

* **layout.html** - It incorporates the Django template engine to. It is the base template of the application where the other templates `extends` from it. It contains the nav-bar which is obtained from bootstrap classes.

  * The nav-bar its-self is the root of the application in that it houses the 	various links to navigate the application. 

  * Also the *layout.html* is used to bring in the external dependencies to our project i.e Bootstrap.

  * For **Bootstrap** , the application incorporates it through the *bootstrap CDN*,  with the below version used for the project ;

    ``` html
    <link href="{% static 'company/styles.css' %}?{% now 'U' %}" rel="stylesheet" type="text/css" >
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    ```

* **combine.js** - It contains some of the JS logic that is used across the multiple JavaScript files in the application. The logic been:-

  * `requestPath()` - It attaches the Django `csrftoken` to the request path so that the front end can perform a `fetch` request to the Django server.

  * `fetchItems()` - It used to retrieve items stored in the database and send the data to the JS.

  * `displayCategory()` - Since the *Product Category* is stored in form of an integer in the database, this function converts the integer value to a text format during the display of the product.

  * `pageshow` -reloading the page in case of back_forward navigation or if page is loading from a cache.

    

* **styles.css** - It contains some of applications css. Some of the notables codes used are:

  * Row counter : Used in numbering the rows in the various tables

    ```css
    /* To number the table rows */
    table {
        counter-reset: rowCount;
    }
    .rowCounter::before{
        /* Increase counter by 1 */
        counter-increment: rowCount;
        content: counter(rowCount);
    }
    ```

  * Also modal class was incorporate so that to incorporate floating div.

* **views.py** -  Some of the functions used throughout the project are;

  `fetchItems(request)` - It is used to retrieve items stored in the database and send the data to the JS.

* **util.py** - It contains some functions that are used across the pages. The functions include:-

  * `get_counties()` , `get_categories()`, `get_status()`, `get_zones()`,  ` get_county()` and `get_data()` , they retrieve data from the external excel sheet and are respectively used to set the *counties, categories, status, zones, county* and *data* variables in the views.py file.

* **data.xlsx** - It contains some data that is imported into some of the functions.

### Page 1: Home Page

This is the front page of the application. It does not contain much in terms of functionality but its the gateway to the various parts of the application.  With nav-bar included we can navigate to the various pages.

The page is incorporates the below files

*  **home.html** - Containing the html syntax that is rendered.
* **url.py** - Containing the url pattern for to navigate to page `path('', views.index, name='index')`
* **views.py** - The url links to the `index()` function in the views.py, which is used to render the `home.html`

### Page 2: Login

The login page contains the login form that is used to login to the application. Point to note most of the functionality of the app can be accessed without login in.  The link to navigate to the login page is located in the top right corner of all pages, and while the nav-bar is collapsed it is located at the bottom of the nav-bar.

The following files are used in the rendering of the login page

* **login.html** - It contains both the login form and registration form, and with a button a user is able to toggle between the two pages. The link to the login page has an additional get parameter `next` . The parameter enables the user to navigate back the previous page before login.

* **urls.py** - It contains the url pattern, for navigating to the login page `path("login", views.login_view, name="login")`

* **views.py** - In the views.py ,  the `login_view()` , receives either a `GET` or `POST` request. In case of `POST`  it validates the received data from the login form, while `GET` returns the `login.html` to be render by the browser.

  * The below modules(dependencies) are imported to help in the authentication and login and logout

    ```python
    from django.contrib.auth import authenticate, login, logout
    ```



* **models.py** - The `User` model contains the fields for a users data to be stored. The `User model` incorporates the ` AbstractUser`  dependency, which enables the use of *Django auth classes*.

### Page 3: Registration

The page contains the registration form.

The following files are used in the rendering of the registration page

* **register.html** - It contains both the login form and registration form, and JavaScript code for toggling between the two pages.
* **urls.py** - Containing the url pattern for to navigate to page `path("register", views.logut_view, name="logout")`
* **views.py** - In the views.py ,  the `logout_view()`  is used to logout the user out of the app, `logut` function is used to do so. 



### PAGE 4: Products

#### I: Products List Page

This page contains a list a products displaying their buying prices from the different suppliers.

The following files are used in the rendering of the login page

* **products.html** - It contains the logic for the;

  * product table, displaying all the products in the directory with attached prices,
  * product search field, 
  * product form, for adding new products to our directory.

* **products.js** - It houses the JS for the page. It contains the below functions  with each functions logic explained

  * `class Product()` - which is a class template used for creating product objects.
  * `UI.openForm()` and `UI.closeForm()` - Deals with the opening and closing of the product input form.
  * `UI.productCheck()` - It does some slight form validation; in that, it checks whether the product been added by the form  exists.
  * `UI.enableButtons()` and `UI.disableButtons()`- They are a subsidiary of the `UI.productCheck()`, in that they enable and disable the form submit button as a measure of the form validation. 
  * `UI.addProduct()` - It receive a `product` object and displays it in the product table. It adds the newly created product to the products' table.
  * `UI.clearForm()` - Clears out all the input fields in the product form.
  * `UI.renameRow()` - It renames a product row that has been newly added, and also attaches a click event listener to the row, to trigger the `UI.productDetails()`.
  * `UI.productDetails()` - It deals with the redirecting of the user to a page with the specific details of the a product, once the product item is clicked.
  * `UI.filterProducts()` -  It creates a filter table that displays a list of products with a similar name to the query typed in the product filter input.
  * `Store.storeProducts()` -  It receives the created *product object* then sends the object to the server for storage. It also initialize the renaming of the new product row.
  

Some of the events include

* `DOMContentLoaded` - initialize some of the functions
  * `click` - for opening and closing of the product form, redirecting to products detail page.
  * `submit` - collects the data from the form's input fields, then trigger the necessary functions for storing and displaying the data collected.
  * `keyup` - used to trigger the product search function, and also some part of the form validation. 
  
* **url.py** - the url `path('products', views.products, name='products')` Is used for both the `GET` and `POST` request.

* **views.py** - The page is serviced by the function:

  * `products(request)` - Deals with rendering of the page, retrieving items(i.e products and suppliers) from the data base and also saving new products to the database.
  
* **models.py** -  The page uses the  `Product` model contains the fields for creating a *Product Object*.

#### II Product Details Page

We navigate into the page by clicking one of the product items from the product table in the product page. This page contains all the products details

The files used in the rendering of this page are as follows;-

* **productdetails.html** -  It displays the products details form its name to its description. It has two buttons, for the editing and deleting of the product. It also houses a suppliers table showing the product prices from different suppliers and also a button to add a different supplier-price.

* **productDetails.js** - This is the dedicated JS file for the page, which contains the below variables, classes, functions and events.

  * `class Price{}` -   is a class template used for creating 
    *Price* objects. It links a product to a specific supplier, stating the product price from that particular supplier.
* `class Product{}` - is a class template used for creating 
    *Product* objects.
  * `UI.addRow()` - It adds a new row below the last row of the table, the added row is an input field, used to enter a new supplier-price to the the selected product. It also triggers the `UI.disableButtons()` and `UI.dropDownValues()` functions.
* `UI.dropDownValues()` - It filters through all the suppliers in the directory and returns a list with suppliers not linked to the selected product (i.e suppliers that don't have a price listed for the selected product). The returned list is then rendered to the display in the drop-down list, for the user to pick while adding a new supplier-price for the selected product.
  * `UI.addPrice()` - It renders the added supplier-price to the table and also triggers the functions `Store.addPrice(), UI.enableButtons()` and `UI.dropDownValues()`. 
* `UI.renameRow()` - It sets the row id for the newly created row.
  * `UI.editInput()` - It deals with editing of the supplier-prices' table, and it receives an evet input, whereby it does the following functions:- 
  * opening and closing the edit field, 
    * capturing the edited data, 
  * canceling the data in the input fields and 
    * triggering functions for enabling and disabling the buttons depending on the stage of edit.
* `UI.disableButtons()` and `UI.enableButtons()` - Deals with enabling and disabling the *edit, delete, add* and *cancel* buttons in the supplier-price table.
  

Note that the above function deals with the supplier-prices table, the functions below deal with product's details in general.

* `UI.productEditMode()` and `UI.cancelProductEdit()` - It displays and closes the product edit field, while doing the reverse for the product details field.
  
* `UI.updateProductDetails()` - Collects the edited product details and sends the data to the `Store.updateProduct()` 
  
* `Store.updateProduct()` - Receives edited product data and sends it to the server for storage.
  
* `Store.updateProduct()` - Sends edited product details to the server.
  
* `Store.addPrice()` - It receives *price* objects and sends it to the server, it also initializes the `UI.renameRow()`.
  
* `Store.updatePrice()` - It receives edited `price` object and sends it to the server through a fetch request.
  
* `Store.deletePrice()` - Sends a delete request to the server to delete a particular supplier-price.
  

Events 

* `DOMContentLoaded` - It triggers the following functions  - `fetchItems()`, `UI.dropDownValues()` and `UI.displayCategory()`.
  
* `click` - Triggering the various functions in the file
  
* **urls.py** - the below URLs are used for the page 

  * `path('products/<int:id>', views.productDetail, name='productDetail')` - Navigates to the `productDetail()` in our views.py file. 
* `path('products/productPrice', views.productPrice, name='productPrice'`  - Navigates to the `productPrice()` in our views.py file. 
  
* **views.py** -  The page is serviced with the below functions

  * `products()` - Deals with rendering of the page, retrieving items(i.e products and suppliers) from the data base and also saving new products to the database.
  * `productDetail()` - Deals with;- retrieval of data from the database and rendering of the product details to the page, updating the database with edits made to the product and deleting the product.
  *  `productPrice()` - It contains logic for adding, editing and deleting supplier-prices to the database.
  
* **util.py** -  The functions used for this page are:-

  * `updateSupplies()` - It is triggered form `productPrice()`, it is used to update the the *supplier-prices* of the selected product.
  * `supply_factor()` -  The function returns a factor that is used in calculating the supply price of a particular product item. The supply factor price is affected by; the distance to the institution, weight of the product, VAT of 16%, and profit of 10%. It is triggered from the `updateSupplies()` function.
  * `updateJobValue()` - It is triggered from the `updateSupplies()` function. In case of a particular change in price in a specific object, it fetches all the jobs that has that particular product as one of the items to supply and recalculates the field `value` for the *Job Object*.

* **models.py** -  The page uses the  `Product` and `Price` model .



### Page 5: Suppliers

Point of note, most of the functionalities for the *Supplier* and *Client* pages are similar

#### I Suppliers List

It deals with displaying of the a list of Suppliers 

The files used to render the page are;

* **suppliers.html** -  When rendered it displays a table with a list of suppliers , which is paginated to ten rows per page. Also included in the page is a link to navigate the supplier form
* **company.js** -  It contains logic for both the suppliers page and clients page. The variables, classes, functions and events, contained in the file that pertain to the supplier page are as follows;
  * `class Company{}` - which is a class template used for creating a
    *Company* object, which is transferred to the server side as a `Supplier` object.
  * `UI_Company.clearForm()` - It clears the input fields for the company(i.e supplier) form
  * `UI_Company.supplierDetails()` - Once triggered it redirects the user to the `supplier's detail` page.
* **urls.py** - The url that servers this page is `path('suppliers', views.suppliers, name='suppliers')`
* **views.py** - The functions serving the page are
  * `suppliers()` - it fetches the suppliers contained in the directory,  and also deals with the pagination and rendering of the page.
* **models.py** - The page uses the `Company` and `Supplier` models.

#### II Supplier Form

It collects data to create a *Supplier Object* and then saving the object. We navigate to the page by clicking the `+ Supplier` button from the *Suppliers List* Page. Files used for rendering the page are:-

* **companyForm.html** - It contains the form that collects the supplier details that are to be collected. 

* **company.js** -  It contains the below variables, classes, functions and events:-

  * `UI_Company.clearForm()` - It resets the form fields.
* `Store_Company.addCompany()` - it submits the form data to the server side. It redirects the user to the *Supplier's Details Page*, once the form is submitted. The *Supplier's Details Page* contains details that have just been collected from the form. Finally it triggers the `UI_Company.clearForm()` function.
  

The events been

* `DOMContentLoaded` - It triggers the `Store_Company.fetchItems()` function.
  
* `click` - Used to trigger the  `UI_Company.supplierDetails()` functions.
  
* `submit` - Triggers the `Store_Company.addCompany()` function.
  
* **urls.py** -  The default route for the  page is `path('supplierform', views.supplierForm, name='supplierForm')`.

* **views.py** -  The main function for the page is `supplierForm()`,  which is used to; save the received form  data into a supplier object. It also deals with the rendering of the `companyForm.html`.

* **models.py** - The page uses the `Company` and `Supplier` models. Point to note, `Supplier` model inherits the `Company` model which is a *Polymorphic* model class. To make the `Company` model polymorphic we pass `PolymorphicModel` into it. 

  `PolymorphicModel`  is a module import from `polymorphic.models `. To enable the `polymorphic.models `, it is install to the system by `pip install django-polymorphic`.



#### III Supplier Details Page

This page contains details for a particular *Supplier*. The page is navigate into, from either the *Suppliers List Page* by clicking on a particular supplier row, or from the *Supplier Form Page*, after the form is submitted. 

Files that are used in the page include;-

* **supplierDetails.html** - It contains logic that show cases the following - 

  * supplier's details - name, address, email, contact, zone and location.
  * Buttons to edit or delete the supplier 
  * personnel table - showcasing the supplier's personnel and also add or delete a person.
  * table of products - showcasing all the products the supplier deals with. The table also has an option to edit or delete a product from it.
  * a floating form that pops up once the edit button is clicked. The form provides  an avenue to edit the supplier's details.

* **company.js** - It contains the below variables, classes, functions and events:-

  * `class Company{}` - which is a class template used for creating a
    *Company* object, which will be transferred to the server side as a `Supplier` object.

  * `UI_Company.editCompany()` - It receives a company object from the *Supplier Edit Form*, and displays it to the user.

  * `Store_Company.updateSupplier()` - It receives a *Company(Supplier)* object which it sends to the server to update the records in the database.

   For Events

  * `DOMContentLoaded` - It triggers the `Store_Company.fetchItems()` function.

  * `click` - collects the form edit data and triggers the functions `UI_Company.editCompany()` and `Store_Company.updateSupplier()`.

* **companyDetails.js** - 

  * `class Personnel {}` - Is a class template used for creating a
    *Personnel* object, which will be used in collecting of a supplier's personnel/staff.

  * `UI.displayPersonnels()` and `UI.hidePersonnels()`- Deals with opening and closing of the personnel's table.

  * `UI.addRow()` - It adds a new empty input field to the `personnel` table, with the input field used for collecting personnel details to create a *Personnel Object*. It also triggers the `UI.disableButtons()` .

  * `UI.savePerson()` - It receives a *Personnel* object, and deals with adding a new personnel row to the personnel table and also updating details of an edited personnel row. It then triggers the `UI.enableButtons()`.

  * `UI.removeRow()` - It receives a row object, which it then deletes. The row to be deleted is mostly the new input field row added to the *personnel* table.

  * `UI.editForm()`- It puts the selected personnel row into an input edit mode, with the input fields populated with the current row values.

  * `UI.enableButtons()` and `UI.disableButtons()`  - They deal with enabling and disabling of the edit, delete and add buttons.

  * `UI.renameRow()` - It sets the *id* attribute of a new personnel row, whose value is the id of the *Personnel object* from the database.

  * `UI.displayZone()`- Since the value of the zone is saved to our database in form of an integer, this functions changes the value to a text format which is easily readable by a user.

  * `UI.editSupplier()` and `UI.closeForm()`- It opens and closes the supplier edit form.

  * `UI.priceEdits()` - Deals with changing of the *supplier-prices* table, in that it; opens and closes the edit price field, collects edited data and deletes a particular *supplier-price* from the table. It does so while also triggering the relevant functions.

  * `Store.storePerson()`- It receives a *Personnel* objects and sends it to the sever for storage.

  * `Store.updatePerson()` It receives edited *Personnel object* and sends it to the server for updating the relevant records in the database.

  * `Store.deletePerson()` - It receives a *personnel id* which it sends to the server, so that the corresponding *personnel object* can be deleted.

  * `Store.deleteCompany() `-  It sends a request to server to delete the selected *Supplier object*.

  * `Store.updatePrice()` and`Store.deletePrice()`- Sends to the server a request for updating or deleting a particular *supplier-price*.

    Events 

  * `click` - Enables the collecting of data from the *personnel table* and *supplier-price* and triggering the various functions.

  * `DOMContentLoaded` - Triggers the functions:- `UI.displayZone(),  UI.displayCounty(), Store.fetchItems(), UI.displayCategory()` and `UI.disableButtons()`.

* **urls.py** - The following paths servers this page:- 

  * `path('products/productPrice', views.productPrice, name='productPrice')` 

  * `path('suppliers/<int:id>', views.supplierDetail, name='supplierDetail')` 

  * `path('personnel', views.personnel, name="personnel")`

* **views.py** - The below functions are used in the rendering of the page.
  * `productPrice()` - It deals with adding, editing or deleting a *Price Object* from the database.
  * `supplierDetail()` - Deals with updating and deleting of a *Supplier Object*  and also rendering of the suppliers page.
  * `personnel()` - Deals with adding, editing or deleting of a *Personnel Object* 
* **models.py** - The page uses the `Company` and `Supplier` models, that contains the fields for the *Supplier Object*. The `Price` and `Personnel` models are also used.

### Page 6: Clients

It contains some sub-pages that deal with the display and manipulation of the *Client Object* 

#### I Client List

* **clients.html** - The page displays a paginated table list of Clients(Institutions) details. It also contains a link to navigate to the Client Form Page. 
* **company.js** - It contains logic for both the suppliers page and clients page. Function included are:-
  - `UI_Company.clearForm()` - It clears the input fields for the company(i.e client) form
  - `UI_Company.clientDetails()` - Once triggered it redirects the user to the `client's detail` page.
* **urls.py** - The url that serves this page is `path('clients', views.clients, name='clients')`
* **views.py** - The functions serving the page are
  - `clients()` - It fetches the clients contained in the directory, and also deals with the pagination and rendering of the page.

*  **models.py** - The page uses the `Company` and `Client` models



#### II Client Form

It collects data to create a *Client Object* and save the object. `+ Client` in *Supplier List* page is used to navigate to the *Client Form Page* .The files used to make the functionality of this page possible are:-

- **companyForm.html** - It contains the form that collects the supplier details.
- **company.js** - the functions used, are similar to the ones used in the *Supplier Form Page* , which are:- `UI_Company.clearForm(), Store_Company.addCompany() and Store_Company.fetchItems()`, with the events been similar.
- **urls.py** - The default route for the page `path('clientform', views.clientForm, name='clientForm')`
- **views.py** - The main function for the page is `clientForm()`, which saves the received form data, into a *Client object*, into our database. It also deals with the rendering of the `companyForm.html`.

- **models.py** - The page uses the `Company` and `Client` models. Similar to the `Supplier` model, the `Client` model inherits the `Company` model which is a *Polymorphic* model class. 



#### III Client Details Page

The page contains details for a particular *Client Object*. The user can navigate to this page from the *Clients List Page* by clicking one of the row items or from the *Client Form Page* after submitting the form. Files required for the page are:-

- **clientDetails.html** - It contains logic that show cases the following -
  - client's details - name, address, email, contact, county and location.
  - Buttons to edit or delete the client.
  - personnel table, that showcase the client's personnel and also add or delete a person.
  - table of jobs, showcasing all the jobs linked to the selected client. The table also has an option o navigate to the particular page.
  - a floating form that pops up once the edit button is clicked. The form provides an avenue to edit the client's details.
- **company.js** - It contains similar functions and events, to that of the *Supplier Details Page*, namely; `class Company{}, requestPath(url), UI_Company.editCompany(), Store_Company.updateCompany, DOMContentLoaded` and `click`. 

* **companyDetails.js** - Similar function in the *Supplier Details Page* are:- `UI.displayPersonnels()` , `UI.hidePersonnels(), UI.addRow(), UI.savePerson(), UI.removeRow(), UI.editForm(), UI.enableButtons()` , `UI.disableButtons(), UI.renameRow(), UI.displayCategory(), UI.editSupplier()`  `UI.closeForm()`, `Store.storePerson(), Store.updatePerson(), Store.deletePerson()` and `Store.deleteCompany()`.

  Other functions include:-

  * `UI.displayCounty()` - Used to display the `county` field in the `Client` model in a string format.
  * `UI.jobsDetails()` - When triggered it navigates the user to the details page of the clicked job item.

* **urls.py** - The following paths servers this page:-

  - `path('clients/<int:id>', views.clientDetail, name='clientDetail')`
  - `path('personnel', views.personnel, name="personnel")`
  - `path('jobs/<int:id>', views.jobDetail, name='jobDetail')`

* **views.py** - The below functions are used in the rendering of the page;

  * `clientDetail()` - Deals with rendering of the *Client Detail* page and also the editing and deleting of a particular *Client Object*.
  * `personnel()` - Deals with adding, editing or deleting of a *Personnel Object*.
  * `jobDetail()` - When triggered, it directs a user to the *Job Details* page.

* **models.py** - The page uses the `Company` and `Client` models, that contains the fields for the *Client Object*. The `Job` and `Personnel` models are also used.

### Page 7: Jobs

It contains several pages that deal with the display and manipulation of *Job Objects*.

#### I Job List Page

It displays a list of all the jobs in the directory. The below files are used for the rendering of the page:-

* **jobs.html** -  It contains:- 
  * a table with a list of *Job Objects* in the inventory,
  * a search bar to search for Job Items in the table list. 
  * a job form used to add new job items.
* **jobs.js** - The file contains the below functionalities:-
  * `class Job {}` - It is a template used for creating a `Job Object`.
  * `UI.openForm()`,  `UI.closeForm()` and `UI.clearForm()` - It respectively deals with; opening, closing and clearing of the job input form.
  * `UI.jobDetails()` - Once triggered it redirects the user to the *Job Details Page* of the clicked job item from the table.
  * `UI.filterJobs()` - It filters the items in the table according to the search query in the search input field.
  * `UI.jobCheck()` - Its a type of validation, in that it compares the input query, from the job form, to the already existing jobs in the directory. If similarity is found the user is given a warning that the job already exists, while at the same time the form submit button is disabled.
  * `UI.enableButtons()` and `UI.disableButtons()` - They deal with the enabling and disabling of the form submit button, depending on the validation of the function `UI.jobCheck()`.
  * `Store.storeJob()` - It sends the created `Job Object` to the server.
  * With the various event listeners used for triggering the above functions.
* **urls.py** - The default url route for the page is `path('jobs', views.jobs, name='jobs')`
* **views.py** - It uses the function:
  * `jobs()` - The function is used to render the `jobs.html` and also to store the received *Job Object* to the database.
* **models.py** - The `Job` model is used for the creating of the *Job Object*.



#### II Job Detail

It contains details of a particular job item. Note that , only logged in members can view and manipulate the page.

The files used are:-

* **jobDetails.html** - The page displays all the particulars of the selected job item. It contains the name of the client and job code(name), a table of products  that displays the products the client wants to be supplied with, links to download various documents and lastly an options bar change the page into various modes(status), namely:-

  * *RFQ* - In this mode we feed in the supplies the clients wants from the RFQ form issued by the client.
  * *LPO* - In this mode, we are able to feed in the LPO Number, as per the one received form client. And also we are able to change the quantities of the supplies as per the LPO received.
  * *Supplied* - This mode indicates that the products have already been supplied to the client, and once payment is received we are able to feed-in the Cheque number.
  * *Paid* - Final mode indicating that payment is done and the job order is closed.

* **styles_print.css** - contains the necessary css used in the HTML for generating pdf files.

  

* **jobDetails.js** - It contains the below functionality

  * `class Supply{}` - It a class template used for creating a *Supply Object*.

  * `UI.addInputRow()` - When triggered it adds an empty input row field into the table where the user can feed in a product into the RFQ list.

  * `UI.enableButtons()` and `UI.disableButtons()` - Used to toggle off the buttons on and off depending if the table input field is on or off.

  * `UI.searchList()` - It generates a list of products to be displayed in the search filter list. The products to be displayed are only the ones not yet listed in our table.

  * `UI.filterProducts()` - The function is triggered on `keyup` in the *filter search bar*. The functions compares the queried input to the items generated by the `UI.searchList()`, and displays the result for the user.

  * `UI.addProduct()` - The function has the following functionality

    * Trigger the functions  `UI.clearFilter()`, `UI.calc_selling()`, `UI.enableButtons(), UI.searchList(), Store.storeSupply(), UI.calculateValue()` and `UI.censorLinks()`.
    * Clearing the search list
    * create a *Supply Object*, and display the object and also send it for storage.

  *  `UI.calc_selling()` - The function returns a factor that is used in calculating the supply price of a particular product item. The supply factor price is affected by the distance to the institution from Nairobi(Kenya), weight of the product, VAT of 16%, and profit of 10%.

  * `UI.clearFilter()` - it resets the value of the filter input field.

  * `UI.productEdits()` - It works on event propagation. It used in the editing of the rows in the supply table, in that the user can edit, save and delete a supply row. 

  * `UI.calculateTotal()` - Its used to make the *Total Column* in the supplies table dynamic, so that the value of the column can change with change in the *Price or Qty Column*.

  * `UI.calculateValue()` - It used to update the displayed job value depending on a change in the *Price or Qty Column* of the supply table. It also recalculates the job value on addition of new supply objects.

  * `UI.updateStatus()` - It used to update the display depending on the selected *Status*. Depending on the *Status* selected, some of the items in the display are turned visible or invisible.

  * `UI.LPO_inputfield()` - It works on event propagation, and only available when the *Status* is *LPO*. It is used to either collect the *LPO Number* feed in in the LPO input field, or to open the LPO input field, so as to change the current LPO number.

  * `UI.displayLPO()`- It is triggered from `UI.LPO_inputfield()`, and is used to display the collected *LPO Number* to the user.

  * `UI.supply_inputfield()` -  It works on event propagation, and only available when the *Status* is *Supplied*. It is used to either collect the *Cheque Number* queried in the Cheque input field, or to open the Cheque input field, so as to change the current Cheque number.

  * `UI.displayCheque()` - Its function is to display the received cheque number to the user.

  * `UI.resetLPO_inputField()` and `UI.resetCheque_inputField()`, their function is to reset the respective form fields.

  * `UI.censorLinks()`- It is used to disable and enable some of the document download links depending on the status selected. It also removes the *Action Column* from the column depending on the current status.

  * `UI.enable_links()` and `UI.disable_links()` - Triggered from the 

    `UI.censorLinks()` function, and the respectively deal with the enabling and disabling of the selected link.

  * `UI.toggle_actionColumn()` - Triggered from the `UI.updateStatus()` and `UI.censorLinks()` function. It deals with changing the visibility of the *Action Column* depending on the selected status.

  * `Store.deleteJob()` - Sends a request to the server to delete the selected job.

  * `Store.updateStatus()` - It receives the current status selected and sends it to the sever for updating of the *Job Object*.

  * `Store.storeSupply()` - It receives a *Supply Object*, and sends it to the server for saving.

  * `Store.saveEdits()` - It receives edited *Supply Object* and saves it 

  * `Store.deleteSupply()` - It sends a delete request to the server to delete the selected *Supply Item*.

  * `Store.saveLPO()` and `Store.saveCheque()`- It receives the LPO and *Cheque* numbers respectively and sends it the sever for storage.

* **urls.py** - Default path for the page are

  * `path('jobs/<int:id>', views.jobDetail, name='jobDetail')` 
  * `path('supplies/<int:id>', views.supplies, name='supplies')`
  * `path('jobs/<str:type>/<int:id>', views.getItems, name='getItems')`

* **views.py** - The functions used for the functionality of the page are

  * `jobDetail()` - Whose functions are; 
    * rendering the `jobDetails.html` page, 
    * deleting a *Job Object* from the directory, 
    * updating the status of a selected *Job Object*, 
    * adding the *LPO* or *Cheque Number* into the *Job Object*
    * triggering the `util.create_notes()` to create a *Notes Object*.
  * `supplies()`- It functions is to save, edit or delete selected *Supply Objects*.
  * `getItems()` - It deals with the printing of the various documents. The function enables the below functionalities:-
    * printing of job analysis, i.e comparing the Selling and Buying Prices. The analysis is printed in either a *.csv* format or *.xlsx*.
    * sending of an *.xlsx* email attachment to the different supplies, containing a list of products contained in a particular *RFQ list* that the selected supplier supplies. This is to be used to confirm the current prices of the item.
    * printing of the delivery, invoice and receipt. This is done by triggering an outside function `util.create_pdf()`

* **util.py** - The functions used for the page are:

  * `create_xlsx() ` - The function is triggered from the `getItems()` in the `views.py`. It creates the *.xlsx*, and returns it in the form of a bytes item.
  * `create_pdf()` - The function is triggered from the `getItems()` in the views.py. It used in the creation a pdf bytes item  and also in the combination of pdfs.
  * `create_notes()` - The function is triggered from the `jobDetail()` in the views.py. It is used to create a new *Notes Object*.
  * `updateJobValue()` - It is triggered from the `supplies()` function. For every object added to the supplies list, the function recalculates the  `job.value` for the *Job Object*.

  External Modules import into the **views.py** and **util.py** are:

  * `io`- Used for creating bytes object
  * `csv` and `xlsxwriter` - Used in creating csv and .xlsx files respectively
  * `weasyprint`  and from it `HTML` and `CSS`- Used in the creation of pdf files.
  * `PyPDF2` from it `PdfFileMerger` - Used in merging of pdf documents
  * `pandas` - Used for data manipulation, in this case used in retrieving of data from an external excel file.

* **models.py** - The models used for this page are `Job` and `Notes`.



### settings.py

For some of the functionality to work, the settings app is modified. Some of the modifications are:-

* Inclusion of `company` and `polymorphic` into the installed apps. 

  ``` python
  INSTALLED_APPS = [
      'company',
      'polymorphic',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```

* setting of the static root `STATIC_ROOT = '/static/'`

* Setting of email settings:-

  * For testing, to set the email server to a local host, hence email sent displayed in the console

    ```python
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = '1025'
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = False
    ```

    To open the email server we will have to open a new console page and run the command `python -m smtpd -n -c DebuggingServer localhost:1025`

  * To send the mail to an outside server i.e google:-

    ```
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'kevin.dev254@gmail.com'
    EMAIL_HOST_PASSWORD = 'password'
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False
    ```



## Credits

Below are some of the links that were helpful in development of the application

* https://cs50.harvard.edu/web/2020/weeks/ - Contianing the course material
* https://xlsxwriter.readthedocs.io/tutorial02.html - Contains examples for the use of [xlsxwriter]
* https://mdbootstrap.com/docs/b4/jquery/plugins/table-editor/
* https://medium.com/@nerdplusdog/a-how-to-guide-for-modal-boxes-with-javascript-html-and-css-6a49d063987e - Helpful in the creation of floating div(i.e modal boxes)
* https://www.programcreek.com/python/example/115974/weasyprint.HTML - Examples of pdf generation code using WeasyPrint.



## Glossary

1. RFQs :	Request for Quotations

2. LPO:	Local Purchase Order

3. RFQ prices: 	this are the product selling prices, the price we sell to the institutions.

4. JS:	JavaScript

5. Nav-bar:	Navigation bar

6. CDN:	Content Delivery Network

7. UI:	User interface, It is JS class that house the functions that affect the page display

8. Store:	Class that houses functions used in the storage and manipulation of data.

9. Supplier-price : 	the price of a product from a particular supplier, a product can be offered by different suppliers, with each supplier having a price for the product, hence the term supplier-price.