/* =============
File: pretty.js
Authors: Eric, Nelson, and Karena
Course: CSE
Description: module exporting various cosmetic and utility functions
============= */

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
    },

    // convenience function for a range from [start, end)
    range: (start, end) => {
      return [...Array(end - start).keys()].map(n => n + start);
    },

    // convenience strings for the alphabet
    alpha: {
        "lower": "abcdefghijklmnopqrstuvwxyz",
        "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      }
  };
}());
