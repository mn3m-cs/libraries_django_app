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

async function postData(url = '', data = {}) {
    const response = await fetch(url, {
        method: 'POST',
        mode: 'cors',
        credentials: 'same-origin',
        headers: {
            'Content-type': 'application/json',
            "X-CSRFToken": csrftoken,
        },
        redirect: 'follow',
        // referrerPolicy:'no-referrer',
        body: JSON.stringify(data)
    });
    return response.json();
    console.log(response)
}

add_review_btn = document.getElementById('add_review_btn');
add_review_btn.addEventListener('click', addReview)


const book_name = document.getElementById('book_name').innerText;
url = 'http://127.0.0.1:8000/add_review/'

function addReview() {
    // starNumber is a global variable from another script , which indicate the rate
    // rate = starNumber
    const title = document.querySelector("[name='title']").value;
    const body = document.querySelector("[name='body']").value;
    postData(url, data = {'book_name': book_name, 'rate': starNumber,'title':title,'body':body}).catch(err => console.error(err))

}
// don't show form if user already review this book

// Hide Review Form if successful