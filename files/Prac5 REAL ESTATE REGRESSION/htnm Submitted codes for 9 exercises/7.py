import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class DataPreprocessing():
    def __init__(self):
        # Auto initialize necessary attributes of the object
        self.dataframe = None
        self.X = None
        self.y = None
        
    def read_from_csv(self):
        # Read data from .csv file into the dataframe and display the first 5 rows
        df = pd.read_csv('real_estate.csv', index_col='No')
        self.dataframe = df
        #print(df.head)
        #print(df.iloc[0][1])

    def set_attributes_and_output(self):
        # Set X and y to data attributes and output from the dataframe
        
        ##################
        # YOUR CODE HERE #
        ##################

        #print(self.dataframe)
        self.X = self.dataframe.values[:, :-1]
        self.y = self.dataframe.values[:, -1]
        
    def final_train_test_data(self, attributes_list=[0,1,2,3,4,5], test_size=0.2):
        # Split the data X and output y into training data and testing data
        # Output: a tuple (X_train, X_test, y_train, y_test), 
        # using train_test_split with random_state=42
        return \
                 train_test_split(
                     self.X[:, attributes_list], 
                     self.y, 
                     random_state = 42, 
                     test_size = test_size)