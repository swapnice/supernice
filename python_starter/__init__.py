#!/usr/bin/env python

import sys
from argparse import ArgumentParser, Namespace

__version__ = "0.0.1"

def parse_inputs() -> Namespace:
   """Parses the user program input"""
   parser = ArgumentParser(description='Add your arguments')
   parser.add_argument('name', help='Add a name')
   return parser.parse_args()

def main() -> int:
    """Build many objects to process into our algolia database"""
    arguments_namespace = parse_inputs()
    print(arguments_namespace.name)
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit