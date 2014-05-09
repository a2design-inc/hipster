Hipster
=======

Simple Python module for the HipChat API

Description
-----------

Simple Python library for the `HipChat API <https://www.hipchat.com/docs/api>`. 

Dependencies
------------
Standart library and urllib3

Python version
------------
 2.6, 2.7

Usage
-----

Install::

```bash
git clone https://github.com/a2design-company/hipster
python setup.py install
````

Instantiate::
```python
from hipster import Hipster
hipchat = Hipster(Your token)
```

Call API methods::

```python
hipchat.create_room(name='My room', owner_user_id=1, topic='Hello, room!')
```
or

```python
hipchat.create_room({
 'name': 'My another room',
 'owner_user_id': 1,
 'topic': 'Hello, room!'
})
```
Attention:: If you use named arguments in methods `send_messages()` and `set_room_topic()` use the 'sender' argument instead 'from': `

```python
hipchat.send_messages(room_id='your room id', sender='your user id', message='Hello, room!')
```
or
```python
hip.send_messages({
    'sender':'your user id', 
    'message':'Hello world!', 
    'room_id':'your room id'})
```
In last case you may use 'from' if you need.

```python
hip.send_messages({
    'from':'your user id', 
    'message':'Hello world!', 
    'room_id':'your room id'})
```

All available API methods::

```python
create_room()
delete_room()
get_messages()
get_rooms_list()
send_messages()
set_room_topic()
get_room_details()
create_user()
delete_user()
get_users_list()
get_users_details()
undelete_user()
update_user_info()




