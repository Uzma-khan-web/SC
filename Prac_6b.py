#Aim: Write a program for Adaptive Resonance Theory (ART).
import numpy as np

VIGILANCE = 0.6
LEARNING_COEF = 0.5

train = np.array([
    [1,0,0,0,0,0],
    [1,1,1,1,1,0],
    [1,0,1,0,1,0],
    [0,1,0,0,1,1],
    [1,1,1,0,0,0],
    [0,0,1,1,1,0],
    [1,1,1,1,1,0],
    [1,1,1,1,1,0],
    [1,1,1,1,1,1],
])

test = np.array([
    [1,1,1,1,1,1],
    [1,1,1,1,1,0],
    [1,1,1,1,0,0],
    [1,1,1,0,0,0],
    [1,1,0,0,0,0],
    [1,0,0,0,0,0],
    [0,0,0,0,0,0],
])

L1_neurons_cnt = len(train[0])
L2_neurons_cnt = 1

bottomUps = np.array([[1/(L1_neurons_cnt + 1) for _ in range(L1_neurons_cnt)]], np.float64)
topDowns = np.array([[1 for _ in range(L1_neurons_cnt)]], np.float64)

for tv in train:
    print("\nTrain Vector: ", tv)
    createNewNeuron = True
    OUTPUTs = [bottomUps[i].dot(tv) for i in range(L2_neurons_cnt)]
    counter = L2_neurons_cnt

    while counter > 0:
        winning_OUTPUT = max(OUTPUTs)
        winner_neuron_idx = OUTPUTs.index(winning_OUTPUT)

        tv_sum = sum(tv)
        similarity = 0 if tv_sum == 0 else topDowns[winner_neuron_idx].dot(tv) / tv_sum

        print(" TopDowns[Winner]: ", topDowns[winner_neuron_idx])
        print(" BottomUps Weights: ", bottomUps[winner_neuron_idx])
        print(" Similarity: ", similarity)

        if similarity >= VIGILANCE:
            createNewNeuron = False
            new_bottom_weights = tv * topDowns[winner_neuron_idx] / \
                                 (LEARNING_COEF + tv.dot(topDowns[winner_neuron_idx]))
            new_top_weights = tv * topDowns[winner_neuron_idx]

            topDowns[winner_neuron_idx] = new_top_weights
            bottomUps[winner_neuron_idx] = new_bottom_weights
            break
        else:
            OUTPUTs[winner_neuron_idx] = -1
            counter -= 1

    if createNewNeuron:
        print(" Creating a new neuron")
        new_bottom_weights = np.array([[i / (LEARNING_COEF + sum(tv)) for i in tv]], np.float64)
        new_top_weights = np.array([[i for i in tv]], np.float64)

        print(" Weights bottomUps: ", new_bottom_weights)
        print(" Weights topDown: ", new_top_weights)

        bottomUps = np.append(bottomUps, new_bottom_weights, axis=0)
        topDowns = np.append(topDowns, new_top_weights, axis=0)
        L2_neurons_cnt += 1

print("=======")
print(f"Total Classes: {L2_neurons_cnt}")
print("Center of masses")
print(topDowns)

for tv in test:
    A = list(range(L2_neurons_cnt))
    OUTPUTs = [bottomUps[i].dot(tv) for i in A]
    winner_neuron_idx = OUTPUTs.index(max(OUTPUTs))
    print(f"Class {winner_neuron_idx} for test vector {tv}")
