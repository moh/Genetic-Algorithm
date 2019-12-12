In that problem, we should find the best set of directions to be able to traverse a set of haunted field of number N.

To test that problem : 
>python main.py N pop_size nbgeneration proba size monster
where:
1 - N : the number of field to try to traverse
2 - pop_size : the size of population used in algo gen
3 - nbgeneration : the number of generation to be tested
4 - proba : mutation probability
5 - size : the size of the haunted field
6 - monster : number of monsters in the terrain

Example : 
> python main.py 5 150 80 0.05 16 4

Sometime the algorithm doesn't find an individual that can travers the field with success