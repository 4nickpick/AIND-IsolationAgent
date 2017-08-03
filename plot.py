import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

N = 7
ab_improved_means = [
    [.9, .6, 1., .6, .5, .5, .5],
    [.9, .7, .9, .6, .5, .6, .5],
    [1., .8, .9, .7, .5, .6, .4]
]
ab_improved_means = [(a + b + c) / 3 for a, b, c in zip(ab_improved_means[0], ab_improved_means[1], ab_improved_means[2])]

print(ab_improved_means)

ind = np.arange(N)  # the x locations for the groups
width = 0.2       # the width of the bars

rects1 = ax.bar(ind, ab_improved_means, width, color='b')

ab_custom_means = [
    [1., .8, .7, .8, .5, .8, .5],
    [.8, .7, .8, .9, .5, .7, .6],
    (1., .8, .9, .8, .5, .7, .5)
]
ab_custom_means = [(a + b + c) / 3 for a, b, c in zip(ab_custom_means[0], ab_custom_means[1], ab_custom_means[2])]
rects2 = ax.bar(ind + width, ab_custom_means, width, color='g')

ab_custom_2_means = [
    [.9, .8, 1., .7, .5, .4, .5],
    [.9, .7, .8, .8, .5, .4, .4],
    [1., 1., 1., .8, .4, .4, .4]
]
ab_custom_2_means = [(a + b + c) / 3 for a, b, c in zip(ab_custom_2_means[0], ab_custom_2_means[1], ab_custom_2_means[2])]
rects3 = ax.bar(ind + (width * 2), ab_custom_2_means, width, color='r')

ab_custom_3_means = [
    [.8, .8, 1., .8, .6, .6, .5],
    [1., .7, .7, .6, .6, .4, .4],
    [1., .7, .9, .7, .5, .5, .5]
]
ab_custom_3_means = [(a + b + c) / 3 for a, b, c in zip(ab_custom_3_means[0], ab_custom_3_means[1], ab_custom_3_means[2])]
rects4 = ax.bar(ind + (width * 3), ab_custom_3_means, width, color='y')


# add some text for labels, title and axes ticks
ax.set_ylabel('Average Wins/Losses by Student Agent')
ax.set_xlabel('Algorithm used by Opponent')
ax.set_ylim(bottom=.3, top=1.2)
ax.set_title('Knight Isolation Heuristic Analyses - Nick Pickering')
ax.set_xticks(ind + width * 1.5)
ax.set_xticklabels(('Random', 'MM_Open', 'MM_Center', 'MM_Improved', 'AB_Open', 'AB_Center', 'AB_Improved'))

ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('AB_Improved', 'AB_Custom', 'AB_Custom_2', 'AB_Custom_3'),
          title="Algorithm used by Student Agent")


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.2f' % float(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

plt.show()
