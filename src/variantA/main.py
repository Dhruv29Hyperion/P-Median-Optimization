import numpy as np
from solvers import greedy_solver, enumerate_solver, compute_better_cost

def variantA_enumerate(distance_matrix, cost_array, node_count: int) -> tuple[list[int], float]:
    """
    A solving system for "variantA" of our problem. The "variantA" problem requires us to *test* different values of p
    to find the best one. This is a brute-force approach.

    @arguments
    problem_definition: list[Node] - a list of nodes representing the problem.
    node_count: int - the number of nodes.

    @returns 
    tuple with elements best_medians, best_cost
    best_median: list[int] - a list of indexes of the best (selected) medians.
    best_cost: float - the cost incurred when selecting the best medians.
    """

    best_cost = np.inf
    best_medians = []

    for p in range(1, node_count + 1):
        selected_medians = enumerate_solver(
                distance_matrix, 
                cost_array,
                node_count, 
                p
                )

        if selected_medians is not None:
            # we were able to find a solution
            total_cost = compute_better_cost(
                    distance_matrix, 
                    cost_array, 
                    node_count,
                    selected_medians
                    )
            # print(f"{total_cost=}")
            # print(f"{selected_medians=}")
            if total_cost < best_cost:
                best_cost = total_cost
                best_medians = selected_medians
        else:
            print(f"\tUnable to find a solution for {p=}")

    return best_medians, best_cost

def variantA_greedy(distance_matrix, cost_array, node_count: int) -> tuple[list[int], float]:
    """
    A solving system for "variantA" of our problem. The "variantA" problem requires us to *test* different values of p
    to find the best one. This is a brute-force approach.

    @arguments
    problem_definition: list[Node] - a list of nodes representing the problem.
    node_count: int - the number of nodes.

    @returns 
    tuple with elements best_medians, best_cost
    best_median: list[int] - a list of indexes of the best (selected) medians.
    best_cost: float - the cost incurred when selecting the best medians.
    """

    best_cost = np.inf
    best_medians = []

    for p in range(1, node_count + 1):
        selected_medians = greedy_solver(
                distance_matrix, 
                cost_array,
                node_count, 
                p
                )

        if selected_medians is not None:
            # we were able to find a solution
            total_cost = compute_better_cost(
                    distance_matrix, 
                    cost_array, 
                    node_count,
                    selected_medians
                    )
            # print(f"{total_cost=}")
            # print(f"{selected_medians=}")
            if total_cost < best_cost:
                best_cost = total_cost
                best_medians = selected_medians
        else:
            print(f"\tUnable to find a solution for {p=}")

    return best_medians, best_cost

def nandini_parlor_attributes():
    Dij = np.array([
            [0.00,4.76,5.48,8.4,7.64,10.20,4.11,3.71,5.12,4.21],
            [4.76,0.00,1.23,5.08,5.50,11.3,4.89,2.45,3.99,4.27],
            [5.48,1.23,0.00,3.83,4.36,10.5,4.51,2.26,3.22,3.76],
            [8.40,5.08,3.83,0.00,1.82,8.98,5.51,4.68,3.69,4.76],
            [7.64,5.50,4.36,1.82,0.00,7.27,4.32,4.19,2.61,3.53],
            [10.2,11.3,10.5,9.98,7.27,0.00,6.77,9.13,7.44,7.21],
            [4.11,4.89,4.51,5.51,4.32,6.77,0.00,2.61,1.96,0.88],
            [3.71,2.45,2.26,4.68,4.19,9.13,2.61,0.00,1.87,1.77],
            [5.12,3.99,3.22,3.60,2.61,7.44,1.96,1.87,0.00,1.13],
            [4.21,4.27,3.76,4.76,3.53,7.21,0.88,1.77,1.13,0.00]
            ])
    D_cost = Dij * 7.5 * 365
    C = np.array([4400,10100,10100,4400,4400,6700,4710,4710,4710,4710])
    node_count = 10
    return D_cost, C, node_count

def generate_random_inputs(n):
    # Generating a random symmetric matrix
    matrix = np.random.rand(n,n)
    distance_matrix = (matrix + matrix.T) / 2  # Ensuring symmetry

    # Fill diagonal entries with zeros
    np.fill_diagonal(distance_matrix, 0)

    cost_matrix = np.random.rand(n)
    
    return distance_matrix,cost_matrix

if __name__ == "__main__":

    distance_matrix, cost_array, node_count = nandini_parlor_attributes()
    # solving and printing the problem
    selected_median_indexes_greedy, cost_incurred_greedy = variantA_greedy(
            distance_matrix,
            cost_array, 
            node_count
            )

    distance_matrix, cost_array, node_count = nandini_parlor_attributes()
    selected_median_indexes_enumerate, cost_incurred_enumerate= variantA_enumerate(
            distance_matrix,
            cost_array, 
            node_count
            )

    # print the best medians (we must do list comprehension to get the actual nodes)
    print('Greedy: ')
    print(f"Best Medians: {selected_median_indexes_greedy}")
    print(f"Cost: {cost_incurred_greedy}") # print the cost
    print('\n\nEnumerate: ')
    print(f"Best Medians: {selected_median_indexes_enumerate}")
    print(f"Cost: {cost_incurred_enumerate}") # print the cost
