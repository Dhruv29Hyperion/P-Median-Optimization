import numpy as np

def calculate_total_cost(median_idxs, distance_matrix, node_count: int, cost_array, production_array, demand_array) -> float:
    """
    A method to calculate greedy total cost of given set medians.
    
    @arguments
    median_idxs: list[int] - the indexes of the medians for which we want to calculate the total cost
    distance_matrix - distances from node i to node j
    node_count: int - the number of nodes.
    cost_array - cost per unit area for each median
    production_array - production per unit area for each median
    demand_array - demand of each customer

    @returns
    cost: float - the total cost of choosing the given medians
    """
    
    # Defining Visted Medians, Cost, and Total Demand #
    visited_median_idxs = []
    cost = 0
    total_demand = np.sum(demand_array)
    #print(f'{median_idxs=}')
    for median_idx in median_idxs:
        # Calculating Distance of Median to Remaining Nodes #
        total_distance = 0
        median_cost = 1
        for i in range(node_count):
            if i not in visited_median_idxs:
                total_distance += distance_matrix[median_idx,i]
                # Dividing Demand to be Fulfilled by Production per unit area #
        area = total_demand/production_array[median_idx]
        median_cost = area*cost_array[median_idx]
        print(f'\t{median_idx=}')
        print(f'\t\t{median_cost=}')
        print(f'\t\t{total_distance=}')
        
        # Adding Cost of median to Total Cost #
        cost += median_cost + total_distance
        print(f'\t{cost=}')

        # Removing Demand of Median from Total_Demand #
        total_demand -= demand_array[median_idx]

        # Appending Current Median to Visited Medians #
        visited_median_idxs.append(median_idx)
        #print(f'{visited_median_idxs=}')

   # print(f'{median_idxs=},{cost=}')
    return cost 

def greedy_solver_B(distance_matrix, node_count: int, cost_array, production_array, demand_array, p: int = 1) -> list[int]:
    """
    Modified Greedy heuristic system for the variant B p-median problem.
    Returns the "indexes" of the best p medians.

    @arguments
    distance_matrix - distances from node i to node j
    node_count: int - the number of nodes.
    cost_array - cost per unit area for each median
    production_array - production per unit area for each median
    demand_array - demand of each customer
    p: int - the number of medians to select.

    @returns
    best_median_idxs: list[int] - a list of indexes of the best (selected) medians.
    """

    # If p >= nodes, select all nodes
    if p >= node_count:
        return list(range(node_count))

    # Initializing Best Medians and Remaining Points #    
    best_median_idxs: list[int] = []
    remaining_point_idxs = np.arange(node_count)

    # For each p, finding lowest cost median, appending to best_median_idxs and removing median from remaining_point_idxs
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
    A method to calculate total cost is given using minimum distance heuristic to build Xij matrix.
    
    @arguments
    distance_matrix - distances from node i to node j
    node_count: int - the number of nodes.
    medians_idxs: list[int] - the indexes of the medians for which we want to calculate the total cost
    cost_array - cost per unit area for each median
    production_array - production per unit area for each median
    demand_array - demand of each customer

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

    print(f'\t{X=}')
    # Finding Facility Cost
    facility_cost = 0
    delivery_cost = 0
    for median in median_idxs:
        median_demand = np.dot(demand_array,X[median]) + demand_array[median]
        print(f'\t\t{median=}')
        print(f'\t\t{median_demand=}')
        facility_area = median_demand/production_array[median]
        print(f'\t\t{facility_area=},{cost_array[median]=}')
        facility_cost += facility_area*cost_array[median]
        delivery_cost += np.dot(X[median],distance_matrix[median])

    print(f'\t{facility_cost=}')

    return delivery_cost+facility_cost 

