import numpy as np
from utils.classes import Node, Point
from utils.visualizer import show_problem_plot, save_problem_plot
from solvers import greedy_solver, compute_better_cost


def variantA(problem_definition, node_count):
    """
    A solving system for "variantA" of our problem. The "variantA" problem requires us to *test* different values of p
    to find the best one. This is a brute-force approach.
    """

    best_cost = np.inf
    best_medians = []

    for p in range(1, node_count + 1):
        print(f">>> Solving for {p=}")

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
    problem_definition = [
        Node(Point((0, 0)), 100),
        Node(Point((2, 2)), 10),
        Node(Point((2, -2)), 20),
        Node(Point((-2, 2)), 10),
        Node(Point((-2, -2)), 20),
    ]
    node_count = 5  # len(problem_definition)
    print(problem_definition)

    problem = variantA(problem_definition, node_count)
    print([problem_definition[idx] for idx in problem[0]])
    print(problem)

    show_problem_plot(problem_definition, node_count)
    # greedy()
