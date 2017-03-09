import React from "react";
import ReCAPTCHA from "react-google-recaptcha";

var SubmitForm = React.createClass({
  getInitialState: function() {
    return {
      recaptcha: ""
    }
  },
  updateRecaptcha: function(captcha) {
    this.setState({
      recaptcha: captcha
    });
  },
  submit: function(e) {
    e.preventDefault();

    var data = {
      "g-recaptcha-response": this.state.recaptcha,
      email: this.email.value,
      order: this.props.items
    };
    if (this.state.recaptcha !== "") {
      fetch("/submit",
      {
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            "x-csrftoken": document.getElementById("csrf").content
          },
          credentials: 'same-origin',
          method: "POST",
          body: JSON.stringify(data)
      })
      .then(function(response) {
        return response.json();
      }).then(function(json) {
        if (json.success) {
          window.location.replace("/complete/");
        } else {
          alert("Only Princeton emails are allowed!");
        }
      })
      .catch(function(response) {
        alert("Error sending order. Try refreshing the page.")
      })

    }
  },
  render: function() {
    var items = this.props.items;
    var total = items.reduce(((sum, item) =>
      sum + item.price), 0
    );
    return (
      <div>
          <h4>TOTAL - ${total.toFixed(2)}</h4>
          <form onSubmit={this.submit} action="#" method="POST">
              <div className="row">
                  <label htmlFor="email">Email (Princeton email required)</label>
                  <input
                    className="u-full-width"
                    type="email"
                    ref={(input) => this.email = input}
                    placeholder="example@princeton.edu"
                    name="email"
                    required
                  />
              </div>
              <ReCAPTCHA
                ref="recaptcha"
                sitekey={document.getElementById("recaptcha-key").content}
                onChange={this.updateRecaptcha}
              />
              <input id="submit" className="button-primary" type="submit" value="Submit" />
          </form>
      </div>
    );
  }
});

export default SubmitForm;