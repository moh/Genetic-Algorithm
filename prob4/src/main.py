from ga import AlgoGen
from problem_individu import Problem_Interface
from haunted_field import Haunted_Field
import sys
import string

DIRECTIONS = ["U", "D", "R", "L"]

if __name__ == "__main__":
    if len(sys.argv) == 7:
        N = int(sys.argv[1])
        pop_size = int(sys.argv[2])
        generation_nb = int(sys.argv[3])
        mut_proba = float(sys.argv[4])
        size = int(sys.argv[5])
        b = int(sys.argv[6])
    else:
        print("The number of argument is not sufficient,you have 6 arguments : N, population size, number of generation and mutation probability, the with/height of the terrain, the number of bomb")
        print("N is the number of terrain that we are gonna try")
        exit()

    fields = [Haunted_Field(size,size) for x in range(N)]
    
    for x in fields:
        x.init_monsters(b)
    
    prob = Problem_Interface(fields, 243, DIRECTIONS)
    algo = AlgoGen(prob,pop_size,mut_proba)
    algo.creat_pop()
    
    pop = algo.population
    print("Generation : 1")
    print("maximum score = ",algo.population[0].get_score())
    print("............")
    
    while algo.generation <= generation_nb:
        algo.next_generation()
        print("Gneration : ",algo.generation)
        print("max score = ",algo.population[0].get_score())
        print("............")

    print("The fields used in the test are : ")
    for x in range(len(fields)):
        print("Field"+str(x)+" : ")
        print(fields[x])

    print("The best configuration is : ", algo.population[0].get_value()[0])
    print("The final results for this config are : ", algo.population[0].state_f)
    
    
