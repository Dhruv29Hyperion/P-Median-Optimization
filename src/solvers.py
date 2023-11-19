import numpy as np

from utils.classes import Node


def calculate_total_cost(problem_definiton: list[Node], node_count: int, median_idxs: list[int]) -> float:
    """
    THIS FUNCTION IS NOT USED AND **MIGHT** NOT BE WORKING!

    A method to calculate total cost is given.
    
    @arguments
    problem_definition: list[Node] - the problem definition
    node_count: int - the number of Nodes
    median_idxs: list[int] - the indexes of the medians for which we want to calculate the total cost

    @returns
    cost: float - the total cost of choosing the given medians
    """
    for median_idx in median_idxs:
        median = problem_definiton[median_idx]
        dist_arr = np.zeros(shape=(node_count,))

        # distances of MEDIAN to all points as below
        facility_cost_of_median = median.cost

        i = 0
        for node in problem_definiton:
            dist_arr[i] = np.linalg.norm(node.point.asnumpy() - median.point.asnumpy())
            i += 1
        
        cost = np.sum(dist_arr) + facility_cost_of_median

    return cost


def compute_better_cost(problem_definition: list[Node], median_idxs: list[int]) -> float:
    """
    A method to calculate total cost is given.
    
    @arguments
    problem_definition: list[Node] - the problem definition
    medians_idxs: list[int] - the indexes of the medians for which we want to calculate the total cost

    @returns
    cost: float - the total cost of choosing the given medians
    """

    cost = 0
    for point in problem_definition:
        mindist = float("inf")
        for median in median_idxs:
            median = problem_definition[median]
            dist = np.linalg.norm(point.point.asnumpy() - median.point.asnumpy())
            if dist < mindist:
                mindist = dist
        cost += mindist

    cost += sum([problem_definition[median].cost for median in median_idxs])

    return cost


def greedy_solver(problem_definition: list[Node], node_count: int, p: int = 1) -> list[int]:
    """
    Greedy heuristic system for the p-median problem.
    Returns the "indexes" of the best p medians.

    @arguments
    problem_definition: list[Node] - a list of nodes representing the problem.
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

            cost = compute_better_cost(
                problem_definition, candidate_positions_for_medians
            )

            if cost < best_cost:
                best_cost = cost
                best_median_idx = node_idx

        best_median_idxs.append(best_median_idx)

        # delete the selected median from the candidate list
        remaining_point_idxs = np.delete(
            remaining_point_idxs, np.where(remaining_point_idxs == best_median_idx)
        )

    return best_median_idxs
