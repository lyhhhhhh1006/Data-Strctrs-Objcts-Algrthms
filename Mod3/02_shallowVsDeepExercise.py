# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:55:30 2020

@author: jerem
"""

# Shallow vs Deep Copy for Python Objects
## Lets inspect Python Objects to determine whether default assignment is 
## a deep or shallow copy. This is important for memory management and 
## information passing, referential transparency, and resulting side effects

# ints

#%%
a = 1
b = a

print(id(a))
print(id(b))

print(a)
print(b)

a += 1

print(id(a))  # id retrieves the memory address of the variable
print(id(b))

print(a)
print(b)

# Clear environment for upcoming trials
del(a)
del(b)

# Observe: This has the appearence of a shallow copy! (Note this is not exactly
# true but it is functionally true!! See text for details if you so wish)

#%%
import copy

a = 1
b = copy.deepcopy(a)

print(id(a))
print(id(b))

a = 2

print(id(a))
print(id(b))

print(a)
print(b)

# strings

#%%
a = 'a'
b = 'b'

print(id(a))
print(id(b))

print(a)
print(b)

a += '`'

print(id(a))
print(id(b))

print(a)
print(b)

# Clear environment for upcoming trials
del(a)
del(b)



#%%


a = 'a'
b = copy.deepcopy(a)

print(id(a))
print(id(b))

a += '`'

print(id(a))
print(id(b))

print(a)
print(b)



# lists


a = [1,2,3]
b = a

print(id(a))
print(id(b))

print(a)
print(b)

a.append(4)

print(id(a))
print(id(b))

print(a)
print(b)

# Clear environment for upcoming trials
del(a)
del(b)

# Observe: This has the appearence of a shallow copy! (Note this is not exactly
# true but it is functionally true!! See text for details if you so wish)

#%%
import copy

a = [1,2,3]
b = copy.deepcopy(a)

print(id(a))
print(id(b))

a.append(4)

print(id(a))
print(id(b))

print(a)
print(b)




## Try these out at home!!
# tuples



# dictionaries 


