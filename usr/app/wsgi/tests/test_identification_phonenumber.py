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
    phonenumber = "+31612345678"
    metadata = orm.Relation.metadata

    def setUp(self):
        super(PhonenumberSubjectIdentificationTestCase, self).setUp()
        self.endpoint = IdentificationEndpoint()
        self.service = ioc.require('SubjectIdentificationService')
        self.service.associate(self.gsid,
            {'type': 'phonenumber', 'phonenumber': self.phonenumber})

    def test_subject_is_identified_by_phonenumber(self):
        """Identify a Subject by phonenumber."""
        dto = {
            'type': 'phonenumber',
            'phonenumber': self.phonenumber
        }
        response = self.request(self.endpoint.handle, method='POST', json=dto)
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.response[0])
        self.assertIn('gsid', result)
        self.assertEqual(result['gsid'], self.gsid.replace('-', ''))

    def test_subject_is_not_identified_by_unknown_phonenumber(self):
        """Identify a Subject by phonenumber that does not exist."""
        dto = {
            'type': 'phonenumber',
            'phonenumber': "+31687654321"
        }
        response = self.request(self.endpoint.handle, method='POST', json=dto)
        self.assertEqual(response.status_code, 404)


#pylint: skip-file
