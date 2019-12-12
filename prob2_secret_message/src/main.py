from ga import AlgoGen
from problem_individu import Problem_Interface
import sys
import string

LETTERS = string.ascii_lowercase + " "

if __name__ == "__main__":
    if len(sys.argv) == 4:
        pop_size = int(sys.argv[1])
        generation_nb = int(sys.argv[2])
        mut_proba = float(sys.argv[3])
    else:
        print("the number of argument is not sufficient,you have 3 arguments : population size, number of generation and mutation probability")
        exit()

    prob = Problem_Interface(LETTERS,30)
    algo = AlgoGen(prob,pop_size,mut_proba)
    algo.creat_pop()
    
    pop = algo.population
    print("Generation : 1")
    print("maximum number = ",algo.population[0].get_score())
    while algo.generation <= generation_nb:
        algo.next_generation()
        print("Gneration : ",algo.generation)
        print("max number = ",algo.population[0].get_score())
        print("word : ",algo.population[0].get_value()[0])
        print("............")
    
