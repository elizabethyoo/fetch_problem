import numpy as np

def get_evenly_spaced_coords(dims, corners): 
    """
    Returns a specified number of evenly spaced coordinates enclosed in corner points. 
        inputs:
            dims: tuple consisting of the number of rows and columns in rectangle
            corners: array of tuples consisting of the x and y coordinates of the corners of the rectangle
        
        outputs:
            grid.tolist(): list consisting of the x and y coordinates of the enclosed points
    """
    # order coordinates in increasing order i.e., x_1 < x_2, y_1 < y_2
    # assume that pixels are real numbers
    x_1, y_1 = np.array(corners).min(axis=0)
    x_2, y_2 = np.array(corners).max(axis=0)
    # for each axis, obtain array of evenly spaced coordinates from start to end points
    x_coords = np.linspace(x_1, x_2, dims[1])
    y_coords = np.linspace(y_1, y_2, dims[0])
    # obtain lattice that is the "2D product" of the above coordinates, reshape dimensions
    grid = np.array(np.meshgrid(x_coords, y_coords)).T.reshape(-1, 2)
    
    return grid.tolist()