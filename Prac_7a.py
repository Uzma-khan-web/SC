#Aim: Write a program for Line Separation.
import numpy as np
import matplotlib.pyplot as plt

def create_distance_function(a, b, c):
    def distance(x, y):
        nom = a * x + b * y + c

        if nom == 0:
            pos = 0
        elif (nom < 0 and b < 0) or (nom > 0 and b > 0):
            pos = -1
        else:
            pos = 1

        return (np.abs(nom) / np.sqrt(a**2 + b**2), pos)

    return distance

def main():
    points = [(3.5, 1.8), (1.1, 3.9)]  # Example points

    fig, ax = plt.subplots()
    ax.set_xlabel("sweetness")
    ax.set_ylabel("sourness")
    ax.set_xlim([-1, 6])
    ax.set_ylim([-1, 8])

    X = np.arange(-0.5, 5, 0.1)  # X values for plotting line

    # Plot points
    size = 10
    for index, (x, y) in enumerate(points):
        color = "darkorange" if index == 0 else "yellow"
        ax.plot(x, y, "o", color=color, markersize=size)

    # Define the step for line plotting and slope generation
    step = 0.05
    for x_param in np.arange(0, 1 + step, step):
        slope = np.tan(np.arccos(x_param))  # Slope
        dist4line1 = create_distance_function(slope, -1, 0)

        # Generate Y for line
        Y = slope * X

        # Check position of points relative to the line
        results = []
        for point in points:
            results.append(dist4line1(*point))

        print(slope, results)

        # If points are separated, draw green line else red
        if results[0][1] != results[1][1]:
            ax.plot(X, Y, "g-")
        else:
            ax.plot(X, Y, "r-")

    plt.show()


if __name__ == "__main__":
    main()
