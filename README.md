# Simulating the Conway's game of life using jupyter

This project involves simulating the Conway's game of life using a Jupyter notebook. In this project, matplotlib submodule animation was used to animate this cell automate game. Moreover ipywidgets module was also used to make the selection of the parameters more interactive.  

__Authors__:  Tom Gutman,Saida Hajjou

__Date__ = "2018/09" 

Release note:
=============
    *  Used Programme: Python3 and jupyter lab or notebook
    *  Packages      : numpy, matplotlib.animation, ipywidgets, gol_module,gol_execute 
    
## Requirements:

You need to have anaconda and / or jupyter notebook installed on your machine. 
If you are on a PC machine, you will also need to follow this tutorial to enable the animation: [link](https://www.wikihow.com/Install-FFmpeg-on-Windows). Also make sure, ipywidgets module is installed to benefit the nice user interface.
with the conda environnment provided by P.Poulain, the script and the animation works fine. 

## Use: 

Download the repository, 3 files are needed to run the Game of Life : 
* the GOL_notebook.ipynb : a jupyter notebook containing the main functions. You will play the game from this notebook and choose the parameters
* gol_module.py : a python3 module containing the function I created
* gol_execute.py : another python3 module containing the behind the scenes for the animation.

Open your jupyter notebook and from there open the GOL_notebook.ipynb file. Simply run cell by cell the notebook. After running the first cell (which can take around 30s), choose the parameters and the patterns you want to display for the game of life. Once it's done, run the second cell just below (it can also take several seconds). Normally, the animation should appear and a gol.gif file should have been added to your folder with the corresponding gif. 

If you have the message "MovieWriter imagemagick unavailable.". It can happend. Check your folder to see if you still have the gif. This is a reported bug. 
 





