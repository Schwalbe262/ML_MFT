import matplotlib.pyplot as plt

def plot_histogram(raw_data, parameter, bins=100, plt_size=[6,5], fontsize={}, grid_en=False, title_en=False, title=""):

    # plt size
    plt.rcParams["figure.figsize"] = (plt_size)

    # font size
    plt.rcParams.update(fontsize)

    # grid enable opt
    if(grid_en == True) :
        plt.grid(True)

    # title enable opt
    if(title_en == True) : 
        if title == "" :
            plt.title(f'{parameter} data distribution')
        else :
            plt.title(title)

    # histogram
    plt.hist(raw_data[parameter], bins=bins)
    plt.show()






