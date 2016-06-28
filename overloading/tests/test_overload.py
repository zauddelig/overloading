import unittest
from overloading.overload_function import overload, AbsOverload

class TestOverload(unittest.TestCase):
    def test_register(self):
        @overload
        def function():
            pass
        self.assertIsInstance(function, AbsOverload)

    def test_register(self):
        @overload
        def function():
            pass

        @function.register
        def overloading_function():
            pass

        self.assertIs(function, overloading_function)


if __name__ == "__main__":
    unittest.main()