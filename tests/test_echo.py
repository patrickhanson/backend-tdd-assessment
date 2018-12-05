#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo

# Your test case class goes here
class TestEcho(unittest.TestCase):

    def setUp(self):
        self.parser = echo.create_parser()
    
    def test_upper_short(self):
        arg_list = ['-u', 'hello']
        namespace = self.parser.parse_args(arg_list)
        # Was the '-u' parsed and converted into a namespace attribute?
        self.assertTrue(namespace.upper)
        # Did the program transform our text to uppercase?
        self.assertEquals(echo.main(arg_list), 'HELLO')

    def test_upper_long(self):
        arg_list = ['--upper', 'hello']
        namespace = self.parser.parse_args(arg_list)
        # Was the '-u' parsed and converted into a namespace attribute?
        self.assertTrue(namespace.upper)
        # Did the program transform our text to uppercase?
        self.assertEquals(echo.main(arg_list), 'HELLO')

    def test_lower_short(self):
        arg_list = ['-l', 'HELLO']
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.lower)
        self.assertEquals(echo.main(arg_list), 'hello')

    def test_lower_long(self):
        arg_list = ['--lower', 'HELLO']
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.lower)
        self.assertEquals(echo.main(arg_list), 'hello')

    def test_title_short(self):
        arg_list = ['-t', 'hello']
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.title)
        self.assertEquals(echo.main(arg_list), 'Hello')

    def test_title_long(self):
        arg_list = ['--title', 'hello']
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.title)
        self.assertEquals(echo.main(arg_list), 'Hello')


if __name__ == '__main__':
    unittest.main()
