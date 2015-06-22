# -*- coding: utf-8 -*-
"""
Transform the result of the parser into a dictionary.

:copyright: (C) 2015 Tryolabs SRL
:license:   MIT
"""

from graphql_parser.parser import Field

def transform_block(block):
    return {
        'type': 'block',
        'children': [transform_child(child) for child in block]
    }


def transform_child(child):
    # Is it a field name or a call?
    if child is Field:
        return child.name()
    else:
        return transform_call(child)


def transform_call(call):
    return {
        'type': 'call',
        'chain': call.names(),
        'arguments': call.arguments(),
        'body': transform_block(call.body())
    }
