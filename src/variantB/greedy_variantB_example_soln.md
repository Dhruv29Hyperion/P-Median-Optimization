# p=1 #
 
## Greedy Cost for [0] ##
    
    median_idx=0
    median_cost=13.0
    total_distance=10
    cost=23.0
 
## Greedy Cost for [1] ##
    
    median_idx=1
    median_cost=18.571428571428573
    total_distance=12
    cost=30.571428571428573
 
## Greedy Cost for [2] ##
    
    median_idx=2
    median_cost=16.25
    total_distance=14
    cost=30.25
 
## Greedy Cost for [3] ##
    
    median_idx=3
    median_cost=9.1
    total_distance=8
    cost=17.1
    Selected Median: [3]
 
## Calculating Cost of [3,0] ##
    median=3
    median_demand=65.0
    facility_area=13.0
    cost_array[median]=0.7
    
    facilities_cost=9.1
    distance_cost=8
    
    total_cost=17.1

# p=2 #
 
## Greedy Cost for [3,0] ##
    median_idx=3
    median_cost=9.1
    total_distance=8
    cost=17.1
    
    median_idx=0
    median_cost=10.0
    total_distance=7
    cost=34.1
 
## Greedy Cost for [3,1] ##
    median_idx=3
    median_cost=9.1
    total_distance=8
    cost=17.1
    
    median_idx=1
    median_cost=14.285714285714286
    total_distance=10
    cost=41.385714285714286
 
## Greedy Cost for [3,2] ##
    median_idx=3
    median_cost=9.1
    total_distance=8
    cost=17.1
 
    median_idx=2
    median_cost=12.5
    total_distance=11
    cost=40.6
 
    Selected Median: [3,0]
 
## Calculating Cost of [3,0] ##
    median=3
    median_demand=55.0
    facility_area=11.0
    cost_array[median]=0.7
 
    median=0
    median_demand=10.0
    facility_area=2.0
    cost_array[median]=1.0
 
    facilities_cost=9.7
    distance_cost=5
    total_cost = 14.7
 
# p=3 #
 
## Greedy Cost for [3,0,1] ##
    median_idx=3
    median_cost=9.1
    total_distance=8
    cost=17.1
 
    median_idx=0
    median_cost=10.0
    total_distance=7
    cost=34.1
 
    median_idx=1
    median_cost=11.428571428571429
    total_distance=7
    cost=52.52857142857143

## Greedy Cost for [3,0,2] ##
    median_idx=3
    median_cost=9.1
    total_distance=8
    cost=17.1
 
    median_idx=0
    median_cost=10.0
    total_distance=7
    cost=34.1
 
    median_idx=2
    median_cost=10.0
    total_distance=7
    cost=51.1
 
    Selected Medians: [3,0,2]

## Calculating Cost of [3,0,2] ##
    median=3
    median_demand=30.0
    facility_area=6.0
    cost_array[median]=0.7
 
    median=0
    median_demand=10.0
    facility_area=2.0
    cost_array[median]=1.0
        
    median=2
    median_demand=25.0
    facility_area=4.166666666666667
    cost_array[median]=1.5
 
    facilities_cost=12.45
    distance_cost=2
 
    total_cost=14.45

# p=4 #

Selected Medians: [0,1,2,3]

## Calculating Cost of [0,1,2,3] ##
    median=0
    median_demand=10.0
    facility_area=2.0
    cost_array[median]=1.0
 
    median=1
    median_demand=15.0
    facility_area=2.142857142857143
    cost_array[median]=2.0
 
    median=2
    median_demand=25.0
    facility_area=4.166666666666667
    cost_array[median]=1.5
 
    median=3
    median_demand=15.0
    facility_area=3.0
    cost_array[median]=0.7
 
    facility_cost=14.635714285714284
    delivery_cost=0
 
    total_cost=14.635714285714284

## Summary ##
p=1
    selected_medians=[3]
    total_cost=17.1

p=2
    selected_medians=[3, 0]
    total_cost=14.7

p=3
    selected_medians=[3, 0, 2]
    total_cost=14.45

p=4
    selected_medians=[0, 1, 2, 3]
    total_cost=14.635714285714284

**Best Medians: [3, 0, 2]**
**Cost: 14.45**
