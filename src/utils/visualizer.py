import matplotlib.pyplot as plt
import numpy as np
from .classes import Node

def plt_backend_plot(problem_definition: list[Node], problem_length: int):
    xarr = np.zeros(shape=(problem_length,))
    yarr = np.zeros(shape=(problem_length,))
    tags = [""]*problem_length
    i = 0
    for node in problem_definition:
        xarr[i] = node.point.x
        yarr[i] = node.point.y
        tags[i] = f"i{node.id}: {node.cost}"
        i += 1

    plt.figure(figsize=(10, 10))
    plt.title("Problem Definition Plot")
    plt.scatter(xarr, yarr, color="red")
    plt.axhline(0, color="grey")
    plt.axvline(0, color="grey")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    for i in range(problem_length):
        plt.annotate(tags[i], (xarr[i] + 0.05, yarr[i] - 0.10))

def show_problem_plot(problem_definition: list[Node], problem_length: int):
    plt_backend_plot(problem_definition, problem_length)
    plt.show()

def save_problem_plot(problem_definition: list[Node], problem_length: int, filename: str):
    plt_backend_plot(problem_definition, problem_length)
    # margins minimum
    plt.margins(0.1)
    plt.savefig(filename, dpi=300)
