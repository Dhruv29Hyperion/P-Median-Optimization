import copy
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

from solvers import greedy_solver
# from main import tietz_and_bart
from DEATH import enumeration_solver, tietz_and_bart


def input_creator(N):
    # D is a randomly generated NxN symmetric matrix
    # with zeros on the diagonal
    D = np.random.randint(0, 500, size=(N, N))
    D = (D + D.T) / 2

    # H is a randomly generated NxN diagonal matrix
    H = np.diag(np.random.randint(1, 2000, size=N))

    return D, H


def plotter(N, TIME_tb, TIME_es):
    # TIME_greedy_avgs = []
    TIME_tb_avgs = []
    TIME_es_avgs = []
    for p in range(1, N):
        # TIME_greedy_avgs.append(np.mean(TIME_greedy[p]))
        TIME_tb_avgs.append(np.mean(TIME_tb[p]))
        TIME_es_avgs.append(np.mean(TIME_es[p]))

    # plt.plot(list(range(2, N)), label="Greedy")

    plt.plot(list(range(2, N+1)), TIME_tb_avgs, label="tb")

    plt.plot(list(range(2, N+1)), TIME_es_avgs, label="es")
    plt.legend()
    plt.title("Woe")
    plt.xticks(list(range(2, N+1)))
    plt.show()


def comparator(N):
    TIME_greedy = [[]] * N

    TIME_tb = [[] for _ in range(N)]
    TIME_es = [[] for _ in range(N)]

    for p in range(1, N):
        for i in range(100):
            D, H = input_creator(N)
            actp = p + 1
            # st = datetime.now()
            # print(D, H, N, actp)
            # greedy_solver(D, H, N, actp)
            # ttg = datetime.now() - st
            st = datetime.now()
            tietz_and_bart(D, H, actp)
            tttb = datetime.now() - st
            st = datetime.now()
            enumeration_solver(D, H, actp)
            ttes = datetime.now() - st

            # TIME_greedy[p].append(ttg.microseconds)
            TIME_tb[p].append(tttb.microseconds)
            TIME_es[p].append(ttes.microseconds)

    return TIME_tb, TIME_es


if __name__ == "__main__":
    N = 15
    TIME_tb, TIME_es = comparator(N)
    print("\n\n\n")
    print(f"{TIME_tb=}\n\n{TIME_es=}\n")
    print("\n\n\n")
    plotter(N, TIME_tb, TIME_es)