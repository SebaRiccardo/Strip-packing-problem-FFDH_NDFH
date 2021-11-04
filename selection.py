import random
from global_variables import SEED

def select_tournament(population, tournament_size):
    new_offspring = []
    for _ in range(len(population)):
        #random.seed(_)
        candidates = [random.choice(population) for _ in range(tournament_size)]
        new_offspring.append(min(candidates, key=lambda ind: ind.fitness))
    return new_offspring