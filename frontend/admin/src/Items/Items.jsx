import React, { Component } from 'react';

class Items extends Component {
  render() {
    var items = this.props.items;
    return (
      <div>
        {
          items.map((item) => 
            <p key={item.id}>{item.name}</p>
          )
        }
      </div>
    );
  }
}

export default Items;
