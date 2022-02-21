# Python Testing

```py
python3 -m unittest
```

[unittest docs](https://docs.python.org/3/library/unittest.html)

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

Test structure:

- Arrange: add entries
- Act: check using method
- Assert: whether the act returns correctly (true / false)

Each test should be its own definition, if you're using comments to explain, it probably needs to be broken up into more defs