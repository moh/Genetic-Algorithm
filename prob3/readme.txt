In that problem, we should try to find a path in a labyrinth of the size N**2, in our case N = 7 (the example given a size equal to 7)

To test the problem type : python main.py filename pop_size nbgeneration proba

Where : 
1 - filename : the file where the labyrinth is.
2 - pop_size : the size of population used by Algo gen
3 - nbgeneration : the number of generation used by Algo gen
4 - proba : the mutation probability used by algo gen

Exemple:
> python main.py maze/maze2.txt 200 150 0.05

sometime the algorithm is not able to find the best path to travers the labyrinth.