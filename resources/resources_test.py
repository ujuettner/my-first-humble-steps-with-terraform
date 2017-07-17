#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test suite for Terraform resources."""

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
        tagged_resources = [
            'aws_security_group', 'aws_ebs_volume', 'aws_instance'
        ]
        required_tags = ['Name']
        self.validator.error_if_property_missing()
        self.validator.resources(tagged_resources).property('tags'). \
            should_have_properties(required_tags)

    def test_sg_for_ssh(self):
        """Checks SGs for open SSH access."""
        self.validator.resources(['aws_security_group']).property('ingress'). \
            property('from_port').should_equal(22)
        self.validator.resources(['aws_security_group']).property('ingress'). \
            property('to_port').should_equal(22)

    def test_ebs_block_device(self):
        """Checks instances for NOT having a EBS block device directly
           mapped."""
        self.validator.resources(['aws_instance']). \
            should_not_have_properties(['ebs_block_device'])

    def test_ebs_volume_encryption(self):
        """Checks EBS volume for enabled encryption."""
        self.validator.error_if_property_missing()
        self.validator.resources(['aws_ebs_volume']).property('encrypted'). \
            should_equal(True)

    def test_number_of_instances_and_volumes(self):
        """Checks the number of instances and EBS volumes against the default
           value."""
        self.validator.enable_variable_expansion()
        self.validator.resources(['aws_instance']).property('count'). \
            should_equal(2)
        self.validator.resources(['aws_ebs_volume']).property('count'). \
            should_equal(2)

if __name__ == '__main__':
    SUITE = unittest.TestLoader().loadTestsFromTestCase(TestResources)
    unittest.TextTestRunner(verbosity=0).run(SUITE)

# vim:ts=4:sw=4:expandtab
