# Python Testing

```py
python3 -m unittest
```

You can skip a test case by adding a line above the def:

```py
@unittest.skip("WIP")
def test_name(self):
```

Maintain a good test suite:

All the test cases are using `phonebook = Phonebook()`, is there a way to clean this up?

Use Test Fixture:

1. setUp()
1. TestCaseMethod()
1. tearDown()