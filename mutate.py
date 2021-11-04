
from individual import Individual
from global_variables import SEED
import numpy as np


def mutate(ind, rectangles, rectangles_number, fitness_function):
    #np.random.seed(SEED)
    genes = ind.get_gene_list()
    indexA = 0
    indexB = 0
    # checks if the indexes are the same
    while indexA == indexB:
        indexA = np.random.randint(0, rectangles_number)
        indexB = np.random.randint(0, rectangles_number)
    # swap values at indexA and indexB A y B
    geneA = genes[indexA]
    genes[indexA] = genes[indexB]
    genes[indexB] = geneA
    return Individual(genes, rectangles, fitness_function)
