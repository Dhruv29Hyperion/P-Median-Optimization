import matplotlib.pyplot as plt
import numpy as np
from .classes import Node

def plt_backend_plot(problem_definition: list[Node], node_count: int, solution_idxs: list[int] = None) -> None:
    """
    Matplotlib.pyplot powered plotting backend.
    
    @arguments
    problem_definition: list[Node] - a list of nodes representing the problem.
    node_count: int - the number of nodes.
    solution_idxs: list[int] - if present, plots the solution with the given indexes highlighted.

    @returns
    None
    """

    xarr = np.zeros(shape=(node_count,))
    yarr = np.zeros(shape=(node_count,))
    tags = [""]*node_count
    i = 0

    for node in problem_definition:
        xarr[i] = node.point.x
        yarr[i] = node.point.y
        tags[i] = f"i{node.id}: {node.cost}"
        i += 1

    plt.figure(figsize=(10, 10))
    if not solution_idxs:
        plt.title("Problem Definition Plot")
    else:
        plt.title("Problem Solution Plot")

    plt.scatter(xarr, yarr, color="red", label="Point")
    plt.axhline(0, color="grey")
    plt.axvline(0, color="grey")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    for i in range(node_count):
        plt.annotate(tags[i], (xarr[i] + 0.05, yarr[i] - 0.10))
    
    if solution_idxs is not None:
        for i in solution_idxs:
            # make circle around the selected median, transparent fill
            plt.scatter(xarr[i], yarr[i], color="blue", marker="o", s=150, alpha=0.2, label="Selected Median")

        # legend to indicate what selected is
        plt.legend(loc="upper center")
        

            

def show_problem_plot(problem_definition: list[Node], node_count: int) -> None:
    """
    Shows a plot for the problem_definition on a graph.

    @arguments
    problem_definition: list[Node] - a list of nodes representing the problem.
    node_count: int - the number of nodes.

    @returns
    None
    """
    plt_backend_plot(problem_definition, node_count)
    plt.show()

def save_problem_plot(problem_definition: list[Node], node_count: int, filename: str) -> None:
    """
    Exports the plot for the problem_definition into the file "filename"

    @arguments
    problem_definition: list[Node] - a list of nodes representing the problem.
    node_count: int - the number of nodes.
    filename: str - the name of the file to save to (path).

    @returns 
    None
    """

    plt_backend_plot(problem_definition, node_count)

    plt.margins(0.1)
    plt.savefig(filename, dpi=300)  

def show_solution_plot(problem_definition: list[Node], node_count: int, solution_idxs: list[int]) -> None:
    """
    Shows a plot for the problem_definition with solution highlighted on a graph.

    @arguments
    problem_definition: list[Node] - a list of nodes representing the problem.
    node_count: int - the number of nodes.
    solution_idxs: list[int] - a list of indexes of the selected medians.
    filename: str - the name of the file to save to (path).

    @returns
    None
    """

    plt_backend_plot(problem_definition, node_count, solution_idxs)
    plt.show()

def save_solution_plot(problem_definition: list[Node], node_count: int, solution_idxs: list[int], filename: str) -> None:
    """
    Shows a plot for the problem_definition with solution highlighted on a graph.

    @arguments
    problem_definition: list[Node] - a list of nodes representing the problem.
    node_count: int - the number of nodes.
    solution_idxs: list[int] - a list of indexes of the selected medians.

    @returns
    None
    """

    plt_backend_plot(problem_definition, node_count, solution_idxs)

    plt.margins(0.1)
    plt.savefig(filename, dpi=300)  
