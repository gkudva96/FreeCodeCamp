# Importing Libraries
import numpy as np

# Function definition to return the statistics
def calculate(list):

  # Check to see if the list had 9 elements
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  
  # Converting list to numpy array
  array = np.array(list).reshape(3, 3)

  # Obtaining the means
  mean_final = []
  mean_final.append(np.mean(array, axis = 0).tolist())
  mean_final.append(np.mean(array, axis = 1).tolist())
  mean_final.append(np.mean(array.flatten('F')))

  # Obtaining the variances
  var_final = []
  var_final.append(np.var(array, axis = 0).tolist())
  var_final.append(np.var(array, axis = 1).tolist())
  var_final.append(np.var(array.flatten('F')))

  # Obtaining the standard deviations
  std_final = []
  std_final.append(np.std(array, axis = 0).tolist())
  std_final.append(np.std(array, axis = 1).tolist())
  std_final.append(np.std(array.flatten('F')))

  # Obtaining the maximum values
  max_final = []
  max_final.append(np.max(array, axis = 0).tolist())
  max_final.append(np.max(array, axis = 1).tolist())
  max_final.append(np.max(array.flatten('F')))

  # Obtaining the minimum values
  min_final = []
  min_final.append(np.min(array, axis = 0).tolist())
  min_final.append(np.min(array, axis = 1).tolist())
  min_final.append(np.min(array.flatten('F')))

  # Obtaining the sums
  sum_final = []
  sum_final.append(np.sum(array, axis = 0).tolist())
  sum_final.append(np.sum(array, axis = 1).tolist())
  sum_final.append(np.sum(array.flatten('F')))

  # Creating the final dictionary to be returned
  calculations = {'mean' : mean_final, 'variance' : var_final, 'standard deviation' : std_final, \
  'max' : max_final, 'min' : min_final, 'sum' : sum_final}

  return calculations