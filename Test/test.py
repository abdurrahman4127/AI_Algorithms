import numpy as np

ages = np.array([20, 25, 30, 20, 22, 25, 20, 20, 30, 30])
# most_common_age = np.bincount(ages)
most_common_age = np.bincount(ages).argmax()    
print(most_common_age)