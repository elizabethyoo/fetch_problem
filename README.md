# fetch_problem
This application calculates pixel coordinate values for an image that is to be displayed on a two dimensional surface given the dimensions and the corner points. 

For example, if an image is defined by a 3x3 grid of pixel values, and the (x, y) coordinates of the four corner points are: (1, 1), (3, 1), (1, 3), and (3, 3), then the application calculates and returns the nine coordinates that are evenly spaced within the corner points : (1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (3, 1), (3, 2), (3, 3). 


# to build 
To build the application run the following command:
```$ docker-compose build fetch_problem```


# to run 
To run the application run the following command: 
```$ docker-compose up fetch_problem```


# to call
This application takes in a JSON POST request specifying the four corner coordinates ("corners") and number or rows and columns ("dims").
```$ curl --header "Content-Type: application/json" \
	--request POST \
	--data '{"corners": [[1, 1], [3, 1], [1, 3], [3, 3]], "dims": [3, 3]}' \
	localhost:5000/get_evenly_spaced_coords
```