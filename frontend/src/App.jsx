import React from "react";
import Menu from "./Menu/Menu";
import Cart from "./Cart/Cart";
import Complete from "./Cart/Complete";

var newId = (function() {
  var id = 0;
  return () => id++;
}());

var App = React.createClass({
  getInitialState: function() {
    return {
      items: []
    };
  },
  addItem: function(item) {
    var itemInfo = this.props.menu[item.id];
    item.name = itemInfo.name;
    item.price = item.in_half ? itemInfo.price_half : itemInfo.price;
    item.removalId = newId();
    this.setState({
      items: [ ...this.state.items, item ]
    });
  },
  removeItem: function(removalId) {
    console.log(removalId);
    this.setState({
      items: this.state.items.filter(item => item.removalId !== removalId)
    });
  },
  render: function() {
    var hasItems = (this.state.items.length > 0);
    var complete;
    if (hasItems) {
      complete = <Complete />;
    }
    return (
      <div>        
        <Menu addItem={this.addItem} menu={this.props.menu} />
        <Cart items={this.state.items} removeItem={this.removeItem} hasItems={hasItems} />
        {complete}
      </div>
    );
  }
});

export default App;