import numpy as np
from utils.classes import Node, Point
from utils.visualizer import show_problem_plot, save_problem_plot, show_solution_plot
from solvers import greedy_solver, compute_better_cost


def variantA(problem_definition: list[Node], node_count: int) -> tuple[list[int], float]:
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
        selected_medians = greedy_solver(problem_definition, node_count, p)

        if selected_medians is not None:
            # we were able to find a solution
            total_cost = compute_better_cost(problem_definition, selected_medians)
            # print(f"{total_cost=}")
            # print(f"{selected_medians=}")
            if total_cost < best_cost:
                best_cost = total_cost
                best_medians = selected_medians
        else:
            print(f"\tUnable to find a solution for {p=}")

    return best_medians, best_cost


if __name__ == "__main__":

    # Defining the problem
    problem_definition = [
        Node(Point((0, 0)), 100),
        Node(Point((2, 2)), 10),
        Node(Point((2, -2)), 20),
        Node(Point((-2, 2)), 10),
        Node(Point((-2, -2)), 20),
    ]
    node_count = 5  # len(problem_definition)

    # Showing what was just defined
    print(f"{problem_definition=}")

    # solving and printing the problem
    selected_median_indexes, cost_incurred = variantA(problem_definition, node_count)

    # print the best medians (we must do list comprehension to get the actual nodes)
    print(f"Best Medians: {[problem_definition[idx] for idx in selected_median_indexes]}")
    print(f"Cost: {cost_incurred}") # print the cost

    # Visualize
    # show_problem_plot(problem_definition, node_count)
    show_solution_plot(problem_definition, node_count, selected_median_indexes)
