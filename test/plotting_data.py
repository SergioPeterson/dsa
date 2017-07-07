import sys
sys.path.append('..')
import tkinter
import matplotlib.pyplot as plt
import numpy

from random import randint
from cluster.dbscan.Point import Point
from cluster.dbscan.DBScan import DBScan

def plotting_data():
    points = []
    for i in range(0, 500):
        p = randint(0, 1000)
        q = randint(0, 1000)
        point = Point(p, q)
        points.append(point)
    
    dbscan = DBScan(points, 169, 50)
    colors = ['blue', 'red', 'green', 'yellow', 'black', 'purple']
    for point in dbscan.get_clusters():
        for p in point:
            m, n  = p.get_values()
            plt.scatter(m, n, c=colors[p.get_cluster() - 1])
    plt.show()

if __name__ == "__main__":
    plotting_data()
