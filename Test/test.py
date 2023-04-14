# import numpy as np

# ages = np.array([20, 25, 30, 20, 22, 25, 20, 20, 30, 30])
# # most_common_age = np.bincount(ages)
# most_common_age = np.bincount(ages).argmax()    

# print(most_common_age)
# print(np.argsort(ages))


# -*- coding: utf-8 -*-
"""K_means_clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ay_hcR-KQlUcqLW4ix7IGRQg8Ndqlaea
"""

import numpy as np
import matplotlib.pyplot as plt
import random



class KmeansClustering:

    def __init__(self, num_clusters):
        self.k = num_clusters

    def read_data(self, file_name):
        self.data_sets = np.genfromtxt(file_name, delimiter=',')

    def initial_centers(self):
        
        initial_center = random.sample(self.data_sets.tolist(), self.k)
        return np.array(initial_center)

    def plot_initial_data(self, cluster_centers):
  
        x = self.data_sets[:, 0]
        y = self.data_sets[:, 1]


        plt.scatter(x, y,s=0.8, marker='.', label='initial data',color='k')

        cx = cluster_centers[:, 0]
        cy = cluster_centers[:, 1]

        plt.scatter(cx, cy, color='g', marker='*', label='Initial center points')

        plt.legend()

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Initial Data Sets')
        plt.show()

    def decide_cluster(self, point, cluster_centers):
       

        distance = cluster_centers - point
        squared = distance ** 2
        arr = squared.sum(axis=1)
        return arr.argmin()

    def cluster_formation(self, cluster_centers):

        full_cluster = {}
        for point in self.data_sets.tolist():
            key = self.decide_cluster(point, cluster_centers)
            full_cluster.setdefault(key, []).append(point)

        return full_cluster

    def new_center(self, full_cluster):
        
        lst = []
        for key in full_cluster:
            cluster_points = np.array(full_cluster[key])
            avg = cluster_points.mean(axis=0)
            lst.append(avg)

        return np.array(lst)

    def switch_counts(self, prevcluster, newcluster):
      

        count = 0
        for key in prevcluster:
            my_members = prevcluster[key]
            newcluster_members = newcluster[key]
            for point in my_members:
                if point not in newcluster_members:
                    count += 1

        return count

    def kmeans_algo(self):
        
        data = self.initial_centers()
        self.plot_initial_data(data)
        old_cluster = self.cluster_formation(data)

        l = True
        while l:
            new_center = self.new_center(old_cluster)
            #print("C: ", new_center)
            new_cluster = self.cluster_formation(new_center)
            if self.switch_counts(old_cluster, new_cluster) < 5:
                l = False
            old_cluster = new_cluster
        return old_cluster

    def plot_final_cluster(self, clusters):

        for key in clusters:
            # print(key)
            data = np.array(clusters[key])
            x = data[:, 0].tolist()
            y = data[:, 1].tolist()
            plt.scatter(x, y, marker='.')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Final Data Sets')
        plt.show()





k=6
obj = KmeansClustering(k)
obj.read_data("/content/data.csv")  # will read the data from the file and store in a 2D numpy array (for example, datapoints)
final_cluster = obj.kmeans_algo()  # calling the main kmeans clustering algorithm for cluster formation
#print("final: ",final_cluster)
#obj.plot_final_cluster(final_cluster)  # will scatter plot all the clusters with corresponding centers