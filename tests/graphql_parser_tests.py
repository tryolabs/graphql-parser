# -*- coding: utf-8 -*-
from nose.tools import *
from pypeg2 import parse

from graphql_parser.parser import number

def test_arguments():
    assert parse("1", number) == '1'
