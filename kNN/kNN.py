import numpy as np

class kNN:
    def __init__(self, k):
        self.k = k

    # skipping 1st line of dataset (as it contains header)
    def read_dataset(self, file_path):
        data = np.genfromtxt(file_path, delimiter=",", skip_header=1)
        self.X = data[: , :4]              # 1st 4 cols (might be float)
        self.y = data[: , 5].astype(int)   # output col = 0 or 1 (integer)
        
        
    # shuffling the dataset (mapping with index)
    def shuffle_dataset(self):
        all_indices = np.random.permutation(len(self.X))  # generate random num (0 to lenght of dataset) 
        self.X = self.X[all_indices]
        self.y = self.y[all_indices]
        
            
    # splitting the dataset into 80% - 20% 
    def split_dataset(self, ratio=0.8):
        split_size = int(len(self.X) * (ratio))
        self.X_train = self.X[:split_size]   # first 80% of X
        self.X_test = self.X[split_size:]    # remaining 20% of X
        self.y_train = self.y[:split_size]   # first 80% of y
        self.y_test = self.y[split_size:]    # remaining 20% of y


    # the kNN algorithm
    def predict_dataset(self, X_test, k=5):
        y_test_predicted = np.zeros(len(X_test), dtype=int)
        
        for i in range(len(X_test)):
            x_test = X_test[i]
            eucleadian_dist = np.sqrt(np.sum((self.X_train - x_test) ** 2, axis=1)) 
            min_dist_indices = np.argsort(eucleadian_dist)[:k]         # indices of k nearest neighbors
            y_neighbor = self.y_train[min_dist_indices]                # output (y) of k nearest neighbors
            y_test_predicted[i] = np.bincount(y_neighbor).argmax()     # most occurance
        
        return y_test_predicted
    
    
    # measuring the accuracy of the dataset
    def get_result(self):
        y_test_predicted = self.predict_dataset(self.X_test)
        accurate_prediction = 0
        
        for i in range(len(y_test_predicted)):
            if y_test_predicted[i] == self.y_test[i]:    
                accurate_prediction += 1     # accurate if test & test-prediction match
        
        accuracy = accurate_prediction / len(y_test_predicted)
        print(f"accuracy: {accuracy*100:.2f}%")



# starting the exeucution
def main():
    knn = kNN(k = 5)
    knn.read_dataset("kNN/iris.csv")
    knn.shuffle_dataset()
    knn.split_dataset(ratio=0.8)
    knn.get_result()
    
    # make a prediction for a new input data point
    new_input_data = np.array([5.1, 3.8, 1.6, 0.2])
    new_predicted_output = knn.predict_dataset(new_input_data.reshape(1,-1), k=5)

    print(f"new input dataset: {new_input_data}")
    print(f"new predicted output: {new_predicted_output[0]}")
    
main()