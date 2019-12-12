from ga import AlgoGen
from problem_individu import Problem_Interface
import sys
import string

DIRECTIONS = ['N', 'E', 'S', 'W']

if __name__ == "__main__":
    if len(sys.argv) == 5:
        filename = sys.argv[1]
        pop_size = int(sys.argv[2])
        generation_nb = int(sys.argv[3])
        mut_proba = float(sys.argv[4])
    else:
        print("the number of argument is not sufficient,you have 4 arguments : filename, population size, number of generation and mutation probability")
        exit()

    prob = Problem_Interface(filename, DIRECTIONS)
    algo = AlgoGen(prob,pop_size,mut_proba)
    algo.creat_pop()
    
    pop = algo.population
    print("Generation : 1")
    print("maximum score = ",algo.population[0].get_score())
    while algo.generation <= generation_nb:
        algo.next_generation()
        print("Gneration : ",algo.generation)
        print("max score = ",algo.population[0].get_score())
        print("Path : ",algo.population[0].get_value()[0])
        print("............")

    step, d = algo.problem.get_step_dist(algo.population[0])
    if d == 0:
        print("Path found, Path : ", algo.population[0].get_value()[0][0:step])
        exit(0)
    print("Path not found")
    
