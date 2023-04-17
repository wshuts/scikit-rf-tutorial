# This is a sample Python script.
# from beginner import Beginner
from introduction import Introduction


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    intro = Introduction()
    # intro.run_networks_demo()

    # beginner = Beginner()
    # beginner.prepare()
    # beginner.render()
    # beginner.scatter()
    # beginner.bar()
    # beginner.show_as_image()
    # beginner.filled_contour()
    # beginner.pie()
    # beginner.hist()
    # beginner.error_bar()
    # beginner.box_plot()
    # intro.run_plotting_demo()

    intro.run_networkset_demo()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
