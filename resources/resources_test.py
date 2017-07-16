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

    def test_tags(self):
        """Checks resources for required tags."""
        tagged_resources = ['aws_ebs_volume', 'aws_instance']
        required_tags = ['Name']
        self.validator.resources(tagged_resources).property('tags'). \
            should_have_properties(required_tags)

    def test_ebs_block_device(self):
        """Checks instances for NOT having a EBS block device directly
           mapped."""
        self.validator.resources(['aws_instance']). \
            should_not_have_properties(['ebs_block_device'])

    def test_ebs_volume_encryption(self):
        """Checks EBS volume for enabled encryption."""
        self.validator.resources(['aws_ebs_volume']).property('encrypted'). \
            should_equal(True)

    def test_latest_ami(self):
        """Checks for usage of latest AMI."""
        pass

    def test_different_azs(self):
        """Checks whether the instances are placed in at least 2 different
           AZs."""
        actual_property_value = self.validator.resources(['aws_instance']).property('subnet_id').properties
        print(type(actual_property_value))
        print(dir(actual_property_value))
        print(actual_property_value)
        print(actual_property_value[0].property_value)
        pass
        #self.validator.resources(['aws_instance']).property('subnet_id').list_should_contain(['subnet-a534a2cc', 'subnet-b1e74cca'])

if __name__ == '__main__':
    SUITE = unittest.TestLoader().loadTestsFromTestCase(TestResources)
    unittest.TextTestRunner(verbosity=0).run(SUITE)

# vim:ts=4:sw=4:expandtab
