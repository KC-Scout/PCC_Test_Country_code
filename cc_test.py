from country_codes import get_country_code
import unittest
from pygal.maps.world import COUNTRIES



class CCTestCase(unittest.TestCase):
    """Tests for 'get_country_code"""
    
    def test_country_code(self):
        x = get_country_code('zimbabwe')
        self.assertEqual(x, 'zw')
        
        y = get_country_code('niger')
        self.assertEqual(y, 'ne')
        
        z = get_country_code('afghanistan')
        self.assertEqual(z, 'af')
    

unittest.main()
