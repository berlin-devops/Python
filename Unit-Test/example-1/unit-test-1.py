import unittest
import main

''' Code reference
main.py
def some_function(num):
    try:
        return int(num) + 5
    except ValueError as e:
        print(f'ValueError:\n{e}')
        return e
    except TypeError as e:
        print(f'TypeError:\n{e}')
        return e
'''
''' Standard approach for creating a class TestMain
using unittest module '''
class TestMain(unittest.TestCase):
    # Inheriting class unittest attributes
    def test_do_stuff(self):
        test_param = 10
        expected_result = 15 # num=10 + 5 = 15

        # passed-in 'num' for main.some_function(num) 
        result = main.some_function(test_param)
        
        # .assertEqual(trueResult, desiredResult) is a method inherited from class unittest 
        self.assertEqual(result, expected_result)

    def test_do_sth2(self):
        test_param = 'abcdefg'
        expected_result = 'abcdefg'
        result = main.some_function(test_param)

        '''
        # No try except (try/catch) is needed
        # all types of Errors are auto-specified by
        # class unittest
        # .assertTrue(isinstance(result, ValueError))
        # Asking whether result is a ValueError
        # rather than just comparing result vs expected_result'''
        self.assertTrue(isinstance(result, ValueError))

# Run this Unit Test
# python3 Unit-Test/example-1/unit-test-1.py
unittest.main()