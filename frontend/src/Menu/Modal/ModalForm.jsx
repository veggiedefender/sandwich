import React from "react";

var ModalForm = React.createClass({
  getInitialState: function() {
    return {
      notes: "",
      in_half: false
    }
  },
  updateNotes: function(e) {
    this.setState({
      notes: e.target.value
    });
  },
  toggleHalf: function(e) {
    this.setState({
      in_half: e.target.checked
    });
  },
  submit: function() {
    this.props.submit({
      id: this.props.item.id,
      notes: this.state.notes,
      in_half: this.state.in_half
    });
  },
  render: function() {
    var item = this.props.item;
    var checkBox;
    if (item.price !== item.price_half) {
      checkBox = (
        <label id="in_half_container">
          <input type="checkbox" value={this.state.in_half} onChange={this.toggleHalf}/>
          <span className="label-body">Only half:
            ${(item.price_half).toFixed(2)}
            {" "}
            (-${(item.price - item.price_half).toFixed(2)})
          </span>
        </label>
      );
    }
    return (
      <form>
        {checkBox}
        <div className="row">
            <label htmlFor="notes">Notes</label>
            <textarea
              value={this.state.notes} onChange={this.updateNotes}
              className="u-full-width"
              placeholder="Add five slices of ham but make the third one from the left 67% transparent."
            ></textarea>
        </div>
        <input type="button" className="button-primary" value="Submit" onClick={this.submit}/>
        {" "}
        <input type="button" value="Cancel" onClick={this.props.cancel}/>
      </form>
    );
  }
});

export default ModalForm;