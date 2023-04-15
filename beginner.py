import numpy as np
import matplotlib.pyplot as plt


class Beginner:
    def __init__(self):
        self.ax = None
        self.fig = None
        self.X = None
        self.Y = None
        self.Z = None

    def prepare(self):
        self.X = np.linspace(0, 4 * np.pi, 1000)
        self.Y = np.sin(self.X)

    def render(self):
        self.fig, self.ax = plt.subplots()
        self.ax.clear()
        self.ax.plot(self.X, self.Y)
        self.fig.show()

    def scatter(self):
        self.X = np.random.uniform(0, 1, 100)
        self.Y = np.random.uniform(0, 1, 100)
        self.ax.clear()
        self.ax.scatter(self.X, self.Y)
        self.fig.show()

    def bar(self):
        self.X = np.arange(10)
        self.Y = np.random.uniform(1, 10, 10)
        self.ax.clear()
        self.ax.bar(self.X, self.Y)
        self.fig.show()

    def show_as_image(self):
        self.Z = np.random.uniform(0, 1, (8, 8))
        self.ax.clear()
        self.ax.imshow(self.Z)
        self.fig.show()

    def filled_contour(self):
        self.Z = np.random.uniform(0, 1, (8, 8))
        self.ax.clear()
        self.ax.contourf(self.Z)
        self.fig.show()

    def pie(self):
        self.Z = np.random.uniform(0, 1, 4)
        self.ax.clear()
        self.ax.pie(self.Z)
        self.fig.show()

    def hist(self):
        generator = np.random.default_rng()
        self.Z = generator.normal(0, 5, 100)
        self.ax.clear()
        self.ax.hist(self.Z)
        self.fig.show()

    def error_bar(self):
        self.ax.clear()
        self.fig.show()

    def box_plot(self):
        self.ax.clear()
        self.fig.show()
