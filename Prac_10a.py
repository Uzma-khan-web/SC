#Aim: Implementation of Simple Genetic Algorithm
import random

POPULATION_SIZE = 250

GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890,
.;:_!"#%&/()=?@${[]}'''

TARGET = "HELLO"


class Individual(object):

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @staticmethod
    def mutated_genes():
        global GENES
        gene = random.choice(GENES)
        return gene

    @classmethod
    def create_gnome(cls):
        global TARGET
        gnome_len = len(TARGET)
        return [cls.mutated_genes() for _ in range(gnome_len)]

    def cal_fitness(self):
        global TARGET
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET):
            if gs != gt:
                fitness += 1
        return fitness

    def crossover(self, par2):
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            prob = random.random()

            if prob < 0.50:
                child_chromosome.append(gp1)
            elif prob < 0.90:
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(self.mutated_genes())

        return Individual(child_chromosome)


def selection(population):
    population = sorted(population, key=lambda x: x.fitness)
    return population


def main():
    global POPULATION_SIZE

    generation = 1
    found = False
    population = []

    for _ in range(POPULATION_SIZE):
        gnome = Individual.create_gnome()
        population.append(Individual(gnome))

    while not found:

        population = selection(population)

        if population[0].fitness == 0:
            found = True
            break

        new_generation = []

        # Elitism — Keep top 10%
        s = int((10 * POPULATION_SIZE) / 100)
        new_generation.extend(population[:s])

        # Remaining 90% — new children
        s = int((90 * POPULATION_SIZE) / 100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])

            child = parent1.crossover(parent2)
            new_generation.append(child)

        population = new_generation

        print("Generation:", generation,
              "\tString:", "".join(population[0].chromosome),
              "\tFitness:", population[0].fitness)

        generation += 1

    print("\nFinal Output:")
    print("Generation:", generation,
          "\tString:", "".join(population[0].chromosome),
          "\tFitness:", population[0].fitness)


if __name__ == "__main__":
    main()
