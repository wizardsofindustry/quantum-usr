import os
import json
import unittest

import ioc
import sq.test

from ....infra import orm
from ..endpoints import IdentificationEndpoint



@sq.test.integration
class PhonenumberSubjectIdentificationTestCase(sq.test.SystemTestCase):
    gsid = "00000000-0000-0000-0000-000000000000"
    bin = "CMBANL9Z3xOcyYKUhR8s0mS+tbkNO2xF2/U/Ns3eIyMOWYWmOZeUGw8StPKPhAdRTyN1XWne1rgJQA"
    metadata = orm.Relation.metadata

    def setUp(self):
        super(PhonenumberSubjectIdentificationTestCase, self).setUp()
        self.endpoint = IdentificationEndpoint()
        self.service = ioc.require('SubjectIdentificationService')
        self.service.associate(self.gsid,
            {'type': 'idin:bin', 'bin': self.bin})

    def test_subject_is_identified_by_bin(self):
        """Identify a Subject by Bank Identification Number (BIN)."""
        dto = {
            'type': 'idin:bin',
            'bin': self.bin
        }
        response = self.request(self.endpoint.handle, method='POST', json=dto)
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.response[0])
        self.assertIn('gsid', result)
        self.assertEqual(result['gsid'], self.gsid.replace('-', ''))

    def test_subject_is_not_identified_by_unknown_bin(self):
        """Identify a Subject by BIN that does not exist."""
        dto = {
            'type': 'idin:bin',
            'bin': "bla"
        }
        response = self.request(self.endpoint.handle, method='POST', json=dto)
        self.assertEqual(response.status_code, 404)


#pylint: skip-file
