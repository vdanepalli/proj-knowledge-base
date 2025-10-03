# [PyTorch](../../courses.md)


- [PyTorch](#pytorch)
  - [ZTM: PyTorch for Deep Learning](#ztm-pytorch-for-deep-learning)
    - [PyTorch Fundamentals](#pytorch-fundamentals)


## ZTM: PyTorch for Deep Learning

### PyTorch Fundamentals

- ML is turning data into numbers and finding patterns in that numbers
- AI > ML > DL
- traditional -- inputs > rules > output
- ML -- inputs > outputs > rules
- [Learn PyTorch](https://www.learnpytorch.io/)
- [Code Slides Resources](https://github.com/mrdbourke/pytorch-deep-learning)
- [PyTorch Discussions](https://github.com/mrdbourke/pytorch-deep-learning/discussions)


<br/><br/>

- simple rule-based system > ML 
- when
  - problems with long list of rules
  - continually changing environments
  - discovering insights within large collections of data
- when not
  - when you need explainability
  - when traditional approach is a better option
  - when errors are unacceptable
  - when you don't have much data
- ML - structured data -- shallow algorithms
  - Random Forest
  - Gradient Boost
  - Naive Bayes
  - Nearest Neighbors
  - Support Vector Machines
- DL - unstructured data
  - Neural Networks
  - CNNs
  - RNNs
  - Transformers


<br/><br/>

- Inputs -> Numerical Encoding -> Neural Networks (learns representation - patterns/features/weights) -> Representation outputs -> Outputs
- Input Layer (data goes in) -> Hidden Layer(s) (learns patterns in data) -> Output Layer (otputs learned representations or predicted probabilities)
- each layer is usually a combination of linear and non-linear functions
- types of learning
  - supervised -- data and labels (input - output mappings)
  - unsupervised & self-supervised -- data, no labels
  - transfer learning -- transferring patterns learned by a model over a dataset to another model
  - reinforcement learning -- agent actions rewards observations
- applications
  - recommendations
  - translation
  - speech recognition
  - computer vision
  - natural language processing
- types
  - classification/regression
  - sequence to sequence seq2seq


<br/><br/>

- PyTorch -- Deep Learning framework
  - pre-built models
  - whole stack -- pre-process, build, deploy
  - originally designed by Meta, now open-sourced
  - enables you to leverage GPU/TPU
- [AIML Research Papers - Paperswithcode](https://paperswithcode.com/)
- Tensor
  - Numerical Encoding and Representaion Outputs -- Tensors
  - Inputs -> Numerical Encoding -> Neural Networks (learns representation - patterns/features/weights) -> Representation outputs -> Outputs

1. Get Data Ready (turn into tensors)
2. Build or pick pre-trained Model (to suit your problem)
   1. Pick a loss function and optimizer
   2. Build a training loop
3. Fit the model to data and make prediction
4. Evaluate the model
5. Improve through experimentation
6. Save and reload your trained model


<br/><br/>

1. Code along
2. Explore and experiment
3. Visualize what you don't understand
4. Ask questions
5. Do the exercies
6. Share your work

- `!nvidia-smi` -- info on GPU -- colab
- `import torch`
- `torch.__version__`

```py
scalar = torch.tensor(39) # tensor(39)
scalar.ndim # 0
scalar.item # 39

vector = torch.tensor([12, 39]) # tensor([12, 39])
vector.ndim # 1 -- number of square brackets
vector.shape # torch.Size([2])

MATRIX = torch.tensor([[12, 39], [39, 12]])
MATRIX.ndim # 2
MATRIX[0] # tensor([12, 39])
MATRIX.shape # torch.Size([2, 2])

TENSOR = torch.tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
TENSOR.ndim # 3
TENSOR.shape # torch.Size([1, 3, 3])
```

- Start with random numbers (tensors) -> look at data -> update random numbers -> look at data -> update ....

```py
random_tensor = torch.rand(3, 4) # [[1,2,3,4], [1,2,3,4], [1,2,3,4]]
random_tensor.ndim # 2

random_image_size_tensor = torch.rand(size=(224, 224, 3)) # height width color channels
random_image_size_tensor = torch.rand(size=(3, 224, 224)) # color channels height width

zeroes = torch.zeros(size=(3, 4))
ones = torch.ones(size=(3, 4))

ones.dtype # torch.float32

one_to_ten = torch.arange(1, 11, 2) # start end step
ten_zeros = torch.zeros_like(input=one_to_ten)

float_32_tensor = torch.tensor([1, 2, 3], 
    dtype = None, # defaults to float32 even when specified as None
    device = None, # defaults to cpu; can change to cuda for gpu; what device is your tensor on
    requires_grad = False # whether or not to track gradients with this tensors operation
)

float_16_tensor = float_32_tensor.type(torch.float16)

tensor.dtype
tensor.shape
tensor.size()
tensor.device
```

- 3 big errors
  - tensors not right data type
  - tesnors not right shape
  - tensors not on the right device
- tensor operations
  - addition `tensor + 10` -- add 10 to each element
  - subtraction 
  - multiplication (element-wise) `tensor * 10` -- multiply each element by 10 -- `torch.mul(tensor, 10)`
  - division
  - matrix multiplication (dot product) - `torch.matmul(tensor, tensor)` `tensor @ tensor` `torch.mm(tensor, tensor)`
    - inner dimensions must match 
    - result has shape of outer dimensions
    - [matrixmultiplication xyz website](https://matrixmultiplication.xyz/)
    - 

```py
%%time # magic function - gives CPU Times (user, sys, total) and Wall Time

tensor_a @ tensor_a.T

torch.min(tensor)
tensor.min()

torch.max(tensor)
tensor.max()

torch.mean(int_tensor.type(torch.float32)) # mean doesn not support int64
int_tensor.type(torch.float32).mean()

torch.sum(tensor)
tensor.sum()

tensor.argmin() # position in tensor that has min val - returns position of target tensor where min value occurs
tensor.argmax()
```

```py
x = torch.arange(1, 10)
x, x.shape

# Reshaping 
x_reshaped = x.reshape(1, 9)

# View -- shares the same memory as original tensor; same as reshape; changing z changes x
z = x.view(1, 9)

# Stacking -- stack, hstack, vstack -- combine multiple tensors on top of each other (vstack) or side by side (hstack)
x_stacked = torch.stack([x,x,x,x], dim=0)

# Squeeze -- removes all 1 dimensions from a tensor
x_reshaped.squeeze()

# Unsqueeze -- add a 1 dimension to a target vector
x_unsqueezed = x_squeezed.unsqueeze(dim=0)

# Permute -- rearranges the dimensions of a target tensor in a specified order -- returns view of original tensor with dimensions permuted
x_original = torch.rand(size=(224, 224, 3))
x_permuted = x_original.permute([2, 0, 1]) # shift axis 0->1, 1->2, 2->0
```

```py
x = torch.rand(size=(3, 3)).reshape(1, 3, 3)
x[0] # [[]]
x[0][0] # [] x[0,0,:]
x[0][1][1] # 39

x[:, :, 1] # all values of 0th and 1st dimensions, but only index 1 of second dimension

x[:, 1, 1] # []
x[0, 1, 1] # 39
```

