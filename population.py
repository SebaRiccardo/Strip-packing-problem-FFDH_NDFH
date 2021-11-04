import random
import numpy as np

from individual import Individual
from fitness import calculate_fitness_FFDH,calculate_fitness_NFDH

def create_random_individual(chromosome_length, rectangles,fitness_fuction, seed):
    # solo usarlo cuando se quiere hacer debug
    #np.random.seed(seed)
    gene_list = np.random.permutation(chromosome_length) #chromosome_length es un arreglo ej: [0,1,2,3,4,5,6,7,8,9] donde hace las permutaciones
    # a list of rectangles are passed down to each Individual to calculate its fitness
    return Individual(list(gene_list), rectangles, fitness_fuction)

def create_starting_population_NFDH(population_size, rectangles, genes):
    return np.array([create_random_individual(genes, rectangles, calculate_fitness_NFDH, _) for _ in range(population_size)])

def create_starting_population_FFDH(population_size, rectangles, genes):
    return np.array([create_random_individual(genes, rectangles, calculate_fitness_FFDH, _) for _ in range(population_size)])



