import matplotlib.pyplot as plt
import csv
import numpy as np

reader = csv.reader(open("C:/Users/Sara/Desktop/Term 7/هوش محاسباتی/Homeworks/hw2/hw2/Dataset/Dataset2.csv"))
data = [raw for raw in reader]

def plot(a, b):
    #Todo: Plot data points with the best vector for dimension reduction
    for i in range(1, len(data)):
        plt.scatter(float(data[i][0]), float(data[i][1]), c='black', marker='x', s=15)
    z = [None] * (len(data) - 1)
    for i in range(1, len(data)):
        z[i - 1] = a * float(data[i][0]) + b * float(data[i][1])
        plt.scatter(z[i-1]*a, z[i-1]*b, s=20, facecolors='none', edgecolors='b')
        #xi=( float(data[i][0]) + (b/a)*float(data[i][1]) ) / (1 + ((b*b)/(a*a)))
        #yi=(b/a)*xi
        #plt.scatter(xi, yi, s=20, facecolors='none', edgecolors='b')

    x = np.linspace(-10,60)
    y = (b/a)*x
    plt.plot(x,y, 'r')
    plt.show()
