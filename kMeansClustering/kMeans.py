import numpy as np
import matplotlib.pyplot as plt

class KMeansClustering:
    def __init__(self, k):
        self.k = k
        
    # drawing the initial scatter plot
    def draw_initial_clusters(self):
        self.X = np.loadtxt("kMeansClustering/jain_feats.txt")              # initial points
        self.centroid_old = np.loadtxt("kMeansClustering/jain_centers.txt") # initial centroids
         
        plt.scatter(self.X[:, 0], self.X[:, 1], c='blue', label='X')
        plt.scatter(self.centroid_old[:, 0], self.centroid_old[:, 1], marker="*", c='red', label='centroid_old', s=200)
        plt.legend()
        plt.show()
        
        
    # ploting points to the clusters
    def update_centroids(self):
        self.centroid_new = np.zeros_like(self.centroid_old)  # for updated centroids

        for e in range(1000):
            label = np.zeros(len(self.X), dtype=int)
            
            for i in range(len(self.X)):
                dist = np.zeros(len(self.centroid_old))
                for j in range(len(self.centroid_old)):
                    dist[j] = np.linalg.norm(self.X[i,:] - self.centroid_old[j,:])  # euclidean distance
                label[i] = np.argmin(dist)
    
            # mean of those val(s) assigned to the new centroid
            for j in range(len(self.centroid_new)):
                self.centroid_new[j,:] = np.mean(self.X[label==j,:], axis=0) 
    
            # terminating condition 
            if np.max(np.abs(self.centroid_new - self.centroid_old)) < 1E-7:
                break
            else:
                self.centroid_old = self.centroid_new.copy()
        
        return label, self.centroid_new
    
    
    # drawing the final scatter plot 
    def draw_final_cluster(self):
        label, centroid_new = self.update_centroids()
        colors = ['green', 'red']
        plt.scatter(self.X[:, 0], self.X[:, 1], c=[colors[i] for i in label])
        plt.scatter(centroid_new[:, 0], centroid_new[:, 1], marker='*', s=200, c=colors)
        plt.show()


# starting the execution
def main():
    kMeans = KMeansClustering(k=2)
    kMeans.draw_initial_clusters()
    kMeans.draw_final_cluster()
    
main()