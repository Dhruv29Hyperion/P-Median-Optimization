import numpy as np
from solvers import greedy_solver_B, compute_better_cost

def variantB(distance_matrix, node_count: int, cost_array, production_array, demand_array) -> list[int]:
    """
    A solving system for "variantB" of our problem. The "variantB" problem requires us to *test* different values of p
    to find the best one. This is a brute-force approach.

    @arguments
    distance_matrix - distances from node i to node j
    node_count: int - the number of nodes.
    cost_array - cost per unit area for each median
    production_array - production per unit area for each median
    demand_array - demand of each customer

    @returns 
    tuple with elements best_medians, best_cost
    best_median: list[int] - a list of indexes of the best (selected) medians.
    best_cost: float - the cost incurred when selecting the best medians.
    """

    best_cost = np.inf
    best_medians = []

    # Iterating for p from 1 to node_count, and finding medians with least cost #
    for p in range(1, node_count + 1):
        selected_medians = greedy_solver_B(
                distance_matrix, 
                node_count, 
                cost_array, 
                production_array, 
                demand_array, 
                p
        )

        if selected_medians is not None:
            total_cost = compute_better_cost(
                            distance_matrix, 
                            node_count,
                            selected_medians,
                            cost_array,
                            production_array,
                            demand_array
                        )
            print(f'{p=},{selected_medians=},{total_cost=}')
            if total_cost < best_cost:
                best_cost = total_cost
                best_medians = selected_medians
        else:
            print(f"\tUnable to find a solution for {p=}")

    return best_medians, best_cost


def generate_random_inputs(n):
    # Generating a random symmetric matrix
    matrix = np.random.rand(n,n)
    distance_matrix = (matrix + matrix.T) / 2  # Ensuring symmetry

    # Fill diagonal entries with zeros
    np.fill_diagonal(distance_matrix, 0)

    cost_matrix = np.random.rand(n)
    
    production_matrix = np.random.rand(n)
    
    demand_matrix = np.random.rand(n)

    return distance_matrix,cost_matrix,production_matrix,demand_matrix

if __name__ == '__main__':
    
    # Distance Matrix
    #dist_mat = np.array([[0,3,3],[2,0,4],[3,4,0]])
    #dist_mat = np.array([[0,3,4,3],[3,0,7,2],[4,7,0,3],[3,2,3,0]])

    # Number of Customers
    #node_count = len(dist_mat)

    # Cost of median per Unit Area
    #C = np.array([10,50,70])
    #C = np.array([1,2,1.5,0.7])

    # Production per Unit Area
    #P = np.array([100,100,100])
    #P = np.array([5,7,6,5])

    # Demand of Customer
    #W = np.array([20,10,15])
    #W = np.array([10,15,25,15])

    #node_count = 100
    #dist_mat,C,P,W = generate_random_inputs(node_count)

    D = np.array([[0,5,10],[5,0,7],[10,7,0]])
    C = np.array([1,2,1])
    W = np.array([4,6,5])
    P = np.array([1.5,2,1.7])

    selected_median_indexes, cost_incurred = variantB(D,3,C,P,W)

    #selected_median_indexes, cost_incurred = variantB(dist_mat,node_count,C,P,W)

    print(f"Best Medians: {selected_median_indexes}")
    print(f"Cost: {cost_incurred}")
