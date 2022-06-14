from matplotlib import pyplot as plt
from dataclasses import dataclass
from axes import XAxis, YAxis

@dataclass
class Chart:
    # Bottom side of the chart.
    x_axis: XAxis
    # Left side of the chart.
    y_axis: YAxis
    # Right side of the chart. (Optional)
    y_axis2: YAxis = None
    
    # Style of the chart.
    style: str = 'seaborn'
    # Gives a sketcy look when True.
    sketchy_look: bool = True
    
    # Shows the title on upper side of the chart.
    title: str = None
    # Size of the chart model. (15, 8) means 1500x800 px.
    size: tuple = None
    # Shows value of each data shown in the chart.
    annotation: bool = True

    def __post_init__(self):
        # Prepares plt and creates fig and ax objects for further processes.
        self.prepare_plt()

        # Sets up charts needed.
        self.set_up_charts()

        # Sets the size of the fig.
        if self.size:
            self.fig.set_size_inches(self.size, forward=True)

        # Sets up the legend.
        self.fig.legend(
            frameon = True,
            loc = 'lower right',
            ).get_frame().set_linewidth(1.2)
        
        # Sets up padding for overflow issues.
        self.fig.tight_layout()
    
    def prepare_plt(self):
        # Clears the current data inside plot.
        plt.clf()

        # Sets the plot style.
        plt.style.use(self.style)

        # Sketchy look.
        if self.sketchy_look:
            plt.xkcd()

        # Gets rid of the current empty figure.
        plt.close()
        
        # Gets fig and axis1.
        self.fig, self.ax1 = plt.subplots()

        # Sets the title.
        plt.title(self.title)

    def set_up_charts(self):
        # Sets up chart for first y axis.
        self.set_up_chart(self.ax1, self.y_axis)

        # Checks if there is a second y axis.
        if self.y_axis2 is not None:
            # Creates a twinx of first axis.
            self.ax2 = self.ax1.twinx()
            # Sets it up as a plot chart.
            self.set_up_chart(self.ax2, self.y_axis2, plot=True)
        
        # Sets the x label.
        self.ax1.set_xlabel(self.x_axis.label)

    def set_up_chart(self, ax, y_axis, plot=False):
        # Creates args and kwargs for chart.
        args = (self.x_axis.data, y_axis.data)
        kwargs = {'label': y_axis.label, 'color': y_axis.color}
        
        # Selects if it's a bar or plot chart and adds additional kwargs.
        chart = ax.bar
        if plot:
            chart = ax.plot
            kwargs['marker'] = y_axis.marker
        
        # Creates the chart selected.
        chart(*args, **kwargs)
        # Changes the appearance of ticks, tick labels, and gridlines.
        ax.tick_params(axis='y', labelcolor=y_axis.color)
        # Sets the y label for axis.
        ax.set_ylabel(y_axis.label)

        # Sets the y limits.
        if y_axis.limits is not None:
            ax.set_ylim(y_axis.limits)
        
        # Sets annotation.
        if self.annotation:
            self.set_annotation(ax, y_axis)
        
        # Rotates xticks by 90 degree so it can fit properly.
        plt.xticks(rotation=90)
    
    def set_annotation(self, ax, y_axis):
        for x, y in zip(self.x_axis.data, y_axis.data):
            ax.annotate(
                str(y),
                xy = (x, y),
                horizontalalignment = 'center',
                verticalalignment = 'bottom',
                fontsize = 10
            )

    def show(self):        
        # Displays the figure.
        plt.show()
    
    def save(self, path):
        # Saves the current figure to given path.
        self.fig.savefig(path)
