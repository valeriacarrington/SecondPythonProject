import numpy as np
import nnfs
import matplotlib.pyplot as plt

nnfs.init()

def generate_spiral_data(points, classes):
    X = []
    y = []
    for class_number in range(classes):
        r = np.linspace(0.0, 1, points)
        t = np.linspace(class_number * 4, (class_number + 1) * 4, points) + np.random.randn(points) * 0.2
        for i in range(points):
            X.append([r[i] * np.sin(t[i] * 2.5), r[i] * np.cos(t[i] * 2.5)])
            y.append(class_number)
    return np.array(X), np.array(y, dtype="uint8")

points = 100
classes = 3
X, y = generate_spiral_data(points, classes)

plt.scatter(X[:, 0], X[:, 1], c=y, cmap="plasma")  # Purple
plt.show()

plt.scatter(X[:, 0], X[:, 1], c=y, cmap="viridis")  # Turquoise
plt.show()

plt.scatter(X[:, 0], X[:, 1], c=y, cmap="magma")  # Fuchsia
plt.show()

plt.title('Spiral dataset')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
