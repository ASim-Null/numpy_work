# import numpy library

import numpy as np

# Create a numpy array

a = np.array([20, 1, 2, 3, 4])
print(a)

#change the first element 

a[0] = 100
a

# Assign the 5th element to 0

a[4] = 0
a

# Slicing the numpy array

d = c[1:4]
d

# Set the fourth element and fifth element to 300 and 400

c[3:5] = 300, 400
c

#Assign value using a list 

#list
select = [0, 2, 3]

# Use List to select elements , example will be non functional

d = c[select]
d

# Get the size of numpy array

a.size

# Get the number of dimensions of numpy array

a.ndim

# Get the shape/size of numpy array

a.shape

# Get the mean of numpy array

mean = a.mean()
mean

# Get the standard deviation of numpy array

standard_deviation=a.std()
standard_deviation


# Get the biggest value in the numpy array

max_b = b.max()
max_b

# Get the smallest value in the numpy array

min_b = b.min()
min_b




