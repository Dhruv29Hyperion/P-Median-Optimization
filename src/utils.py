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


def compare_heuristics(distances,costs,nodes):
    """
    A function to compare greedy's algorithm and enumeration for the same input.

    @arguments
    distance_matrix - distances from node i to node j
    cost_array - cost per unit area for each median
    node_count: int - the number of nodes.

    @returns 
    Nothing
    """

    distance_matrix = copy.deepcopy(distances)
    cost_array = copy.deepcopy(costs)
    node_count = copy.deepcopy(nodes)
    selected_median_indexes_greedy, cost_incurred_greedy = variantA_greedy(
            distance_matrix,
            cost_array, 
            node_count
            )
    print('Greedy: ')
    print(f"Best Medians: {selected_median_indexes_greedy}")
    print(f"Cost: {cost_incurred_greedy}") # print the cost

    distance_matrix = copy.deepcopy(distances)
    cost_array = copy.deepcopy(costs)
    node_count = copy.deepcopy(nodes)
    selected_median_indexes_enumerate, cost_incurred_enumerate= variantA_enumerate(
            distance_matrix,
            cost_array, 
            node_count
            )

    print('\n\nEnumerate: ')
    print(f"Best Medians: {selected_median_indexes_enumerate}")
    print(f"Cost: {cost_incurred_enumerate}\n\n") # print the cost