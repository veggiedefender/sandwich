import React from "react";
import ModalForm from "./ModalForm";

var Modal = React.createClass({
  render: function() {
    var item = this.props.item;
    return (
      <div id="modal">
        <div className="container">
          <div className="twelve columns modal-content">
            <h1>Customize your {item.name}</h1>
            <ModalForm
              item={item}
              cancel={this.props.cancel}
              submit={this.props.addItem}
            />
          </div>
        </div>
      </div>
    );
  }
});

export default Modal;