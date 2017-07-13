#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests"""

import os
import unittest
import terraform_validate


class TestResources(unittest.TestCase):
    """Tests related to resources."""

    def setUp(self):
        self.path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), '.')
        self.validator = terraform_validate.Validator(self.path)

    def test_aws_instance(self):
        """Tests instance for tags."""
        tagged_resources = ['aws_instance']
        required_tags = ['Name']
        # required_tags = ['Name', 'Humppa']
        self.validator.resources(tagged_resources).property('tags'). \
            should_have_properties(required_tags)

if __name__ == '__main__':
    SUITE = unittest.TestLoader().loadTestsFromTestCase(TestResources)
    unittest.TextTestRunner(verbosity=0).run(SUITE)

# vim:ts=4:sw=4:expandtab
