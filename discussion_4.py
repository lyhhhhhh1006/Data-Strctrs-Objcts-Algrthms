#!/usr/bin/env python
# coding: utf-8

# In[15]:


class SparseMatrix:
# create sparse matrix that only add non-zero elements

    def __init__(self, rows, cols):
    # initiate some attributes
        self.row = rows #number of rows
        self.col = cols #number of cols
        self.data = {} #store data
    
    def setitem(self, rows, cols, data):
        
        if rows > self.row or cols > self.col:
            raise ValueError("Wrong entry")
        
        elif data == 0:
            if (rows, cols) in self.data:
                del self.data[(rows, cols)]
        else:
            self.data[(rows,cols)] = data 

    def get_item(self, idx):
    # return value at the given index

        i,j = idx
        if i in self.data and j in self.data[i]:
            return self.data[(i,j)]
        else:
            return 0
    
    def __add__(self, other):
    # add non-zero items and store the result

        if self.row != other.row or self.col != other.col:

            raise ValueError("Matrices have different dimensions.")

            fin_result = SparseMatrix(self.row, self.col)
        
        else:
            for i in range(self.row):
                for j in range(self.col):
                    if (i,j) in self.data and (i,j) in other.data:
                        self.data[(i,j)] += other.data[(i,j)]
            
            fin_result = SparseMatrix(self.row, self.col)
            fin_result.data = self.data
            return fin_result


# In[21]:


if __name__ == "__main__":
    matrix_or = SparseMatrix(5,6)
    matrix_or.setitem(0,0,6)
    matrix_or.setitem(3,5,6)
    matrix_or.setitem(2,6,3)
    matrix_or.setitem(3,5,3)
    matrix_oth = SparseMatrix(5,6)
    matsum = matrix_or + matrix_oth
    print(matsum)


# #Assuming that two SparseMatrices (A and B) are compatible for addition, and both are m x n, derive a Step Count Function T(n) and Space Count Function S(n). You can assume the number of non-zero entries in A is a and the number of non-zero entries in B is b.
# #Do this for both the best case and the worst case. Explain your counts line-by-line. Remember, the cases are determined by the value of the input and not the size of the input. 

# ### step count function T(n)
# #best case: for both for loops in terms of rows and columns, we would only have non-zero items and iterate over those non-zero items
# #best T(n) = O(a+b)
# 
# #worst case: for both matrix, we have to iterate over each non-zero items
# #worst T(n) = O(ab)

# ### Space count function S(n)
# #best case: for both matrix, we have to store data for each non-zero items, each value needs space
# #best S(n) = O(a+b)
# 
# #worst case: for both matrix, we have to store data for each non-zero items, each value needs space
# #worst S(n) = O(a+b)
