# define variables

# number of customers (N) is the DEMAND points
# TOTAL number of POTENTIAL FACILITY LOCATIONS (p)
# Distance matrix (D) is the distance between each customer and each facility (N x p)
# Cost vector (C) is the cost of opening each facility (p x 1)

# X_ij is 1 if customer i is assigned to facility j else 0
# Y_j is 1 if a POTENTIAL location is chosen else 0
# j belong to p and i belong to N

# Total COST (to minimize) = sum of (C_j * Y_j) + sum of (sum of (D_ij * X_ij))

# Code to find the optimal solution for the p-median problem
# using heuristic of tietz_and_bart (1989)

# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random


# the tietz and bart heuristic
def t_and_b_heuristic(p, N, D, C, iterations):
    best_cost = float("inf")
    best_X = None
    best_Y = None

    for _ in range(iterations):
        # Step 2
        X = np.zeros((N, p))
        Y = np.zeros(p)

        # Step 3
        remaining_demand_points = set(range(N))

        # Step 4
        while len(remaining_demand_points) > 0:
            j = random.choice(list(remaining_demand_points))
            Y[j] = 1
            remaining_demand_points.remove(j)

            # Step 5
            for i in range(N):
                if X[i].sum() == 0 or D[i][j] < D[i][X[i].argmin()]:
                    X[i] = np.zeros(p)
                    X[i][j] = 1

        # Step 7
        cost = (C * Y).sum() + (D * X).sum()

        if cost < best_cost:
            best_cost = cost
            best_X = X
            best_Y = Y

    return best_cost, best_X, best_Y


if __name__ == "__main__":
    # define variables
    p = 5
    N = 4
    D = np.array(
        [
            [2, 2, 2, 4 * np.sqrt(2), 4 * np.sqrt(2)],
            [2, 4 * np.sqrt(2), 2, 2, 4 * np.sqrt(2)],
            [4 * np.sqrt(2), 2, 2, 4 * np.sqrt(2), 2],
            [4 * np.sqrt(2), 4 * np.sqrt(2), 2, 2, 2],
        ]
    )
    C = np.array([5, 6, 12, 5, 6])
    iterations = 100

    # run the heuristic
    cost, X, Y = t_and_b_heuristic(p, N, D, C, iterations)

    # print the results
    print("Cost: ", cost)
    print("X: \n", X)


