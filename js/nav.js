/* nav.js

nav bar responsive JS */

// load common navbar when document loads
window.addEventListener("load", event => {
  document.body.innerHTML = `<div class="nav-bar">
    <ul>
      <div style="float: left;">
        <li><span><b>Linnaeus</b></span></li>
      </div>
      <div style="float: right;">
        <li><a href="home.html">Home</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="pedigree.html">Pedigree</a></li>
        <li><a href="punnett.html">Punnett Square</a></li>
        <li><a href="contact.html">Contact</a></li>
      </div>
      <div style="float: right;" class="narrow-menu">
        <!-- this is such a sketchy way to make a menu button -->
          <button id="dropbtn">
            <div class="menu"></div>
            <div class="menu"></div>
            <div class="menu"></div>
          </button>

          <!-- the actual dropdown menu -->
          <div id="dropdown">
            <a href="home.html">Home</a>
            <a href="about.html">About</a>
            <a href="pedigree.html">Pedigree</a>
            <a href="punnett.html">Punnett Square</a>
            <a href="contact.html">Contact</a>
          </div>
      </div>
    </ul>
  </div>` + document.body.innerHTML;
});

// respond to clicks when in small mode
window.addEventListener("click", event => {
  menu = document.getElementById("dropdown");
  if (event.target.matches("#dropbtn") || event.target.matches(".menu")) {
    if (menu.style.display === "none" || menu.style.display === "") {
      menu.style.display = "block";
    } else {
      menu.style.display = "none";
    }
  } else {
    menu.style.display = "none";
  }
});