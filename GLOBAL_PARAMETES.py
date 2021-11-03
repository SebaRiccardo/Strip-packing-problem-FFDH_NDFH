
# genes lo uso solo como parametro para determinar la longitud
# de los arreglos que hacen de lista de genes, en caso de aumentar la cantidad de rectangulos
# se debe aumentar el arrelgo, el orden es indistinto solo es necesario que tenga la longitud adecuada
# ej: num de rectangulos = 3 [1,2,3]  o [3,2,1] o [3,1,2]. Cualquiera sirve ya que despues np.permutation() permuta
# y crea las distintas variantes de los genes

# 10 rectangulos
genes =[0,1,2,3,4,5,6,7,8,9]
RECTANGLES_NUMBER =10

# 20 rectangulos

#genes20= [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19]
#RECTANGLES_NUMBER =20
FOLDER_FFDH = "FFDH_PLOTS"
FOLDER_NFDH = "NFDH_PLOTS"

TOURNAMENT_SIZE = 10
POPULATION_SIZE =50
MAX_GENERATIONS =10
MUTATION_PROBABILITY= .1
CROSS_OVER_PROBABILITY = .65
W=100