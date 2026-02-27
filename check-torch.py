import torch

scalar= torch.tensor(7)
# print(scalar.item())

vector= torch.tensor([7,7])
# print(vector.shape)

MATRIX = torch.tensor([
    [7,8],
    [9,10]
])
print(MATRIX.shape)

# Tensor
TENSOR = torch.tensor([[[1, 2, 3],
                        [3, 6, 9],
                        [2, 4, 5]]])
# print(TENSOR)

print(TENSOR.shape)

# Create a random tensor of size (3, 4)
random_tensor = torch.rand(size=(3, 4))
# print(random_tensor, random_tensor.dtype)

# Create a tensor of all zeros
zeros = torch.zeros(size=(3, 4))
# print(zeros, zeros.dtype)

# Create a tensor of all ones
ones = torch.ones(size=(3, 4))
# print (ones, ones.dtype)

