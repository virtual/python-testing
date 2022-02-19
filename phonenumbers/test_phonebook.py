import unittest

from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):
    # Constructs a Phonebook object in each test method.
    def setUp(self) -> None:
        self.phonebook = Phonebook()

    # Removes resources if needed, 
    # but phonebook is in memory so unnecessary
    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        self.phonebook.add('Bob', '12345')
        number = self.phonebook.lookup('Bob')
        self.assertEqual(number, '12345')

    def test_missing_name(self):
        self.phonebook = Phonebook()
        # lines enclosed in with function will throw key error
        # this WILL throw an error to pass
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')

    # @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        self.phonebook = Phonebook()
        # is_consistent method will return True
        self.assertTrue(self.phonebook.is_consistent())

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
