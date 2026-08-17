let menu_tog=document.querySelector(".menu-toggle");
let sidebar=document.querySelector(".sidebar");

menu_tog.addEventListener("click",()=>{
    menu_tog.classList.toggle("isactive");
    sidebar.classList.toggle("isactive");
})