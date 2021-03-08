phone2 = document.querySelector('[name="phone2"]');
address = document.querySelector('[name="address1"]');
country = document.querySelector('[name="country1"]');
city = document.querySelector('[name="city1"]');

// add_phone = document.createElement("input");
// add_phone.type = "text";

(function additions() {
  // ADD MORE PHONES
  more_phones = document.createElement("a"); // without var so we can use it globally
  more_phones.innerText = "+ Add more phones";
  more_phones.classList.add("more");
  // insert after
  phone2.parentNode.insertBefore(more_phones, phone2.nextSibling);
  more_phones.addEventListener("click", addPhone);

  // ADD MORE ADDRESSES
  more_addresses = document.createElement("a");
  more_addresses.innerText = "+ Add more addresses";
  more_addresses.classList.add("more");
  address.parentNode.insertBefore(more_addresses, address.nextSibling);
  more_addresses.addEventListener("click", addAddress);

  // ADD more countries
  more_countries = document.createElement("a");
  more_countries.innerText = "+ Add more countries";
  more_countries.classList.add("more");
  country.parentNode.insertBefore(more_countries,country.nextSibling);
  more_countries.addEventListener("click", addCountry);

    // ADD more Cities
    more_Cities = document.createElement("a");
    more_Cities.innerText = "+ Add more Cities";
    more_Cities.classList.add("more");
    city.parentNode.insertBefore(more_Cities,city.nextSibling);
    more_Cities.addEventListener("click", addCity);
  
})();

// function GFG_Fun(event) {
//   // THIS WORK ON EDGE ONLY
//   /* #TODO:
//     Use the document.defaultView.getComputedStyle() method to get all the cascading styles
//     associated with that particular element. After that, append the style to a string one by one
//     by traversing the object.
//     */
//   //  console.log(event)
//   var ar = document.defaultView.getComputedStyle(event, null);
//   console.log(ar)
//   var str = "";
//   for (var key in ar) {
//     if(isNaN(key)){
//       // console.log(key)
//       str = str + key + ": " + ar[key] + ", ";
//     }
//     // str = str + key + ": " + ar[key] + "-";
//   }
//   console.log(str);
//   return str;
// }

function addPhone(event) {
  // get number of lastphone number ex.2 add give the new field 3
  const lastPhoneIndex = event.target.previousSibling.name.slice(-1);
  const lastPhoneField = document.querySelector(`[name=phone${lastPhoneIndex}]`);
  const newPhoneIndex = parseInt(lastPhoneIndex) + 1;
  // create new phone field and give the style of lastPhone element
  let newPhone = document.createElement("input");
  newPhone.type = "text";
  newPhone.name = "phone" + newPhoneIndex;
  // newPhone.style = GFG_Fun(lastPhoneField);
  // newPhone.style.background ='';
  newPhone.classList.add('form-control')
  // label
  const phoneLabel = document.createElement("label");
  phoneLabel.textContent = 'Phone'+newPhoneIndex+':';
  more_phones.parentNode.insertBefore(newPhone, more_phones);
  newPhone.parentNode.insertBefore(phoneLabel, newPhone);
}

function addAddress(event){
    const lastAddressIndex = event.target.previousSibling.name.slice(-1);
    const lastAddressField = document.querySelector(`[name=address${lastAddressIndex}]`);
    const newAddressIndex = parseInt(lastAddressIndex) + 1;
    let newAddress = document.createElement("input");  
    newAddress.type = "text";
    newAddress.name = "address" + newAddressIndex;
    // newAddress.style = GFG_Fun(lastAddressField);
    // newAddress.style.background =''
    newAddress.classList.add('form-control')
    const AddressLabel = document.createElement("label");
    AddressLabel.textContent = 'Address'+newAddressIndex+':';
    more_addresses.parentNode.insertBefore(newAddress, more_addresses);
    newAddress.parentNode.insertBefore(AddressLabel, newAddress);
}

function addCountry(event){
  const lastCountryIndex = event.target.previousSibling.name.slice(-1);
  const lastCountryField = document.querySelector(`[name=country${lastCountryIndex}]`);
  const newCountryIndex = parseInt(lastCountryIndex) + 1;
  // create new Country field and give the style of lastCountry element
  let newCountry = document.createElement("input");
  newCountry.type = "text";
  newCountry.name = "country" + newCountryIndex;
  // newCountry.style = GFG_Fun(lastCountryField);
  // newCountry.style.background =''
  newCountry.classList.add('form-control')
  const CountryLabel = document.createElement("label");
  CountryLabel.textContent = 'Country'+newCountryIndex+':';
  more_countries.parentNode.insertBefore(newCountry, more_countries);
  newCountry.parentNode.insertBefore(CountryLabel, newCountry);
}

function addCity(event){
  const lastCityIndex = event.target.previousSibling.name.slice(-1);
  const lastCityField = document.querySelector(`[name=city${lastCityIndex}]`);
  const newCityIndex = parseInt(lastCityIndex) + 1;
  // create new City field and give the style of lastCity element
  let newCity = document.createElement("input");
  newCity.type = "text";
  newCity.name = "city" + newCityIndex;
  // newCity.style = GFG_Fun(lastCityField);
  // newCity.style.background =''
  newCity.classList.add('form-control')
  const CityLabel = document.createElement("label");
  CityLabel.textContent = 'City'+newCityIndex+':';
  more_Cities.parentNode.insertBefore(newCity, more_Cities);
  newCity.parentNode.insertBefore(CityLabel, newCity);


}

