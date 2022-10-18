import numpy 

def get_evenly_spaced_coords(dims, corners): 
    # inputs: 
    # dims: tuple consisting of the number of rows and columns in rectangle
    # corners: array of tuples consisting of the x and y coordinates of the corners of the rectangle
    # order coordinates in increasing order i.e. x_1 < x_2, y_1 < y_2
    # we assume that pixels are real numbers, not restricted to integers
    x_1, y_1 = np.array(corners).min(axis=0)
    x_2, y_2 = np.array(corners).max(axis=0)
    # for each axis, obtain array of evenly spaced coordinates from start to end points
    x_coords = np.linspace(x_1, x_2, dims[1])
    y_coords = np.linspace(y_1, y_2, dims[0])
    # obtain lattice that is the "2D product" of the above coordinates, reshape dimensions
    grid = np.array(np.meshgrid(x_coords, y_coords)).T.reshape(-1, 2)
    return grid

def main():
    dims1 = [3,3]
    corners1 = [(1, 1), (3, 1), (1, 3), (3, 3)]
    output1 = get_evenly_spaced_coords(dims1, corners1)
    print(f"output1: {output1}")

    dims2 = [5,13]
    corners2 = [
    (1.5, 1.5),  # (x, y)
    (4.0, 1.5),  # (x, y)
    (1.5, 8.0),  # (x, y)
    (4.0, 8.0)] 
    output2 = get_evenly_spaced_coords(dims2, corners2)
    print(f"output2: {output2}")

main()