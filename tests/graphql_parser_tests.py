# -*- coding: utf-8 -*-
from nose.tools import *
from pypeg2 import parse

import graphql_parser as gqlp

from graphql_parser.parser import number, Arguments, Field, Block, Call


def test_number():
    assert parse('1', number) == '1'
    assert parse('1234', number) == '1234'
    assert parse('-34', number) == '-34'


def test_arguments():
    assert parse('1,2,3', Arguments) == ['1', '2', '3']
    assert parse('1,2 ,3 ', Arguments) == ['1', '2', '3']


def test_field():
    assert parse('test', Field).name == 'test'


def test_block():
    assert [f.name for f in parse('{a,b,c}', Block)] == ['a', 'b', 'c']


def test_call():
    call = parse('test(3, 4) { a, b, c }', Call)
    assert [f.name for f in call.names()] == ['test']
    assert call.arguments() == ['3', '4']
    assert [f.name for f in call.body()] == ['a', 'b', 'c']


def test_multi_call():
    call = parse('test.method(1) { a }', Call)
    assert [f.name for f in call.names()] == ['test', 'method']
    assert call.arguments() == ['1']
    assert [f.name for f in call.body()] == ['a']


def test_all():
    block = parse('{a, test.method(1) { b }, c}', Block)


def test_transform():
    assert gqlp.parse('{ a, b, c }') == {
        'type': 'block',
        'children': 'a b c'.split()
    }
