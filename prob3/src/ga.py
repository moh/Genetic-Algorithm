import random


class AlgoGen():

    def __init__(self, problem, population_size, mutation_probability):
        """
        :return: a genetic algorithm to solve the problem
        :param problem: the problem that we will apply the algorithm on it to find the solution
        :param population_size: an integer that represents the size of population
        :param mutation_probability: the probability of mutation in the gens
        :UC: population size must be even and more then 5, mutation probability must be between 0 and 1
        :Example:

        >>> prob = Problem_Interface(13,18,["0","1"],12)
        >>> algo = AlgoGen(prob,20,0.01)
        
        """
        
        assert population_size%2 == 0 and population_size > 5, "the size of population must be even"
        assert 0 <= mutation_probability < 1, "the probability must be positive and less then 1"
        self.problem = problem
        self.pop_size = population_size
        self.mut_proba = mutation_probability

        # setting variable to be used in other functions
        
        self.population = []
        self.generation  = 1

    def creat_pop(self):
        """
        this method will create a set of random individus that forms the population, and then sort it accorrding to the fitness value
        """

        self.population = [self.problem.create_individual() for x in range(self.pop_size)]
        self.population = self.update_pop_value(self.population)

    def update_pop_value(self, pop):
        """
        :param pop: the population 
        this method will sort the population after associating the fitness value to each individu using method from problem class
        """
        return self.problem.sort_population(self.problem.update_fitness(pop))
        # this function will associate the fitness value to each individual of the population

    def selection(self):
        """
        the selection method will take randomly two individual from the population then, keep the on that is more adapted,
        i.e the one who has the highest fitness value or the inverse depending on the problem.
        see the compare_fitness method in the problem class
        """
        pop = [x for x in self.population] # it is better that x is a copy of the individues
        new_half_pop = []
        for x in range(self.pop_size//2):
            p1 = random.choice(pop)
            pop.remove(p1)
            p2 = random.choice(pop)
            pop.remove(p2)

            # select the better individual
            
            if self.problem.compare_fitness(p1,p2) >=0:
                new_half_pop.append(p1)
            else:
                new_half_pop.append(p2)
        return new_half_pop

    def crossover(self):
        """
        this method uses the technique of one point crossover, it takes randomly two individus from the population,
        then divide each one into half and exchange the divided part, then keep the most adapted one.

        NOTE : the crossover methode between two individual is written in the individual class
        """
        pop = [x for x in self.population] # it is better that x is a copy of the individues
        new_half_pop = []
        for x in range(self.pop_size // 2):
            p1 = random.choice(pop)
            pop.remove(p1)
            p2 = random.choice(pop)
            pop.remove(p2)
            n1, n2 = p1.crossover(p2)  # p1 and p2 are individuals

            self.problem.update_fitness([n1,n2]) # update the fitness value of the children

            if self.problem.compare_fitness(n1,n2) >=0:
                new_half_pop.append(n1)
            else:
                new_half_pop.append(n2)
        return new_half_pop

    def mutation(self, pop):
        """
        :param pop: the population of solution to be mutated
        
        this method start by calculation the total number of genes that should be mutated in all the population using the population probability,
        then randomly distributes the number of genes to be muted in each individu, and mutate those genes using method in individu class. 
        """

        for x in pop:
            x.mutate(self.mut_proba)
            self.problem.evaluate_fitness(x)

    def next_generation(self):
        """
        this method will update the population following the algorithm described in the document of the project
        """
        c1 = self.selection()

        c2 = self.crossover()

        next_gen = c1 + c2

        best_five = [x.copy() for x in self.population[0:5]]
        self.mutation(next_gen) # that mutation is changing the population so we should extract the best five before
        next_gen = self.update_pop_value(next_gen)

        self.population = best_five + next_gen[0:-5]
        self.population = self.update_pop_value(self.population)

        self.generation += 1
