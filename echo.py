#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import sys

"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "???"


import sys


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    # Create and define your parser engine here, but DON'T PARSE.
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.'
    )
    parser.add_argument('text', help='text to be manipulated')
    parser.add_argument('-u', '--upper', action='store_true', help='convert text to uppercase')
    parser.add_argument('-l', '--lower', action='store_true', help='convert text to lowercase')
    parser.add_argument('-t', '--title', action='store_true', help='convert text to titlecase')

    return parser


def main(args):
    """Implementation of echo"""
    # Needs more work here
    parser = create_parser()
    echo_input = parser.parse_args(args)
    result = echo_input.text
    if echo_input.upper:
        result = echo_input.text.upper()
    if echo_input.lower:
        result = echo_input.text.lower()
    if echo_input.title:
        result = echo_input.text.title()
    
    return result


if __name__ == '__main__':
    pass
