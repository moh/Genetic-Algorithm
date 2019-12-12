in that problem, the goal is to find the maximum of the function f(x) = (x**2)*sin(x)*cos(x), in an interval xmin to xmax, we use the genetic algorithm to produce a population of many possible solution, and evolve them to get the best solution possible.
To test this problem, type "python main.py xmin xmax pop_size generations proba"
where:
1- xmin : the minimum x in the interval
2- xmax : the maximum x in the interval
3- pop_size : the size of population used in the genetic algorithm
4- generations : number of generations to be tested
5- proba: mutation probability used in AG

Example : 
> python main.py 13 18 30 40 0.01