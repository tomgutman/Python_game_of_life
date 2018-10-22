#! usr/bin/env python3

#importing all the requiered modules from python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML, display
import ipywidgets as widgets
import gol_module as gol

def update_widget_result():
    ''' This function put in different variables all the outcomes from
        the widgets shown to define the parameters of the game of life.
    '''
    if gol.widget_pattern1.result != None:
        size = gol.widget_grid_size.result                             #size contains the size of the numpy array
        generation = gol.widget_generation.result                      #generation contains the number of generation chosen by the player

        coord_pattern1 = gol.widget_coord_pattern1.result              #those next variables are the pattern and the positions extracted from the ipywidgets.
        pattern1 = gol.widget_pattern1.result
        coord_i1 = int(coord_pattern1[0])
        coord_j1 = int(coord_pattern1[1])

        coord_pattern2 = gol.widget_coord_pattern2.result
        pattern2 = gol.widget_pattern2.result
        coord_i2 = int(coord_pattern2[0])
        coord_j2 = int(coord_pattern2[1])

        coord_pattern3 = gol.widget_coord_pattern3.result
        pattern3 = gol.widget_pattern3.result
        coord_i3 = int(coord_pattern3[0])
        coord_j3 = int(coord_pattern3[1])

        grid = gol.grid_size(size)                                     # the grid variable now contains a numpy array filled with zeros with the selected size
        grid = gol.init_pattern(grid, pattern1, coord_i1, coord_j1)    # grid now contains the selected patterns at the selected positions
        grid = gol.init_pattern(grid, pattern2, coord_i2, coord_j2)
        grid = gol.init_pattern(grid, pattern3, coord_i3, coord_j3)

        return grid, size, generation

def update_animation(grid, size, generation):
    '''this function is to set up the parameters for the animation by
       the submodule animation from matplotlib

    arguments:
    ----------
    *grid: correspond to the numpy array with the patterns
    *size: correspond to size of the grid
    *generation: correspond to the number of generations selected by the player
    '''

    count = [0]
    list_of_matrices = [grid]                                          #This list contains the first initail grid for now
    fig = plt.figure()                                               #The canvas for the aniamtion
    im = plt.imshow(grid, cmap="gray_r", animated=True)                  # imshow is used to display the grid with the lines and the axes
    plt.grid(axis='both', color='k', linestyle='-', linewidth=2)
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, size, 1))                           # This axes parameters are very important so the lines are not crossing the cells in the center
    ax.set_yticks(np.arange(-.5, size, 1))
    plt.tick_params(
        bottom=False,       # ticks along the bottom edge are off
        left=False,         # ticks along the top edge are off
        labelbottom=False,  # labels along the bottom edge are off
        labelleft=False)    # labels along the left edge are off

    count_text = ax.text(0, -1, '')                                  # a counter for the generation that will be displayed in the animation

    for i in range(generation):                                     #for loop with the number of generation to apply the rules of the game and create next generation grid
        grid = gol.Rule_of_life(grid)                                  #and add the new grid to the list containing all the previous grids. Also add the number of the generation
        grid = gol.evolve(grid)                                        #to the counter
        list_of_matrices.append(grid)
        count.append(i)

    def init():
        """initialize animation"""
        count_text.set_text('')                                      #at each new frame, the counter is replaces by blank to avoid superposition of the text.
        return count_text,

    def updatefig(j):
        ''' this function update the figure for each frame of the animation

        arguments:
        ----------
        *j: linked to the updated frame. The rank of the frame to display '''
        im.set_array(list_of_matrices[j])                            # set the correct array at the correct frame
        count_text.set_text("n={}".format(j))                        # set the correct generation count at the correct frame
        return im,

    anim = animation.FuncAnimation(fig, updatefig, init_func=init, interval=500, frames=len(list_of_matrices), blit=True, repeat=True) # create the animation and store it in the variable anim
    anim.save('gol.gif', fps=60, writer='imagemagick')                                                                             # to save the animation as a gif
    HTML(anim.to_html5_video())                                                                                                    # to display the animation in jupyter
    plt.rc('animation', html='html5')                                                                                              # to get rid of the HTML module and just type anim to display
    anim                                                                                                                           # the animation

    return anim
