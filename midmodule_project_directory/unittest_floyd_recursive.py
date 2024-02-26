import unittest
import sys  # Import sys module for sys.maxsize

from floyd_recursive import floyd  # Import the functions to be tested

class TestFloydRecursive(unittest.TestCase):
    def test_floyd_recursive(self):
        # Define a test graph
        graph = [
            [0, 7, sys.maxsize, 8],  # Use sys.maxsize instead of NO_PATH
            [sys.maxsize, 0, 5, sys.maxsize],
            [sys.maxsize, sys.maxsize, 0, 2],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0]
        ]

        # Define the expected shortest path distances after running Floyd's algorithm
        expected_distances = [
            [0, 7, 12, 8],
            [sys.maxsize, 0, 5, 7],
            [sys.maxsize, sys.maxsize, 0, 2],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0]
        ]

        # Make a copy of the graph to avoid modifying the original
        distance = [row[:] for row in graph]

        # Run Floyd's algorithm
        floyd(distance)

        # Verify that the computed distances match the expected distances
        self.assertEqual(distance, expected_distances)

    def test_floyd_recursive_with_no_path(self):
        # Define a test graph with no path between certain nodes
        graph = [
            [0, 7, sys.maxsize, 8],  # Use sys.maxsize instead of NO_PATH
            [sys.maxsize, 0, 5, sys.maxsize],
            [sys.maxsize, sys.maxsize, 0, 2],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0]
        ]

        # Define the expected shortest path distances after running Floyd's algorithm
        expected_distances = [
            [0, 7, 12, 8],
            [sys.maxsize, 0, 5, 7],
            [sys.maxsize, sys.maxsize, 0, 2],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0]
        ]

        # Make a copy of the graph to avoid modifying the original
        distance = [row[:] for row in graph]

        # Run Floyd's algorithm
        floyd(distance)

        # Verify that the computed distances match the expected distances
        self.assertEqual(distance, expected_distances)

if __name__ == '__main__':
    unittest.main()
