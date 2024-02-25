import timeit

# Import the imperative Floyd function from your main code
from floyd_imperative import floyd

# Define your performance test function
def test_performance_floyd_imperative():
    # Define your test input
    NO_PATH = float('inf')
    GRAPH = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
    ]
    distance = [row[:] for row in GRAPH]

    # Measure the time taken to execute the floyd function
    time_taken = timeit.timeit(lambda: floyd(distance), number=1)

    # Print the time taken
    print(f"Time taken to execute floyd function (imperative): {time_taken} seconds")


# Run the performance test
if __name__ == "__main__":
    test_performance_floyd_imperative()
