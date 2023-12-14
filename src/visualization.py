from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

from solvers import enumeration_solver, greedy_solver, vertex_substitution_solver


def input_creator(N):
    # D is a randomly generated NxN symmetric matrix
    D = np.random.randint(0, 500, size=(N, N))
    D = (D + D.T) / 2

    # H is a randomly generated N array
    C = np.random.randint(1, 2000, size=N)

    return D, C


def plotter(N, TIME_greedy, TIME_tb, TIME_es):
    TIME_greedy_avgs = []
    TIME_tb_avgs = []
    TIME_es_avgs = []
    for p in range(1, N):
        TIME_greedy_avgs.append(np.mean(TIME_greedy[p]))
        TIME_tb_avgs.append(np.mean(TIME_tb[p]))
        TIME_es_avgs.append(np.mean(TIME_es[p]))

    plt.plot(list(range(2, N)), label="greedy")
    plt.plot(list(range(2, N + 1)), TIME_tb_avgs, label="tb")
    plt.plot(list(range(2, N + 1)), TIME_es_avgs, label="es")

    plt.legend()
    plt.title("Woe")
    plt.xticks(list(range(2, N + 1)))
    plt.show()


def comparator(N):

    TIME_greedy = [[] for _ in range(N)]
    TIME_tb = [[] for _ in range(N)]
    TIME_es = [[] for _ in range(N)]

    for p in range(1, N):
        for i in range(100):
            D, C = input_creator(N)
            actp = p + 1

            st = datetime.now()
            greedy_solver(D, C, N, actp)
            ttg = datetime.now() - st

            st = datetime.now()
            vertex_substitution_solver(D, C, N, actp)
            tttb = datetime.now() - st

            st = datetime.now()
            enumeration_solver(D, C, N, actp)
            ttes = datetime.now() - st

            TIME_greedy[p].append(ttg.microseconds)
            TIME_tb[p].append(tttb.microseconds)
            TIME_es[p].append(ttes.microseconds)

    return TIME_greedy, TIME_tb, TIME_es


if __name__ == "__main__":
    N = 15
    TIME_greedy, TIME_tb, TIME_es = comparator(N)
    print("\n\n\n")
    print(f"{TIME_tb=}\n\n{TIME_es=}\n\n{TIME_greedy=}\n")
    print("\n\n\n")
    plotter(N, TIME_greedy, TIME_tb, TIME_es)


# types of visualizations:
# 1. time taken for each p, averaged over multiple runs {Fixed N=10} -> Line graph {generic showcase of which is better}
# 2. time taken for whole "solution", averaged over multiple runs {Fixed N=10} -> Bar graph
# 3. time taken for different Ns (N=3, p=2 to N=20, p=2) {Fixed p} -> Line graph
# 4. accuracy for whole "solution", compared to enumeration {Fixed N=10} -> if p value =, then line graph

# Graph representation of the problem
# Graph representation of the problem with selected medians circled
# Graph representation with image underneath, with selected medians circled


def visualize_each_p():
    pass

def visualize_solution():
    pass

def visualize_n_increase():
    pass

def plot_problem():
    pass

def plot_solution():
    pass

def plot_graph():
    pass 