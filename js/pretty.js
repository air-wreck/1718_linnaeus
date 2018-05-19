/* pretty.js

various functions for improving looks */

/* the function closure isn't really necessary for now,
   but we'll keep it because it's cool */
const pretty = (function () {
  return {
    // custom warning box, for prettier looks than a basic window.alert()
    warn_user: text => {
      var alert_box = document.getElementById("alert");
      var alert_text = document.getElementById("alert-text");
      alert_text.innerHTML = text;
      alert_box.style.display = "inline-block";
    },

    // returns a pretty input field
    // optionally style with input's outerHTML
    input: input_outerHTML => {
      let div = document.createElement("div");
      div.className = "input-wrap";
      div.innerHTML = `<input ${input_outerHTML}>
        <div class="overbar"></div>
        <div class="underbar"></div>`;
      return div;
    }
  };
}());
