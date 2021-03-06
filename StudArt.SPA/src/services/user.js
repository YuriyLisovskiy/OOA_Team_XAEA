import BaseService from "./base";

class UserService extends BaseService {

	constructor() {
		super();
		this._URL_CORE = this._BASE_URL + '/core';
		this._URL_USERS = this._URL_CORE + '/users';
		this._URL_ADMIN_USERS = this._URL_CORE + '/admin/users';
		this._URL_SELF = this._URL_USERS + '/self';
	}

	// returns:
	//  {
	//    "id": <int>,
	//    "first_name": <string>,
	//    "last_name": <string>,
	//    "username": <string>,
	//    "email": <string>,
	//    "avatar_link": <string (full url)>,
	//    "is_superuser": <bool>,
	//    "rating": <float>,
	//    "is_banned": <bool>,
	//    "is_subscribed": <bool>,
	//    "is_blocked": <bool>,
	//    "show_full_name": <bool>,
	//    "show_rating": <bool>,
	//    "show_subscriptions": <bool>
	//  }
	getUser = (id, handler) => {
		return this.get({
			url: this._URL_USERS + '/' + id.toString()
		}, handler);
	}

	// returns:
	//  {
	//    "id": <int>,
	//    "first_name": <string>,
	//    "last_name": <string>,
	//    "username": <string>,
	//    "email": <string>,
	//    "avatar_link": <string (full url)>,
	//    "is_superuser": <bool>,
	//    "rating": <float>,
	//    "is_banned": <bool>,
	//    "is_subscribed": <bool>,
	//    "is_blocked": <bool>,
	//    "show_full_name": <bool>,
	//    "show_rating": <bool>,
	//    "show_subscriptions": <bool>
	//  }
	getMe = (handler) => {
		return this.get({url: this._URL_SELF}, handler);
	}

	// returns:
	//  {
	//    "first_name": <string>,
	//    "last_name": <string>,
	//    "avatar_link": <string> (full url),
	//    "show_full_name": <bool>,
	//    "show_rating": <bool>,
	//    "show_subscriptions": <bool>
	//  }
	editUser = (id, firstName, lastName, showFullName, showRating, showSubscriptions, handler) => {
		let data = {};
		if (firstName !== null) {
			data['first_name'] = firstName;
		}

		if (lastName !== null) {
			data['last_name'] = lastName;
		}

		if (showFullName !== null) {
			data['show_full_name'] = showFullName;
		}

		if (showRating !== null) {
			data['show_rating'] = showRating;
		}

		if (showSubscriptions !== null) {
			data['show_subscriptions'] = showSubscriptions;
		}

		this.put({
			url: this._URL_SELF + '/edit',
			data: data
		}, handler);
	}

	// returns:
	//  {
	//    "first_name": <string>,
	//    "last_name": <string>,
	//    "avatar_link": <string> (full url),
	//    "show_full_name": <bool>,
	//    "show_rating": <bool>,
	//    "show_subscriptions": <bool>
	//  }
	updateAvatar = (id, avatar, handler) => {
		let formData = new FormData();
		if (avatar) {
			formData.append('avatar', avatar);
		}

		this.put({
			url: this._URL_SELF + '/edit/avatar',
			data: formData,
			headers: {
				'Content-Type': 'multipart/form-data'
			}
		}, handler);
	}

	editEmail = (id, email, password, handler) => {
		this.put({
			url: this._URL_SELF + '/edit/email',
			data: {
				email: email,
				password: password
			}
		}, handler);
	}

	editPassword = (id, oldPassword, newPassword, handler) => {
		this.put({
			url: this._URL_SELF + '/edit/password',
			data: {
				old_password: oldPassword,
				new_password: newPassword
			}
		}, handler);
	}

	deactivateMe = (id, password, handler) => {
		this.put({
			url: this._URL_SELF + '/deactivate',
			data: {
				password: password
			}
		}, handler);
	}

	// returns:
	// {}
	blockAuthor = (authorId, handler) => {
		this.put({
			url: this._URL_SELF + '/block/author',
			data: {
				'author_pk': authorId
			}
		}, handler);
	}

	// returns:
	// {}
	unblockAuthor = (authorId, handler) => {
		this.put({
			url: this._URL_SELF + '/unblock/author',
			data: {
				'author_pk': authorId
			}
		}, handler);
	}

	// returns:
	// {}
	subscribeToAuthor = (authorId, handler) => {
		this.put({
			url: this._URL_SELF + '/subscribe',
			data: {
				'author_pk': authorId
			}
		}, handler);
	}

	// returns:
	// {}
	unsubscribeFromAuthor = (authorId, handler) => {
		this.put({
			url: this._URL_SELF + '/unsubscribe',
			data: {
				'author_pk': authorId
			}
		}, handler);
	}

	// returns:
	//  {
	//    "count": <int (total pages quantity)>,
	//    "next": <string (link to load next page)>,
	//    "previous": <string (link to load previous page)>,
	//    "results": [
	//      {
	//        "id": <int>,
	//        "first_name": <string>,
	//        "last_name": <string>,
	//        "username": <string>,
	//        "email": <string>,
	//        "avatar_link": <string (full url)>,
	//        "is_superuser": <bool>,
	//        "rating": <float>,
	//        "is_banned": <bool>,
	//        "is_subscribed": <bool>,
	//        "is_blocked": <bool>,
	//        "show_full_name": <bool>,
	//        "show_rating": <bool>,
	//        "show_subscriptions": <bool>
	//      },
	//      ...
	//    ]
	//  }
	getSubscriptions = (authorId, page, handler) => {
		let data = {};
		if (page) {
			data.page = page;
		}

		this.get({
			url: this._URL_USERS + '/' + authorId.toString() + '/subscriptions',
			data: data
		}, handler);
	}

	// returns:
	//  {
	//    "count": <int (total pages quantity)>,
	//    "next": <string (link to load next page)>,
	//    "previous": <string (link to load previous page)>,
	//    "results": [
	//      {
	//        "id": <int>,
	//        "first_name": <string>,
	//        "last_name": <string>,
	//        "username": <string>,
	//        "email": <string>,
	//        "avatar_link": <string (full url)>,
	//        "is_superuser": <bool>,
	//        "rating": <float>,
	//        "is_banned": <bool>,
	//        "is_subscribed": <bool>,
	//        "is_blocked": <bool>,
	//        "show_full_name": <bool>,
	//        "show_rating": <bool>,
	//        "show_subscriptions": <bool>
	//      },
	//      ...
	//    ]
	//  }
	getBlacklist = (page, handler) => {
		let data = {};
		if (page) {
			data.page = page;
		}

		this.get({
			url: this._URL_SELF + '/blacklist',
			data: data
		}, handler);
	}

	// returns:
	//  [
	//    {
	//      "text": <string>
	//    },
	//    ...
	//  ]
	getMostUsedTagsForAuthor = (authorId, limit, handler) => {
		let data = {};
		if (limit) {
			data.limit = limit;
		}

		this.get({
			url: this._URL_USERS + '/' + authorId.toString() + '/tags/top',
			data: data
		}, handler);
	}

	// Administration privileges are required.
	// returns:
	// {}
	banUser = (userId, handler) => {
		this.put({
			url: this._URL_ADMIN_USERS + '/' + userId.toString() + '/ban'
		}, handler);
	}

	// Administration privileges are required.
	// returns:
	// {}
	unbanUser = (userId, handler) => {
		this.put({
			url: this._URL_ADMIN_USERS + '/' + userId.toString() + '/unban'
		}, handler);
	}
}

export default new UserService();
