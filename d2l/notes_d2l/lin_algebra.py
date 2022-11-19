import torch

# Scalars
x = torch.tensor(5.0)
y = torch.tensor(2.0)

print(x * y)
print(x / y)
print(x + y)

# Vectors
    # Fixed-length arrays of scalars
    # Values hold real world signficance for real world datasets
    # Example 1: Training a model to predict the risk of a loan defaulting
    #   - Each applicant is a vector with components corresponding to quantities like income, length of employment,
    #     number of previous defaults
    # Example 2: Heart attacka risk
    #   - Vector represents patient and its components correspond to vital signs, cholesterol lvls, mins of exercise
    #
a = torch.arange(5)

print(a[2])

# Indicates that a vector contains n elements
print(len(a))

# Accessing length via shape attribute - 
print(a.shape)

# 0th order tensors - Scalar
# 1st order tensor - vector
# 2nd order tensor - matrices

A = torch.arange(6).reshape(3,2)
print(A)
# Transpose of A: SO transpose of m x n matrax is an n x m matrix
print(A.T)

# Tensors are important for images as 3rd order tensors
#   - Axes correspond to height, width, channel
# Collection of images is represented by 4th order tensors

print(torch.arange(24).reshape(2,3,4))

C = torch.arange(6, dtype=torch.float32).reshape(2,3)
D = C.clone() # Assigning a copy of C to D by allocating new memory
print(C)
#print(C * D)

b = 2
X = torch.arange(24).reshape(2,3,4)
#print(b * X)

sum_ex = torch.arange(5, dtype=torch.float32)
#print(sum_ex.sum())

print(C.shape)
print(C.sum())

# Sum(Axis = 0) sums the elements along the rows
# sum(Axis = 1) sums the elements of all the columns
print(C.sum(axis=1))

# Below is true
print(C.sum(axis=[0,1]) == C.sum())

# Below is the mean or average calculated by dividing the sum by total number of elements

print(C.mean())

print(C.sum() / C.numel())

print(C.mean(axis=0))
print(C.mean(axis=1))

sum_C = C.sum(axis=1, keepdims= True)
print(sum_C)

print(C.cumsum(axis=0))

y = torch.ones(3, dtype = torch.float32)

print(x.shape)
