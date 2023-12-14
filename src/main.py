from solvers import *


def uncapacitated_problem(
    distance_matrix, cost_array, node_count, solver="greedy"
) -> tuple[list[int], float]:
    best_cost = np.inf
    best_medians = []
    best_p = 0
    opcount = 0

    for p in range(2, node_count + 1):
        if solver == "greedy":
            selected_medians, no_ops = greedy_solver(
                distance_matrix, cost_array, node_count, p
            )
        elif solver == "enumeration":
            selected_medians, no_ops = enumeration_solver(
                distance_matrix, cost_array, node_count, p
            )
        elif solver == "vertex_substitution":
            selected_medians, no_ops = vertex_substitution_solver(
                distance_matrix, cost_array, node_count, p
            )
        else:
            raise ValueError(f"Unknown solver: {solver}")

        if selected_medians is not None:
            # we were able to find a solution
            total_cost = cost_of_configuration(
                distance_matrix, cost_array, node_count, selected_medians
            )
            if total_cost < best_cost:
                best_cost = total_cost
                best_medians = selected_medians
                best_p = p
                opcount += no_ops
        else:
            print(f"\tUnable to find a solution for {p=}")

    return best_cost, best_medians, best_p, opcount


def capacitated_problem(
    distance_matrix,
    cost_array,
    node_count,
    production_array,
    demand_array,
    solver="greedy",
):
    best_cost = np.inf
    best_medians = []
    best_p = 0
    opcount = 0

    # Iterating for p from 1 to node_count, and finding medians with least cost #
    for p in range(1, node_count + 1):
        if solver == "greedy":
            selected_medians, no_ops = greedy_like(
                distance_matrix,
                cost_array,
                node_count,
                production_array,
                demand_array,
                p,
            )
        else:
            raise ValueError(f"Unknown solver: {solver}")

        if selected_medians is not None:
            total_cost = cost_of_configuration_for_variantB(
                distance_matrix,
                selected_medians,
                node_count,
                cost_array,
                production_array,
                demand_array,
            )
            if total_cost < best_cost:
                best_cost = total_cost
                best_medians = selected_medians
                best_p = p
                opcount += no_ops
        else:
            print(f"\tUnable to find a solution for {p=}")

    return best_cost, best_medians, best_p, opcount


def real_world_input():
    Dij = np.array(
        [
            [0.00, 4.76, 5.48, 8.4, 7.64, 10.20, 4.11, 3.71, 5.12, 4.21],
            [4.76, 0.00, 1.23, 5.08, 5.50, 11.3, 4.89, 2.45, 3.99, 4.27],
            [5.48, 1.23, 0.00, 3.83, 4.36, 10.5, 4.51, 2.26, 3.22, 3.76],
            [8.40, 5.08, 3.83, 0.00, 1.82, 8.98, 5.51, 4.68, 3.69, 4.76],
            [7.64, 5.50, 4.36, 1.82, 0.00, 7.27, 4.32, 4.19, 2.61, 3.53],
            [10.2, 11.3, 10.5, 9.98, 7.27, 0.00, 6.77, 9.13, 7.44, 7.21],
            [4.11, 4.89, 4.51, 5.51, 4.32, 6.77, 0.00, 2.61, 1.96, 0.88],
            [3.71, 2.45, 2.26, 4.68, 4.19, 9.13, 2.61, 0.00, 1.87, 1.77],
            [5.12, 3.99, 3.22, 3.60, 2.61, 7.44, 1.96, 1.87, 0.00, 1.13],
            [4.21, 4.27, 3.76, 4.76, 3.53, 7.21, 0.88, 1.77, 1.13, 0.00],
        ]
    )
    D_cost = Dij * 7.5 * 365
    C = np.array([4400, 10100, 10100, 4400, 4400, 6700, 4710, 4710, 4710, 4710])
    node_count = 10

    return D_cost, C, node_count


if __name__ == "__main__":
    distance_matrix = np.array(
        [
            [0, 5, 10],
            [5, 0, 5],
            [10, 5, 0],
        ]
    )
    cost_array = np.array([15, 10, 10])
    node_count = 3
    # demand_array = np.array([10, 15, 25, 15])
    # production_array = np.array([5, 7, 6, 5])

    print("Vertex Substition:", uncapacitated_problem(distance_matrix, cost_array, node_count, solver="vertex_substitution"))
    print("Greedy:", uncapacitated_problem(distance_matrix, cost_array, node_count, solver="greedy"))
    print("Enumeration:", uncapacitated_problem(distance_matrix, cost_array, node_count, solver="enumeration"))

    # D = np.array([[0, 5, 10], [5, 0, 7], [10, 7, 0]])
    # C = np.array([1, 2, 1])
    # W = np.array([4, 6, 5])
    # P = np.array([1.5, 2, 1.7])
    # NC = 3

    # cost, selected_medians, p, no_ops = capacitated_problem(
    #     D, C, NC, P, W, solver="greedy"
    # )
    # print(f"{cost=} {selected_medians=} {p=} {no_ops=}")
