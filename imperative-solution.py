import sys
import itertools

NO_PATH = sys.maxsize
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]
MAX_LENGTH = len(graph[0])

def floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """
    for intermediate, start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        # If there's no direct path, we skip this iteration
        if distance[start_node][intermediate] == NO_PATH or distance[intermediate][end_node] == NO_PATH:
            continue
        # Calculate the minimum distance
        distance[start_node][end_node] = min(
            distance[start_node][end_node],
            distance[start_node][intermediate] + distance[intermediate][end_node]
        )

# Make a copy of the graph to avoid modifying the original
distance = [row[:] for row in graph]

# Run Floyd's algorithm
floyd(distance)

# Print the result
for row in distance:
    print(row)
