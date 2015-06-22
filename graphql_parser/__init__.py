from graphql_parser.parser import Block
from graphql_parser.transform import transform_block
from pypeg2 import parse

def parse(string):
    transform_block(parse(string, Block))
