import numpy as np
import matplotlib.pyplot as plt


class Beginner:
    def __init__(self):
        self.X = None
        self.Y = None
        self.Z = None

    def prepare(self):
        self.X = np.linspace(0, 4 * np.pi, 1000)
        self.Y = np.sin(self.X)
        return

    def render(self):
        fig, ax = plt.subplots()
        ax.plot(self.X, self.Y)
        fig.show()
        return

    def scatter(self):
        pass

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
