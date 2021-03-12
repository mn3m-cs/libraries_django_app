phone1 = document.querySelector('[name="phone1"]');

(function more_phones_adder() {
    more_phones = document.createElement("a");
    more_phones.innerText = "+ Add more phones";
    more_phones.classList.add("more");
    phone1.parentNode.insertBefore(more_phones, phone1.nextSibling);
    more_phones.addEventListener("click", addPhone);
})();

function addPhone(event) {
    const lastPhoneIndex = event.target.previousSibling.name.slice(-1);
    const lastPhoneField = document.querySelector(`[name=phone${lastPhoneIndex}]`);
    const newPhoneIndex = parseInt(lastPhoneIndex) + 1;
    let newPhone = document.createElement("input");
    newPhone.type = "text";
    newPhone.name = "phone" + newPhoneIndex;
    newPhone.classList.add('form-control')
    const phoneLabel = document.createElement("label");
    phoneLabel.textContent = 'Phone' + newPhoneIndex + ':';
    more_phones.parentNode.insertBefore(newPhone, more_phones);
    newPhone.parentNode.insertBefore(phoneLabel, newPhone);
    more_phones.style.display = 'none';
}

is_author_form_group = document.getElementById('id_is_author');
is_author_form_group.parentElement.style.position = 'relative';


is_library_account_form_group = document.getElementById('id_is_library_account');
is_library_account_form_group.parentElement.style.position = 'relative';

// Add event listener to is_author and is_library_account
// if both checked disable submit button and shoe message
// already we handle it in our view , this for front-end

is_author_form_group.addEventListener('click', checkLibrary)
is_library_account_form_group.addEventListener('click', checkAuthor)

function checkLibrary() {
    if (is_library_account_form_group.checked == true ) {
        is_library_account_form_group.checked = false;
        is_author_form_group.checked = true;
    }
}

function checkAuthor(){
    if (is_author_form_group.checked == true ) {
        is_library_account_form_group.checked = true;
        is_author_form_group.checked = false;
    }
}