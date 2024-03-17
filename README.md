# goit-algo-hw-10
The repository for the 10th GoItNeo Basic Algorithms homework: Linear programming and randomized algorithms

### To run the project please complete the following steps:

pip install -r requirements.txt or pip3 install -r requirements.txt

python main.py or python3 main.py

## Task 1 Bevegare Production Calculations
The beverage lines of the company include "Lemonade" and "Fruit Juice." These drinks are prepared using various ingredients and minimal equipment. The goal is to maximize output while taking the finite resources into account. 
We have the following list of resources: 

- 100 units of "Water"
- 50 units of "Sugar"
- 30 units of "Lemon Juice"
- 40 units of "Fruit Puree"

To produce one "Lemonade" unit, the following are needed:

- 2 units of "Water"
- 1 unit of "Sugar"
- 1 unit of "Lemon Juice"

To produce one "Fruit Juice" unit, the following are needed:

- 2 units of "Fruit Puree"
- 1 unit of "Water"

We have the following results: 

Production of "Lemonade": 30.0
Production of "Fruit Juice": 20.0
Total production: 50.0

## Task 2 Сalculation of the definite integral by the Monte Carlo method

The results obtained from the SciPy quad calculation and the Monte Carlo calculation for the integral of the function 
x**3 + x**2 + x + 3 are as follows:

SciPy quad calculation:  14.666666666666668

Monte Carlo calculation:  14.5724

From these results, we can draw the following conclusions:

**Accuracy:** The SciPy quad calculation tends to provide more accurate results compared to Monte Carlo integration. This is because the SciPy quad uses numerical integration techniques that are specifically designed to accurately estimate the integral of a function over a given interval.

**Efficiency:** Monte Carlo integration, on the other hand, is a probabilistic method that relies on random sampling. While it may be less accurate than traditional numerical integration methods, Monte Carlo integration can be more efficient for high-dimensional integrals or integrals with complex boundaries, where other methods may struggle.

**Stability:** SciPy quad is generally more stable and reliable for a wide range of functions and integration problems. Monte Carlo integration may require a larger number of samples to achieve acceptable accuracy, especially for functions with irregular or oscillatory behavior.

**Computational Cost:** Monte Carlo integration can be computationally expensive, especially when a large number of samples is required to achieve the desired accuracy. SciPy quad may offer a more computationally efficient solution for many problems, particularly when high accuracy is needed and the function is well-behaved.

In summary, while both methods have their advantages and disadvantages, the choice between SciPy quad and Monte Carlo integration depends on factors such as the desired level of accuracy, the complexity of the function and integration domain, and the computational resources available.
