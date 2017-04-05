import React from "react";
import ModalForm from "./ModalForm";

var Modal = React.createClass({
  render: function() {
    var item = this.props.item;
    return (
      <div className="modal-container">
        <div className="backdrop" onClick={this.props.cancel}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <i className="material-icons close-button" onClick={this.props.cancel}>clear</i>
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