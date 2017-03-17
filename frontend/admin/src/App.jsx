import React, { Component } from "react";
import Items from "./Items/Items";

class App extends Component {
  render() {
    return (
      <div>
        <Items items={this.props.items}/>
      </div>
    );
  }
}

export default App;
