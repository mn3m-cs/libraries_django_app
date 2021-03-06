const searchInput = document.getElementById('search-lib');

(function firstLibraries(){
    fetch(`http://127.0.0.1:8000/libraries_list_api/?format=json&search=`).then(onResponse).then(onJsonReady);
})()

searchInput.addEventListener('input',getLibraries);
searchInput.addEventListener('change',getLibraries);
librariesList = []

listsContainer = document.createElement('div');
listsContainer.classList.add('listsContainer');
searchInput.parentNode.insertBefore(listsContainer,searchInput.nextSibling);
listsContainer.appendChild(searchInput);
searchInput.classList.add('searchInContainer')

let ul =document.createElement('ul');
ul.classList.add('results');

let chosenList = document.createElement('ol');
chosenList.classList.add('chosenList');
listsContainer.appendChild(chosenList);

foundIn = document.createElement('span');
foundIn.innerText='Found In'
foundIn.classList.add('chosenListHeader');
listsContainer.insertBefore(foundIn,chosenList) 


function getLibraries(evt){
    query = evt.target.value;
    fetch(`http://127.0.0.1:8000/libraries_list_api/?format=json&search=${query}`).then(onResponse).then(onJsonReady);
}

function onJsonReady(json){
    ul.innerHTML =''
    json.forEach((lib)=>{
        console.log(lib['name'])
        let li = document.createElement('li');
        li.innerText = lib['name'];
        li.addEventListener('click',addToList);
        ul.appendChild(li);
    })
    searchInput.parentNode.insertBefore(ul,searchInput.nextSibling);

}

function onResponse(response){
    return response.json();
}

function addToList(evt){
    if (!librariesList.includes(evt.target.innerText)){
        librariesList.push(evt.target.innerText);
        // postData(url,{'library':evt.target.innerText,'book':bookName});
        chosenList.appendChild(evt.target);
        evt.target.removeEventListener('click',addToList);
        // console.log(librariesList)
    }
    else{
        alert(evt.target.innerText + ' aleardy added.')
    }
    evt.target.addEventListener('click', cancelLibrary);
}

function cancelLibrary(evt){
    ul.appendChild(evt.target);
    // chosenList.removeChild(evt.target)
    librariesList.pop(evt.target.value);
    console.log(librariesList)
    evt.target.removeEventListener('click',cancelLibrary);
    evt.target.addEventListener('click',addToList);
}

// DRF save LibraryBooks DataBase
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

async function postData(url='',data={}){
    const response = await fetch(url, {
        method: 'POST',
        mode: 'cors',
        credentials:'same-origin',
        headers: {
            'Content-type':'application/json',
            "X-CSRFToken":csrftoken,
        },
        redirect:'follow',
        // referrerPolicy:'no-referrer',
        body: JSON.stringify(data)
    });
    return response.json();
}

const add_book = document.querySelector('.block-btn');
add_book.addEventListener('click',start);

function add_library_books(){
    var bookISBN = document.querySelector("[name='isbn']").value;
    console.log(bookISBN) 
    var url = 'http://127.0.0.1:8000/add_library_books/';
    for (let lib of librariesList){
        console.log(lib,bookISBN)
        postData(url,{'lib_name':lib,'book_isbn':bookISBN}).catch(err => console.error(err))
    }
}

function redirect(){
    location.href='/home';
}

function start(){
    // wait until book object is created.
    setTimeout(add_library_books,100);
    // wait untill fetch
    setTimeout(redirect,2000);
}