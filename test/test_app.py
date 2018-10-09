from unittest import TestCase
from name_normalization.dhp_nameparser import name_normalization
from model.req_parser_model import MemberName_schema

class TestNameNormalization(TestCase):
 
    def test_dhp_nameparser(self):
        self.assertEqual(name_normalization('Ducrow'), {'status': 'UNCHANGED', 'name': 'DUCROW'})
        self.assertEqual(name_normalization('shawl III'), {'status': 'CHANGED', 'name': 'SHAWL '})
