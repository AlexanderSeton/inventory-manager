import unittest
from models.vendor import Vendor

class TestVendor(unittest.TestCase):
    def setUp(self):
        self.vendor1 = Vendor("vendor1")
    
    def test_vendor_has_name(self):
        self.assertEqual("vendor1", self.vendor1.name)
    
    def test_vendor_has_active_status(self):
        self.assertEqual(True, self.vendor1.active)
    
    def test_vendor_has_id(self):
        self.assertEqual(None, self.vendor1.id)

    def test_method_check_active(self):
        self.assertEqual(True, self.vendor1.check_active())
    
    def test_method_set_inactive(self):
        self.vendor1.set_inactive()
        self.assertEqual(False, self.vendor1.active)
    
    def test_method_set_active(self):
        self.vendor1.set_active()
        self.assertEqual(True, self.vendor1.active)
