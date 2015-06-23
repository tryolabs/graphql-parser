import pypeg2

from graphql_parser.parser import Block
from graphql_parser.transform import transform_block


def parse(string):
    """Parse a GraphQL string into a dictionary."""
    return transform_block(pypeg2.parse(string, Block))
