import numpy as np
import matplotlib.pyplot as plt
def double_plot(x_list, y1_list, y2_list, x_label, y1_label, y2_label,
                x_label_kwargs = {"fontsize": 14}, 
                y1_fmt = "ro", y1_label_kwargs = {"color": "r", "fontsize": 14},
                y2_fmt = "bo", y2_label_kwargs = {"color": "b", "fontsize": 14}):
    # create figure and axis objects with subplots()
    fig,ax = plt.subplots()
    # make a plot
    ax.plot(x_list, y1_list, y1_fmt)
    # set y-axis label
    ax.set_ylabel(y1_label, **y1_label_kwargs)

    # twin object for two different y-axis on the sample plot
    ax2=ax.twinx()
    # make a plot with different y-axis using second axis object
    ax2.plot(x_list, y2_list, y2_fmt)
    ax2.set_ylabel(y2_label, **y2_label_kwargs)

    # set x-axis label
    ax.set_xlabel(x_label, **x_label_kwargs)
    
    return fig, ax, ax2