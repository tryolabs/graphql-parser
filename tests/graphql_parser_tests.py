# -*- coding: utf-8 -*-
from nose.tools import *
from pypeg2 import parse

from graphql_parser.parser import number, Arguments, Field

def test_number():
    assert parse("1", number) == '1'
    assert parse("1234", number) == '1234'
    assert parse("-34", number) == '-34'

def test_arguments():
    assert parse("1,2,3", Arguments) == ['1', '2', '3']
    assert parse("1,2 ,3 ", Arguments) == ['1', '2', '3']

def test_field():
    assert parse("test", Field).name == 'test'
