import copy
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from main import uncapacitated_problem, real_world_input

from solvers import enumeration_solver, greedy_solver, vertex_substitution_solver

import threading as th

def input_creator(N):
    # D is a randomly generated NxN symmetric matrix
    D = np.random.randint(0, 500, size=(N, N))
    D = (D + D.T) / 2

    # C is a randomly generated N array
    C = np.random.randint(1, 1000, size=N)

    return D, C


def plotter(N, TIME_greedy, TIME_tb, TIME_es):
    TIME_greedy_avgs = []
    TIME_tb_avgs = []
    TIME_es_avgs = []
    for p in range(2, N):
        TIME_greedy_avgs.append(np.mean(TIME_greedy[p]))
        TIME_tb_avgs.append(np.mean(TIME_tb[p]))
        TIME_es_avgs.append(np.mean(TIME_es[p]))

    plt.plot(list(range(2, N)), TIME_greedy_avgs, label="greedy")
    plt.plot(list(range(2, N)), TIME_tb_avgs, label="vertex_substitution")
    plt.plot(list(range(2, N)), TIME_es_avgs, label="enumeration")

    plt.legend()
    plt.title(f"Time Comparision (N = {N})")
    plt.xticks(list(range(2, N)))
    plt.xlabel("p")
    plt.ylabel("Time (microseconds)")
    plt.show()


def comparator(N):
    TIME_greedy = [[] for _ in range(N)]
    TIME_tb = [[] for _ in range(N)]
    TIME_es = [[] for _ in range(N)]

    for p in range(2, N):
        for i in range(50):
            print(f"{N=}, {p=}, {i=}")

            D, C = input_creator(N)
            actp = p + 1
            Di, Ci = copy.deepcopy(D), copy.deepcopy(C)

            st = datetime.now()
            greedy_solver(Di, Ci, N, actp)
            ttg = datetime.now() - st
            Di, Ci = copy.deepcopy(D), copy.deepcopy(C)

            st = datetime.now()
            vertex_substitution_solver(Di, Ci, N, actp)
            tttb = datetime.now() - st
            Di, Ci = copy.deepcopy(D), copy.deepcopy(C)

            st = datetime.now()
            enumeration_solver(Di, Ci, N, actp)
            ttes = datetime.now() - st

            TIME_greedy[p].append(ttg.microseconds)
            TIME_tb[p].append(tttb.microseconds)
            TIME_es[p].append(ttes.microseconds)

    return TIME_greedy, TIME_tb, TIME_es


def visualize_each_p():
    # from utils import cost_of_configuration
    D, C, node_count = real_world_input()

    greedy_times = []
    tb_times = []
    es_times = []


    for i in range(1000):
        Di, Ci, ni = copy.deepcopy(D), copy.deepcopy(C), copy.deepcopy(node_count)
        st = datetime.now()
        uncapacitated_problem(Di, Ci, ni, solver="greedy")
        greedy_times.append(datetime.now() - st)
        Di, Ci, ni = copy.deepcopy(D), copy.deepcopy(C), copy.deepcopy(node_count)
        st = datetime.now()
        uncapacitated_problem(Di, Ci, ni, solver="vertex_substitution")
        tb_times.append(datetime.now() - st)
        Di, Ci, ni = copy.deepcopy(D), copy.deepcopy(C), copy.deepcopy(node_count)
        st = datetime.now()
        uncapacitated_problem(Di, Ci, ni, solver="enumeration")
        es_times.append(datetime.now() - st)

    return np.mean(greedy_times), np.mean(tb_times), np.mean(es_times)
    # print(f"{greedy_time=}\n{tb_time=}\n{es_time=}")

def visualize_each_n(p = 5):
    # from utils import cost_of_configuration
    Nmax = 21
    TIME_greedy = [[] for _ in range(Nmax)]
    TIME_tb = [[] for _ in range(Nmax)]
    TIME_es = [[] for _ in range(Nmax)]

    avgs_g = []
    avgs_tb = []
    avgs_es = []

    for N in range(3, 21):
        D, C = input_creator(N)

        for i in range(100):
            Di, Ci, ni = copy.deepcopy(D), copy.deepcopy(C), copy.deepcopy(N)
            st = datetime.now()
            greedy_solver(D, C, N, p)
            TIME_greedy[N].append((datetime.now() - st).microseconds)
            Di, Ci, ni = copy.deepcopy(D), copy.deepcopy(C), copy.deepcopy(N)
            st = datetime.now()
            vertex_substitution_solver(D, C, N, p)
            TIME_tb[N].append((datetime.now() - st).microseconds)
            Di, Ci, ni = copy.deepcopy(D), copy.deepcopy(C), copy.deepcopy(N)
            st = datetime.now()
            enumeration_solver(D, C, N, p)
            TIME_es[N].append((datetime.now() - st).microseconds)
            print(f"{N=}, {i=}")

        avgs_g.append(np.mean(TIME_greedy[N]))
        avgs_tb.append(np.mean(TIME_tb[N]))
        avgs_es.append(np.mean(TIME_es[N]))
    
    print(avgs_g, end="\n\n")
    print(avgs_tb, end="\n\n")
    print(avgs_es, end="\n\n")

    # p = 5
    # avgs_g = [0.83, 0.65, 0.73, 140.91, 167.68, 198.78, 232.1, 275.05, 314.36, 346.54, 410.7, 434.5, 481.31, 514.83, 549.0, 582.02, 614.77, 652.85]
    # avgs_tb = [26.37, 36.64, 52.16, 262.03, 284.75, 561.78, 621.15, 975.14, 1567.64, 1505.18, 2394.58, 3051.89, 3374.13, 2826.44, 4351.62, 5327.13, 5618.67, 6718.34]
    # avgs_es = [1.48, 1.46, 6.54, 33.45, 120.55, 353.52, 866.24, 1919.46, 3796.39, 6915.65, 12252.08, 20420.13, 32480.14, 49786.66, 75983.48, 110364.27, 158368.82, 221628.27]

    plt.plot(list(range(3, 21)), avgs_g, label="greedy")
    plt.plot(list(range(3, 21)), avgs_tb, label="vertex_substitution")
    plt.plot(list(range(3, 21)), avgs_es, label="enumeration")
    plt.legend()
    plt.title(f"Time Comparision (p = {p})")
    plt.xticks(list(range(3, 21)))
    plt.xlabel("N")
    plt.ylabel("Time (microseconds)")
    plt.savefig("time_comparison_nchange.png")
    plt.show()



def plot_bar(time_greedy, time_tb, time_es):

    plt.bar(0, time_greedy.microseconds, label="greedy")
    plt.bar(1, time_tb.microseconds, label="greedy")
    plt.bar(2, time_es.microseconds, label="greedy")
    plt.title("Time Comparision (for Real World Problem)")
    plt.xlabel("Solver")
    plt.xticks([0, 1, 2], ["Greedy", "Vertex Substitution", "Enumeration"])
    plt.ylabel("Time (microseconds)")
    # plt.legend()
    plt.show()

if __name__ == "__main__":
    # N = 15
    # TIME_greedy, TIME_tb, TIME_es = comparator(N)
    # print("\n\n\n")
    # print(f"{TIME_tb=}\n\n{TIME_es=}\n\n{TIME_greedy=}\n")
    # print("\n\n\n")
    # plotter(N, TIME_greedy, TIME_tb, TIME_es)
    # plot_bar(*visualize_each_p())
    visualize_each_n(p=17)



# types of visualizations:
# 1. time taken for each p, averaged over multiple runs {Fixed N=10} -> Line graph {generic showcase of which is better}
# 2. time taken for whole "solution", averaged over multiple runs {Fixed N=10} -> Bar graph
# 3. time taken for different Ns (N=3, p=2 to N=20, p=2) {Fixed p} -> Line graph
# 4. accuracy for whole "solution", compared to enumeration {Fixed N=10} -> if p value =, then line graph
