import unittest

import ioc
import sq.test
import sq.lib.x509

from ....infra import orm
from ..endpoints import PrincipalEndpoint


class CreatePrincipalTestCase(sq.test.SystemTestCase):
    metadata = orm.Relation.metadata

    def setUp(self):
        super(CreatePrincipalTestCase, self).setUp()
        self.endpoint = PrincipalEndpoint()
        with open('dev/usr.testing.crt', 'rb') as f:
            self.pem = f.read()
            self.crt = sq.lib.x509.Certificate.frompem(self.pem)

    @sq.test.integration
    def test_associate_x509_responds_ok(self):
        """Associate a X.509 certificate to a **Principal**."""

        request = sq.test.request_factory(
            method='POST',
            json={
                'gsid': "00000000-0000-0000-0000-000000000000",
                'principals': [
                    {'type': 'x509', 'crt': bytes.hex(self.pem)}
                ]
            }
        )
        self.run_callable(self.loop, self.endpoint.handle, request)


class MockRequest:
    pass


#pylint: skip-file
