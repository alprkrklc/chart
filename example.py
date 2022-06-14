from employee import Employee
from axes import XAxis, YAxis
from chart import Chart

def main():
    # Creates random employees.
    employees = [Employee.create_random() for _ in range(25)]

    names = []
    performances = []
    salaries = []

    # Fetches names, performances and salaries to separate lists.
    for employee in employees:
        names.append(employee.name)
        performances.append(employee.performance)
        salaries.append(employee.salary)

    # x axis for bottom side of the chart.
    x = XAxis(data=names, label='Names')
    # y axis for left side of the chart. (First axis going to be a bar chart. color argument is optional)
    y = YAxis(data=performances, label='Performances', color='tab:blue')
    # y2 axis for right side of the chart. (Second axis going to be a plot chart. limits and marker arguments are optional)
    y2 = YAxis(data=salaries, label='Salaries', limits=(0, 12_000), marker='o')

    # Creates a chart object. At least one x_axis and one y_axis is required. The rest is optional.
    chart = Chart(
        x_axis = x,
        y_axis = y,
        y_axis2 = y2,
        
        title = 'Employee Performance/Salary Chart',
        # It's going to be a 1500x800 px chart.
        size = (15, 8),
    )

    # Displays the chart.
    chart.show()

    # Saves the chart.
    # chart.save('chart.jpg')

if __name__ == '__main__':
    main()
