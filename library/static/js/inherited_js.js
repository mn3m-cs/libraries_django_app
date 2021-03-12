const dropDown = document.querySelector('.dropdown');
const dropDownContent = document.querySelector('.dropdown-content');
dropDown.addEventListener('click', displayDropDownContent);

function displayDropDownContent(){
    dropDownContent.style.display= 'block';
}