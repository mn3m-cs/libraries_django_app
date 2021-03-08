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
    phoneLabel.textContent = 'Phone'+newPhoneIndex+':';
    more_phones.parentNode.insertBefore(newPhone, more_phones);
    newPhone.parentNode.insertBefore(phoneLabel, newPhone);
    more_phones.style.display='none';
}

is_author_form_group = document.getElementById('id_is_author');
console.log(is_author_form_group)
is_author_form_group.parentElement.style.position ='relative';
