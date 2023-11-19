import numpy as np

def calculate_total_cost(median_idxs, distance_matrix, node_count: int, cost_array, production_array, demand_array) -> float:
    
    # Defining Visted Medians, Cost, and Total Demand #
    visited_median_idxs = []
    cost = 0
    total_demand = np.sum(demand_array)
    for median_idx in median_idxs:

        # Calculating Distance of Median to Remaining Nodes #
        total_distance = 0
        for i in range(node_count):
            if i not in visited_median_idxs:
                total_distance += distance_matrix[median_idx,i]

        #print(f'{total_distance=}')
        # median Cost #
        for i in range(node_count):
            # Dividing Demand to be Fulfilled by Production per unit area #
            area = total_demand/production_array[i]
            median_cost = area*cost_array[i]
        
        # Adding Cost of median to Total Cost #
        cost += median_cost + total_distance

        # Removing Demand of Median from Total_Demand #
        total_demand -= demand_array[median_idx]

        # Appending Current Median to Visited Medians #
        visited_median_idxs.append(median_idx)
        #print(f'{visited_median_idxs=}')

   # print(f'{median_idxs=},{cost=}')
    return cost 

def greedy_solver_B(distance_matrix, node_count: int, cost_array, production_array, demand_array, p: int = 1) -> list[int]:

    if p >= node_count:
        return list(range(node_count)) # select all
        
    best_median_idxs: list[int] = []
    remaining_point_idxs = np.arange(node_count)

    for _ in range(p):
        best_cost = np.inf

        for node_idx in remaining_point_idxs:
            # node_idx is the index that I am currently considering as a median(s)
            candidate_positions_for_medians = best_median_idxs.copy() + [node_idx]
            #print(f'{candidate_positions_for_medians=}')

            cost = calculate_total_cost(
                    candidate_positions_for_medians,
                    distance_matrix, 
                    node_count, 
                    cost_array, 
                    production_array, 
                    demand_array
            )


            if cost < best_cost:
                best_cost = cost
                best_median_idx = node_idx

        best_median_idxs.append(best_median_idx)

        # delete the selected median from the candidate list
        remaining_point_idxs = np.delete(
            remaining_point_idxs, np.where(remaining_point_idxs == best_median_idx)
        )
        #print(f'{remaining_point_idxs=}')

    return best_median_idxs

def compute_better_cost(distance_matrix, node_count, median_idxs, cost_array, production_array, demand_array) -> float:
    """
    A method to calculate total cost is given.
    
    @arguments
    problem_definition: list[Node] - the problem definition
    node_count: int - the number of nodes.
    medians_idxs: list[int] - the indexes of the medians for which we want to calculate the total cost

    @returns
    cost: float - the total cost of choosing the given medians
    """

    # Generating X Matrix based on minimum distance
    X = np.zeros((node_count,node_count))
    for i in range(node_count):
        # If i is already a median, skip #
        if i in median_idxs:
            continue

        # Initializing Minimum Distance and Best Median
        mindist = float("inf")
        best_median = None

        # Iterating though Medians to find Closest Median
        for median in median_idxs:
            dist =  distance_matrix[median][i]
            if dist < mindist and median != i:
                mindist = dist
                best_median = median 

        # Assigning Node to Closest Median
        X[best_median,i] = 1

    # Finding Facility Cost
    facility_cost = 0
    for median in median_idxs:
        median_demand = np.dot(demand_array,X[median]) + demand_array[median]
        facility_area = median_demand/production_array[median]
        facility_cost += facility_area*cost_array[median]
    
    # To find Delivery Cost #
    delivery_cost = 0
    for i in range(node_count):
        delivery_cost += np.dot(X[median],distance_matrix[median])

    return delivery_cost+facility_cost 

def variantB(distance_matrix, node_count: int, cost_array, production_array, demand_array) -> list[int]:
    """
    A solving system for "variantB" of our problem. The "variantB" problem requires us to *test* different values of p
    to find the best one. This is a brute-force approach.

    @arguments
    distance_matrix - Distance of each node to every other node
    node_count: int - the number of nodes.
    cost_array - Cost per unit area of each median
    production_array - Product per unit area at each median
    demand_array - Demand at each Customer

    @returns 
    tuple with elements best_medians, best_cost
    best_median: list[int] - a list of indexes of the best (selected) medians.
    best_cost: float - the cost incurred when selecting the best medians.
    """

    best_cost = np.inf
    best_medians = []

    for p in range(1, node_count + 1):
        selected_medians = greedy_solver_B(
                distance_matrix, 
                node_count, 
                cost_array, 
                production_array, 
                demand_array, 
                p
        )
        #print(f'{p=},{selected_medians=}')
        if selected_medians is not None:
            total_cost = compute_better_cost(
                            distance_matrix, 
                            node_count,
                            selected_medians,
                            cost_array,
                            production_array,
                            demand_array
                        )
            if total_cost < best_cost:
                best_cost = total_cost
                best_medians = selected_medians
        else:
            print(f"\tUnable to find a solution for {p=}")

    return best_medians, best_cost


if __name__ == '__main__':
    
    # Distance Matrix
    dist_mat = np.array([[0,10,3],[10,0,4],[3,4,0]])

    # Number of Customers
    node_count = len(dist_mat)

    # Cost of median per Unit Area
    C = np.array([10,5,7])

    # Production per Unit Area
    P = np.array([10,10,10])

    # Demand of Customer
    W = np.array([1,1,15])

    selected_median_indexes, cost_incurred = variantB(dist_mat,node_count,C,P,W)

    print(f"Best Medians: {selected_median_indexes}")
    print(f"Cost: {cost_incurred}") # print the cost
