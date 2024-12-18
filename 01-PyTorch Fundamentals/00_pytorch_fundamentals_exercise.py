# -*- coding: utf-8 -*-
"""00_pytorch_fundamentals_exercise.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1URvySlkRixdVynBRUFyD-G3T-HN_h2g3

**1. Create a random tensor with shape (7, 7).**
"""

# Import torch
import torch

# Create random tensor
X = torch.rand(size=(7, 7))
X, X.shape

"""**2. Perform a matrix multiplication on the tensor from 2 with another random tensor with shape (1, 7) (hint: you may have to transpose the second tensor).**"""

# Create another random tensor
Y = torch.rand(size=(1, 7))
# Z = torch.matmul(X, Y) # will error because of shape issues
Z = torch.matmul(X, Y.T) # no error because of transpose
Z, Z.shape

"""**3. Set the random seed to 0 and do 2 & 3 over again.**"""

# Set manual seed
torch.manual_seed(0)

# Create two random tensors
X = torch.rand(size=(7, 7))
Y = torch.rand(size=(1, 7))

# Matrix multiply tensors
Z = torch.matmul(X, Y.T)
Z, Z.shape

"""**4. Speaking of random seeds, we saw how to set it with torch.manual_seed() but is there a GPU equivalent?**"""

# Set random seed on the GPU
torch.cuda.manual_seed(1234)

"""**5. Create two random tensors of shape (2, 3) and send them both to the GPU (you'll need access to a GPU for this). Set torch.manual_seed(1234) when creating the tensors (this doesn't have to be the GPU random seed). The output should be something like:**"""

# Set random seed
torch.manual_seed(1234)

# Check for access to GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Device: {device}")

# Create two random tensors on GPU
tensor_A = torch.rand(size=(2,3)).to(device)
tensor_B = torch.rand(size=(2,3)).to(device)
tensor_A, tensor_B

"""**6. Perform a matrix multiplication on the tensors you created in 6**"""

# Perform matmul on tensor_A and tensor_B
# tensor_C = torch.matmul(tensor_A, tensor_B) # won't work because of shape error
tensor_C = torch.matmul(tensor_A, tensor_B.T)
tensor_C, tensor_C.shape

"""**7. Find the maximum and minimum values of the output of 7.**"""

# Find max
max = torch.max(tensor_C)

# Find min
min = torch.min(tensor_C)
max, min

"""**8. Find the maximum and minimum index values of the output of 7.**"""

# Find arg max
arg_max = torch.argmax(tensor_C)

# Find arg min
arg_min = torch.argmin(tensor_C)
arg_max, arg_min

"""**9. Make a random tensor with shape (1, 1, 1, 10) and then create a new tensor with all the 1 dimensions removed to be left with a tensor of shape (10). Set the seed to 7 when you create it and print out the first tensor and it's shape as well as the second tensor and it's shape.**"""

# Set seed
torch.manual_seed(7)

# Create random tensor
tensor_D = torch.rand(size=(1, 1, 1, 10))

# Remove single dimensions
tensor_E = tensor_D.squeeze()

# Print out tensors
print(tensor_D, tensor_D.shape)
print(tensor_E, tensor_E.shape)