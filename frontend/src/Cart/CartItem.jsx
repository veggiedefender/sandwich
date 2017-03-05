import React from "react";

var CartItem = React.createClass({
  onClickHandler: function() {
    this.props.onClick(this.props.item.removalId);
  },
  render: function() {
    var item = this.props.item;
    var in_half;
    if (item.in_half) {
      in_half = <p><b>Cut in half</b></p>;
    }
    return (
      <div className="order" onClick={this.onClickHandler}>
        <h4>{item.name} - ${item.price.toFixed(2)}</h4>
        {in_half}
        <p>{item.notes}</p>
        <hr />
      </div>
    );
  }
});

export default CartItem;