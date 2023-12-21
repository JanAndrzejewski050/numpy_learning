import numpy as np


# a_mul = np.array([[[1, 2, 3, 1],
#                    [4, 5, 6, 1],
#                    [7, 8, 9, 1]],
#                   [[1, 1, 1, 1],
#                    [1, 1, 1, 1],
#                    [1, 1, 1, 1]]])
#
# print(a_mul.shape)
# print(a_mul.ndim)
# print(a_mul.size)
# print(a_mul.dtype)


# a = np.array([[1, 2, 3],        # If There is even 1 string, every element becomes a string
#               [4, "5", 6],  # But if we have integers only, type will be "numpy.int32"
#               [7, 8, 9]], dtype=np.int32)   # if the string is a number, we can change it into an int
#
# print(a.dtype)
# print(a[0][0])
# print(a[0][0].dtype)


# a = np.full((3,3,3,3), 7)
# print(a)
#
# a = np.zeros((3,3,2))
# print(a)
#
# a = np.ones((2,3,4))
# print(a)
#
# a = np.empty((4,2,3))   # Allocates the space in the memory
# print(a)


# x_values = np.arange(0, 1000, 5)
# print(x_values)
#
# x_values = np.linspace(0, 1000, 11)  # evenly spread 11 values between 0-1000
# print(x_values)

# print(np.nan)
# print(np.inf)
# print(np.isnan(np.sqrt(-1)))    # if something is missing
# print(np.isinf(np.array(10)/0)) # in case e.g. dividing by 0


# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,0]
#
# a1 = np.array(l1)
# a2 = np.array(l2)
#
# print(l1*5)     # Python lists repeat the list 5 times
# print(a1*5)     # Numpy arrays multiply every element of the array by 5
#
# print(l1+l2)    # Python lists combine 2 lists in one
# print(a1+a2)    # Numpy lists adds up like vectors (a1[i] + a2[i])
# print(a1*a2)    # same with every other operation


# a1 = np.array([1,2,3])
# a2 = np.array([[1],
#                [2]])
#
# print(a1+a2)    # [[2 3 4],[3 4 5]]


# a = np.array([[1,2,3],
#              [4,5,6]])
#
# print(np.sqrt(a))   #it gives us a sqrt for each element of the array
# print(np.sin(a))    #same
# print(np.log(a))    #same


# -------ARRAY FUNCTIONS------

# a = np.array([1,2,3])
#
# print(np.append(a, [7,8,9]))    # adding [7,8,9] temporarily
# print(a)    # a does not have [7,8,9] here
#
# a = np.append(a, [7,8,9])       # now the array a is changed
# a = np.insert(a, 3, [4,5,6])    # insert some elements inside the array
#
# print(a)

# a = np.array([[1,2,3],
#              [4,5,6]])
#
# #a = np.delete(a, 1)     # its gonna delete 2, not [4,5,6]
# #a = np.delete(a, 1, 0)  # delete the second row - 0 tells about rows
# a = np.delete(a, 1, 1)   # delete second column - 1 tells about columns
#
# print(a)


# -----------STRUCTURING METHODS------------------

# a = np.array([[1,2,3,4,5],
#               [6,7,8,9,10],
#               [11,12,13,14,15],
#               [16,17,18,19,20]])

# print(a.shape)
# print(a.reshape((5,4)))     # change the shape if is compatible with starting array
# print(a.reshape((10,2)))
# print(a.reshape((20,1)))    # every element is a 1-element array
# print(a.reshape((20,)))     # 20 elements in 1 common array
# print(a.reshape((2,2,5)))   # we can add dimensions
#
# a = a.reshape((2,5,2))      # u have to assign to change an array
# a.resize((10,2))            # with resize u don't have to assign

# print(a.flatten())            # gives 1 dimensional array. Returns a copy of an array
# print(a.ravel())              # works the same, but gives only a look on a flatten array, doesn't return anything
#
# var = [v for v in a.flat]
# print(var)

# print(a.transpose())    # change columns with rows
# print(a.T)              #same
#
# print(a.swapaxes(1, 1))     # is better for multidimensional arrays


# a1 = np.array([[1,2,3,4,5],
#               [6,7,8,9,10]])
#
# a2 = np.array([[11,12,13,14,15],
#               [16,17,18,19,20]])
#
# # a = np.concatenate((a1, a2), axis=0)    #axis=0 - adding rows, axis=1 - adding colums
# # print(a)
#
# # a = np.stack((a1,a2))       # adds a new dimension to the whole array
# # print(a)
#
#
# #numbers = np.random.randint(0, 100, (3,3,5))        # fast creating random arrays with given size
# numbers = np.random.binomial(10, p=0.5, size=(5,10))
# print(numbers)


# --------EXPORTING AND IMPORTING NUMPY ARRAYS-------------------

#np.save("my_array.npy", a)     # saving
a = np.load("my_array.npy")     # loading
print(a)
