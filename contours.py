"""
Take a bunch of points on a plot, and return the contours
of the interpolated function.
"""

import numpy as np
from scipy.interpolate import griddata
from matplotlib import contourf

def get_contours(x,y,z,bounds):
    r"""
    points x and y with values z, with whole shape bounded by 
    a matplotlib.path bounds
    """

    grid_x, grid_y = np.mgrid[1.1*min(x):1.1*max(x):complex(0,10*len(x)j), 
                              1.1*min(y):1.1*max(y):complex(0,10*len(y))]

    grid_z = griddata(zip(x,y), z, (grid_x, grid_y), method='cubic')
    grid_x = grid_x.flatten(); grid_y = grid_y.flatten(); grid_z = grid_z.flatten()
    new_grid_x = []; new_grid_y = []; new_grid_z = []
    for i in xrange(len(grid_x)):
        if bounds.contains_point((grid_x[i], grid_y[i])):
            new_grid_x.append(grid_x[i])
            new_grid_y.append(grid_y[i])
            new_grid_z.append(grid_z[i])

    return contourf(grid_x, grid_y, grid_z)


    
        
