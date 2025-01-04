from bitarray import bitarray
from bitarray.util import urandom
import numpy as np

class RecordEncoding:
  def __init__(self, dimension, num_features, num_slices, min_value, max_value ):
    self.num_features = num_features
    self.dimension = dimension
    self.hv_ids = [urandom(dimension)]
    self.hv_features = []
    self.num_slices = num_slices
    self.min_value = min_value
    self.max_value = max_value
    self.delta_feature = (max_value - min_value)/num_slices
    self.feature_intervals = [min_value + self.delta_feature]
    self.hv_bias = None
    self.enconde_func = self.encode_odd

    # Creating Hyper Vector IDS
    for i in range(num_features):
      self.hv_ids.append(urandom(dimension))   
    
    # Creating Hyper Vector Feature Intervals
    current_interval = min_value + self.delta_feature

    # Hyper Vector for min value
    current_hv = urandom(dimension)
    self.hv_features.append(current_hv)

    # Number of bits to be inverted in feature interval
    num_random_bits = int(dimension/num_slices)

    # Iterating each feature slice
    for i in range(1, num_slices):
      # Including integer feature interval
      current_interval += self.delta_feature
      self.feature_intervals.append(current_interval)

      # Including hyper vector feature interval
      current_hv = current_hv.copy()
      random_positions = np.random.choice(dimension, num_random_bits)
      
      for index in random_positions:
        current_hv.invert(index)

      self.hv_features.append(current_hv)

    #Defining fixed Hyper Vector containing -1 values 
    zero_array = np.zeros((dimension,), dtype=int)   
    one_array = np.ones((dimension,), dtype=int)
    self.minus_array = zero_array - one_array

    # Adding extra hyper vector when number of features is even
    # Majority function needs odd number of vectors
    if (not num_features & 1):
      bias = urandom(dimension)
      self.hv_bias = bias.tolist() + self.minus_array + bias.tolist()
      self.enconde_func = self.encode_bias        

  def encode(self, features):
    #print("Encoding: ", self.enconde_func)
    # Call encode_odd or encode_bias
    return self.enconde_func(features)

  def encode_odd(self, features):
    hv_entry = bitarray(self.dimension)

    # Majority Function is used as add operation
    majority_counter = np.zeros((self.dimension,), dtype=int)       

    for i in range(self.num_features):
      hv_feature = self.get_feature_hv(features[i])
      hv_feature ^= self.hv_ids[i]
      hv_one_minus = hv_feature.tolist() + self.minus_array + hv_feature.tolist()
      majority_counter += hv_one_minus
    
    #print(majority_counter)
    
    for i in range(self.dimension):
      hv_entry[i] = 1 if majority_counter[i] > 0 else 0
    
    #print(hv_entry)
    return hv_entry
  
  def encode_bias(self, features):
    hv_entry = bitarray(self.dimension)

    # Majority Function is used as add operation
    majority_counter = self.hv_bias.copy()
    #print(majority_counter)

    for i in range(self.num_features):
      hv_feature = self.get_feature_hv(features[i])
      hv_feature ^= self.hv_ids[i]
      hv_one_minus = hv_feature.tolist() + self.minus_array + hv_feature.tolist()
      majority_counter += hv_one_minus
    
    #print(majority_counter)
    
    for i in range(self.dimension):
      hv_entry[i] = 1 if majority_counter[i] > 0 else 0
    
    #print(hv_entry)
    return hv_entry

  def get_feature_hv(self, value):
    hv = None
    
    for i in range(self.num_slices):
      if (value <= self.feature_intervals[i]):
        #print('Index:', i, "; val:", value, ", interval: ",self.feature_intervals[i])
        hv = self.hv_features[i]
        break
    
    return hv
