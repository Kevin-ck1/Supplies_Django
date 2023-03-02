//Attaching the csrf token 
function requestPath(url){
    //Function for getting crsf token
    function getCookie(name) {  
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }

        return cookieValue;
    }

    //Get csrf token
    const csrftoken = getCookie('csrftoken');
    const request = new Request(
        `${url}`,
        {headers: {'X-CSRFToken': csrftoken}}
    );

    return request;
};

//Display of the category field to text
function displayCategory(tableName, n){
    var productTable = document.querySelector(tableName);
    var rows = productTable.querySelectorAll('tr');
    for(let i = 0; i<rows.length-n; i++){
        var a = rows[i].querySelector('#category')
        var b = rows[i].querySelector('.categoryColumn');
        var categoryColumn = a || b
 
        var categoryValue = categoryColumn.innerText;
        if(parseInt(categoryValue)){
            categoryColumn.innerHTML = categories[categoryValue - 1];
        };   
    } 
};

//Fetch Items and set to local storage
function fetchItems(){
    const request = requestPath(`/company/fetchItems`)
    fetch(request)
    .then(response=> response.json())
    .then((res)=>{
        localStorage.setItem("products", JSON.stringify(res.products));
        localStorage.setItem("suppliers", JSON.stringify(res.suppliers));
        localStorage.setItem("jobs", JSON.stringify(res.jobs));
        localStorage.setItem("prices", JSON.stringify(res.prices));
        localStorage.setItem("data", res.data);
        localStorage.setItem("counties", res.counties);
    })
};


//Reload page on back
window.addEventListener("pageshow", (event)=>{
    const hist = event.persisted || window.performance.getEntriesByType("navigation") == "back_forward"
    if(hist){
        window.location.reload(true);
    }
});

//Global Variables 
var categories = JSON.parse(localStorage.getItem("data")).Categories
var zones = JSON.parse(localStorage.getItem("data")).Zones
var counties = JSON.parse(localStorage.getItem("data")).Counties
var status = JSON.parse(localStorage.getItem("data")).Status

