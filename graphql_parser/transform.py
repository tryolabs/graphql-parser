# -*- coding: utf-8 -*-
"""
Transform the result of the parser into a dictionary.

:copyright: (C) 2015 Tryolabs SRL
:license:   MIT
"""

from graphql_parser.parser import Call


def transform_block(block):
    """Transform a block and its children into a dictionary."""
    return {
        'type': 'block',
        'children': [transform_child(child) for child in block]
    }


def transform_child(child):
    """Transform an element of a block."""
    # Is it a field name or a call?
    if isinstance(child, Call):
        return transform_call(child)
    else:
        return str(child.name)


def transform_call(call):
    """Transform a call into a dictionary."""
    return {
        'type': 'call',
        'chain': [str(fn.name) for fn in call.names()],
        'arguments': [str(arg) for arg in call.arguments()],
        'body': transform_block(call.body())
    }
