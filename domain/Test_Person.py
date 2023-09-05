import unittest
from unittest import TestCase
from Person import Person

class Test_Person(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.person_test = Person("test-00-0-0-0d-a", 
                        "Vinitest", 
                        "Testtest", 
                        "test",
                        "test@test.com")
        

    def test_get_uuid(self):
        expected_result = "test-00-0-0-0d-a"
        self.assertEqual(expected_result, self.person_test.uuid)
    
    def test_get_firstname(self):
        expected_result = "Vinitest"
        self.assertEqual(expected_result, self.person_test.firstname)
    
    def test_get_lastname(self):
        expected_result = "Testtest"
        self.assertEqual(expected_result, self.person_test.lastname)

    def test_get_nickname(self):
        expected_result = "test"
        self.assertEqual(expected_result, self.person_test.nickname)

    def test_get_email(self):
        expected_result = "test@test.com"
        self.assertEqual(expected_result, self.person_test.email)
    
    def test_set_uuid(self):
        self.person_test.uuid = "test2-11-1-1-1e-b"
        self.assertEqual(self.person_test.uuid, "test2-11-1-1-1e-b")

    def test_set_firstname(self):
        self.person_test.firstname = "test-firstname"
        self.assertEqual(self.person_test.firstname, "test-firstname")

    def test_set_lastname(self):
        self.person_test.lastname = "test-lastname"
        self.assertEqual(self.person_test.lastname, "test-lastname")

    def test_set_nickname(self):
        self.person_test.nickname = "test-nickname"
        self.assertEqual(self.person_test.nickname, "test-nickname")
    
    def test_set_email(self):
        self.person_test.email = "test-email"
        self.assertEqual(self.person_test.email, "test-email")

    def test_to_dict(self):
        expected_result = {
            "uuid": self.person_test.uuid,
            "firstname": self.person_test.firstname,
            "lastname": self.person_test.lastname,
            "nickname": self.person_test.nickname,
            "email": self.person_test.email
        }
        result = self.person_test.to_dict()
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()