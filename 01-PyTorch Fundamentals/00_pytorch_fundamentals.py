# -*- coding: utf-8 -*-
"""00_pytorch_fundamentals.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-2DJJnE4KIIqNXE8rhxRaS12iiexYMMN
"""

!nvidia-smi

import torch
print(torch.__version__)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""## Introduction to tensors
### creating tensors
pytorch tensors are created using torch.tensor()
"""

# scalar
scalar = torch.tensor(7)
scalar

scalar.ndim

# get tensor back as python int
scalar.item()

# vector
vector = torch.tensor([7, 7])
vector

vector.ndim

vector.shape

# Matrix
MATRIX = torch.tensor([[7, 8],
                       [9, 10]])
MATRIX

MATRIX.ndim

MATRIX[1]

MATRIX.shape

# Tensor
TENSOR = torch.tensor([[[1, 2, 3],
                        [3, 6, 9],
                        [2, 4, 5]]])
TENSOR

# Check number of dimensions for TENSOR
TENSOR.ndim

# Check shape of TENSOR
TENSOR.shape

"""### Random Tensors

Why Random tensors?
Random tensors are important because the way many neural networks learn is that they start with tensors full of random numbers and then adjust those random numbers to better represent the data.

Start with random numbers -> look at data -> update random numbers -> look at data -> update random numbers
"""

# Create a random tensor of size (3, 4)
random_tensor = torch.rand(size=(3, 4))
random_tensor, random_tensor.dtype

# Create a random tensor of size (224, 224, 3)
random_image_size_tensor = torch.rand(size=(224, 224, 3))
random_image_size_tensor.shape, random_image_size_tensor.ndim

"""### Zeros and ones"""

# Create a tensor of all zeros
zeros = torch.zeros(size=(3, 4))
zeros, zeros.dtype

# Create a tensor of all ones
ones = torch.ones(size=(3, 4))
ones, ones.dtype

"""### Creating a range and tensors like"""

# Use torch.arange(), torch.range() is deprecated
zero_to_ten_deprecated = torch.range(0, 10) # Note: this may return an error in the future

# Create a range of values 0 to 10
zero_to_ten = torch.arange(start=0, end=10, step=1)
zero_to_ten

# Can also create a tensor of zeros similar to another tensor
ten_zeros = torch.zeros_like(input=zero_to_ten) # will have same shape
ten_zeros

"""### Tensor datatypes

NOTE: tensor datatypes is one of the big 3 errors you'll run into with PyTorch & deep learning:
1. Tensor not right datatype
2. Tensor not right space
3. Tensors not on the right device
"""

# Default datatype for tensors is float32
float_32_tensor = torch.tensor([3.0, 6.0, 9.0],
                               dtype=None, # defaults to None, which is torch.float32 or whatever datatype is passed
                               device=None, # defaults to None, which uses the default tensor type
                               requires_grad=False) # if True, operations perfromed on the tensor are recorded

float_32_tensor.shape, float_32_tensor.dtype, float_32_tensor.device

float_16_tensor = torch.tensor([3.0, 6.0, 9.0],
                               dtype=torch.float16) # torch.half would also work

float_16_tensor.dtype

float_16_tensor1 = float_32_tensor.type(torch.float16)
float_16_tensor1.dtype

float_16_tensor * float_32_tensor

int_32_tensor = torch.tensor([3, 6, 9], dtype = torch.int32)
int_32_tensor

float_32_tensor * int_32_tensor

"""### Getting information from tensors

1. tensor not right datatype - to do get datatype from a tensor, can use tensor.dtype
2. tensor not right shape - to get shape from a tensor, cam use tensor.shape
3. tensor not on the right device - to get device from a tensor, can use tensor.device
"""

# Create a tensor
some_tensor = torch.rand(3, 4)

# Find out details about it
print(some_tensor)
print(f"Shape of tensor: {some_tensor.shape}")
print(f"Datatype of tensor: {some_tensor.dtype}")
print(f"Device tensor is stored on: {some_tensor.device}") # will default to CPU

"""### Manipulating tensors (tensor operations)

Tensor operations include:
1. Addition
2. Subtraction
3. Multiplication (element-wise)
4. Division
5. Matrix multiplication
"""

# Create a tensor of values and add a number to it
tensor = torch.tensor([1, 2, 3])
tensor + 10

# Multiply it by 10
tensor * 10

# Tensors don't change unless reassigned
tensor

# Subtract and reassign
tensor = tensor - 10
tensor

# Add and reassign
tensor = tensor + 10
tensor

# Can also use torch functions
torch.multiply(tensor, 10)

# Original tensor is still unchanged
tensor

# Element-wise multiplication (each element multiplies its equivalent, index 0->0, 1->1, 2->2)
print(tensor, "*", tensor)
print("Equals:", tensor * tensor)

"""### Matrix multiplication
Two main ways of performing multiplication in neural networks and deep learning
1. Element-wise multiplication
2. Matrix multiplication

There are two main rules that performing matrix multiplication needs to satisfy:
1. The **inner dimensions** must match:
 * (3, 2) @ (3, 2) won't work
 * (2, 3) @ (3, 2) will work
 * (3, 2) @ (2, 3) will work
2. The resulting matrix has the shape of the **outer dimensions**:
 * (2, 3) @ (3, 2) -> (2, 2)
 * (3, 2) @ (2, 3) -> (3, 3)

"""

import torch
tensor = torch.tensor([1, 2, 3])
tensor.shape

# Element-wise matrix multiplication
tensor * tensor

# Matrix multiplication
torch.matmul(tensor, tensor)

# Can also use the "@" symbol for matrix multiplication, though not recommended
tensor @ tensor

# Commented out IPython magic to ensure Python compatibility.
# %%time
# # Matrix multiplication by hand
# # (avoid doing operations with for loops at all cost, they are computationally expensive)
# value = 0
# for i in range(len(tensor)):
#   value += tensor[i] * tensor[i]
# value

# Commented out IPython magic to ensure Python compatibility.
# %%time
# torch.matmul(tensor, tensor)

"""### one of the common errors in deep learning: shape errors"""

# Shapes need to be in the right way
tensor_A = torch.tensor([[1, 2],
                         [3, 4],
                         [5, 6]], dtype=torch.float32)

tensor_B = torch.tensor([[7, 10],
                         [8, 11],
                         [9, 12]], dtype=torch.float32)

torch.matmul(tensor_A, tensor_B) # (this will error)

"""To fix our tensor shape issues, we can manipulate the shape of ones of our tensors using a **transpose**

A **traanspose** switvhes the axes or dimensions of a given tensor.
"""

# View tensor_A and tensor_B
print(tensor_A)
print(tensor_B)

# View tensor_A and tensor_B.T
print(tensor_A)
print(tensor_B.T)

# The operation works when tensor_B is transposed
print(f"Original shapes: tensor_A = {tensor_A.shape}, tensor_B = {tensor_B.shape}\n")
print(f"New shapes: tensor_A = {tensor_A.shape} (same as above), tensor_B.T = {tensor_B.T.shape}\n")
print(f"Multiplying: {tensor_A.shape} * {tensor_B.T.shape} <- inner dimensions match\n")
print("Output:\n")
output = torch.matmul(tensor_A, tensor_B.T)
print(output)
print(f"\nOutput shape: {output.shape}")

# torch.mm is a shortcut for matmul
torch.mm(tensor_A, tensor_B.T)

# Since the linear layer starts with a random weights matrix, let's make it reproducible (more on this later)
torch.manual_seed(42)
# This uses matrix multiplication
linear = torch.nn.Linear(in_features=2, # in_features = matches inner dimension of input
                         out_features=6) # out_features = describes outer value
x = tensor_A
output = linear(x)
print(f"Input shape: {x.shape}\n")
print(f"Output:\n{output}\n\nOutput shape: {output.shape}")

"""### Finding the min, max, mean, sum etc (tensor aggregation)"""

# Create a tensor
x = torch.arange(0, 100, 10)
x

print(f"Minimum: {x.min()}")
print(f"Maximum: {x.max()}")
# print(f"Mean: {x.mean()}") # this will error
print(f"Mean: {x.type(torch.float32).mean()}") # won't work without float datatype
print(f"Sum: {x.sum()}")

torch.max(x), torch.min(x), torch.mean(x.type(torch.float32)), torch.sum(x)

"""### Finding the positional min and max"""

# Create a tensor
tensor = torch.arange(10, 100, 10)
print(f"Tensor: {tensor}")

# Returns index of max and min values
print(f"Index where max value occurs: {tensor.argmax()}")
print(f"Index where min value occurs: {tensor.argmin()}")

"""### Change tensor datatype"""

# Create a tensor and check its datatype
tensor = torch.arange(10., 100., 10.)
tensor.dtype

# Create a float16 tensor
tensor_float16 = tensor.type(torch.float16)
tensor_float16

# Create an int8 tensor
tensor_int8 = tensor.type(torch.int8)
tensor_int8

"""### Reshaping, stacking, squeezing and unsqueezing
* Reshaping - reshapes an input tensor to a defined shape.
* View - return a view of an input tensor of certain shape but keep the same memory as the original tensor.
* Stacking - combine multiple tensors on top of each other (vstack) or side by side (hstack).
* Squeeze - removes all '1' dimensions from a tensor.
* Unsqueeze - add a '1' dimensions to a target tensor
* Permute - return a view of the input with dimensions permuted (swapped) in a certain way
"""

# Create a tensor
import torch
x = torch.arange(1., 8.)
x, x.shape

# Add an extra dimension
x_reshaped = x.reshape(1, 7)
x_reshaped, x_reshaped.shape

# Change view (keeps same data as original but changes view)
z = x.view(1, 7)
z, z.shape

# Changing z changes x (because a view of a tensor shares the same memory as the original)
z[:, 0] = 5
z, x

# Stack tensors on top of each other
x_stacked = torch.stack([x, x, x, x], dim=0)
x_stacked

print(f"Previous tensor: {x_reshaped}")
print(f"Previous shape: {x_reshaped.shape}")

# Remove extra dimension from x_reshaped
x_squeezed = x_reshaped.squeeze()
print(f"\nNew tensor: {x_squeezed}")
print(f"New shape: {x_squeezed.shape}")

"""torch.unsqueeze() - adds a single dimension to a target tensor at a specific dim"""

print(f"Previous tensor: {x_squeezed}")
print(f"Previous shape: {x_squeezed.shape}")

## Add an extra dimension with unsqueeze
x_unsqueezed = x_squeezed.unsqueeze(dim=0)
print(f"\nNew tensor: {x_unsqueezed}")
print(f"New shape: {x_unsqueezed.shape}")

# torch.permute - rearranges the dimensions of a target tensor in a specified order
# Create tensor with specific shape
x_original = torch.rand(size=(224, 224, 3))

# Permute the original tensor to rearrange the axis order
x_permuted = x_original.permute(2, 0, 1) # shifts axis 0->1, 1->2, 2->0

print(f"Previous shape: {x_original.shape}")
print(f"New shape: {x_permuted.shape}")

"""## Indexing (selecting data from tensors)

Indexing with PyTorch is similar to indexing with NumPy
"""

# Create a tensor
import torch
x = torch.arange(1, 10).reshape(1, 3, 3)
x, x.shape

# Let's index bracket by bracket
print(f"First square bracket:\n{x[0]}")
print(f"Second square bracket: {x[0][0]}")
print(f"Third square bracket: {x[0][0][0]}")

# Get all values of 0th dimension and the 0 index of 1st dimension
x[:, 0]

# Get all values of 0th & 1st dimensions but only index 1 of 2nd dimension
x[:, :, 1]

# Get all values of the 0 dimension but only the 1 index value of the 1st and 2nd dimension
x[:, 1, 1]

# Get index 0 of 0th and 1st dimension and all values of 2nd dimension
x[0, 0, :] # same as x[0][0]

# Index on x to return 9
print(x[0][2][2])

# Index on x to return 3, 6, 9
print(x[:, :, 2])

"""## Pytorch tensors & Numpy
* Data in NumPy, want in PyTorch tensor -> torch.from_numpy(ndarray)
* PyTorch tensor -> NumPy -> torch.Tensor.numpy()
"""

# NumPy array to tensor
import torch
import numpy as np
array = np.arange(1.0, 8.0)
tensor = torch.from_numpy(array)
array, tensor

# Change the array, keep the tensor
array = array + 1
array, tensor

# Tensor to NumPy array
tensor = torch.ones(7) # create a tensor of ones with dtype=float32
numpy_tensor = tensor.numpy() # will be dtype=float32 unless changed
tensor, numpy_tensor

# Change the tensor, keep the array the same
tensor = tensor + 1
tensor, numpy_tensor

"""## Reproductibility (trying to take random out of random)

In short how a neural network learns:
'Start with a random numbers -> tensor operations -> update random numbers to try and make them better representations of the data -> again -> again -> again.....

To reduce the randomness in neural networks and PyTorch comes the concept of a **random seed**

Essentially what the random seed does is "flavor" the randomness.
"""

import torch

# Create two random tensors
random_tensor_A = torch.rand(3, 4)
random_tensor_B = torch.rand(3, 4)

print(f"Tensor A:\n{random_tensor_A}\n")
print(f"Tensor B:\n{random_tensor_B}\n")
print(f"Does Tensor A equal Tensor B? (anywhere)")
random_tensor_A == random_tensor_B

# Let's make some random but reproducible tensors
import torch
import random

# # Set the random seed
RANDOM_SEED=42 # try changing this to different values and see what happens to the numbers below
torch.manual_seed(seed=RANDOM_SEED)
random_tensor_C = torch.rand(3, 4)

# Have to reset the seed every time a new rand() is called
# Without this, tensor_D would be different to tensor_C
torch.random.manual_seed(seed=RANDOM_SEED) # try commenting this line out and seeing what happens
random_tensor_D = torch.rand(3, 4)

print(f"Tensor C:\n{random_tensor_C}\n")
print(f"Tensor D:\n{random_tensor_D}\n")
print(f"Does Tensor C equal Tensor D? (anywhere)")
random_tensor_C == random_tensor_D

"""## Running tensors and PyTorch objects on the GPUs (and making faster computations)

GPUs = faster computation on numbers, thanks to CUDA + NVIDIA hardware + PyTorch
"""

! nvidia-smi

"""### Check for GPU access with PyTorch"""

# Check for GPU
import torch
torch.cuda.is_available()

# Set device type
# Setup device agnostic code
device = "cuda" if torch.cuda.is_available() else "cpu"
device

# Count number of devices
torch.cuda.device_count()

"""### Putting tensors and models on the GPU"""

# Create tensor (default on CPU)
tensor = torch.tensor([1, 2, 3])

# Tensor not on GPU
print(tensor, tensor.device)

# Move tensor to GPU (if available)
tensor_on_gpu = tensor.to(device)
tensor_on_gpu

"""### Moving tensors back to the CPU"""

# If tensor is on GPU, can't transform it to NumPy (this will error)
tensor_on_gpu.numpy()

# Instead, copy the tensor back to cpu
tensor_back_on_cpu = tensor_on_gpu.cpu().numpy()
tensor_back_on_cpu

tensor_on_gpu