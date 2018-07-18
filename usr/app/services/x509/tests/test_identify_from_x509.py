"""Specifies test cases for X.509 certificate subject resolving."""
import unittest

import sq.test

from ..impl import X509Service


@sq.test.integration
class X509InvalidCertificateTestCase(unittest.TestCase):

    def setUp(self):
        self.pem = open('dev/usr.testing.invalid.crt', 'rb').read()
        self.service = X509Service()

    def test_load_principals_from_pem(self):
        """Load **Principal** objects from a PEM certificate."""
        self.service.principals_from_pem(self.pem)


@sq.test.integration
class X509ReferenceCertificateTestCase(unittest.TestCase):
    """Run unit tests with the reference Subject certificate."""

    def setUp(self):
        self.pem = open('dev/usr.testing.crt', 'rb').read()
        self.service = X509Service()

    def test_load_principals_from_pem(self):
        """Load **Principal** objects from a PEM certificate."""
        self.service.principals_from_pem(self.pem)


#pylint: skip-file
