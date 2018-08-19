import unittest

import ioc
import sq.test
import sq.lib.x509

from ....infra import orm
from ..endpoints import PrincipalEndpoint


class CreatePrincipalTestCase(sq.test.SystemTestCase):
    metadata = orm.Relation.metadata
    gsid = "00000000-0000-0000-0000-000000000000"

    def setUp(self):
        super(CreatePrincipalTestCase, self).setUp()
        self.endpoint = PrincipalEndpoint()
        with open('dev/usr.testing.crt', 'rb') as f:
            self.pem = f.read()
            self.crt = sq.lib.x509.Certificate.frompem(self.pem)

    @sq.test.integration
    def test_associate_phonenumber_responds_ok(self):
        """Associate a X.509 certificate to a **Principal**."""

        request = sq.test.request_factory(
            method='POST',
            json={
                'gsid': self.gsid,
                'principals': [
                    {'type': 'phonenumber', 'phonenumber': "+31612345678"}
                ]
            }
        )
        response = self.run_callable(self.loop, self.endpoint.handle, request)
        self.assertEqual(response.status_code, 200)

    @sq.test.integration
    def test_associate_x509_responds_ok(self):
        """Associate a X.509 certificate to a **Principal**."""

        request = sq.test.request_factory(
            method='POST',
            json={
                'gsid': self.gsid,
                'principals': [
                    {'type': 'x509', 'crt': bytes.hex(self.pem)}
                ]
            }
        )
        response = self.run_callable(self.loop, self.endpoint.handle, request)
        self.assertEqual(response.status_code, 200)


class MockRequest:
    pass


#pylint: skip-file
