import pypeg2

from graphql_parser.parser import Block
from graphql_parser.transform import transform_block


def parse(string):
    transform_block(pypeg2.parse(string, Block))
