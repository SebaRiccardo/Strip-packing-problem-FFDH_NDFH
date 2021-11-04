import random
import numpy as np

from rectangle import generate_rectangles,generate_ractangles_fixed
from selection import select_tournament
from crossover import crossover
from mutate import mutate
from population import create_starting_population_FFDH
from fitness import calculate_fitness_FFDH
from utils import generate_stack_of_strips_FFDH, get_best_individual, get_average_fitness
from plotting import plot_result, plot_rectangles

from global_variables import W, POPULATION_SIZE, MAX_GENERATIONS, MUTATION_PROBABILITY, \
    CROSS_OVER_PROBABILITY, FOLDER_FFDH, TOURNAMENT_SIZE, RECTANGLES_NUMBER

def main(number_of_rectangles, genes):
    solutions = []
    best_individuals = []
    best_fitness_acc = []
    average_fitness_acc = []

    # Generate reference rectangle list
    rectangles = generate_rectangles(number_of_rectangles)

    # Start inicial population
    population = create_starting_population_FFDH(POPULATION_SIZE, rectangles, genes)

    # Calculates the best and average for que starting population
    best_initial_individual = get_best_individual(population)
    average_fitness = get_average_fitness(population)
    stack = generate_stack_of_strips_FFDH(best_initial_individual.get_gene_list(), rectangles, W)

    print("-------RECTANGLES----------")
    for rec in rectangles:
        print(rec)

    print("-----------------------------------------------------")
    print("Best Initial individual: ", best_initial_individual.gene_list)
    print("Best Initial Fitness: ", best_initial_individual.fitness)
    print("Initial population Average fitness: ", average_fitness)
    print("Solution: ", stack)
    print("-----------------------------------------------------")
    plot_rectangles(rectangles, stack, best_initial_individual.gene_list,best_initial_individual.fitness, "initial", W, FOLDER_FFDH)

    for generation_number in range(MAX_GENERATIONS):
        
        # SELECTION
        selected = select_tournament(population, TOURNAMENT_SIZE)

        # CROSSOVER
        crossed_offspring = []

        for ind1, ind2 in zip(selected[::2], selected[1::2]):
            #random.seed(1)
            if random.random() < CROSS_OVER_PROBABILITY:
                children = crossover(ind1.gene_list, ind2.gene_list, rectangles, calculate_fitness_FFDH)
                crossed_offspring.append(children[0])
                crossed_offspring.append(children[1])
            else:
                crossed_offspring.append(ind1)
                crossed_offspring.append(ind2)
        # MUTATION
        mutated = []
        for ind in crossed_offspring:
            #random.seed(1)
            if random.random() < MUTATION_PROBABILITY:
                mutated.append(mutate(ind.gene_list, rectangles, number_of_rectangles, calculate_fitness_FFDH))
            else:
                mutated.append(ind)

        population = mutated

        # Best individual for the current generation
        best_one = get_best_individual(population)
        best_individuals.append(best_one.gene_list)
        best_fitness_acc.append(best_one.fitness)


        #averagen fitness
        average_fitness = get_average_fitness(population)
        average_fitness_acc.append(average_fitness)


        # Add a new configuration to the solutions list ej: [[2,1][5,3][4]]
        solution = generate_stack_of_strips_FFDH(best_one.gene_list, rectangles, W)
        solutions.append(solution)
        solution = []

    plot_result(average_fitness_acc, MAX_GENERATIONS, FOLDER_FFDH, "Average fitness")
    plot_result(best_fitness_acc, MAX_GENERATIONS, FOLDER_FFDH, "Best fitness")

    for j in range(MAX_GENERATIONS):
        print(" -- ")
        print("Generation: ", j)
        print("Best individual: ", best_individuals[j])
        print("Solution: ",solutions[j])
        print("Fitness: ",best_fitness_acc[j])

    #Print and save the plots
    #if MAX_GENERATIONS <= 1000:
    for c in range(MAX_GENERATIONS):
        plot_rectangles(rectangles, solutions[c], best_individuals[c],best_fitness_acc[c], c , W, FOLDER_FFDH)


if __name__ == '__main__':
 #    rectangles =generate_ractangles_fixed(15,[(37,11),(26,68),(25,75),(24,17),(20,73),(30,28),(12,35),(25,47),(15,21),(48,26),(11,41),(32,10),(12,15),(20,36),(41,24)])
      #rectangles = generate_rectangles(15)
      #genes = [3, 1, 11, 0, 8, 10, 6, 7, 9, 5, 4, 14, 13, 12, 2]

     #fitness =calculate_fitness_FFDH(genes,rectangles,100)
     #stack =generate_stack_of_strips_FFDH(genes,rectangles,100)
     #plot_rectangles(rectangles, stack,genes, fitness, 0, 100, FOLDER_FFDH)
     #print(fitness)
     #print(stack)
     #Generation: 0
     #Best individual: [3, 1, 11, 0, 8, 10, 6, 7, 9, 5, 4, 14, 13, 12, 2]
     #Solution: [[3, 1, 11, 0, 8], [4, 6, 7, 10], [9, 5], [14, 13], [12, 2]]
     #Fitness: 212
     main(RECTANGLES_NUMBER, np.arange(RECTANGLES_NUMBER))
