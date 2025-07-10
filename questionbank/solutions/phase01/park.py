Q1. 1. Write a Python script to print the current working directory and Python version.

import os
import sys
print("Current Working Directory:", os.getcwd())
print("Python Version:", sys.version)
Q2. 2. Create a virtual environment and install pandas and NumPy using pip.

# In terminal or command line (not Python script):
# python -m venv venv
# source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows)
# pip install pandas numpy
Q3. 3. Load a `.csv` file using pandas and display the first 5 rows.

import pandas as pd
df = pd.read_csv('your_file.csv')
print(df.head())
Q4. 4. Count missing values column-wise using pandas.

import pandas as pd
df = pd.read_csv('your_file.csv')
print(df.isnull().sum())
Q5. 5. Write a Python program to check whether a given number is prime.

def is_prime(n):
if n <= 1:
return False
for i in range(2, int(n**0.5) + 1):
if n % i == 0:
return False
return True

print(is_prime(7)) # Example
Q6. 6. Demonstrate usage of `for`, `if`, `break`, `continue`, and `else` in a loop.

for i in range(10):
if i == 3:
continue

if i == 8:
break
print(i)
else:
print("Loop ended successfully.")
Q7. 7. Create a class `Employee` with attributes and a method to display salary after tax.

class Employee:
def __init__(self, name, salary):
self.name = name
self.salary = salary
def net_salary(self):
return self.salary * 0.8 # Assume 20% tax
emp = Employee("John", 50000)
print(emp.net_salary())
Q8. 8. Handle `ZeroDivisionError` and `ValueError` in a calculator program.

try:
a = float(input("Enter numerator: "))
b = float(input("Enter denominator: "))
print("Result:", a / b)
except ZeroDivisionError:
print("Error: Division by zero.")
except ValueError:
print("Error: Invalid input.")
Q9. 9. Demonstrate inheritance using `Vehicle` `Car`.

class Vehicle:
def __init__(self, brand):
self.brand = brand

def honk(self):
print("Honk!")
class Car(Vehicle):
def __init__(self, brand, model):
super().__init__(brand)
self.model = model

car = Car("Toyota", "Corolla")
car.honk()

print(car.brand, car.model)
Q10. 10. Create a 33 matrix in NumPy and compute its transpose and determinant.
import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Transpose:", A.T)
print("Determinant:", np.linalg.det(A))
Q11. 11. Generate a 1D NumPy array of 50 random numbers and plot a histogram using matplotlib.
import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(50)
plt.hist(data)
plt.show()
