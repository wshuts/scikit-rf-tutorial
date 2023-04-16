import numpy as np
import matplotlib.pyplot as plt


class Beginner:
    def __init__(self):
        self.generator = np.random.default_rng()
        self.fig, self.ax = plt.subplots()
        self.X = None
        self.Y = None
        self.Z = None

    def prepare(self):
        self.X = np.linspace(0, 4 * np.pi, 1000)
        self.Y = np.sin(self.X)

    def render(self):
        self.ax.clear()
        self.ax.plot(self.X, self.Y)
        self.fig.show()

    def scatter(self):
        self.X = self.generator.uniform(0, 1, 100)
        self.Y = self.generator.uniform(0, 1, 100)
        self.ax.clear()
        self.ax.scatter(self.X, self.Y)
        self.fig.show()

    def bar(self):
        self.X = np.arange(10)
        self.Y = self.generator.uniform(1, 10, 10)
        self.ax.clear()
        self.ax.bar(self.X, self.Y)
        self.fig.show()

    def show_as_image(self):
        self.Z = self.generator.uniform(0, 1, (8, 8))
        self.ax.clear()
        self.ax.imshow(self.Z)
        self.fig.show()

    def filled_contour(self):
        self.Z = self.generator.uniform(0, 1, (8, 8))
        self.ax.clear()
        self.ax.contourf(self.Z)
        self.fig.show()

    def pie(self):
        self.Z = self.generator.uniform(0, 1, 4)
        self.ax.clear()
        self.ax.pie(self.Z)
        self.fig.show()

    def hist(self):
        self.Z = self.generator.normal(0, 5, 100)
        self.ax.clear()
        self.ax.hist(self.Z)
        self.fig.show()

    def error_bar(self):
        self.X = np.arange(5)
        self.Y = self.generator.uniform(0, 1, 5)
        self.ax.clear()
        self.ax.errorbar(self.X, self.Y, self.Y / 4)
        self.fig.show()

    def box_plot(self):
        self.Z = self.generator.normal(0, 1, (100, 3))
        self.ax.clear()
        self.ax.boxplot(self.Z)
        self.fig.show()
        self.fig.savefig("box_plot.png", dpi=300)
        self.fig.savefig("box_plot.pdf")
