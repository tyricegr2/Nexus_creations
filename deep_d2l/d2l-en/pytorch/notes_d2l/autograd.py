# Autograd: Automatic differentiation
#   - Works backwards through a computational graph through applying the chain rule 
#       - Backpropagation: Computing gradients
# In general - avoid allocating new memory every time we take a derivative
# since deep learning requires computing derivatives thousands or millions of times
# risking us to run out of memory

import torch

x = torch.arange(5.0)
# print(x)

# x is true if gradients need to be computed for the tensor
x.requires_grad_(True)
print(x.grad) # Default value is none

print(x)
 
# Below multiplies the matrix x and x together, then adds them up
#y = torch.dot(x, x)
y_2 = 2 * torch.dot(x,x)
#print(y)
print(y_2)

#y.backward()
y_2.backward()

print(x.grad)

x.grad.zero_()
y_2 = x.sum()
y_2.backward()
print(x.grad)

# Backward for Non-scalar variables
# - Sum up the gradients of each component of y with respect to a full vector x,
#   yielding a vector of the same as x if we are dealing with jacobian
#
x.grad.zero_()
y_1 = x * x
# y_1.backward(gradient=torch.ones(len(y_1)))
# If we don't want to compute a gradient we detach from the recorded computational graph
u = y_1.detach()
z = u * x

z.sum().backward()
print(x.grad)
print(u)
