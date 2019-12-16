USERS = [
    {
        "_id": 44,
        "url": "http://initech.tokoin.io.com/api/v2/users/44.json",
        "external_id": "b5d38224-29c5-4aea-81a4-0da83d0a3f80",
        "name": "John Floyd",
        "alias": "Mr Gonzales",
        "created_at": "2016-06-08T10:26:06 -10:00",
        "active": False,
        "verified": False,
        "shared": False,
        "locale": "de-CH",
        "timezone": "Hong Kong",
        "last_login_at": "2014-11-04T08:34:49 -11:00",
        "email": "gonzalesfloyd@flotonic.com",
        "phone": "9894-382-253",
        "signature": "Don't Worry Be Happy!",
        "tags": [
            "Dunlo",
            "Greer",
            "Crown",
            "Strong"
        ],
        "suspended": False,
        "role": "end-user"
    },{
        "_id": 45,
        "url": "http://initech.tokoin.io.com/api/v2/users/45.json",
        "external_id": "6c1ee6e7-060b-4ceb-8729-e80cc6dcab66",
        "name": "Harper Sandoval",
        "created_at": "2016-04-27T12:43:57 -10:00",
        "active": True,
        "verified": False,
        "shared": False,
        "locale": "en-AU",
        "timezone": "Zaire",
        "last_login_at": "2012-11-26T03:11:27 -11:00",
        "email": "schroedersandoval@flotonic.com",
        "phone": "9594-242-912",
        "signature": "Don't Worry Be Happy!",
        "organization_id": 104,
        "tags": [
            "Hemlock",
            "Stewart",
            "Barrelville",
            "Martinsville"
        ],
        "suspended": False,
        "role": "admin"
    }
]

ORGANIZATIONS = [
{
    "_id": 104,
    "url": "http://initech.tokoin.io.com/api/v2/organizations/104.json",
    "external_id": "f6eb60ad-fe37-4a45-9689-b32031399f93",
    "name": "Xylar",
    "domain_names": [
      "anixang.com",
      "exovent.com",
      "photobin.com",
      "marqet.com"
    ],
    "created_at": "2016-03-21T10:11:18 -11:00",
    "details": "MegaCörp",
    "shared_tickets": False,
    "tags": [
      "Hendricks",
      "Mclaughlin",
      "Stephens",
      "Garner"
    ]
  },
  {
    "_id": 105,
    "url": "http://initech.tokoin.io.com/api/v2/organizations/105.json",
    "external_id": "52f12203-6112-4fb9-aadc-70a6c816d605",
    "name": "Koffee",
    "domain_names": [
      "farmage.com",
      "extrawear.com",
      "bulljuice.com",
      "enaut.com"
    ],
    "created_at": "2016-06-06T02:50:27 -10:00",
    "details": "MegaCorp",
    "shared_tickets": False,
    "tags": [
      "Jordan",
      "Roy",
      "Mckinney",
      "Frost"
    ]
  },
  {
    "_id": 106,
    "url": "http://initech.tokoin.io.com/api/v2/organizations/106.json",
    "external_id": "2355f080-b37c-44f3-977e-53c341fde146",
    "name": "Qualitern",
    "domain_names": [
      "gology.com",
      "myopium.com",
      "synkgen.com",
      "bolax.com"
    ],
    "created_at": "2016-07-23T09:48:02 -10:00",
    "details": "Artisân",
    "shared_tickets": True,
    "tags": [
      "Nolan",
      "Rivas",
      "Morse",
      "Conway"
    ]
  }
]

TICKETS = [
{
    "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
    "url": "http://initech.tokoin.io.com/api/v2/tickets/436bf9b0-1147-4c0a-8439-6f79833bff5b.json",
    "external_id": "9210cdc9-4bee-485f-a078-35396cd74063",
    "created_at": "2016-04-28T11:19:34 -10:00",
    "type": "incident",
    "subject": "A Catastrophe in Korea (North)",
    "description": "Nostrud ad sit velit cupidatat laboris ipsum nisi amet laboris ex exercitation amet et proident. Ipsum fugiat aute dolore tempor nostrud velit ipsum.",
    "priority": "high",
    "status": "pending",
    "submitter_id": 44,
    "assignee_id": 45,
    "organization_id": 104,
    "tags": [
      "Ohio",
      "Pennsylvania",
      "American Samoa",
      "Northern Mariana Islands"
    ],
    "has_incidents": False,
    "due_at": "2016-07-31T02:37:50 -10:00",
    "via": "web"
  },
  {
    "_id": "1a227508-9f39-427c-8f57-1b72f3fab87c",
    "url": "http://initech.tokoin.io.com/api/v2/tickets/1a227508-9f39-427c-8f57-1b72f3fab87c.json",
    "external_id": "3e5ca820-cd1f-4a02-a18f-11b18e7bb49a",
    "created_at": "2016-04-14T08:32:31 -10:00",
    "type": "incident",
    "subject": "A Catastrophe in Micronesia",
    "description": "Aliquip excepteur fugiat ex minim ea aute eu labore. Sunt eiusmod esse eu non commodo est veniam consequat.",
    "priority": "low",
    "status": "hold",
    "submitter_id": 71,
    "assignee_id": 38,
    "organization_id": 112,
    "tags": [
      "Puerto Rico",
      "Idaho",
      "Oklahoma",
      "Louisiana"
    ],
    "has_incidents": False,
    "due_at": "2016-08-15T05:37:32 -10:00",
    "via": "chat"
  }
]