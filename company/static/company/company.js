//Supplier Class
class Company{
    constructor(nameC, address, email, contact, zone, county, location){
        this.nameC = nameC;
        this.address = address;
        this.email = email;
        this.contact = contact;
        this.zone = zone;
        this.county = county;
        this.location = location;
    }
}

//UI_Company Class: User Interface
class UI_Company {
    static clearForm(){
        document.querySelector('#companyForm').reset()
    }

    static supplierDetails(id){
        window.location=`/company/suppliers/${id}`
    };

    static clientDetails(id){
        window.location=`/company/clients/${id}`
    }

    static editCompany(company){
        const zone = zones[company.zone - 1];
        const county = counties[company.county - 1];
        document.querySelector('.cName').innerHTML = company.nameC
        document.querySelector('.cAddress').innerHTML = company.address;
        document.querySelector('.cEmail').innerHTML = company.email;
        document.querySelector('.cContact').innerHTML = company.contact;
        document.querySelector('.cZone').innerHTML = zone
        document.querySelector('.cCounty').innerHTML = county
        document.querySelector('.cLocation').innerHTML = company.location;
        UI.closeForm();
    };
}

//Storage Class
class Store_Company {
    static addCompany(company, mode){
        let request;
        if(mode == "Supplier"){
            request = requestPath(`supplierform`);
        }else{
            request = requestPath(`clientform`);
        }
        fetch(request, {
            method: "POST",
            mode: "same-origin",
            body: JSON.stringify({
                newCompany: company
            })
        })
        .then(response => response.json())
        .then((res)=>{
            if(mode == "Supplier"){
                window.location=`/company/suppliers/${res.id}`
            }else{
                window.location=`/company/clients/${res.id}`
            }
            //Clear Form Fields
            UI_Company.clearForm()     
        })
        
    };

    static updateCompany(company){
        const request = requestPath(``);
        fetch(request, {
            method: "PUT",
            mode: "same-origin",
            body: JSON.stringify({
                updateCompany: company
            })
        })
        .then(response => response.json())
        .then((res)=>{
            console.log(res.message)
              
        })
    }
}

//Events
//Onload
window.addEventListener('DOMContentLoaded', ()=>{
    //Fetch data
    fetchItems()
})

try {
    //Clicking Product: Opening supplier details
    document.querySelector('#companyTable').querySelectorAll('tr').forEach((tr)=>{
        tr.addEventListener('click', (event)=>{
            if (event.target.parentElement.className == "suppliers"){
                UI_Company.supplierDetails(tr.id)
            } else {
                UI_Company.clientDetails(tr.id)
            }
           
        })
    })
} catch {
    //Submiting Form
    document.querySelector('#companyForm').addEventListener('submit', (e)=>{
        e.preventDefault();
        const mode = document.querySelector('.mode').innerText;
        const nameC = document.querySelector('#nameC').value;
        const address = document.querySelector('#address').value;
        const email = document.querySelector('#email').value;
        const contact = document.querySelector('#contact').value;
        const location = document.querySelector('#location').value;
        const zone = document.querySelector('#zone').value; 
        const county = document.querySelector('#county').value;

        if(nameC == '' || address == '' || email =='' || contact == '' || zone == '' || location == '' || county == ''){
            alert('Please Fill in All the Fields')
        }else{
            const company = new Company(nameC, address, email, contact, zone, county, location)

            //Obtain mode of submission either edit or add
            const buttonType = document.querySelector('.submitButton').value;


            if (buttonType == "add"){
                //Add The new Company to the database
                Store_Company.addCompany(company, mode);

            } else {
                //Change the Display
                UI_Company.editCompany(company)
                //Update the Data base
                Store_Company.updateCompany(company)
            }
        }

    });

}

