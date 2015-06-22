# -*- coding: utf-8 -*-
"""
Transform the result of the parser into a dictionary.

:copyright: (C) 2015 Tryolabs SRL
:license:   MIT
"""

from graphql_parser.parser import Call


def transform_block(block):
    return {
        'type': 'block',
        'children': [transform_child(child) for child in block]
    }


def transform_child(child):
    # Is it a field name or a call?
    if isinstance(child, Call):
        return transform_call(child)
    else:
        return str(child.name)


def transform_call(call):
    return {
        'type': 'call',
        'chain': call.names(),
        'arguments': call.arguments(),
        'body': transform_block(call.body())
    }
