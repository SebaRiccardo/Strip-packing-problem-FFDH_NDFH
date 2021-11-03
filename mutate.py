
from individual import Individual
import numpy as np

def mutate(ind, rectangles, rectangles_number,fitness_fuction):
    genes = ind.get_gene_list()
    indexA = 0
    indexB = 0
    # controlla que los index no sean iguales
    while indexA == indexB:
        indexA = np.random.randint(0, rectangles_number)
        indexB = np.random.randint(0, rectangles_number)
    # hace swap de los genes segun los index A y B
    geneA = genes[indexA]
    genes[indexA] = genes[indexB]
    genes[indexB] = geneA
    return Individual(genes, rectangles,fitness_fuction)