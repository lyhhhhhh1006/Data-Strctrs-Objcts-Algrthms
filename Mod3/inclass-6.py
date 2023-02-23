#!/usr/bin/env python
# coding: utf-8

# Implement a recursive function allCharsPerm(  listOfChars ) the generates all unique permutations of the chars in  listOfChars. You can assume listOfChars contains unique chars (no repeated characters in the list).
# 
# Derive a recurrence that is a worst-case, step count function T(n) for allCharsPerm, where n is the length of listOfChars.
# 
# Describe the cases (Best, Worst, Average)
# 
# Solve the recurrence and state the time complexity using Big-O notation.

# In[1]:


def allCharsPerm(listOfChars):
# generate all unique permutations of the chars in listOfChars
    if len(listOfChars) <= 1:
        return listOfChars
    
    else:   
        permutation = []
        for perm in listOfChars:
            permu = allCharsPerm("".join(listOfChars).replace(perm,""))
            for ele in permu:
                permutation.append(perm + ele)
        return permutation


# In[2]:


## for testing
allCharsPerm(["a"])


# In[3]:


allCharsPerm(['a','b','c','d'])


# In[5]:


#line 3: 2
#line 4: 1
#line 7: 1
#line 8: 2n
#line 9: n-1
#line 10: 2(n-1)
#line 11: (n-1)*n
#line 12: 1

#Depends on the size of n
# T(n) = n^2 + 4n + 2
# T(1) = 2 BEST CASE
# O(n) = n^2


# In[ ]:





# In[ ]:




