# Dynamic programming

**References:**
- https://en.wikipedia.org/wiki/Dynamic_programming


[Wikipedia][wikipedia_dp]:

> Dynamic programming is both a mathematical optimization method and a computer programming method. 
> 
> It refers to simplifying a complicated problem by breaking it down into simpler sub-problems in a
> recursive manner. While some decision problems cannot be taken apart this way, decisions that span
> several points in time do often break apart recursively. Likewise, in computer science, if a problem
> can be solved optimally by breaking it into sub-problems and then recursively finding the optimal
> solutions to the sub-problems, then it is said to have optimal substructure. 


[Introduction to algorithms][intro_to_algorithms]:

> Dynamic programming typically applies to optimization problems in which we
> make a set of choices in order to arrive at an optimal solution. As we make
> each choice, subproblems of the same form often arise. Dynamic programming
> is effective when a given subproblem may arise from more than one partial set of
> choices; the key technique is to store the solution to each such subproblem in case it
> should reappear.


## Examples


- Coin change problem
- Dijkstra's algorithm for the shortest path problem
- Fibonacci sequence
- A type of balanced 0–1 matrix
- ...




## Approaches

- **Top-down approach**:
	This is the direct fall-out of the recursive formulation of
	any problem. If the solution to any problem can be formulated recursively using
	the solution to its sub-problems, and if its sub-problems are overlapping, then
	one can easily memoize or store the solutions to the sub-problems in a table.
	Whenever we attempt to solve a new sub-problem, we first check the table to see
	if it is already solved. If a solution has been recorded, we can use it
	directly, otherwise we solve the sub-problem and add its solution to the table.

- **Bottom-up approach**:
	Once we formulate the solution to a problem recursively as in terms of its
	sub-problems, we can try reformulating the problem in a bottom-up fashion: try
	solving the sub-problems first and use their solutions to build-on and arrive
	at solutions to bigger sub-problems. This is also usually done in a tabular
	form by iteratively generating solutions to bigger and bigger sub-problems by
	using the solutions to small sub-problems. For example, if we already know the
	values of F41 and F40, we can directly calculate the value of F42.

## Properties

Properties indicating that the problem can be solved using dynamic programming:
- overlapping subproblems
- optimal substructure


See below


## Overlapping subproblems

**References:**
- https://en.wikipedia.org/wiki/Overlapping_subproblems
- https://www.geeksforgeeks.org/?p=12635
- https://www.geeksforgeeks.org/?p=12819


> In computer science, a problem is said to have overlapping subproblems if the
> problem can be broken down into subproblems which are reused several times or a
> recursive algorithm for the problem solves the same subproblem over and over
> rather than always generating new subproblems.



### Examples


#### Fibonacci

The problem of computing the Fibonacci sequence exhibits overlapping
subproblems.

The problem of computing the `n`th Fibonacci number `F(n)`, can be
broken down into the subproblems of computing `F(n − 1)` and `F(n − 2)`, and
then adding the two. The subproblem of computing `F(n − 1)` can itself be broken
down into a subproblem that involves computing `F(n − 2)`. Therefore, the
computation of `F(n − 2)` is reused, and the Fibonacci sequence thus exhibits
overlapping subproblems. 


## Optimal substructure


**References:**
- https://en.wikipedia.org/wiki/Optimal_substructure
- https://www.geeksforgeeks.org/optimal-substructure-property-in-dynamic-programming-dp-2


[Wikipedia][wikipedia_optimal_substructure]:
> In computer science, a problem is said to have optimal substructure if an
> optimal solution can be constructed from optimal solutions of its subproblems.
> This property is used to determine the usefulness of dynamic programming and
> greedy algorithms for a problem.

[Introduction to algorithms][intro_to_algorithms]:
> Optimal solutions to a problem incorporate optimal solutions to related subproblems.

### Examples

Consider finding a shortest path for travelling between two cities by car, as
illustrated in Figure 1. Such an example is likely to exhibit optimal
substructure. That is, if the shortest route from Seattle to Los Angeles passes
through Portland and then Sacramento, then the shortest route from Portland to
Los Angeles must pass through Sacramento too. That is, the problem of how to
get from Portland to Los Angeles is nested inside the problem of how to get
from Seattle to Los Angeles. (The wavy lines in the graph represent solutions
to the subproblems.) 



[wikipedia_dp]: https://en.wikipedia.org/wiki/Dynamic_programming
[wikipedia_optimal_substructure]: https://en.wikipedia.org/wiki/Optimal_substructure
[intro_to_algorithms]: https://mitpress.mit.edu/books/introduction-algorithms-third-edition
