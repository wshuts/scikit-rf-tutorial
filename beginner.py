import numpy as np
import matplotlib.pyplot as plt


class Beginner:
    def __init__(self):
        self.Y = None
        self.X = None

    def prepare(self):
        self.X = np.linspace(0, 4 * np.pi, 1000)
        self.Y = np.sin(self.X)
        return

    def render(self):
        fig, ax = plt.subplots()
        ax.plot(self.X, self.Y)
        fig.show()
        return
