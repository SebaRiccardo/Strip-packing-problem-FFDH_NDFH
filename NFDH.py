import random
import numpy as np

from rectangle import generate_rectangles
from selection import select_tournament
from crossover import crossover
from mutate import mutate
from population import create_starting_population_NFDH
from fitness import calculate_fitness_NFDH
from utils import generate_stack_of_strips_NFDH, get_best_individual, get_average_fitness
from plotting import plot_result, plot_rectangles

from global_variables import W, POPULATION_SIZE, MAX_GENERATIONS, MUTATION_PROBABILITY, \
    CROSS_OVER_PROBABILITY, FOLDER_NFDH, TOURNAMENT_SIZE,RECTANGLES_NUMBER


def main(number_of_rectangles, genes):
    solutions = []
    best_individuals = []
    best_fitness_acc = []
    average_fitness_acc = []

    # Generate reference rectangle list
    rectangles = generate_rectangles(number_of_rectangles)

    # Start inicial population
    population = create_starting_population_NFDH(POPULATION_SIZE, rectangles, genes)

    # Calculates the best and average for que starting population
    best_initial_individual = get_best_individual(population)
    average_fitness = get_average_fitness(population)
    stack = generate_stack_of_strips_NFDH(best_initial_individual.get_gene_list(), rectangles, W)

    print("-------RECTANGLES----------")
    for rec in rectangles:
        print(rec)

    print("-----------------------------------------------------")
    print("Best Initial individual: ", best_initial_individual.gene_list)
    print("Best Initial Fitness: ", best_initial_individual.fitness)
    print("Initial population Average fitness: ", average_fitness)
    print("Solution: ", stack)
    print("-----------------------------------------------------")
    plot_rectangles(rectangles, stack, best_initial_individual.gene_list, best_initial_individual.fitness, "initial", W,
                    FOLDER_NFDH)

    for generation_number in range(MAX_GENERATIONS):

        # SELECTION
        selected = select_tournament(population, TOURNAMENT_SIZE)

        # CROSSOVER
        crossed_offspring = []

        for ind1, ind2 in zip(selected[::2], selected[1::2]):
            # random.seed(1)
            if random.random() < CROSS_OVER_PROBABILITY:
                children = crossover(ind1, ind2, rectangles, calculate_fitness_NFDH)
                crossed_offspring.append(children[0])
                crossed_offspring.append(children[1])
            else:
                crossed_offspring.append(ind1)
                crossed_offspring.append(ind2)
        # MUTATION
        mutated = []
        for ind in crossed_offspring:
            # random.seed(1)
            if random.random() < MUTATION_PROBABILITY:
                mutated.append(mutate(ind, rectangles, number_of_rectangles, calculate_fitness_NFDH))
            else:
                mutated.append(ind)

        population = mutated

        # Best individual for the current generation
        best_one = get_best_individual(population)
        best_individuals.append(best_one.gene_list)
        best_fitness_acc.append(best_one.fitness)

        # averagen fitness
        average_fitness = get_average_fitness(population)
        average_fitness_acc.append(average_fitness)

        # Add a new configuration to the solutions list ej: [[2,1][5,3][4]]
        solution = generate_stack_of_strips_NFDH(best_one.gene_list, rectangles, W)
        solutions.append(solution)
        solution = []

    # plot_result(average_fitness_acc,MAX_GENERATIONS, FOLDER_FFDH, "Average fitness")
    # plot_result(best_fitness_acc, MAX_GENERATIONS, FOLDER_FFDH, "Best fitness")

    for j in range(MAX_GENERATIONS):
        print(" -- ")
        print("Generation: ", j)
        print("Best individual: ", best_individuals[j])
        print("Solution: ", solutions[j])
        print("Fitness: ", best_fitness_acc[j])

    # Print and save the plots
    if MAX_GENERATIONS <= 1000:
        for c in range(MAX_GENERATIONS):
            plot_rectangles(rectangles, solutions[c], best_individuals[c], best_fitness_acc[c], c, W, FOLDER_NFDH)

if __name__ == '__main__':
    main(RECTANGLES_NUMBER, np.arange(RECTANGLES_NUMBER))
