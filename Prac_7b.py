#Aim: Write a program for Hopfield Network model for Associative Memory.
import numpy as np
import matplotlib.pyplot as plt

# === Pattern creation functions ===
def create_checkerboard(size):
    return np.indices((size, size)).sum(axis=0) % 2

def create_random_pattern(size, on_prob=0.5):
    return (np.random.rand(size, size) < on_prob).astype(int)

def create_random_pattern_list(size, nr_patterns, on_prob=0.5):
    return [create_random_pattern(size, on_prob) for _ in range(nr_patterns)]

def plot_pattern_list(pattern_list, titles=None):
    n = len(pattern_list)
    plt.figure(figsize=(n * 2, 2))

    for i, p in enumerate(pattern_list):
        plt.subplot(1, n, i + 1)
        plt.imshow(p, cmap='gray_r')
        plt.axis('off')
        if titles:
            plt.title(titles[i])
    plt.show()

def compute_overlap(p1, p2):
    # Convert binary 0/1 to bipolar -1/+1
    p1_bipolar = 2 * p1.flatten() - 1
    p2_bipolar = 2 * p2.flatten() - 1
    return np.dot(p1_bipolar, p2_bipolar) / len(p1_bipolar)

def compute_overlap_matrix(pattern_list):
    n = len(pattern_list)
    mat = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            mat[i, j] = compute_overlap(pattern_list[i], pattern_list[j])
    return mat

def plot_overlap_matrix(mat):
    plt.imshow(mat, cmap='coolwarm', vmin=-1, vmax=1)
    plt.colorbar()
    plt.title("Overlap matrix")
    plt.show()

# === Hopfield network class ===
class HopfieldNetwork:
    def __init__(self, nr_neurons):
        self.nr_neurons = nr_neurons
        self.weights = np.zeros((nr_neurons, nr_neurons))

    def train(self, patterns):
        patterns_bipolar = [2 * p.flatten() - 1 for p in patterns]

        for p in patterns_bipolar:
            self.weights += np.outer(p, p)

        np.fill_diagonal(self.weights, 0)
        self.weights /= len(patterns)

    def recall(self, state, steps=5):
        s = 2 * state.flatten() - 1
        states = [s.copy()]

        for _ in range(steps):
            s = np.sign(self.weights @ s)
            s[s == 0] = 1
            states.append(s.copy())

        return states

    def state_to_pattern(self, state, shape):
        return ((state.reshape(shape) + 1) // 2).astype(int)

def flip_n_bits(pattern, n):
    p_flat = pattern.flatten()
    indices = np.random.choice(len(p_flat), size=n, replace=False)
    p_flat[indices] = 1 - p_flat[indices]
    return p_flat.reshape(pattern.shape)

# === Main script ===
pattern_size = 5

checkerboard = create_checkerboard(pattern_size)
pattern_list = [checkerboard]
pattern_list.extend(create_random_pattern_list(pattern_size, 3, on_prob=0.5))

# Plot original patterns
plot_pattern_list(pattern_list, titles=["Checkerboard"] + [f"Random {i+1}" for i in range(3)])

# Overlap matrix
overlap_matrix = compute_overlap_matrix(pattern_list)
plot_overlap_matrix(overlap_matrix)

# Train Hopfield network
hp_net = HopfieldNetwork(nr_neurons=pattern_size ** 2)
hp_net.train(pattern_list)

# Create noisy version of checkerboard (flip 4 bits)
noisy_init = flip_n_bits(checkerboard, 4)

# Recall sequence
states = hp_net.recall(noisy_init, steps=6)
states_as_patterns = [hp_net.state_to_pattern(s, (pattern_size, pattern_size)) for s in states]

# Plot recall sequence
plot_pattern_list(states_as_patterns, titles=[f"Step {i}" for i in range(len(states_as_patterns))])
