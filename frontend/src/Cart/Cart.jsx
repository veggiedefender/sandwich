import React from "react";
import CartItem from "./CartItem";
import SubmitForm from "./SubmitForm";

var Cart = React.createClass({
  render: function() {
    var items = this.props.items;
    var submitForm;
    if (this.props.hasItems) {
      submitForm = <SubmitForm items={items}/>;
    }
    return (
      <div className="four columns cart" id="order">
        <div className="container">
          <h1><b>YOUR ORDER</b></h1>
          {items.map((item, key) =>
            <CartItem item={item} key={key} onClick={this.props.removeItem}/>
          )}
          {submitForm}
        </div>
      </div>
    );
  }
});

export default Cart;