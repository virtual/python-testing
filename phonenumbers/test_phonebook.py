import unittest

from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):
    def test_lookup_by_name(self):
        phonebook = Phonebook()
        phonebook.add('Bob', '12345')
        number = phonebook.lookup('Bob')
        self.assertEqual(number, '12345')

    # def test_missing_name(self):
    #     phonebook = Phonebook()
    #     with self.assertRaises(KeyError):
    #         phonebook.lookup('missing')

    # def test_is_consistent(self):
    #     phonebook = Phonebook()
    #     phonebook.add('Bob', '12345')
    #     self.assertTrue(phonebook.is_consistent())
    #     phonebook.add('Mary', '012345')
    #     self.assertTrue(phonebook.is_consistent())
    #     phonebook.add('Sue', '12345')
    #     self.assertTrue(phonebook.is_consistent())
    #     phonebook.add('Sue', '123')
    #     self.assertFalse(phonebook.is_consistent())