import sys

NO_PATH = sys.maxsize
GRAPH = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]
MAX_LENGTH = len(GRAPH[0])


def floyd_recursive(distance, start_node, end_node, intermediate):
    """
    A recursive implementation of Floyd's algorithm.
    """
    # Base case: If start_node and end_node are the same, distance is 0.
    if start_node == end_node:
        return 0
    # If either start_node or end_node has no path through intermediate node, return infinity.
    if intermediate == -1:
        return distance[start_node][end_node]
    if distance[start_node][intermediate] == NO_PATH or distance[intermediate][end_node] == NO_PATH:
        return floyd_recursive(distance, start_node, end_node, intermediate - 1)
    # Compute the distance via intermediate node recursively.
    return min(
        floyd_recursive(distance, start_node, end_node, intermediate - 1),
        distance[start_node][intermediate] + distance[intermediate][end_node]
    )


def floyd(distance):
    """
    A wrapper function to apply Floyd's algorithm recursively.
    """
    for intermediate in range(MAX_LENGTH):
        for start_node in range(MAX_LENGTH):
            for end_node in range(MAX_LENGTH):
                distance[start_node][end_node] = min(
                    distance[start_node][end_node],
                    floyd_recursive(distance, start_node, end_node, intermediate)
                )


# Make a copy of the graph to avoid modifying the original.
distance = [row[:] for row in GRAPH]

# Run Floyd's algorithm.
floyd(distance)

# Print the result.
for row in distance:
    print(row)
