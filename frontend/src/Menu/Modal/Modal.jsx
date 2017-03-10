import React from "react";
import ModalForm from "./ModalForm";

var Modal = React.createClass({
  render: function() {
    var item = this.props.item;
    return (
      <div class="modal-container">
        <div className="backdrop" onClick={this.props.cancel}></div>
        <div className="modal-content">
          <i className="material-icons close-button" onClick={this.props.cancel}>clear</i>
          <h1>Customize your {item.name}</h1>
          <ModalForm
            item={item}
            cancel={this.props.cancel}
            submit={this.props.addItem}
          />
        </div>
      </div>
    );
  }
});

export default Modal;