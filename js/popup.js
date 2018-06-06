/* =============
File: popup.js
Authors: Eric, Nelson, and Karena
Course: CSE
Description: allows for popup help div on appropriate pages
============= */

const toggle = div_id => {
  var el = document.getElementById(div_id);
  if (el.style.display == "none") el.style.display = "block";
  else el.style.display = "none";
}
const blanket_size = popUpDivVar => {
  blanket_height = document.body.parentNode.scrollHeight;
  var blanket = document.getElementById("blanket");
  blanket.style.height = blanket_height + "px";
  var popUpDiv = document.getElementById(popUpDivVar);
  popUpDiv_height=blanket_height/2-(blanket_height*.2);
  popUpDiv.style.top = popUpDiv_height + "px";
}
const window_pos = popUpDivVar => {
  var popUpDiv = document.getElementById(popUpDivVar);
}
const popup = windowname => {
  blanket_size(windowname);
  window_pos(windowname);
  toggle("blanket");
  toggle(windowname);
}
