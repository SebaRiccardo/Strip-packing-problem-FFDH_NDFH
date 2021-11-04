
from individual import Individual
from global_variables import SEED
import numpy as np


def mutate(genes, rectangles, rectangles_number, fitness_function):
    #np.random.seed(SEED)
    indexA = 0
    indexB = 0
    newGenes = []
    # checks if the indexes are the same
    while indexA == indexB:
        indexA = np.random.randint(0, rectangles_number)
        indexB = np.random.randint(0, rectangles_number)

    # swap values at indexA and indexB A y B
    newGenes = np.copy(genes)
    geneA = newGenes[indexA]
    newGenes[indexA] = newGenes[indexB]
    newGenes[indexB] = geneA

    newIndividual = Individual(newGenes, rectangles, fitness_function)
    return newIndividual
