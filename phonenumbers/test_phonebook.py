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
        # lines enclosed in with function will throw key error
        # this WILL throw an error to pass
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_some_names_is_consistent(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Mary', '012345')
        self.phonebook.add('Sue', '12345')
        self.assertTrue(self.phonebook.is_consistent())

    @unittest.skip("WIP")
    def test_phonebook_with_duplicate_names_is_inconsistent(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Mary', '012345')
        self.phonebook.add('Sue', '12345')
        self.phonebook.add('Bob', '123')
        self.assertFalse(self.phonebook.is_consistent())

    @unittest.skip("WIP")
    def test_phonebook_is_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Mary', '12345')
        self.phonebook.add('Sue', '12345')
        self.phonebook.add('Mike', '123')
        self.assertFalse(self.phonebook.is_consistent())
