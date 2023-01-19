"""
This module contains the GUI for the visualiser.

The GUI contains:
    - A menu bar with 2 dropdowns: Controls and Algorithms
    - A canvas to contain the visualisation
    - An info bar to display information about the algorithm
    - Keyboard shortcuts to control the visualisation

The GUI is built using PyQt6.
"""

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QActionGroup, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar


class Visualiser(QMainWindow):
    """
    The main window for the visualiser.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sorting Visualiser")
        self.setFixedSize(1000, 600)

        menu_bar = self.menuBar()
        menu_bar.addMenu(self.create_control_menu(menu_bar))
        menu_bar.addMenu(self.create_algorithm_menu(menu_bar))
        self.setMenuBar(menu_bar)

    def create_control_menu(self, menu_bar: QMenuBar) -> QMenu:
        """Create the control menu"""
        controls_menu = QMenu("&Controls", menu_bar)
        controls_menu.setToolTipsVisible(True)

        actions = [
            ("&Sort", "Space", "Sort the array"),
            ("&Reset", "Ctrl+R", "Reset the array"),
            ("&Exit", "Ctrl+Q", "Exit the application")
        ]
        for text, shortcut, tooltip in actions:
            action = QAction(QIcon(), text, controls_menu)
            action.setShortcut(shortcut)
            action.setShortcutVisibleInContextMenu(True)
            action.setToolTip(tooltip)
            controls_menu.addAction(action)

        controls_menu.addSeparator()

        array_type_menu = QMenu("&Array Type", controls_menu)
        type_group = QActionGroup(array_type_menu)
        types = ["&Random", "Random &Unique", "&Nearly Sorted", "&Sorted"]
        for type_ in types:
            action = QAction(type_, type_group)
            action.setCheckable(True)
            type_group.addAction(action)
        type_group.actions()[0].setChecked(True)
        array_type_menu.addActions(type_group.actions())
        controls_menu.addMenu(array_type_menu)

        sort_direction_menu = QMenu("Sort &Direction", controls_menu)
        direction_group = QActionGroup(sort_direction_menu)
        directions = ["&Ascending", "&Descending"]
        for direction in directions:
            action = QAction(direction, direction_group)
            action.setCheckable(True)
            direction_group.addAction(action)
        direction_group.actions()[0].setChecked(True)
        sort_direction_menu.addActions(direction_group.actions())
        controls_menu.addMenu(sort_direction_menu)

        sort_speed_menu = QMenu("Sort &Speed", controls_menu)
        speed_group = QActionGroup(sort_speed_menu)
        speeds = ["&Slow", "&Medium", "&Fast"]
        for speed in speeds:
            action = QAction(speed, speed_group)
            action.setCheckable(True)
            speed_group.addAction(action)
        speed_group.actions()[1].setChecked(True)
        sort_speed_menu.addActions(speed_group.actions())
        controls_menu.addMenu(sort_speed_menu)

        return controls_menu

    def create_algorithm_menu(self, menu_bar: QMenuBar) -> QMenu:
        """Create the algorithm menu"""
        algorithms_menu = QMenu("&Algorithms", menu_bar)

        algorithms = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort",
                      "Quicksort", "Heapsort", "Radix Sort", "Counting Sort", "Shellsort",
                      "TimSort"
                      ]
        algorithm_group = QActionGroup(algorithms_menu)
        for algorithm in algorithms:
            action = QAction(algorithm, algorithm_group)
            action.setCheckable(True)
            algorithm_group.addAction(action)
        algorithm_group.actions()[0].setChecked(True)
        algorithms_menu.addActions(algorithm_group.actions())

        return algorithms_menu


def main():
    """Main function to run the GUI"""
    app = QApplication(sys.argv)

    window = Visualiser()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
