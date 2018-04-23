/* nav.js

nav bar responsive JS */

window.onclick = event => {
  menu = document.getElementById("dropdown");
  if (event.target.matches("#dropbtn") || event.target.matches(".menu")) {
    if (menu.style.display == "none" || menu.style.display == "") {
      menu.style.display = "block";
    } else {
      menu.style.display = "none";
    }
  } else {
    menu.style.display = "none";
  }
};
