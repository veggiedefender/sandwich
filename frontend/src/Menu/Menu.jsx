import React from "react";
import MenuTable from "./MenuTable";
import Modal from "./Modal/Modal"

function splitCategories(items) {
  var renderOrder = [
    "HAVEN SPECIALTIES",
    "COLD HOAGIES",
    "HOT HOAGIES",
    "FROM THE GRILL"
  ];
  return renderOrder.map(category => (
    {
      name: category,
      items: items.filter(item => (item.category === category))
    }
  ));
}

var Menu = React.createClass({
  getInitialState: function() {
    return {
      modalOpen: false,
      currentItem: null
    }
  },
  showModal: function(e) {
    this.setState({
      modalOpen: true,
      currentItem: this.props.menu[e.currentTarget.id]
    })
  },
  hideModal: function() {
    this.setState({
      modalOpen: false
    });
  },
  addItem: function(item) {
    this.props.addItem(item);
    this.hideModal();
  },
  render: function() {
    var categories = splitCategories(this.props.menu);
    var modal;
    if (this.state.modalOpen) {
      modal = (
        <Modal
          item={this.state.currentItem}
          onClick={this.showModal}
          cancel={this.hideModal}
          addItem={this.addItem}
        />);
    }
    return (
      <div>
        <div className="eight columns">
          <div className="container">
            <h1><b>THUNCH</b></h1>
            {categories.map((category, key) =>
              <div key={key}>
                <h3>{category.name}</h3>
                <MenuTable items={category.items} onClick={this.showModal}/>
              </div>
            )}

            <div className="footer">
              <span><a href="http://jli.host/">Jesse Li</a></span>/
              <span><a href="https://github.com/veggiedefender/sandwich">Source</a></span>/
              <span><a href="https://github.com/veggiedefender/sandwich/issues/new">Feedback</a></span>
            </div>
          </div>

        </div>
        {modal}
      </div>
    );
  }
});

export default Menu;