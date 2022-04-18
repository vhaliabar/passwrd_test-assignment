import unittest
import pass_validator

class TestPassValidator(unittest.TestCase):
    
    def test_good_passwrd(self):
        result = pass_validator.password_check('VeryGood123474354t$#ss')
        self.assertEqual(result, 'Strong password')
    
    def test_empty_passwrd(self):
        result = pass_validator.password_check('%$#############]]]]]]]34324')
        self.assertEqual(result, None)
    
    def test_password_with_no_digit(self):
        self.assertFalse(pass_validator.password_check('%$#######]]]]]'), )