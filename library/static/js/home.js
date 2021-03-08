setTimeout(function(){
    // TODO: Use intesect API , if scroll down , remove #welcome
    const welcome = document.getElementById('welcome');
    welcome.style.display='none';
},10000);

const welcome = document.getElementById('welcome');
welcome.style.display='block'

// (function is_home(){
//     page = location.href;
//     console.log(page,'asdf')
//   })()