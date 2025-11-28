#Aim: Write a program for Self-Organising Maps (SOM).
import numpy as np
from minisom import MiniSom
import matplotlib.pyplot as plt

colors = np.array([
    [0., 0., 0.], [0., 0., 1.], [0., 0., 0.5], [0.125, 0.519, 1.0],
    [0.33, 0.4, 0.67], [0.6, 0.5, 1.0], [0., 1., 0.], [1., 0., 0.],
    [0., 1., 1.], [1., 1., 0.], [1., 1., 1.], [.33, .33, .33],
    [.5, .5, .5], [.66, .66, .66]
])

color_names = [
    'black', 'blue', 'darkblue', 'skyblue', 'greyblue', 'lilac',
    'green', 'red', 'cyan', 'violet', 'yellow', 'white',
    'darkgrey', 'mediumgrey', 'lightgrey'
]

som = MiniSom(20, 30, 3, sigma=1.0, learning_rate=0.5)
som.train(colors, 1000)

plt.imshow(som.get_weights()[:, :, :3], origin='lower')
plt.title('Color SOM')

for i, color in enumerate(colors):
    w = som.winner(color)
    plt.text(
        w[1],
        w[0],
        color_names[i],
        ha='center',
        va='center',
        bbox=dict(facecolor='white', alpha=0.5, lw=0)
    )

plt.show()
