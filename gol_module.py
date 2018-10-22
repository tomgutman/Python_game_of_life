#! usr/bin/env python3

import numpy as np  
import ipywidgets as widgets

#Fonction qui créer une matrice carré N*N
def grid_size(N):
    '''This function creates a N*N numpy array filled with zeros

    arguments:
    ----------
    *N: size of the numpy array you want'''
    grid = np.zeros((N, N))
    return grid

def init_pattern(matrix, pattern, i, j):
    '''This function adds specific patterns in a numpy array. The top left cell
       has (i,j) coordinates

    arguments:
    ----------
    * matrix: a np array of size N usually defined with grid_size(N) function
    * pattern: a specific pattern of various size to initiate the game of life.
               approximately 12 patterns have been implemented in this function
    * i: ligne of the np array where you want to add the pattern
    * j: column of the np array where you want to add the pattern'''
    if pattern == 'None':
        pass
    if pattern == 'block (2, 2)':
        block = np.array([[1, 1],
                          [1, 1]])
        matrix[i: i+2, j:j+2] = block
    if pattern == 'hive (3, 4)':
        hive = np.array([[[0, 1, 1, 0],
                          [1, 0, 0, 1],
                          [0, 1, 1, 0]]])
        matrix[i: i+3, j:j+4] = hive
    if pattern == 'blinker (3, 1) n = 2':
        blinker = np.array([1, 1, 1])
        matrix[i: i+3, j] = blinker
    if pattern == 'line (1, 5) n = 10':
        line = np.array([1, 1, 1, 1, 1])
        matrix[i, j: j+5] = line
    if pattern == 'spaceships (3, 4)':
        spaceships = np.array([[[1, 0, 0, 0],
                                [1, 1, 1, 0],
                                [0, 0, 1, 1]]])
        matrix[i: i+3, j: j+4] = spaceships
    if pattern == 'LWSS':
        LWSS = np.array([[[0, 1, 0, 0, 1],
                          [1, 0, 0, 0, 0],
                          [1, 0, 0, 0, 1],
                          [1, 1, 1, 1, 0]]])
        matrix[i: i+4, j: j+5] = LWSS
    if pattern == 'glider':
        glider = np.array([[[1, 1, 1],
                            [1, 0, 0],
                            [0, 1, 0]]])
        matrix[i: i+3, j: j+3] = glider
    if pattern == 'toad (2, 4) n = 2':
        toad = np.array([[[0, 1, 1, 1],
                          [1, 1, 1, 0]]])
        matrix[i: i+2, j: j+4] = toad
    if pattern == 'loaf (4, 4)':
        loaf = np.array([[[0, 1, 1, 0],
                          [1, 0, 0, 1],
                          [1, 0, 1, 0],
                          [0, 1, 0, 0]]])
        matrix[i: i+4, j: j+4] = loaf
    if pattern == 'ship (3, 3)':
        ship = np.array([[[1, 1, 0],
                          [1, 0, 1],
                          [0, 1, 1]]])
        matrix[i: i+3, j: j+3] = ship
    if pattern == 'cloverleaf':
        cloverleaf = np.array([[[0, 0, 0, 1, 0, 1, 0, 0, 0],
                                [0, 1, 1, 1, 0, 1, 1, 1, 0],
                                [1, 0, 0, 0, 1, 0, 0, 0, 1],
                                [1, 0, 1, 0, 0, 0, 1, 0, 1],
                                [0, 1, 1, 0, 1, 0, 1, 1, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 1, 0, 1, 0, 1, 1, 0],
                                [1, 0, 1, 0, 0, 0, 1, 0, 1],
                                [1, 0, 0, 0, 1, 0, 0, 0, 1],
                                [0, 1, 1, 1, 0, 1, 1, 1, 0],
                                [0, 0, 0, 1, 0, 1, 0, 0, 0]]])
        matrix[i: i+11, j: j+9] = cloverleaf
    if pattern == 'canoe (5, 5)':
        canoe = np.array([[[0, 0, 0, 1, 1], [0, 0, 0, 0, 1],
                           [0, 0, 0, 1, 0], [1, 0, 1, 0, 0],
                           [1, 1, 0, 0, 0]]])
        matrix[i: i+5, j: j+5] = canoe
    if pattern == 'random':
        random = np.random.randint(2, size=(len(matrix[:, 0]),
                                            len(matrix[:, 0])))
        matrix[i: i+len(matrix[:, 0]), j: j+len(matrix[:, 0])] = random
    if pattern == 'beehive (3, 2)':
        beehive = np.array([[[0, 1], [1, 0], [0, 1]]])
        matrix[i: i+3, j: j+2] = beehive (3, 2)
    if pattern == 'snake':
        snake = np.array([[[1, 1, 0, 1], [1, 0, 1, 1]]])
        matrix[i: i+2, j: j+4] = snake
    if pattern == 'L':
        L = np.array([[[1, 0], [1, 0], [1, 0], [1, 1]]])
        matrix[i: i+4, j: j+2] = L
    if pattern == 'ruche':
        ruche = np.array([[[0, 1, 1], [1, 0, 1],
                           [1, 0, 1], [0, 1, 0]]])
        matrix[i: i+4, j: j+3] = ruche
    if pattern == 'stairs':
        stairs = np.array([[[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 0]]])
        matrix[i: i+3, j: j+4] = stairs
    if pattern == 'gliders (3, 3) n = 1103':
        gliders = np.array([[[0, 1, 1], [1, 1, 0], [0, 1, 0]]])
        matrix[i: i+3, j: j+3] = gliders (3, 3) n = 1103
    if pattern == 'glider (3, 3) n = inf':
        glider = np.array([[[0, 1, 1], [1, 0, 1], [0, 0, 1]]])
        matrix[i: i+3, j: j+3] = glider (3, 3) n = inf
    if pattern == 'pulsar (5, 5) n = 3':
        pulsar = np.array([[[1, 0, 1, 0, 1], [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1], [1, 0, 0, 0, 1],
                            [1, 0, 1, 0, 1]]])
        matrix[i: i+5, j: j+5] = pulsar (5, 5) n = 3
    if pattern == 'pentadecathlon (1, 10) n = 15':
        panthadecathlon = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        matrix[i, j: j+10] = pentadecathlon (1, 10) n = 15
    if pattern == 'gosper glider gun (9, 36) n>=30':
        gosper_glider_gun = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                                      [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                      [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        matrix[i: i+9, j: j+36] = gosper glider gun (9, 36) n>=30
    return matrix

LIBRARY = ['None',
           '##Statics##',
           'block (2, 2)', 'hive (3, 4)', 'beehive (3, 2)', 'ship (3, 3)',
           'canoe (5, 5)', 'loaf (4, 4)',                        # list containing all the patterns implemented with
           '##Oscillators##',
           'blinker (3, 1) n = 2', 'toad (2, 4) n = 2', 'line (1, 5) n = 10',
           'pulsar (5, 5) n = 3', 'pentadecathlon (1, 10) n = 15', # the size of the pattern (x,x) and the recommanded number
           '##Spaceships##',
           'glider (3, 3) n = inf', 'gliders (3, 3) n = 1103', 
           'spaceships (3, 4)', 'gosper glider gun (9, 36) n>=30', 'random',
           'cloverleaf','snake','L','ruche','stairs']       # of generation to see the full evolution of it n=xxx

def Rule_of_life(matrix):
    '''This function was taken from the youtuber 'Sciences Etonnantes'
       and give the rules of the game of life. To do so, the function first
       creates an empty array of the wanted size. Then it calculates for each
       cell the sum of all the adjacent cells by creating 8 smaller arrays
       shifted by one or two cells. This way, in the new array, each cell
       contain the number of adjacent living cells. Then the rules of the game
       are applied using logical function returning booleans.
       The mat_bool array contains booleans for each cell.

    arguments:
    ----------
    *matrix: the previously created numpy array
    '''
    mat_bool = np.zeros(matrix.shape)

    mat_bool[1: -1, 1: -1] = (matrix[: -2, : -2]  + matrix[: -2, 1: -1] + matrix[: -2, 2: ] +     # This part of the functin sums for each position the number of adjacent cells
                              matrix[1: -1, : -2] +                matrix[1: -1, 2: ]  +
                              matrix[2:, : -2]   + matrix[2:, 1: -1]  + matrix[2:, 2: ])

    mat_bool = np.logical_or(mat_bool == 3, np.logical_and(matrix == 1, mat_bool == 2))         # This part applies the rules of the game of life with logical function

    return mat_bool

def evolve(mat_bool):
    '''This function transforms the mat_bool numpy array in a new numpy array
       containing 0 and 1 instead of booleans

    arguments:
    ----------
    * mat_bool: the previously created numpy array containg booleans to
      determine the state (dead/alive) of each cell.
    '''
    mat = np.zeros(mat_bool.shape)
    for i in range(len(mat_bool[:, 1]-1)):
        for j in range(len(mat_bool[:, 1]-1)):
            if mat_bool[i, j] == True:
                mat[i, j] += 1
            else:
                mat[i, j] += 0
    return mat

#Basic and empty functions used for the creation of widgets with the module ipywidgets
def coord_pattern1(i, j):
    return i, j
def coord_pattern2(k, l):
    return k, l
def coord_pattern3(m, n):
    return m, n
def f(x):
    return x

#This part is for the creation of interactive widgets with the pyton module ipywidgets.

bibli = LIBRARY
list_line = list(range(100))
list_col = list_line

#Creating the actuals widgets for the grid size, the number of generation,
#the selection of at most 3 ,different patterns with their
#localization on the grid
Grille = widgets.IntSlider(min=0, max=150, step=1, disabled=False, description='Grille')
Generation = widgets.IntSlider(min=0, max=150, step=1, description='Generation')
patterns1 = widgets.Dropdown(options=bibli, description='pattern: ')
patterns2 = widgets.Dropdown(options=bibli, description='pattern: ')
patterns3 = widgets.Dropdown(options=bibli, description='pattern: ')
coord_line1 = widgets.Dropdown(options=list_line, description='coord_ligne')
coord_col1 = widgets.Dropdown(options=list_col, description='coord_colonne')
coord_line2 = widgets.Dropdown(options=list_line, description='coord_ligne')
coord_col2 = widgets.Dropdown(options=list_col, description='coord_colonne')
coord_line3 = widgets.Dropdown(options=list_line, description='coord_ligne')
coord_col3 = widgets.Dropdown(options=list_col, description='coord_colonne')

#Making the widgets interactive, so i can extract the info from them
widget_generation = widgets.interactive(f, x=Generation)
widget_grid_size = widgets.interactive(f, x=Grille)
widget_coord_pattern1 = widgets.interactive(coord_pattern1, i=coord_line1, j=coord_col1)
widget_coord_pattern2 = widgets.interactive(coord_pattern2, k=coord_line2, l=coord_col2)
widget_coord_pattern3 = widgets.interactive(coord_pattern3, m=coord_line3, n=coord_col3)
widget_pattern1 = widgets.interactive(f, x=patterns1)
widget_pattern2 = widgets.interactive(f, x=patterns2)
widget_pattern3 = widgets.interactive(f, x=patterns3)

#displaying in jupyter the widgets
def show_widgets():
    ''' This function show all the widgets at once in this order.'''
    display(widget_grid_size,
            widget_generation,
            widget_pattern1,
            widget_coord_pattern1,
            widget_pattern2,
            widget_coord_pattern2,
            widget_pattern3,
            widget_coord_pattern3)
