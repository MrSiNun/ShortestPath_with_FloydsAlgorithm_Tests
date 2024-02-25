# performance_test_floyd_recursive.py

import timeit
import sys

# Import the functions from your floyd_recursive.py
from floyd_recursive import floyd_recursive, floyd

# Define the setup code that prepares the environment for the test
setup_code = '''
# Your setup code here (same as before)
'''

# Define the code snippet to be tested
test_code = '''
# Your test code here (same as before)
'''

# Perform the performance test and print the execution time
execution_time = timeit.timeit(stmt=test_code, setup=setup_code, number=1000)
print("Execution time:", execution_time, "seconds")
