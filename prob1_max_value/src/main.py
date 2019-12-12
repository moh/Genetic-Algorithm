from ga import AlgoGen
from problem_individu import Problem_Interface
import sys

if __name__ == "__main__":
    if len(sys.argv) == 6:
        xmin = float(sys.argv[1])
        xmax = float(sys.argv[2])
        pop_size = int(sys.argv[3])
        generation_nb = int(sys.argv[4])
        mut_proba = float(sys.argv[5])
    else:
        print("the number of argument is not sufficient,you have 5 arguments : xmin, xmax, population size, number of generation and mutation probability")
        exit()

    prob = Problem_Interface(xmin,xmax,["0","1"],12)
    algo = AlgoGen(prob,pop_size,mut_proba)
    algo.creat_pop()
    
    pop = algo.population
    print("Generation : 1")
    print("maximum number = ",algo.population[0].get_score())
    while algo.generation <= generation_nb:
        algo.next_generation()
        print("Gneration : ",algo.generation)
        print("max number = ",algo.population[0].get_score())
    
