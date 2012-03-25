import numpy
import Pycluster

points = [
        [1, 2, 3],
        [2, 2, 3],
        [4, 5, 6],
        [5, 5, 6],
        [9, 9, 9],
        [9, 9, 9]
        ]

num_clusters = min(len(points), 3)

labels, error, nfound = Pycluster.kcluster(points, num_clusters)
print labels  # Cluster number for each point
print error   # The within-cluster sum of distances for the solution
print nfound  # Number of times this solution was found

totals = []
for i in range(num_clusters):
    totals.append( [[0, 0, 0], 0] )

for i in range(len(labels)):
    tmp = totals[labels[i]]
    tmp[0][0] += points[i][0]
    tmp[0][1] += points[i][1]
    tmp[0][2] += points[i][2]
    tmp[1] += 1

averages = [ [ 1.0 * a[0]/n, 1.0 * a[1]/n, 1.0 * a[2]/n] for a,n in totals]

print averages
