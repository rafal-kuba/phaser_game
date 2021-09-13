import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password = 'testpassword1234')
        self.assertTrue(u.password_hash is not None)
    
    def test_no_password_getter(self):
        u = User(password = 'testpassword1234')
        with self.assertRaises(AttributeError):
            u.password
        
    def test_password_verification(self):
        u = User(password = 'testpassword1234')
        self.assertTrue(u.verify_password('testpassword1234'))
        self.assertFalse(u.verify_password('badpassword1234'))

    def test_password_random_salts(self):
        u = User(password='testpassword1234')
        u2 = User(password='testpassword1234')
        self.assertTrue(u.password_hash != u2.password_hash)