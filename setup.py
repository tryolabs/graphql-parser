
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'GraphQL parser for Python',
    'author': 'Tryolabs',
    'url': 'https://github.com/tryolabs/graphql-parser',
    'author_email': 'fernando@tryolabs.com.',
    'version': '0.1',
    'install_requires': ['pypeg2'],
    'packages': ['graphql_parser'],
    'scripts': [],
    'name': 'graphql-parser'
}

setup(**config)
