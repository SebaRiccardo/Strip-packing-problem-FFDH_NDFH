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
    CROSS_OVER_PROBABILITY, FOLDER_NFDH, TOURNAMENT_SIZE


def main(number_of_rectangles, genes):
    solutions = []
    best_ones = []
    best_fitness_acc = []
    average_fitness_acc = []

    # Generate reference rectangle list
    rectangles = generate_rectangles(number_of_rectangles)

    # Start inicial population
    population = create_starting_population_NFDH(POPULATION_SIZE, rectangles, genes)

    # Calculates the best and average for que starting population
    best_initial_individual = get_best_individual(population)
    average_fitness = get_average_fitness(population)

    print("-----------------------------------------------------")
    print("Best Initial individual: ", best_initial_individual)
    print("Initial population Average fitness: ", average_fitness)
    print("-----------------------------------------------------")

    stack = generate_stack_of_strips_NFDH(best_initial_individual.get_gene_list(), rectangles, W)

    plot_rectangles(rectangles, stack, best_initial_individual, "initial", W, FOLDER_NFDH)

    for generation_number in range(MAX_GENERATIONS):

        # SELECTION
        selected = select_tournament(population, TOURNAMENT_SIZE)

        # CROSSOVER
        crossed_offspring = []

        for ind1, ind2 in zip(selected[::2], selected[1::2]):
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
            if random.random() < MUTATION_PROBABILITY:
                mutated.append(mutate(ind, rectangles, number_of_rectangles, calculate_fitness_NFDH))
            else:
                mutated.append(ind)

        population = mutated

        # Best individual for the current generation
        best_one = get_best_individual(population)
        average_fitness = get_average_fitness(population)

        # Add a new configuration to the solutions list ej: [[2,1][5,3][4]]
        solution = generate_stack_of_strips_NFDH(best_one.get_gene_list(), rectangles, W)
        solutions.append(solution)

        # best solution in the whole generation
        best_ones.append(best_one)
        average_fitness_acc.append(average_fitness)
        best_fitness_acc.append(best_one.fitness)
        
        print("Generation: ", (generation_number + 1))
        print("Best individual: ", best_one.get_gene_list())
        print("Fitness: ", best_one.fitness)
        print("Solution: ", solution)

    plot_result(average_fitness_acc, MAX_GENERATIONS, FOLDER_NFDH, "Average_fit")
    plot_result(best_fitness_acc, MAX_GENERATIONS, FOLDER_NFDH, "Best_fit")

    if MAX_GENERATIONS <= 1000:

        i = 0
        for stack in solutions:
            plot_rectangles(rectangles, stack, best_ones[i], i+1, W, FOLDER_NFDH)
            i += 1


if __name__ == '__main__':
    main(10, np.arange(10))
