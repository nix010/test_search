A simple cli app for searching on json obj
# How to run
```bash
python3 main.py
```
- There is just pure python code so no need for `pip install`
- To test run `python tests.py`
- Make sure there are 3 data file in `data` folder: `users.json`, `tickets.json`, `organizations.json`
# Example

For normal fields
```bash
python3 main.py

0. Describe Columns (no search)
1. Users
2. Ticket
3. Organization
Input type to search as a number or type "exit" to close: 1
Input the field to search: name
Input the value to search: Russo Vincent
[{'_id': 22,
  'active': True,
  'alias': 'Miss Cohen',
  'created_at': '2016-01-28T08:49:17 -11:00',
  'email': 'cohenvincent@flotonic.com',
  'external_id': 'bf313bac-e4b1-46a3-a7ee-7cc584b7cbb8',
  'last_login_at': '2014-07-30T03:32:49 -10:00',
  'locale': 'en-AU',
  'name': 'Russo Vincent',
  'organization_id': 124,
  'organization_name': 'Bitrex',
  'phone': '8895-892-293',
  'role': 'end-user',
  'shared': False,
  'signature': "Don't Worry Be Happy!",
  'suspended': False,
  'tags': ['Veyo', 'Highland', 'Kiskimere', 'Hoehne'],
  'timezone': 'Qatar',
  'url': 'http://initech.tokoin.io.com/api/v2/users/22.json',
  'verified': False}]
Have 1 results matched
==================
Search again ?(y/n): 

```

For bool fields

```bash
python3 main.py

0. Describe Columns (no search)
1. Users
2. Ticket
3. Organization
Input type to search as a number or type "exit" to close: 3
Input the field to search: shared_tickets
Input the value to search: true

...
Have 10 results matched
==================
Search again ?(y/n):
```

For empty or invalid fields

```bash
python3 main.py

0. Describe Columns (no search)
1. Users
2. Ticket
3. Organization
Input type to search as a number or type "exit" to close: 1
Input the field to search: name
Input the value to search: xxx
No results found for "user" with "name" value of "xxx"
==================
Search again ?(y/n):
```

Describe

```bash
0. Describe Columns
1. Users
2. Ticket
3. Organization
Input type to search as a number or type "exit" to close: 0
Column for search User :
------------------
_id
url
external_id
name
alias
created_at
active
verified
shared
locale
timezone
last_login_at
email
phone
signature
organization_id
tags
suspended
role
------------------
Column for search Organization :
------------------
_id
url
external_id
name
domain_names
created_at
details
shared_tickets
tags
------------------
Column for search Ticket :
------------------
_id
url
external_id
created_at
type
subject
description
priority
status
submitter_id
assignee_id
organization_id
tags
has_incidents
due_at
via
------------------
0. Describe Columns
1. Users
2. Ticket
3. Organization
Input type to search as a number or type "exit" to close:

```
