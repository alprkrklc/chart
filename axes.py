from dataclasses import dataclass
import random

colors = [
    'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 
    'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 
    'tab:olive', 'tab:cyan'
]

markers = [
    ".", ",", "o", "v", "^", "<", ">", "1", "2", "3",
    "4", "8", "s", "p", "P", "*", "h", "H", "+", "x",
    "X", "D", "d", "|", "_"
]

@dataclass
class BaseAxis:
    # List of data to shown in the chart.
    data: list
    # Label or title of this particular data.
    label: str

class XAxis(BaseAxis):
    pass

@dataclass
class YAxis(BaseAxis):
    # Color of the chart for this y_axis.
    color: str = None
    # Sets the lower and upper limits of the chart for this y_axis. (0, 100)
    limits: tuple = None
    # Sets the marker type. Available for plot charts only. (y_axis2)
    marker: str = None

    def __post_init__(self):
        # If color is not defined, picks a random color.
        if self.color is None:
            self.color = random.choice(colors)
        
        # If marker is not defined, picks a random marker.
        if self.marker is None:
            self.marker = random.choice(markers)
