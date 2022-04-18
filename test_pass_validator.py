import unittest
import pass_validator

class TestPassValidator(unittest.TestCase):
    
    def test_good_passwrd(self):
        result = pass_validator.password_check('VeryGood123474354t$#ss')
        self.assertEqual(result, 'Strong password')
    
    # def test_empty_passwrd(self):
    #     result = pass_validator.password_check('')
    #     self.assertEqual(result, '- Password should be at least 14 characters long')
    
    # def test_numeric_passwrd(self):
    #     result = pass_validator.password_check('123456678990')
    #     self.assertEqual(result, '- Password should be at least 14 characters long')
        

# if __name__ == "__main__":
#     unittest.main()