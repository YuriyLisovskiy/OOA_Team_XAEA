import React from "react";

export const required_field = value => {
	if (!value) {
		return (<div className="text-danger"><small>This field is required.</small></div>);
	}
};

export const getResponseMessage = (r) => {
	return r.toString();
}

export const getMessageFromJson = (data) => {
	if (data.hasOwnProperty('message')) {
		return data.message;
	}

	return data.toString();
}
