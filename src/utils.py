import numpy as np

def generate_random_inputs(n):
    """
    A function that generates the random attributes for a Variant A problem.

    @arguments
    node_count: int - the number of nodes.

    @returns
    distance_matrix - distances from node i to node j
    cost_array - cost per unit area for each median
    """

    # Generating a random symmetric matrix
    matrix = np.random.rand(n, n)
    distance_matrix = (matrix + matrix.T) / 2  # Ensuring symmetry

    # Fill diagonal entries with zeros
    np.fill_diagonal(distance_matrix, 0)

    cost_matrix = np.random.rand(n)

    return distance_matrix, cost_matrix, n
