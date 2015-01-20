# Module import
import os
import sys

# Unit testing framework
import unittest
from mock import MagicMock, patch

# Modules under test
from models import cities

class TestCity(unittest.TestCase):
    def test_null(self):
        self.assertTrue(True)
