# -*- coding: utf-8 -*-
"""
This module implements the parser.

:copyright: (C) 2015 Tryolabs SRL
:license:   MIT
"""

import re
from pypeg2 import name, csl

number = re.compile(r"\d+")

class Arguments(object):
    """Arguments to a call."""
    grammar = csl(number)

class Call(object):
    """A function call."""
    grammar = name(), "(", Arguments, ")", Block

class Node(object):
    """Base class of node objects."""

class Field(Node):
    """A field name in a query."""
    grammar = name()

class Value(object):
    pass

class Block(object):
    """A curly brace delimited block."""
    grammar = "{", csl(Node), "}"
