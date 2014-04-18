
api_func = {
	'create_room': {
		'params': [
			'name',
			'owner_user_id',
			'privacy',
			'topic',
			'guest_access',
			'format'
		],
		'required': [
			'name',
			'owner_user_id',
		],
		'method': 'POST',
		'API_url': 'rooms/create'
	},

	'delete_rooms': {
		'params': [
			'room_id',
			'format'
		],
		'required': [
			'room_id'
		],
		'method': 'POST',
		'API_url': 'rooms/delete'
	},
	

	'get_messages': {
		'params': [
			'room_id',
			'date',
			'timezone'
			'format'
		],
		'required': [
			'room_id',
			'date'
		],
		'method': 'GET',
		'API_url': 'rooms/history'
	},

	'get_rooms_list': {
		'params': [
			'format'
		],
		'required': [],
		'method': 'GET',
		'API_url': 'rooms/list'
	},

	'send_messages': {
		'params': [
			'room_id', 
			'message',
			'message_from', 
			'message_format', 
			'notify', 
			'color', 
			'format'],
		'required': [
			'room_id', 
			'message',
			'message_from', 
		],
		 'method': 'POST',
		 'API_url': 'rooms/message'
	},

	'set_room_topic ': {
		'params': [
			'room_id',
			'topic',
			'from',
			'format'
		],
		'required': [
			'room_id',
			'topic',
			'from',
		],
		'method': 'POST',
		'API_url': 'rooms/topic'
	},

	'get_room_details ': {
		'params': [
			'room_id',
			'format'
		],
		'required': [
			'room_id',
		],
		'method': 'GET',
		'API_url': 'rooms/show'
	},
	
	'create_user': {
		'params': [
			'email', 
			'name', 
			'title', 
			'password', 
			'timezone', 
			'mention_name',  
			'is_group_admin',
			'format' ],
		'required':[
			'email', 
			'name', 
			'title', 
			'password', 
			'mention_name'  
		],
		'method': 'POST',
		'API_url': 'users/create'
	},
	'delete_user': {
		'params': [
			'user_id',
			'format'
		],
		'required': [
			'user_id',
		],
		'method': 'POST',
		'API_url': 'users/delete'
	},
	
	'get_users_list': {
		'params': [
			'include_deleted',
			'format'
		],
		'required': [],
		'method': 'GET',
		'API_url': 'users/list'
	},

	'get_users_details': {
		'params': [
			'user_id',
			'format'
		],
		'required': [
			'user_id',
		],
		'method': 'GET',
		'API_url': 'users/show'
	},

	'undelete_user': {
		'params': [
			'user_id',
			'format'
		],
		'required': [
			'user_id',
		],
		'method': 'POST',
		'API_url': 'users/undelete'
	},

	'update_user_info': {
		'params': [
			'user_id'
			'email', 
			'name', 
			'title', 
			'password', 
			'timezone', 
			'mention_name',  
			'is_group_admin',
			'format'
		],
		'required': [
			'email', 
			'name', 
			'title', 
			'password', 
			'mention_name'  
		],
		'method': 'POST',
		'API_url': 'users/update'
	}
}

