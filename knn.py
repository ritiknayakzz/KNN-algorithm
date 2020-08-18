import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')
import math
from statistics import mode

dataset = {'point1' : [[1,4], [2,3], [3,6]], 'point2' : [[6,8], [7,9], [9,8]]}
predict = [2,5]

for i in dataset:
    for j in dataset[i]:
        if i == 'point1':
            plt.scatter(j[0], j[1], color = 'red')
        else:
            plt.scatter(j[0], j[1], color = 'blue')
plt.scatter(predict[0], predict[1], color = 'green')

plt.show()
    

def knn(predict, data, k=3):
    l = []
    l1 = []

    for i in data:
        for j in data[i]:
            euclidean_dist = math.sqrt((j[0] - predict[0])**2 + (j[1] - predict[1])**2)
            l.append((euclidean_dist, i))

    l = sorted(l)
    for i in l:
        l1.append(i[1])
    knn_sorted = l1[:k]
    result = mode(knn_sorted)
    print(result)

knn(predict = predict, data = dataset)
