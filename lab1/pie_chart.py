from matplotlib import pyplot

labels = ['MAC', 'PC', 'LINUX']
colors = ['#f993f1', '#76d7e0', '#e5ed50']
data = [2, 20, 1]

pyplot.pie(data, labels=labels, colors=colors)

pyplot.axis('equal')

pyplot.show()
