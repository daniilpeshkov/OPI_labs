import unittest
from main import get_usd_exchange


class Test(unittest.TestCase):


    def test_type(self):
        self.assertTrue(isinstance(get_usd_exchange(), float))

    
    def test_gt_zero(self):
        self.assertTrue(get_usd_exchange() > 0)


if __name__ == "__main__":
    unittest.main()