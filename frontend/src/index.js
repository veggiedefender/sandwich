import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

import normalize from "./css/normalize.css";
import skeleton from "./css/skeleton.css";
import styles from "./css/index.css";

fetch("/items/")
  .then(function(response) {
    return response.json();
  }).then(function(json) {
    render_app(json);
  }).catch(function(ex) {
    alert("Failed to get menu.");
  });

function render_app(json) {
  ReactDOM.render(<App menu={json} />,
    document.getElementById("app"));
}
