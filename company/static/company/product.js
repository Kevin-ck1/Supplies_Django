
//Product Class: 
class Product{
    constructor(nameP, brand, category, productPrice, size, weight, supplier, description){
        this.nameP = nameP;
        this.brand = brand;
        this.category = category;
        this.productPrice = productPrice;
        this.size = size;
        this.weight = weight;
        this.description = description;
        this.supplier = supplier;
    }
};

//UI Class: UserInterface
class UI {
    //To display the form
    static openForm(){
        var form = document.querySelector('.productForm');
        form.style.display = 'block';
        form.classList.add('card');
    }

    //To close the form
    static closeForm(){
        var form = document.querySelector('.productForm');
        form.style.display = 'none';
        form.classList.remove('card');
    }

     //Validating form - Checking if the product exists
     static productCheck(){
        const name = document.querySelector('#nameP').value;
        const value = document.querySelector('#brand').value;
        const products = JSON.parse(localStorage.getItem("products"))
        const message = document.querySelector('.productWarning')
        const pMessage = message.querySelector('a')
        for (let product of products){
            if(product.nameP == name && product.brand == value){
                message.style.display = "block";
                pMessage.innerHTML = `${name}: ${value}`;
                pMessage.href = `/company/products/${product.id}`;
                UI.disableButtons();
                break;

            }else{
                message.style.display = "none";
                pMessage.innerHTML = ``;
                pMessage.href = ``;
                UI.enableButtons();
            }
        }
        
    };

    static enableButtons(){
        let button = document.querySelector('#submitButton')
        button.disabled = false;
        button.className = "btn btn-primary";
    };

    static disableButtons(){
        let button = document.querySelector('#submitButton')
        button.disabled = true;
        button.className = "btn btn-secondary";
    };

    //Adding the new Product to the display
    static addProduct(product){
        const table = document.querySelector('#tableProduct');
        const newRow = document.createElement('tr');
        var suppliers = JSON.parse(localStorage.getItem("suppliers"));
        var supplierName;
        for(let supplier of suppliers){
            if(supplier.id == product.supplier){
                supplierName = supplier.nameC
            }
        }
        var category = categories[product.category - 1]
        newRow.innerHTML = `
            <td scope="row" class="rowCounter"></td>
            <td>${product.nameP} : ${product.brand}</td>
            <td>${supplierName}</td>
            <td>${category}</td>
            <td>${product.productPrice}</td>
        `;


        //Placing the new row into the table
        table.insertBefore(newRow, table.firstElementChild);

        //Closing form
        UI.closeForm();

    }

    static clearForm(){
        document.querySelector('#productForm').reset();
    };

    //To rename the new product row
    static renameRow(id){
        const table = document.querySelector('#tableProduct')
        const row = table.firstElementChild
        row.setAttribute('id', id)
        row.addEventListener('click',()=>{
            UI.prodcutDetails(id)
        })

    };

     //To redirect to the product details
     static prodcutDetails(id){
        var products = JSON.parse(localStorage.getItem("products"))
        var ids = [];
        for (let product of products){
            ids.push(product.id)
        }
        if(ids.includes(parseInt(id))){
            window.location=`products/${id}`
        }else{
            alert("Product ID Does Not Exist")
        }
    };

    static filterProducts(){
        let filterValue = document.querySelector('.filterInput').value.toUpperCase();
        
        document.querySelector('#tableProduct').querySelectorAll('tr').forEach((tr)=>{
            let productName = tr.querySelector('td').nextElementSibling.innerText.toUpperCase();
            if (productName.indexOf(filterValue) > -1){
                tr.style.display = '';
            }else {
                tr.style.display = "none";
            }
            
        });
    };

};

class Store {
    static storeProduct(product){
        const request = requestPath(`/company/products`)
        fetch(request, {
            method: "POST",
            mode: 'same-origin',
            body: JSON.stringify({
                newProduct: product
            })
        })
        .then(response => response.json())
        .then((res)=>{
            console.log(res.message)
            //Rename New Product Row
            UI.renameRow(res.id);
        })
    };

    
}

//Events

//Event, Load Products
window.addEventListener('DOMContentLoaded', ()=>{
    //Rename the category column
    displayCategory('#tableProduct', 0);
    //Fetch products
    fetchItems()
    //Clear the form fields
    UI.clearForm();
})
//Event, addButton click
document.querySelector('#addButton').addEventListener('click',()=>{UI.openForm()});

//Event, close button click
document.querySelector('.buttonClose').addEventListener('click', ()=>{UI.closeForm()})

//Event, submiting form
document.querySelector('#productForm').addEventListener('submit', (event)=>{
    event.preventDefault();
    const nameP = document.querySelector('#nameP').value;
    const brand = document.querySelector('#brand').value;
    const category = document.querySelector('#category').value;
    const price = document.querySelector('#price').value;
    const size = document.querySelector('#size').value;
    const weight = document.querySelector('#weight').value;
    const supplier = document.querySelector('#supplier').value;
    const description = document.querySelector('#description').value;

    //Validating the form
    if(nameP=='' || brand == ''|| category == ''|| category==''|| price == ''|| size==''|| weight==''|| supplier==''|| description=='' ){
        alert('Please Fill In all fields')
    }else {
        //Creating a new instance of the product
        const newProduct = new Product(nameP, brand, category, price, size, weight, supplier, description);
        //Add The new product to the display
        UI.addProduct(newProduct);

        //Add the new product to the database
        Store.storeProduct(newProduct);

        //Clear the form fields
        UI.clearForm();

    };

    
});

// Event, row(product) click
document.querySelectorAll('tr').forEach((r)=>{
    r.addEventListener('click', ()=>{
        UI.prodcutDetails(r.id);
    })
});


//Event, Filter List
document.querySelector('.filterInput').addEventListener('keyup', ()=>{
    UI.filterProducts();
});

//Event, Check if Product Already Exits
document.querySelector('#brand').addEventListener('keyup',()=>{
    UI.productCheck();
});
document.querySelector('#nameP').addEventListener('keyup', ()=>{
    UI.productCheck();
});





