
from global_variables import W

class Individual:

    def __init__(self, gene_list, rectangles, fitness_fuction):
        self.gene_list = gene_list
        self.fitness = fitness_fuction(self.gene_list, rectangles, W)

    def __str__(self):
        return "Gnome:" + str(self.gene_list) + " fitness:" + str(self.fitness)

    def get_gene_list(self):
        return self.gene_list