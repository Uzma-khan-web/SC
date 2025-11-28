#Aim: Write a program for Radial Basis Function.
from scipy import *
from scipy.linalg import norm, pinv
from matplotlib import pyplot as plt
from numpy import random as random
import numpy as np
from scipy.interpolate import interp1d

class RBF:
    def __init__(self, indim, numCenters, outdim):
        self.indim = indim
        self.outdim = outdim
        self.numCenters = numCenters
        self.centers = [random.uniform(-1, 1, indim) for i in range(numCenters)]
        self.beta = 8
        self.W = random.random((self.numCenters, self.outdim))

    def _basisfunc(self, c, d):
        assert len(d) == self.indim
        return np.exp(-self.beta * norm(c - d) ** 2)

    def _calcAct(self, X):
        G = np.zeros((X.shape[0], self.numCenters), float)
        for ci, c in enumerate(self.centers):
            for xi, x in enumerate(X):
                G[xi, ci] = self._basisfunc(c, x)
        return G

    def train(self, X, Y):
        rnd_idx = random.permutation(X.shape[0])[:self.numCenters]
        self.centers = [X[i, :] for i in rnd_idx]
        print("center", self.centers)
        G = self._calcAct(X)
        self.W = np.dot(pinv(G), Y)

    def test(self, X):
        G = self._calcAct(X)
        Y = np.dot(G, self.W)
        return Y


if __name__ == "__main__":
    n = 100
    x = np.mgrid[-1:1:complex(0, n)].reshape(n, 1)
    y = np.sin(3 * (x + 0.5) ** 3 - 1)
    y += random.normal(0, 0.1, y.shape)

    rbf = RBF(1, 10, 1)
    rbf.train(x, y)
    z_rbf = rbf.test(x)

    # Extract centers
    centers_x = np.array(rbf.centers).flatten()
    centers_y = np.zeros_like(centers_x)

    # Start with first black data point
    start_x = x[0, 0]
    start_y = y[0, 0]

    # Combine start point with centers
    all_x = np.concatenate(([start_x], centers_x))
    all_y = np.concatenate(([start_y], centers_y))

    # Sort points for interpolation
    sorted_indices = np.argsort(all_x)
    all_x_sorted = all_x[sorted_indices]
    all_y_sorted = all_y[sorted_indices]

    # Linear interpolation
    interp_func = interp1d(all_x_sorted, all_y_sorted, kind='linear', fill_value="extrapolate")
    z_interp = interp_func(x.flatten())

    plt.figure(figsize=(12, 8))
    plt.plot(x, y, "k-", label="Original Data")
    plt.plot(x, z_interp, "r-", linewidth=2,
             label="Red Line Touching First Black Point and All Green Centers")
    plt.plot(centers_x, centers_y, "gs", label="RBF Centers (y=0)")
    plt.xlim(-1.2, 1.2)
    plt.legend()
    plt.title("RBF Network with Red Line Starting at First Black Point and Touching All Green Points")
    plt.show()
