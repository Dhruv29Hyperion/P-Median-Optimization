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
            #print(f'{p=},{selected_medians=},{total_cost=}')
            if total_cost < best_cost:
                best_cost = total_cost
                best_medians = selected_medians
        else:
            print(f"\tUnable to find a solution for {p=}")

    return best_medians, best_cost


if __name__ == '__main__':
    
    # Distance Matrix
    dist_mat = np.array([[0,3,3],[2,0,4],[3,4,0]])

    # Number of Customers
    node_count = len(dist_mat)

    # Cost of median per Unit Area
    C = np.array([10,50,70])

    # Production per Unit Area
    P = np.array([100,100,100])

    # Demand of Customer
    W = np.array([20,10,15])

    selected_median_indexes, cost_incurred = variantB(dist_mat,node_count,C,P,W)

    print(f"Best Medians: {selected_median_indexes}")
    print(f"Cost: {cost_incurred}")
