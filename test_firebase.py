# test_firebase.py
"""
Tests for Firebase module.
"""

import unittest
from firebase import Firebase

class TestFirebase(unittest.TestCase):
    """Test cases for Firebase class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Firebase()
        self.assertIsInstance(instance, Firebase)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Firebase()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
