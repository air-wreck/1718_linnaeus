/* custom warning box, for prettier looks than a basic window.alert() */

function warn_user(text) {
  var alert_box = document.getElementById('alert');
  var alert_text = document.getElementById('alert-text');
  alert_text.innerHTML = text;
  alert_box.style.display = 'inline-block';
}
