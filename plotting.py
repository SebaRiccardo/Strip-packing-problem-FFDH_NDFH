import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
from utils import max_height

def plot_result(best_fitness,generation_number,folder,type):
    generations_list =np.arange(1,generation_number+1)
    plt.plot(best_fitness)

    plt.xlabel('Generation')
    plt.ylabel("Best fitness")
    # save the figure
    dir = os.getcwd()
    plt.savefig(dir+"\%s\%s.png" % (folder,type), dpi=100, bbox_inches='tight')

    plt.show()

def plot_rectangles(rectangles,stack,best_solution,generation_number,max_strip_width,folder):
    fig = plt.figure()
    fig.suptitle(folder[0:4])
    ax = fig.add_subplot(111)
    figures =[]
    prevIndex = -1

    colors = ["red", "yellow", "green", "blue", "pink", "orange", "gray", "purple", "lightblue", "brown","magenta","cyan"]
    Xaxis = 0
    Yaxis = 0

    for strip in stack:
        Xaxis = 0
        figures =[]
        for i in strip:

            indexColor= np.random.randint(0,len(colors))
            while indexColor == prevIndex:
                  indexColor = np.random.randint(0, len(colors))

            prevIndex = indexColor
            rectangle = matplotlib.patches.Rectangle((Xaxis,Yaxis),rectangles[i].width,rectangles[i].height,edgecolor='black',facecolor=colors[indexColor],linewidth=0.3,alpha =0.4)
            Xaxis = Xaxis+ rectangles[i].width
            ax.add_patch(rectangle)
            rx, ry = rectangle.get_xy()
            cx = rx + rectangle.get_width() / 2.0
            cy = ry + rectangle.get_height() / 2.0
            ax.annotate(i, (cx, cy), color='black', weight='normal', fontsize=10, ha='center', va='center')

        Yaxis +=  max_height(strip,rectangles)

    plt.xlabel("Generation: "+str(generation_number) +" "+ str(best_solution) )
    plt.xlim([0, max_strip_width])
    plt.ylim([0, Yaxis +10])

    dir = os.getcwd()
    # save the figure
   # plt.savefig(dir+"\%s\generation%a.png" % (folder,generation_number), dpi=100, bbox_inches='tight')

    plt.show()