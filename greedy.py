import numpy as np
import matplotlib.pyplot as plt


class Node:
    i = 0

    def __init__(self, point, cost):
        self.point = np.array(point)
        self.__class__.i += 1
        self.cost = cost
        self.id = self.__class__.i

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return f"Node({self.point}, id={self.id})"


def calculate_total_cost(points, medians):
    for median in medians:
        c = 0
        dist_arr = np.zeros(
            shape=(len(points),)
        )  # distances of MEDIAN to all points as below
        # print(f"{medians=}")
        # print("MEDIAN: ", median)
        facility_cost_of_median = median.cost
        for point in points:
            dist_arr[c] = np.linalg.norm(point.point - median.point)
            # print(f"{dist_arr=}")
            c += 1
        cost = np.sum(dist_arr) + facility_cost_of_median
        # print(f"{cost=}")
    return cost


def compute_better_cost(points, medians):
    cost = 0
    for point in points:
        mindist = float("inf")
        for median in medians:
            dist = np.linalg.norm(point.point - median.point)
            if dist < mindist:
                mindist = dist
        cost += mindist

    cost += sum([median.cost for median in medians])

    return cost


def greedy_p_median(points, p):
    num_points = len(points)
    if p >= num_points:
        return points

    medians = []
    remaining_points = points.copy()
    # print(f"{remaining_points=}")
    for _ in range(p):
        best_cost = float("inf")
        best_medians = []

        for point in remaining_points:
            candidate_medians = medians + [point]

            # print(f"{candidate_medians=} {point=}")
            cost = calculate_total_cost(points, candidate_medians)

            if cost < best_cost:
                best_cost = cost
                best_median = point

        medians.append(best_median)
        # DELETE best_median from remaining_points
        # print(f"{remaining_points=}")
        # print(f"{best_median=}")
        # print(f"{remaining_points == best_median=}")
        # print(f"{np.where(remaining_points == best_median)=}")
        remaining_points = np.delete(
            remaining_points, np.where(remaining_points == best_median)
        )

    return medians


def variantA(point):
    best_cost = float("inf")
    best_medians = []
    for p in range(1, len(points) + 1):
        print(f">>>> {p=}")
        selected_medians = greedy_p_median(points, p)

        if selected_medians is not None:
            total_cost = compute_better_cost(points, selected_medians)
            # print(f"{total_cost=}")
            # print(f"{selected_medians=}")
            if total_cost < best_cost:
                best_cost = total_cost
                best_medians = selected_medians

    return best_medians, best_cost


def iamplot(points):
    xarr = []
    yarr = []
    costtag = []
    tags = []
    for point in points:
        xarr.append(point.point[0])
        yarr.append(point.point[1])
        costtag.append(point.cost)
        tags.append(point.id)

    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.scatter(xarr, yarr)
    # plot the tags also bro
    for i in range(len(xarr)):
        plt.annotate(f"id{tags[i]}: cst{costtag[i]}", (xarr[i] + 0.01, yarr[i] - 0.10))
    plt.show()


# Assuming Facilities can be Located Next to Customer, Hence 0 Distance in the Case that Median is Chosen #
if __name__ == "__main__":
    points = np.array(
        [
            Node([0, 0], 10000),
            Node([2, 2], 0),
            Node([2, -2], 0),
            Node([-2, 2], 0),
            Node([-2, -2], 0),
        ]
    )
    # facility_costs = np.array([10,20,10,20,100000])

    chosen_medians, total_cost = variantA(points)
    print("=== ANSSSSSS ===")
    print(f"Chosen Medians: {chosen_medians}")
    print(f"Total Cost: {total_cost}")

    iamplot(points)
