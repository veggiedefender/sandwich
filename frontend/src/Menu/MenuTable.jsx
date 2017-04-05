import React from "react";

function split(items) {
  var length = items.length;
  var middle = Math.floor(length / 2);
  return [
    items.slice(0, middle),
    items.slice(length - middle, length)
  ];
}

function price(item) {
  if (item.price.toFixed(2) === item.price_half.toFixed(2)) {
    return item.price.toFixed(2);
  }
  return item.price_half.toFixed(2) + "/" + item.price.toFixed(2);
}

var MenuTable = React.createClass({
  render: function() {
    var items = split(this.props.items);
    
    return (      
      <div className="row">
        {items.map((half, key) => 
          <div className="six columns" key={key}>
            <table className="u-full-width">
              <thead>
                <tr>
                  <th>Item</th>
                  <th className="price">Price</th>
                </tr>
              </thead>

              <tbody>
                {half.map((item, key) =>
                  <tr key={item.id} id={item.id} onClick={this.props.onClick}>
                    <td>{item.name}</td>
                    <td className="price">
                      ${price(item)}
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        )}
      </div>
    );
  }
});

export default MenuTable;