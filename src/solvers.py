import numpy as np


# def calculate_total_cost(problem_definiton, node_count, medians):
#     for median_idx in medians:
#         median = problem_definiton[median_idx]
#         dist_arr = np.zeros(shape=(node_count,))

#         # distances of MEDIAN to all points as below
#         facility_cost_of_median = median.cost

#         i = 0
#         for node in problem_definiton:
#             dist_arr[i] = np.linalg.norm(node.point.asnumpy() - median.point.asnumpy())
#             i += 1
        
#         cost = np.sum(dist_arr) + facility_cost_of_median

#     return cost


def compute_better_cost(problem_definition, median_idxs):
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


def greedy_solver(problem_definition, node_count, p=1):
    """
    Greedy heuristic system for the p-median problem.
    Returns the "indexes" of the best p medians.
    """

    if p >= node_count:
        return list(range(node_count)) # select all

    best_median_idxs = []
    remaining_point_idxs = list(range(node_count))

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
        print(f"{remaining_point_idxs=}")
        print(f"Selected {best_median_idx=}")
        remaining_point_idxs = np.delete(
            remaining_point_idxs, np.where(remaining_point_idxs == best_median_idx)
        )

    return best_median_idxs
