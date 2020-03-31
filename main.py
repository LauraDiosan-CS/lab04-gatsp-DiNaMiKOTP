import random
POPULATION_SIZE = 8
NUMB_OF_ELITE_CHROMOSOMES =1
TOURNAMENT_SELECTION_SIZE = 4
MUTATION_RATE = 1
TARGET_CHROMOSOME = [1,3,2,7,4,8,6,5]

class Chromosome:
    def __init__(self):
        self._genes = []
        self._fitness = 0
        self.__initGenes()

    def __initGenes(self):
        i = 0
        while i< TARGET_CHROMOSOME.__len__():
            x= random.randrange(1,TARGET_CHROMOSOME.__len__()+1)
            if x not in self._genes:
                self._genes.append(x)
            else:
                while x in self._genes:
                    x=random.randrange(1, TARGET_CHROMOSOME.__len__()+1)
                self._genes.append(x)
            i+=1
    def getGenes(self):
        return self._genes

    def getFitness(self):
        self._fitness=0
        for i in range( self._genes.__len__()):
            if self._genes[i] == TARGET_CHROMOSOME[i]:
                self._fitness+=1
        return self._fitness

    def __str__(self):
        return self._genes.__str__()
class Population:
    def __init__(self,size):
        self._chromosomes = []
        self.__initChromosomes(size)
    def __initChromosomes(self,size):
        i=0
        while i<size:
            self._chromosomes.append(Chromosome())
            i+=1
    def getChromosomes(self):
        return self._chromosomes

class GeneticAlgorithm:
    @staticmethod
    def evolve(pop):
        return GeneticAlgorithm._mutate_population(GeneticAlgorithm._crossover_population(pop))

    @staticmethod
    def _crossover_population(pop):
        crossover_pop = Population(0)

        for i in range(NUMB_OF_ELITE_CHROMOSOMES):
            crossover_pop.getChromosomes().append(pop.getChromosomes()[i])
        i = NUMB_OF_ELITE_CHROMOSOMES
        while i<POPULATION_SIZE:
            chromosome1 = GeneticAlgorithm._select_tournament_population(pop).getChromosomes()[0]
            chromosome2 = GeneticAlgorithm._select_tournament_population(pop).getChromosomes()[0]
            crossover_pop.getChromosomes().append(GeneticAlgorithm._crossover_chromosomes(chromosome1,chromosome1))
            i+=1
        return crossover_pop

    @staticmethod
    def _mutate_population(pop):
        for i in range(NUMB_OF_ELITE_CHROMOSOMES,POPULATION_SIZE):
            GeneticAlgorithm._mutate_chromosome(pop.getChromosomes()[i])

        return pop

    @staticmethod
    def _crossover_chromosomes(chromosome1,chromosome2):
        crossover_chrom = Chromosome()
        for i in range(TARGET_CHROMOSOME.__len__()):
            if random.random()>=0.5:
                crossover_chrom.getGenes()[i] = chromosome1.getGenes()[i]
            else:
                crossover_chrom.getGenes()[i] = chromosome2.getGenes()[i]
        return crossover_chrom

    @staticmethod

    def _mutate_chromosome(chromosome):

        for i in range(TARGET_CHROMOSOME.__len__()-1):
            if random.random()<MUTATION_RATE:
                if random.random()<0.5:
                    x= random.randrange(1,TARGET_CHROMOSOME.__len__()+1)
                    if x in chromosome.getGenes():
                        swapPositions(chromosome.getGenes(), i, chromosome.getGenes().index(x))

    @staticmethod

    def _select_tournament_population(pop):
        tournament_pop = Population(0)
        i = 0
        while i< TOURNAMENT_SELECTION_SIZE:
            tournament_pop.getChromosomes().append(pop.getChromosomes()[random.randrange(0,POPULATION_SIZE)])
            i+=1
        tournament_pop.getChromosomes().sort(key = lambda x: x.getFitness(), reverse=True)
        return tournament_pop


def _print_population(pop,gen_number):
    print("\n--------------------------------------------------------")
    print("Generation #", gen_number, "|Fittest chromosome fitness:",pop.getChromosomes()[0].getFitness())
    print("Target Chromosome:",TARGET_CHROMOSOME)
    print("--------------------------------------------------------")
    i = 0
    for x in pop.getChromosomes():
        print("Chromosome #",i," :",x,"|Fitness: ",x.getFitness())
        i+=1


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def run():
    population = Population(POPULATION_SIZE)

    population.getChromosomes().sort(key=lambda x: x.getFitness(),reverse=True)

    _print_population(population,0)

    generation_number = 1

    while population.getChromosomes()[0].getFitness()<TARGET_CHROMOSOME.__len__():
        population = GeneticAlgorithm.evolve(population)
        population.getChromosomes().sort(key=lambda x: x.getFitness(), reverse=True)
        _print_population(population, generation_number)
        generation_number += 1


def readFile(array,file):
    file = open(file,'r')
    n = int(file.readline())
    line = file.readline()
    lineValues = line.split(',')

    for value in lineValues:
        array.append(int(value))

    return n

def main():
    file = "medium_01_tsp.txt"
    array = []
    global POPULATION_SIZE,TARGET_CHROMOSOME
    POPULATION_SIZE = readFile(array,file)
    TARGET_CHROMOSOME = array
    run()





main()
