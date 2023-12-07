import numpy as np
import itertools

def calculate_total_cost(distance_matrix, cost_array, node_count: int, median_idxs: list[int]) -> float:
    """
    A method to calculate total cost of given set medians using greedy's
    algorithm.
    
    @arguments
    distance_matrix - distances from node i to node j
    cost_array - cost per unit area for each median
    node_count: int - the number of Nodes
    median_idxs: list[int] - the indexes of the medians for which we want to calculate the total cost

    @returns
    cost: float - the total cost of choosing the given medians
    """
    visited_median_idxs = []
    cost = 0
    for median_idx in median_idxs:

        dist_arr = distance_matrix[:,median_idx]

        # distances of MEDIAN to all points as below
        facility_cost_of_median = cost_array[median_idx]

        # Distance to Visited Medians Must not be considered#
        for i in visited_median_idxs:
            dist_arr[i] = 0

        #print(f'{median_idx=},{visited_median_idxs=},{dist_arr=}')
        cost += np.sum(dist_arr) + facility_cost_of_median
        visited_median_idxs.append(median_idx)

    return cost

def compute_better_cost(distance_matrix, cost_array, node_count, median_idxs: list[int]) -> float:
    """
    A method to calculate total cost is given.
    
    @arguments
    distance_matrix - distances from node i to node j
    cost_array - cost per unit area for each median
    medians_idxs: list[int] - the indexes of the medians for which we want to calculate the total cost

    @returns
    cost: float - the total cost of choosing the given medians
    """

    cost = 0
    for point in range(node_count):
        mindist = float("inf")
        for median in median_idxs:
            dist = distance_matrix[point,median]
            if dist < mindist:
                mindist = dist
        cost += mindist

    cost += sum([cost_array[median] for median in median_idxs])
    return cost


def greedy_solver(distance_matrix,cost_array, node_count: int, p: int = 1) -> list[int]:
    """
    Greedy heuristic system for the p-median problem.
    Returns the "indexes" of the best p medians.

    @arguments
    distance_matrix - distances from node i to node j
    cost_array - cost per unit area for each median
    node_count: int - the number of nodes.
    p: int - the number of medians to select.

    @returns
    best_median_idxs: list[int] - a list of indexes of the best (selected) medians.
    """

    if p >= node_count:
        return list(range(node_count)) # select all

    best_median_idxs: list[int] = []
    remaining_point_idxs = np.arange(node_count)

    for _ in range(p):
        best_cost = np.inf
        best_median_idx = None

        for node_idx in remaining_point_idxs:
            # node_idx is the index that I am currently considering as a median(s)
            candidate_positions_for_medians = best_median_idxs.copy() + [node_idx]

            cost = calculate_total_cost(
                distance_matrix, 
                cost_array, 
                node_count, 
                candidate_positions_for_medians
            )

            if cost < best_cost:
                best_cost = cost
                best_median_idx = node_idx

        best_median_idxs.append(best_median_idx)

        # delete the selected median from the candidate list
        remaining_point_idxs = np.delete(
            remaining_point_idxs, np.where(remaining_point_idxs == best_median_idx)
        )
        #print(remaining_point_idxs)

    return best_median_idxs

def enumerate_solver(distance_matrix, cost_array, node_count: int, p: int = 1) -> list[int]:
    """
    Enumeration method for the p-median problem.
    Returns the "indexes" of the best p medians.

    @arguments
    distance_matrix - distances from node i to node j
    cost_array - cost per unit area for each median
    node_count: int - the number of nodes.
    p: int - the number of medians to select.

    @returns
    best_median_idxs: list[int] - a list of indexes of the best (selected) medians.
    """

    if p >= node_count:
        return list(range(node_count))  # select all

    best_cost = float("inf")
    best_median_idxs = []

    # Enumerate all possible combinations of p medians
    for candidate_median_idxs in itertools.combinations(range(node_count), p):
        cost = compute_better_cost(
            distance_matrix, 
            cost_array,
            node_count, 
            list(candidate_median_idxs)
        )

        if cost < best_cost:
            best_cost = cost
            best_median_idxs = list(candidate_median_idxs)

    return best_median_idxs
