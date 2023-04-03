#!/usr/bin/env python
# coding: utf-8

# In[1]:


class BinHeap:
    def __init__(self, n):
        self.heapList = [0]
        self.currentSize = 0
        self.n = n


    def percUp(self,i):

        while i // self.n > 0:
          if self.heapList[i] < self.heapList[i // self.n]:
             tmp = self.heapList[i // self.n]
             self.heapList[i // self.n] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // self.n

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * self.n) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * self.n + 1 > self.currentSize:
          return i * self.n
      else:
          if self.heapList[i*self.n] < self.heapList[i*self.n+1]:
              return i * self.n
          else:
              return i * self.n + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      i = len(alist) // self.n
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

    def string(self):
        return (self.__toString(0))

    def __toString(self,currentNode = None,i=0):
        if not currentNode:
            currentNode = self.root
        if not self.root:
            return currentstructure 
        
        else:
            currentstructure = [currentNode.key]
            print(i*'-',currentNode.key)
            
            if currentNode.hasAnyChildren():
                left = currentNode.hasLeftChild()     
                right = currentNode.hasRightChild()
                
                if left:
                    currentstructure.append(self.__toString(left,i+1))
                else:
                    currentstructure.append('None')
                    
                if right:
                    currentstructure.append(self.__toString(right,i+1))
                else:
                    currentstructure.append('None')
            return currentstructure


# In[6]:


if __name__ == '__main__':
    bh = BinHeap(3)
    bh.buildHeap([9,5,6,2,3,6,10,7,3,7,35])

    print(bh)
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())


# Discussion for time complexity analysis. One main goal associated with trees is improved time complexity, but how is this related to the branching factor? For example, are 2-ary heaps more or less efficient than 5-ary heaps? Propose an optimal value for n and justify your proposition with an extensive discussion and explanation. 

# The time complexity of operations on a tree inlcuding efficient insertion and deletion, is closely related to the branching factor of the tree. The branching factor determines the maximum number of child nodes that a node can have, and thus affects the depth and width of the tree. A higher branching factor can result in faster insertions and deletions, but slower search times.
# 
# For 2-ary heaps, each node has at most 2 child nodes, and for 5-ary heaps, each node has at most 5 child nodes. A 5-ary heap can store more elements in each level, which results in fewer levels overall and faster insertion and deletion times than a 2-ary heap. However, a 5-ary heap also has a larger memory overhead, as each node needs to store pointers to up to 5 child nodes. 
# 
# However, the choice of branching factor also depends on the specific use case and data being stored. For example, if the data being stored is relatively small, the overhead of storing pointers to 5 child nodes per node may outweigh the benefits of a shallower tree. In this case, a 2-ary heap may be more efficient.
