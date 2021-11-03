import random
import csv
import statistics

reader = csv.reader(open("C:/Users/Sara/Desktop/Term 7/هوش محاسباتی/Homeworks/hw2/hw2/Dataset/Dataset2.csv"))
data = [raw for raw in reader]

class Chromosome:
    def __init__(self, chromosome_length, min, max):
        # Todo: create a random list for genes between min and max below
        self.gene = [None] * chromosome_length
        i : int
        for i in range(chromosome_length-1):
            self.gene[i] = random.uniform(min, max)     #gene[0]=a gene[1]=b
        self.gene[chromosome_length-1] = random.uniform(-1.5, 1.5)
        self.score = 0

    def evaluate(self):
        # Todo: Update Score Field Here
        z = [None]*(len(data)-1)
        for i in range(1, len(data)):
            z[i-1] = self.gene[0]*float(data[i][0]) + self.gene[1]*float(data[i][1])
        self.score = statistics.stdev(z)

"""
c1 = Chromosome(3,0,5)
c1.evaluate()
print(c1.score)
print(c1.gene[0])
print(c1.gene[1])

print(" ")

c2 = Chromosome(3,0,5)
c2.evaluate()
print(c2.score)
print(c2.gene[0])
print(c2.gene[1])

print(" ")

list_of_chromosomes = [None]*2
list_of_chromosomes[0] = copy.deepcopy(c1)
list_of_chromosomes[1] = copy.deepcopy(c2)
c1.gene[0] = c1.gene[0] + 5

print(list_of_chromosomes[0].gene[0])
"""
