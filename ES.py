import Chromosome
import random
import numpy as np
import math
import copy
import Plot

Mu = 10
# Todo: change Mu's coefficient below to attain the best result
Lambda = 7*Mu
crossover_probability = 0.4
mutation_probability = 1
T = 0.05
Q = 4

def Best_evaluation(list):
    best = copy.deepcopy(list[0])
    for i in range(1, len(list)):
        if best.score < list[i].score:
            best = copy.deepcopy(list[i])
    return best

def Worst_evaluation(list):
    worst = copy.deepcopy(list[0])
    for i in range(1, len(list)):
        if worst.score > list[i].score:
            worst = copy.deepcopy(list[i])
    return worst

def Average_evaluation(list):
    avg = 0
    for i in range(0, len(list)):
        avg = avg + list[i].score
    avg = avg/len(list)
    return avg

def generate_initial_population():
    list_of_chromosomes : Chromosome
    list_of_chromosomes = [None]*Mu
    for i in range(Mu):
        list_of_chromosomes[i] = Chromosome.Chromosome(3,0,1)  #min=0 max=1 [a,b,sigma]
    return list_of_chromosomes

def generate_new_seed(list_of_chromosomes):
    #Todo: return lambda selected parents
    list_of_parents: Chromosome
    list_of_parents = [None] * Lambda
    for i in range(Lambda):
        rand = random.randrange(0, Mu)
        list_of_parents[i] = copy.deepcopy(list_of_chromosomes[rand])
    return list_of_parents

def crossover(chromosome1, chromosome2):
    child1 = Chromosome.Chromosome(3,0,1)
    child2 = Chromosome.Chromosome(3,0,1)
    rand = random.uniform(0, 1)
    if rand < crossover_probability:  #do cross over
        alpha = random.uniform(0, 1)
        for i in range(3):
            child1.gene[i] = alpha*chromosome1.gene[i] + (1 - alpha)*chromosome2.gene[i]
            child2.gene[i] = (1 - alpha)*chromosome1.gene[i] + alpha*chromosome2.gene[i]
        return child1, child2
    else:
        return None

def mutation(chromosome):
    #Todo: Use Gaussian Noise here!/param chromosome/return mutated chromosome
    rand = random.uniform(0, 1)
    if rand < mutation_probability:  # do mutation
        noise = np.random.normal(0, 1, None)
        chromosome.gene[2] = chromosome.gene[2] * math.exp(-1 * T * noise)
        for i in range(2):
            noise2 = np.random.normal(0, 1, None)
            chromosome.gene[i] = chromosome.gene[i] + chromosome.gene[2]*noise2
    return chromosome

def evaluate_new_generation(list_of_chromosomes):
    #Todo: Call evaluate method for each new chromosome / return: list of chromosomes with evaluated scores
    for i in range(len(list_of_chromosomes)):
        normalizer = copy.deepcopy(math.sqrt(pow(list_of_chromosomes[i].gene[0] , 2) + pow(list_of_chromosomes[i].gene[1], 2)))
        list_of_chromosomes[i].gene[0] = list_of_chromosomes[i].gene[0]/normalizer
        list_of_chromosomes[i].gene[1] = list_of_chromosomes[i].gene[1]/normalizer
        list_of_chromosomes[i].evaluate()
    """
    list_of_chromosomes.extend(list_of_children)
    evaluate_chromosomes = [None] * len(list_of_chromosomes)

    for i in range(len(list_of_chromosomes)):
        evaluate_chromosomes[i] = list_of_chromosomes[i].evaluate()

    #return evaluate_chromosomes
    """

def choose_new_generation(list_of_chromosomes):
    #Todo: Q-tournament is suggested! / return: Mu selected chromosomes for next cycle
    list_of_survivors = [None] * Mu
    Q_chromosomes = [None] * Q
    for i in range(Mu):
        for j in range(Q):
            Q_chromosomes[j] = copy.deepcopy(list_of_chromosomes[random.randrange(0,len(list_of_chromosomes))])
        list_of_survivors[i] = Best_evaluation(Q_chromosomes)
    return list_of_survivors

if __name__ == '__main__':
    #Todo -- Use Methods In a proper arrangement
    a : float
    b : float
    list_of_chromosomes = generate_initial_population()

    for k in range(200):
        list_of_parents = generate_new_seed(list_of_chromosomes)
        Mutated_chromosomes = [None]*Lambda

        for i in range(Lambda):
            Mutated_chromosomes[i] = mutation(list_of_parents[i])

        list_of_children = []
        for i in range(0, Lambda, 2):
            childs = crossover(Mutated_chromosomes[i],Mutated_chromosomes[i+1])
            if childs != None:
                list_of_children.append(childs[0])
                list_of_children.append(childs[1])

        list_of_chromosomes.extend(list_of_children)
        evaluate_new_generation(list_of_chromosomes)
        list_of_survivors = choose_new_generation(list_of_chromosomes)

        best = Best_evaluation(list_of_survivors)
        a = best.gene[0]
        b = best.gene[1]
        print("Best score = ", best.score)
        worst = Worst_evaluation(list_of_survivors)
        print("Worst score = ", worst.score)
        avg = Average_evaluation(list_of_survivors)
        print("Average score = ", avg)

        print(" ")

        list_of_chromosomes = copy.deepcopy(list_of_survivors)

    Plot.plot(a, b)
