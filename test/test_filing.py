# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Marketplace, we offer a wide selection of financial data feeds sourced by our own proprietary processes as well as from many data vendors. The primary application of the Intrinio API is for use in third-party applications and integrations or for end-users utilizing the Excel add-in and Google Sheets add-on. The Intrinio API uses HTTPS verbs and a RESTful endpoint structure, which makes it easy to request data from Intrinio. Responses are delivered in JSON format. If you need additional help in using the API, go to our home page (https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import intrinio_sdk
from intrinio_sdk.models.filing import Filing  # noqa: E501
from intrinio_sdk.rest import ApiException


class TestFiling(unittest.TestCase):
    """Filing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFiling(self):
        """Test Filing"""
        # FIXME: construct object with mandatory attributes with example values
        # model = intrinio_sdk.models.filing.Filing()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
