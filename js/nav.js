/* =============
File: nav.js
Authors: Eric, Nelson, and Karena
Course: CSE
Description: adds navigation bar to an HTML page when included as <script>
============= */

// do setup on page load
window.addEventListener("load", event => {

  // load common navbar when document loads
  document.body.innerHTML = `<div class="nav-bar">
    <ul>
      <div style="float: left;">
        <li><span><b>Linnaeus</b></span></li>
      </div>
      <div style="float: right;">
        <li>
          <a href="home.html">Home</a>
          <div class="underscore"></div>
        </li>
        <li>
          <a href="about.html">About</a>
          <div class="underscore"></div>
        </li>
        <li>
          <a href="pedigree.html">Pedigree</a>
          <div class="underscore"></div>
        </li>
        <li>
          <a href="punnett.html">Punnett Square</a>
          <div class="underscore"></div>
        </li>
        <li>
          <a href="contact.html">Contact</a>
          <div class="underscore"></div>
        </li>
        <li>
          <a href="faq.html">FAQs</a>
          <div class="underscore"></div>
        </li>
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
            <a href="faq.html">FAQs</a>
          </div>
      </div>
    </ul>
  </div>` + document.body.innerHTML;
  Array.from(document.getElementsByClassName("underscore")).forEach(div => {
    div.style.width = (div.parentNode.offsetWidth-1) + "px";
  });

  // respond to clicks when in small mode
  // this technically should be in here, although it's not necessary
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
});
