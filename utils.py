
import numpy as np

#Calculates the maximun height in a strip
def max_height(elements,rectangles):
    heigts = []
    for i in elements:
        heigts.append(rectangles[i].height)
    return max(heigts)

#fitness best and average
def get_best_individual(population):
    return min(population, key = lambda ind: ind.fitness)

def get_average_fitness(population):
    return sum([i.fitness for i in population]) / len(population)


def strip_width(elements,rectangles,W):
    total =0
    for e in elements:
        total = total+ rectangles[e].width
    return W-total


def generate_stack_of_strips_FFDH(gene_list, rectangles,max_strip_width):
    stack_of_strips = []
    list_of_heights = []
    spaces_left = []

    for i in gene_list:  # ej:[2,4,5,1,9,6,8,3,0,7]
        # itera casa strip en el stack al princiop pasa de largo
        for s in stack_of_strips:  # ej: [[2,3,9],[5,1,4],[9,8,0,7]]
            # indice que indica a que strip pertenece el valor de space left
            indexOfStrip = stack_of_strips.index(s)
            # calcula cuando espacio disponible queda por aca uno de los strips
            space_left_in_the_strip = strip_width(s, rectangles,max_strip_width)
            # si el arreglo spaces_left tiene tantos elementos como el index lo marca entonces
            # se guarda el valor en la posicion de index, en caso contrario quiere decir que debo crar un espacio nuevo con el append sino tira error index out of bounds
            if len(spaces_left) > indexOfStrip:
                spaces_left[indexOfStrip] = space_left_in_the_strip
            else:
                spaces_left.append(space_left_in_the_strip)

        # se fija si existen espacios vacios, en caso de no existir es porque no se agrego ningun rectangulo en ningun strip. inicio
        if len(spaces_left) != 0:
            index = 0
            added = False
            # itera la lista de spaces_left para checkear si el rectangle[i] entra en algun
            # strip con espacio estante en el la posicion index
            while not added and index < len(spaces_left):
                # si el largo del rectangulo[i] (por ejemplor rectangulo[i], con i = 3 ,serian el rectangulo numero 3)
                # es menor al espacio disponible en el strip en posicion index
                if rectangles[i].width <= spaces_left[index]:
                    # lo mete en la lista de strips en el indice donde se encontro el lugar donde cabia
                    stack_of_strips[index].append(i)
                    list_of_heights[index].append(rectangles[i].height)
                    added = True
                else:
                    # pasa el siquiente elemento de la lista de espacios restantes
                    index += 1
            # si sale del while es porque no se encontro un strop al donde meter el rectangulo,
            # entonces se tiene que agregar un strip nuevo
            if not added:
                stack_of_strips.append([i])
                list_of_heights.append([rectangles[i].height])
        else:
            stack_of_strips.append([i])
            list_of_heights.append([rectangles[i].height])

    return stack_of_strips


def generate_stack_of_strips_NFDH(gene_list, rectangles,max_strip_width):
    list_of_strips =[]
    strip = []
    sum_of_widths = 0;

    for i in gene_list:

        # la regla dice que el ancho de los rectangulos no pueden ser masyor a  W
        if max_strip_width <= (sum_of_widths + rectangles[i].width):
            aux = strip
            # ya complete un strip porque si agrego el proximo supera el W =100
            list_of_strips.append(aux)
            strip =[]
            # Agrego la altura del rectangulo en el proximo strip
            strip.append(i)
            # sumo el ancho del nuevo rectangulo en el strip nuevo
            sum_of_widths = rectangles[i].width
        else:
            sum_of_widths = sum_of_widths + rectangles[i].width
            strip.append(i)

    # Lista de strips donde en cada strip estan los triangulos.
    list_of_strips.append(strip)

    return list_of_strips