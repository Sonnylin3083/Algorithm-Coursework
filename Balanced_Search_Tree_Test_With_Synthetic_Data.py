# DO NOT MODIFY THIS CELL

from abc import ABC, abstractmethod  

# abstract class to represent a set and its insert/search operations
class AbstractSet(ABC):
    
    # constructor
    @abstractmethod
    def __init__(self):
        pass           
        
    # inserts "element" in the set
    # returns "True" after successful insertion, "False" if the element is already in the set
    # element : str
    # inserted : bool
    @abstractmethod
    def insertElement(self, element):     
        inserted = False
        return inserted   
    
    # checks whether "element" is in the set
    # returns "True" if it is, "False" otherwise
    # element : str
    # found : bool
    @abstractmethod
    def searchElement(self, element):
        found = False
        return found    
    
    
    
# abstract class to represent a synthetic data generator
class AbstractTestDataGenerator(ABC):
    
    # constructor
    @abstractmethod
    def __init__(self):
        pass           
        
    # creates and returns a list of length "size" of strings
    # size : int
    # data : list<str>
    @abstractmethod
    def generateData(self, size):     
        data = [""]*size
        return data

class TreeNode_BalancedSearchTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.top = None
        self.color = "red"

class BalancedSearchTreeSet(AbstractSet):
    
    def __init__(self):
        self.root = None       
     
    
        
    def insertElement(self, element):
        inserted = False
        if self.root is None:
            self.root = TreeNode_BalancedSearchTree(element)
            inserted = True
            return inserted
        else:
            currentNode = self.root
            while True:
                if currentNode.value == element:
                    return inserted
                elif currentNode.value > element:
                    if currentNode.left is None:
                        currentNode.left = TreeNode_BalancedSearchTree(element)
                        currentNode.left.top = currentNode
                        inserted = True
                        break
                    else:
                        currentNode = currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right = TreeNode_BalancedSearchTree(element)
                        currentNode.right.top = currentNode
                        inserted = True
                        break
                    else:
                        currentNode = currentNode.right
            while True:
                if (currentNode.left is None or currentNode.left.color == "black") and currentNode.right is not None and currentNode.right.color == "red":
                    # left rotation
                    tampNode= currentNode.right
                    if tampNode.left is not None:
                        currentNode.right = tampNode.left
                        tampNode.left.top = currentNode
                    else:
                        currentNode.right = None
                    if currentNode.top is not None:
                        topNode = currentNode.top
                        if topNode.left == currentNode:
                            topNode.left = tampNode
                        else:
                            topNode.right = tampNode
                    elif currentNode == self.root:
                        self.root = tampNode
                    tampNode.left = currentNode
                    tampNode.top = currentNode.top
                    currentNode.top = tampNode
                    tampNode.color = currentNode.color
                    currentNode.color = "red"
                if currentNode.left is not None and currentNode.left.color == "red" and currentNode.right is not None and currentNode.right.color == "red":
                    # shift color
                    currentNode.left.color = "black"
                    currentNode.right.color = "black"
                    currentNode.color = "red"
                if currentNode.top is None:
                    break
                if currentNode.color == "red" and currentNode.left is not None and currentNode.left.color == "red":
                    # right rotation
                    rightNode = currentNode.top
                    if rightNode.top is not None:
                        topNode = rightNode.top
                        if topNode.left == rightNode:
                            topNode.left = currentNode
                        else:
                            topNode.right = currentNode
                    if rightNode == self.root:
                        self.root = currentNode
                    rightNode.left = currentNode.right
                    if currentNode.right is not None:
                        currentNode.right.top = rightNode
                    currentNode.right = rightNode
                    currentNode.top = rightNode.top
                    rightNode.top = currentNode
                    continue
                currentNode = currentNode.top
            return inserted


    def searchElement(self, element):     
        found = False
        currentNode = self.root
        while currentNode is not None:
            if currentNode.value == element:
                found = True
                return found
            elif currentNode.value > element:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return found 

import string
import random

class TestDataGenerator(AbstractTestDataGenerator):
    
    def __init__(self):
        # ADD YOUR CODE HERE
        pass           
        
    def generateData(self, size):     
        # ADD YOUR CODE HERE
        data = []
        # loop size times
        for i in range(size):
            # generate a random string of random length between 1 and 10
            rand_len_str = random.randint(1, 10)
            rand_str = ''.join(random.choices(string.ascii_letters, k = rand_len_str))
            # add the string to the set
            data.append(rand_str)        
        return data

import timeit

# ADD YOUR TEST CODE HERE TO WORK ON SYNTHETIC DATA

# Create an object of class TestDataGenerator and use the object to generateData
SyntheticTest = TestDataGenerator()
num_data = 10
data = SyntheticTest.generateData(num_data)

bal = BalancedSearchTreeSet()
bal_insert_time_data = []
bal_search_time_data = []
bal_space_data = []
for iteration in range(len(data)):
    bal_insert_start_time = timeit.default_timer()
    bal.insertElement(data[iteration])
    bal_insert_end_time = timeit.default_timer()
    bal_insert_time = bal_insert_end_time - bal_insert_start_time
    bal_insert_time_data.append(bal_insert_time)
    bal_space = bal.__sizeof__()
    bal_space_data.append(bal_space)
    bal_tot_search_time = 0
    for id in range(iteration + 1):
        value = data[id]
        bal_search_start_time = timeit.default_timer()
        bal.searchElement(value)
        bal_search_end_time = timeit.default_timer()
        bal_tot_search_time += (bal_search_end_time - bal_search_start_time)
    bal_av_search_time = bal_tot_search_time / (iteration + 1)
    bal_search_time_data.append(bal_av_search_time)

for num_data_have in range(num_data):
    print(f"When there are {num_data_have + 1} elements")
    print(f"Balanced Search Tree insert time: {bal_insert_time_data[num_data_have]:.6f} seconds")
    print(f"Balanced Search Tree search time: {bal_search_time_data[num_data_have]:.6f} seconds")
    print(f"Balanced Search Tree space: {bal_space_data[num_data_have]} bytes")