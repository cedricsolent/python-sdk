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
from intrinio_sdk.api.filing_api import FilingApi  # noqa: E501
from intrinio_sdk.rest import ApiException


class TestFilingApi(unittest.TestCase):
    """FilingApi unit test stubs"""

    def setUp(self):
        self.api = intrinio_sdk.api.filing_api.FilingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_filter_filings(self):
        """Test case for filter_filings

        Filter Filings  # noqa: E501
        """
        pass

    def test_get_all_filings(self):
        """Test case for get_all_filings

        Get All Filings  # noqa: E501
        """
        pass

    def test_get_filing_by_id(self):
        """Test case for get_filing_by_id

        Get a Filing by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
