# -*- coding: utf-8 -*-
"""
This module implements the parser.

:copyright: (C) 2015 Tryolabs SRL
:license:   MIT
"""

import re
from pypeg2 import name, csl, List

number = re.compile(r'[+-]?(\d)+')

class Arguments(List):
    """Arguments to a call."""
    grammar = csl(number)

class Node(object):
    """Base class of node objects."""

class Field(Node):
    """A field name in a query."""
    grammar = name()

class Block(object):
    """A curly brace delimited block."""
    grammar = '{', csl(Node), '}'

class Call(Node):
    """A function call."""
    grammar = csl(name(), separator='.'), '(', Arguments, ')', Block
