import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

fetch("http://localhost:5000/items/")
  .then(function(response) {
    return response.json();
  }).then(function(json) {
    render_app(json);
  }).catch(function(ex) {
    alert("Failed to get menu.");
    console.log(ex);
  });

function render_app(json) {
  ReactDOM.render(<App items={json} />,
    document.getElementById("app"));
}
