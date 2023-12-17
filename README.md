# pmedian_opt

A set of heuristic solutions to the p-median facility location problem.

The following heuristics are implemented:

* Teitz and Bart's "Vertex Substitution Heuristic"
* The "Greedy Heuristic"

Further, a direct brute force solution is also implemented that takes exponential amounts of time to compute.

## File Structure

The `src/solvers.py` file contains the implenetations of the heuristics and the brute force solution.

The `src/main.py` contains some examples on how to use the solvers.
