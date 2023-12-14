import itertools
import numpy as np


def cost_of_configuration(
    distance_matrix: np.ndarray,
    cost_array: np.ndarray,
    node_count: int,
    median_list: np.ndarray,
) -> float:
    """Generic cost calculation function used for comparisions."""

    cost = 0
    for point in range(node_count):
        mindist = float("inf")
        for median in median_list:
            dist = distance_matrix[point, median]
            if dist < mindist:
                mindist = dist
        cost += mindist

    cost += sum([cost_array[median] for median in median_list])

    return cost


def calculate_cost_for_greedy(
    distance_matrix: np.ndarray, cost_array, median_idxs: list[int]
) -> float:
    """Cost calculation algorithm used for greedy."""

    visited_median_idxs = []
    cost = 0
    for median_idx in median_idxs:
        dist_arr = distance_matrix[:, median_idx]

        # distances of MEDIAN to all points as below
        facility_cost_of_median = cost_array[median_idx]

        # Distance to Visited Medians Must not be considered#
        for i in visited_median_idxs:
            dist_arr[i] = 0

        # print(f'{median_idx=},{visited_median_idxs=},{dist_arr=}')
        cost += np.sum(dist_arr) + facility_cost_of_median
        visited_median_idxs.append(median_idx)

    return cost


def greedy_solver(
    distance_matrix: np.ndarray, cost_array: np.ndarray, node_count: int, p: int = 1
) -> tuple[list[int], int]:
    no_ops = 0

    if p >= node_count:
        return list(range(node_count)), no_ops + 1  # select all and return

    best_median_idxs: list[int] = []
    remaining_point_idxs = np.arange(node_count)

    for _ in range(p):
        best_cost = np.inf
        best_median_idx = None

        for node_idx in remaining_point_idxs:
            no_ops += 1
            # node_idx is the index that I am currently considering as a median(s)
            candidate_positions_for_medians = best_median_idxs.copy() + [node_idx]

            cost = calculate_cost_for_greedy(
                distance_matrix, cost_array, candidate_positions_for_medians
            )

            if cost < best_cost:
                best_cost = cost
                best_median_idx = node_idx

        best_median_idxs.append(best_median_idx)

        # delete the selected median from the candidate list
        remaining_point_idxs = np.delete(
            remaining_point_idxs, np.where(remaining_point_idxs == best_median_idx)
        )

    return best_median_idxs, no_ops


def vertex_substitution_solver(D, cost_array, node_count: int, p: int = 2):
    H = np.diag(cost_array)
    V = np.arange(node_count)
    R = H @ D

    V_cand = np.copy(V[:p])

    no_ops = 0

    previous = 0
    cost = 0
    while True:
        # Inside a cycle
        partitions = []

        for jvertex in V_cand:
            part = []
            for ivertex in V:
                r_ij = R[ivertex, jvertex]
                for kvertex in V_cand:
                    r_ik = R[ivertex, kvertex]
                    if r_ij > r_ik:
                        break
                else:
                    part.append(ivertex)
            partitions.append(part)

        # ---- Vb repeat ---- #
        seen = set(V_cand)
        rem = set(V) - seen
        vbidx = 0
        while vbidx < len(rem):
            SubR = R[:, V_cand]

            Vb = rem.pop()
            rem.add(Vb)  # temp, later removed!
            deltabjs = []
            for jvertexidx in np.arange(len(V_cand)):
                # replace jvertex with Vb
                V_cand_copy = V_cand.copy()
                V_cand_copy[jvertexidx] = Vb

                i = 0
                delta = 0
                for ithrow in SubR:
                    minimum = np.min(ithrow)
                    second_minimum = np.sort(ithrow)[1]
                    rij = SubR[i, jvertexidx]
                    delt = 0
                    if minimum == rij:
                        if R[i, Vb] <= rij:
                            delt = R[i, Vb] - rij  # shold be negative
                        elif rij <= R[i, Vb] and rij <= second_minimum:
                            delt = R[i, Vb] - rij  # should be positive
                        elif rij <= R[i, Vb] and second_minimum <= R[i, Vb]:
                            delt = second_minimum - rij  # should be positive
                    delta += delt
                    i += 1

            deltabjs.append(delta)
            bjmin = np.min(deltabjs)
            if bjmin < 0:
                V_cand[np.argmin(deltabjs)] = Vb

            seen.add(Vb)
            rem = set(V) - seen
            vbidx += 1
        # ---- Vb repeat ---- #

        # cost #
        cost = 0
        for j in np.arange(len(V_cand)):
            for i in partitions[j]:
                cost += R[i, V_cand[j]]

        if cost == previous:
            break
        else:
            previous = cost
        if no_ops > 10000:
            break
        
        no_ops += 1

    return V_cand, no_ops


def enumeration_solver(
    distance_matrix, cost_array, node_count: int, p: int = 1
) -> list[int]:
    """Enumeration method for the p-median problem."""

    best_cost = float("inf")
    best_median_idxs = []
    no_ops = 0

    # Enumerate all possible combinations of p medians
    for candidate_median_idxs in itertools.combinations(np.arange(node_count), p):
        no_ops += 1

        cost = cost_of_configuration(
            distance_matrix, cost_array, node_count, candidate_median_idxs
        )

        if cost < best_cost:
            best_cost = cost
            best_median_idxs = candidate_median_idxs

    return best_median_idxs, no_ops


def cost_of_configuration_for_variantB(
    distance_matrix, median_idxs, node_count, cost_array, production_array, demand_array
) -> float:
    # Generating Delivery Weight Matrix #
    delivery_weight = np.zeros((node_count, node_count))
    for node in range(node_count):
        for median in range(node_count):
            delivery_weight[node, median] = (
                demand_array[node] / production_array[median]
            ) * cost_array[median]

    weighted_distance_matrix = delivery_weight + distance_matrix

    # Generating X Matrix based on minimum distance
    X = np.zeros((node_count, node_count))
    for i in range(node_count):
        # If i is already a median, skip #
        if i in median_idxs:
            continue

        # Initializing Minimum Distance and Best Median
        mindist = float("inf")
        best_median = None

        # Iterating though Medians to find Closest Median
        for median in median_idxs:
            dist = weighted_distance_matrix[median][i]
            if dist < mindist and median != i:
                mindist = dist
                best_median = median

        # Assigning Node to Closest Median
        X[best_median, i] = 1

    # Finding Facility and Delivery Cost
    facility_cost = 0
    delivery_cost = 0
    for median in median_idxs:
        median_demand = np.dot(demand_array, X[median]) + demand_array[median]
        facility_area = median_demand / production_array[median]
        facility_cost += facility_area * cost_array[median]

        delivery_cost += np.dot(X[median], distance_matrix[median])

    return delivery_cost + facility_cost


def calculate_cost_for_greedy_for_variantB(
    median_idxs,
    distance_matrix,
    node_count: int,
    cost_array,
    production_array,
    demand_array,
) -> float:
    # Defining Visted Medians, Cost, and Total Demand #
    visited_median_idxs = []
    cost = 0
    total_demand = np.sum(demand_array)

    for median_idx in median_idxs:
        # Calculating Distance of Median to Remaining Nodes #
        total_distance = 0
        median_cost = 1
        for i in range(node_count):
            if i not in visited_median_idxs:
                total_distance += distance_matrix[median_idx, i]

        # Dividing Demand to be Fulfilled by Production per unit area #
        area = total_demand / production_array[median_idx]
        median_cost = area * cost_array[median_idx]

        # Adding Cost of median to Total Cost #
        cost += median_cost + total_distance

        # Removing Demand of Median from Total_Demand #
        total_demand -= demand_array[median_idx]

        # Appending Current Median to Visited Medians #
        visited_median_idxs.append(median_idx)

    return cost


def greedy_like(
    distance_matrix,
    cost_array,
    node_count: int,
    production_array,
    demand_array,
    p: int = 1,
) -> list[int]:
    no_ops = 0

    # If p >= nodes, select all nodes
    if p >= node_count:
        return list(range(node_count)), no_ops + 1

    # Initializing Best Medians and Remaining Points #
    best_median_idxs: list[int] = []
    remaining_point_idxs = np.arange(node_count)

    # For each p, finding lowest cost median, appending to best_median_idxs and removing median from remaining_point_idxs
    for _ in range(p):
        best_cost = np.inf

        for node_idx in remaining_point_idxs:
            no_ops += 1
            # node_idx is the index that I am currently considering as a median(s)
            candidate_positions_for_medians = best_median_idxs.copy() + [node_idx]

            cost = calculate_cost_for_greedy_for_variantB(
                candidate_positions_for_medians,
                distance_matrix,
                node_count,
                cost_array,
                production_array,
                demand_array,
            )

            if cost < best_cost:
                best_cost = cost
                best_median_idx = node_idx

        best_median_idxs.append(best_median_idx)

        # delete the selected median from the candidate list
        remaining_point_idxs = np.delete(
            remaining_point_idxs, np.where(remaining_point_idxs == best_median_idx)
        )

    return best_median_idxs, no_ops
