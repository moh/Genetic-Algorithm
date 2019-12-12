import random
from math import floor
import string
from maze import Maze


class Problem_Interface():
    def __init__(self,filename,gene_set):

        self.genes = gene_set
        self.maze = Maze(filename)
        self.gene_l = self.maze.get_size()
        

    def create_individual(self):
        """
        Creat an individu using the Individual_Interface class
        :return: an individu from Individual_Interface class
        """
        return Individual_Interface(self.gene_l,self.genes)

    def evaluate_fitness(self, individu):
        """
        This method calculates the fitness score of the individu
        :param individu: an object from Individual_Interface class
        :type individu: Individual_Interface
        """
        nb_steps, distance = self.maze.try_path(individu.get_value()[0])
        f = 0

        if distance == 0:
            f += 1000
        
        # taille = self.maze.get_size()** 0.5
        # f += max(0,floor(taille/2) - distance)**2 + nb_steps
        
        f += nb_steps - distance
        individu.set_score(f)
        return f

    def compare_fitness(self,n1,n2):
        """
        This method will compare the fitness and return 1 if n1 is more adopted then n2, and the inverse.
        :param n1: the first individual
        :type n1: Individual_Interface
        :param n2: the second individual
        :type n2: Individual_Interface

        :return : an integer that depend on wich is the most adopted individu
        """
        # in that problem fitness should decrease
        if n1.get_score() > n2.get_score():
            return 1
        elif n1.get_score() == n2.get_score():
            return 0
        else:
            return -1

    def update_fitness(self,population):
        """
        this method will calculate the fitness of each individual of the population,
        and return a list of tuple that contain the individual and its score
        :param population: a list of individuals that represent the population
        :type population: list
        :return: a list of tuple
        """
        # this function is to update the fitness of each member in the population
        ind_value = []
        for x in population:
            s = self.evaluate_fitness(x)
            ind_value.append((x,s))
        return ind_value

    def sort_population(self,population_v):
        """
        this method will sort the population based on the fitness score
        
        :param population_v : a list of tuple containing individual and its score
        :type population_v : List

        :return: a List of sorted individual 
        """
        l =  sorted(population_v, key=lambda couple: couple[1])  # this function is to sort using the fitness value
        return [x[0] for x in l][::-1]

    def get_step_dist(self, individu):
        """
        This method will return the number of steps and manhattan distance of the individual
        :param individu: the individual that we want to get those details
        :type individu: Problem_Interface
        """
        return self.maze.try_path(individu.get_value()[0])
        
    
class Individual_Interface():
    def __init__(self,gene_l,gene_s,rand = True):
        """
        This init method of the class Individual_Interface will initialize an object, individual, of this class
        :param gene_l: a integer that represent the number of genes of the individual
        :type gene_l: int
        :param gene_s: the set of genes used to form the individual
        :type gene_s: list
        :param rand: a boolean variable that determine if individual is random or not
        :type rand: bool

        :return: None
        """
        # fonction est commune pour tt les probleme
        if rand:
            self.__genome = ''.join([random.choice(gene_s) for x in range(gene_l)])
            self.__value = self.get_value()
        else:
            self.__genome = "" # waiting to be set by the program
            self.__value = ("","")
        
        self.__score = 0
        self.__size = gene_l
        self.gene_s = gene_s

    def copy(self):
        """
        The method copy the individual with all its properties
        :return: Idividual_Interface
        """
        x = Individual_Interface(self.__size,self.gene_s,False)
        x.set_value(self.__genome)
        x.set_score(self.get_score())
        return x

    def get_value(self):
        """
        this method will return a tuple of the genome and its value
        :return: tuple
        """
        # cette fonction varie dans tt les probleme
        return (self.__genome,self.__genome)

    def set_score(self,value):
        """
        :param value: the new value of the score, fitness value
        :type vaue: int
        """
        self.__score = value
        

    def get_score(self):
        """
        this method will return the fitness value of the individual
        :return: int
        """
        return self.__score

    def set_value(self,value):
        """
        :param value: the new value of the genome of the Individual
        :type vaue: str
        """
        self.__genome = value

    def crossover(self,other):
        """
        this method will do the one point crossover between two individuals.
        :param other: the other individual to perform the crossover with
        :type other: Individual_Interface
        
        :return : a tuple containing the results of the crossover
        """
        n = self.__size // 2
        ps1 = self.__genome[0:n]
        ps2 = self.__genome[n:]
        po1 = other.__genome[0:n]
        po2 = other.__genome[n:]

        f1 = Individual_Interface(self.__size,self.gene_s)
        f1.set_value(ps1+po2)

        f2 = Individual_Interface(self.__size,self.gene_s)
        f2.set_value(po1+ps2)
        
        return (f1,f2)

    def mutate(self,proba):
        """
        this method will mutate the individual with a probability equal to proba
        :param proba: the mutation probability
        :type proba: float
        """
        g = [ x for x in self.__genome]

        for x in range(self.__size):
            r = random.random()
            if r <= proba:
                # mutate
                s = [y for y in self.gene_s]
                s.remove(g[x])
                g[x] = random.choice(s)
        
        self.__genome = ''.join(g)
