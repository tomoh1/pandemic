# Module import
import os
import sys
base_dir = os.path.join(os.getcwd(), '..')
sys.path.append(base_dir)


# Unit testing framework
import unittest
from mock import MagicMock, patch, Mock

# Modules under test
from models import cities

class TestCity(unittest.TestCase):
    def test_null(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
