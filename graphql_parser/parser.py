# -*- coding: utf-8 -*-
"""
This module implements the parser.

:copyright: (C) 2015 Tryolabs SRL
:license:   MIT
"""

import re
from pypeg2 import name, csl, List


class Field():
    """A field name in a query."""
    grammar = name()


number = re.compile(r'[+-]?(\d)+')


class Arguments(List):
    """Arguments to a call."""
    grammar = csl(number, separator=',')


class CallList(List):
    grammar = csl(Field, separator='.')


class Call(List):
    """A function call."""

    def names(self):
        return self[0]

    def arguments(self):
        return self[1]

    def body(self):
        return self[2]


class Block(List):
    """A curly brace delimited block."""
    grammar = '{', csl([Call, Field], separator=','), '}'


Call.grammar = CallList, '(', Arguments, ')', Block
