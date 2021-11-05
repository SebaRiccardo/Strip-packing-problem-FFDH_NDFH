
# genes lo uso solo como parametro para determinar la longitud
# de los arreglos que hacen de lista de genes, en caso de aumentar la cantidad de rectangulos
# se debe aumentar el arrelgo, el orden es indistinto solo es necesario que tenga la longitud adecuada
# ej: num de rectangulos = 3 [1,2,3]  o [3,2,1] o [3,1,2]. Cualquiera sirve ya que despues np.permutation() permuta
# y crea las distintas variantes de los genes

RECTANGLES_NUMBER = 15

FOLDER_FFDH = "FFDH"
FOLDER_NFDH = "NFDH"
SEED = 100
TOURNAMENT_SIZE = 50
POPULATION_SIZE = 50
MAX_GENERATIONS = 100
MUTATION_PROBABILITY = .1
CROSS_OVER_PROBABILITY = .65
W = 100
