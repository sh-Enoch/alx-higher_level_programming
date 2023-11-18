Python test driven 
  unittest
      functional based testing
      class based testing
        create a test file(must start with the word test_what_you_are_testing)        import the unittest module
	import module to test
	create test case for fxns to test.
	create a test class that inherits from a unittest.TestCase
	then create the methods that start with test_ (this naming conventions helps to know which methods rep testcases)
	methods work like any other class method ie self and parameters
	assertEquals()
	assertRaises()

	python -m unittest test_calc.py
	to run our test directly from within our editor use:
	    if __name__ == "__main__":
		    unittest.main()
	    but import unittest first in the file to test

  doctest
      more straight forward than unittests
      has fewer steps
      0-add_integer.txt
