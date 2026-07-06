# Linear Regression using PyTorch

A simple Linear Regression model built using **PyTorch** to learn the equation:

\[
Y = 2X
\]

The model is trained using **Gradient Descent (SGD)** and **Mean Squared Error (MSE) Loss**. After training, the user can enter a new value of `X`, and the model predicts the corresponding value of `Y`.

---

## Features

- Uses PyTorch tensors
- Implements a Linear Regression model (`nn.Linear`)
- Uses Mean Squared Error Loss (`nn.MSELoss`)
- Uses Stochastic Gradient Descent (`torch.optim.SGD`)
- Trains for 1000 epochs
- Displays training loss every 100 epochs
- Prints the learned weight and bias
- Accepts user input for prediction

---

## Dataset

Training Data:

| X | Y |
|---|---|
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |
| 4 | 8 |

The model learns the relationship:

```
Y ≈ 2X
```

---

## Technologies Used

- Python 3
- PyTorch

---

## Installation

Install PyTorch:

```bash
pip install torch
```

---

## Run the Program

```bash
python Linear_Regression_y=wx+b.py
```

---

## Project Workflow

```
Training Data
      │
      ▼
Linear Model
      │
      ▼
Prediction
      │
      ▼
MSE Loss
      │
      ▼
Backpropagation
      │
      ▼
SGD Optimizer
      │
      ▼
Updated Weights
```

---

## Model Architecture

```
Input (1 Feature)
        │
        ▼
Linear Layer
(1 Input → 1 Output)
        │
        ▼
Predicted Value
```

---

## Loss Function

The project uses:

```python
nn.MSELoss()
```

Formula:

```
Loss = (Predicted - Actual)²
```

The objective is to minimize this loss during training.

---

## Optimizer

The optimizer used is:

```python
torch.optim.SGD(model.parameters(), lr=0.01)
```

It updates the model's weight and bias after every training iteration.

---

## Output Example

```
100 : 0.2153
200 : 0.0318
300 : 0.0048
...
1000 : 0.0000

Learned weight: 2.00
Learned bias: 0.00

The equation is:
Y = 2.00X + 0.00
```

Example prediction:

```
Enter the number:
10

20.00
```

---

## Concepts Covered

- Tensors
- Linear Regression
- Neural Networks
- Forward Pass
- Loss Function
- Backpropagation
- Gradient Descent
- Optimizers
- Epochs
- Model Parameters
- Prediction

---

## Future Improvements

- Train on larger datasets
- Read data from CSV files
- Plot the regression line using Matplotlib
- Save and load trained models
- Add GPU support
- Implement mini-batch training

---

## Author

Created as a beginner-friendly PyTorch Linear Regression project for learning deep learning fundamentals.
