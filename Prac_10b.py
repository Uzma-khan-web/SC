#Aim: Implementation of Simple Genetic Algorithm
import numpy as np
import matplotlib.pyplot as plt
import copy

# Cost function (Sphere Function)
def sphere(x):
    return np.sum(x**2)

# Roulette Wheel Selection
def roulette_wheel_selection(p):
    c = np.cumsum(p)
    r = sum(p) * np.random.rand()
    ind = np.argwhere(r <= c)
    return ind[0][0]

# Crossover
def crossover(p1, p2):
    c1 = copy.deepcopy(p1)
    c2 = copy.deepcopy(p2)

    alpha = np.random.uniform(0, 1, size=c1['position'].shape)

    c1['position'] = alpha * p1['position'] + (1 - alpha) * p2['position']
    c2['position'] = alpha * p2['position'] + (1 - alpha) * p1['position']
    return c1, c2

# Mutation
def mutate(c, mu, sigma):
    y = copy.deepcopy(c)
    flag = np.random.rand(*c['position'].shape) <= mu
    y['position'][flag] += sigma * np.random.randn(np.sum(flag))
    return y

# Apply bounds
def bounds(c, varmin, varmax):
    c['position'] = np.maximum(c['position'], varmin)
    c['position'] = np.minimum(c['position'], varmax)

# Sort population
def sort_population(arr):
    return sorted(arr, key=lambda x: x['cost'])

# Genetic Algorithm
def ga(costfunc, num_var, varmin, varmax, maxit, npop, num_children, mu, sigma, beta):

    population = []

    # Initial population
    for _ in range(npop):
        ind = {}
        ind['position'] = np.random.uniform(varmin, varmax, num_var)
        ind['cost'] = costfunc(ind['position'])
        population.append(ind)

    population = sort_population(population)
    bestsol = copy.deepcopy(population[0])
    bestcost = np.zeros(maxit)

    for it in range(maxit):

        costs = np.array([ind['cost'] for ind in population])
        max_cost = np.max(costs)

        fitness = np.exp(-beta * costs / max_cost)
        probs = fitness / np.sum(fitness)

        children = []

        for _ in range(num_children // 2):
            p1 = population[roulette_wheel_selection(probs)]
            p2 = population[roulette_wheel_selection(probs)]

            c1, c2 = crossover(p1, p2)

            c1 = mutate(c1, mu, sigma)
            c2 = mutate(c2, mu, sigma)

            bounds(c1, varmin, varmax)
            bounds(c2, varmin, varmax)

            c1['cost'] = costfunc(c1['position'])
            c2['cost'] = costfunc(c2['position'])

            children.append(c1)
            children.append(c2)

        population.extend(children)
        population = sort_population(population)[:npop]

        if population[0]['cost'] < bestsol['cost']:
            bestsol = copy.deepcopy(population[0])

        bestcost[it] = bestsol['cost']

        # Print every 50 iterations
        if (it % 50 == 0) or (it == maxit - 1):
            print(f"Iteration {it}: Best Cost = {bestcost[it]}")

    return population, bestsol, bestcost


# Problem Definition
costfunc = sphere
num_var = 5
varmin = -10
varmax = 10

# GA Parameters
maxit = 501
npop = 20
beta = 1

prop_children = 1
num_children = int(np.round(prop_children * npop / 2) * 2)
mu = 0.2
sigma = 0.1

# Run GA
population, bestsol, bestcost = ga(
    costfunc, num_var, varmin, varmax,
    maxit, npop, num_children, mu, sigma, beta
)

# Plot Best Cost Progress
plt.plot(bestcost)
plt.xlim(0, maxit)
plt.xlabel('Generations')
plt.ylabel('Best Cost')
plt.title('Genetic Algorithm Optimization')
plt.grid(True)
plt.show()
