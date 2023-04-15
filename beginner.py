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
        pass

    def show_as_image(self):
        pass

    def filled_contour(self):
        pass

    def pie(self):
        pass

    def hist(self):
        pass

    def error_bar(self):
        pass

    def box_plot(self):
        pass
