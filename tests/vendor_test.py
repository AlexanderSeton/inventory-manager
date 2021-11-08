import unittest
from models.vendor import Vendor

class TestVendor(unittest.TestCase):

    def setUp(self):
        self.vendor1 = Vendor("vendor1", True)
    
    def test_vendor_has_name(self):
        self.assertEqual("vendor1", self.vendor1.name)
    
    def test_vendor_has_active_status(self):
        self.assertEqual(True, self.vendor1.active)
    
    def test_vendor_has_id(self):
        self.assertEqual(None, self.vendor1.id)
