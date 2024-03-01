const collapsedClass = "nav--collapsed";
const nav_collapsed_element = "nav_collapsed_element";
const lsKey = "navCollapsed";
const navbar = document.querySelector(".nav");
const navCollapser = document.getElementById("menu_btn_div");
const navCollapserBtn = document.getElementById("menu_btn");
const logout_btn = document.getElementById("logout_btn");

const nav_elements = document.querySelectorAll(".nav_elements");

const main = document.querySelector(".main"); 
const main_big = "main-big-width";


if (localStorage.getItem(lsKey) === "true") {
    navbar.classList.add(collapsedClass);
    main.classList.add(main_big);

    navCollapser.classList.add("ms-3");
    navCollapserBtn.classList.add("fa-rotate-90");
    logout_btn.classList.add("ms-3");

    nav_elements.forEach(element => {
        element.classList.add(nav_collapsed_element)
    });
}

navCollapser.addEventListener("click", () => {
    navbar.classList.toggle(collapsedClass);
    main.classList.toggle(main_big);

    navCollapser.classList.toggle("ms-3");
    navCollapserBtn.classList.toggle("fa-rotate-90");
    logout_btn.classList.toggle("ms-3");

    nav_elements.forEach(element => {
        element.classList.toggle(nav_collapsed_element)
    });

    localStorage.setItem(lsKey, navbar.classList.contains(collapsedClass));
}); 