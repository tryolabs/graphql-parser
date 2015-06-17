# -*- coding: utf-8 -*-
"""
This module implements the parser.

:copyright: (C) 2015 Tryolabs SRL
:license:   MIT
"""

from pypeg2 import name

class Node(object):
    """Base class of node objects."""

class Field(Node):
    """A field name in a query."""
    grammar = name()

class Block(object):
    """A curly brace delimited block."""
    grammar = "{", csl(Node), "}"
