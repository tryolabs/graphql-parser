# graphql-parser

[![Build Status](https://travis-ci.org/tryolabs/graphql-parser.svg?branch=master)](https://travis-ci.org/tryolabs/graphql-parser)

This is a Python parser for React's GraphQL.

Lacking a specification, the parser was built to parse code along the lines of
examples and other implementations of GraphQL.

# Usage

```python
from graphql_parser import parse

QUERY = '''{
  user(1) {
    name,
    email,
    profile_pic.size(64) {
      date_added
    }
  }
}
'''

parse(QUERY)
```

Produces:

```python
{
  'type': 'block',
  'children': [
    {
      'type': 'call',
      'chain': ['user'],
      'arguments': ['1'],
      'body': {
        'type': 'block',
        'children': [
          'name',
          'email',
          {
            'type': 'call',
            'chain': ['profile_pic', 'size'],
            'arguments': ['64'],
            'body': {
              'type': 'block',
              'children': ['date_added']
            },
          }
        ]
      }
    }
  ]
}
```

# License

Copyright (c) 2015 [Tryolabs][tryo] SRL.

Released under the MIT license.

[tryo]: http://tryolabs.com/
