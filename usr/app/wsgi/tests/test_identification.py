import unittest

import ioc
import sq.test
import sq.lib.x509

from ....infra import orm
from ..endpoints import IdentificationEndpoint


@sq.test.integration
class X509SubjectIdentificationTestCase(sq.test.SystemTestCase):
    gsid ="00000000-0000-0000-0000-000000000000"
    metadata = orm.Relation.metadata

    def setUp(self):
        super(X509SubjectIdentificationTestCase, self).setUp()
        self.endpoint = IdentificationEndpoint()
        self.service = ioc.require('SubjectIdentificationService')
        with open('dev/usr.testing.crt', 'rb') as f:
            self.pem = f.read()
            self.crt = sq.lib.x509.Certificate.frompem(self.pem)
        self.service.associate(self.gsid,
            {'type': 'x509', 'crt': bytes.hex(self.pem)})

    @unittest.skip
    def test_subject_is_identified_by_email(self):
        """Identify a Subject by email."""
        request = sq.test.request_factory(
            method='POST',
            json=[{
                'type': 'email',
                'email': "cochise.ruhulessin@wizardsofindustry.net"
            }]
        )
        response = self.run_callable(self.loop, self.endpoint.handle, request)

    def test_subject_is_identified_by_x509(self):
        """Identify a Subject by X.509 certificate."""
        dto = {
            'type': 'x509',
            'crt': bytes.hex(self.pem)
        }
        request = self.request_factory(method='POST', json=dto)
        response = self.run_callable(self.loop, self.endpoint.handle, request)
        self.assertEqual(response.status_code, 200)


#pylint: skip-file
