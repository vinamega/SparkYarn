# test_sparkyarn.py
"""
Tests for SparkYarn module.
"""

import unittest
from sparkyarn import SparkYarn

class TestSparkYarn(unittest.TestCase):
    """Test cases for SparkYarn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SparkYarn()
        self.assertIsInstance(instance, SparkYarn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SparkYarn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
