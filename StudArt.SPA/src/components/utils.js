import React from "react";

export const required_field = value => {
	if (!value) {
		return (<div className="text-danger"><small>This field is required.</small></div>);
	}
};

export const getResponseMessage = (r) => {
	return (r.response && r.response.data && r.response.data.message) || r.message || r.data.message || r.toString();
}