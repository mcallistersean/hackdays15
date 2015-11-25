/**
 * Created by sean on 11/24/15.
 */
import React from 'react';
import ReactDOM from 'react-dom';

var Speaker = React.createClass({
    getDefaultProps: function(){
        return {
            title: 'Test'
        };
    },
    render: function() {
        return <h1>{this.props.title}</h1>;
    }
});


ReactDOM.render(
    <Speaker />,
    document.getElementById('speaker')
);

