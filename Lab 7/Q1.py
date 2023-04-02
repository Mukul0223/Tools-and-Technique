# Write a NumPy program to create a structured array from given student name, height, age and their data types. Now sort by age, then height if age are equal.
import pandas as ps
import numpy  as np
my_dataset = {'cars': ["BMW", "Volvo", "Ford"],'passings': [3, 7, 2]
}
myvar = ps.DataFrame(my_dataset)
print(myvar)
 
# Creating array object
arr = np.array( [[ 1, 2, 3],
                 [ 4, 2, 5]] )
 
# Printing type of arr object
print("Array is of type: ", type(arr))
 
# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)
 
# Printing shape of array
print("Shape of array: ", arr.shape)
 
# Printing size (total number of elements) of array
print("Size of array: ", arr.size)
 
# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)