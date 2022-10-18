import json

from flask import Flask, request, jsonify

from backend import get_evenly_spaced_coords
 

app = Flask(__name__)

 
@app.route('/get_evenly_spaced_coords', methods=['POST'])
def get_coords():
    content = request.json
    corners = content['corners']
    dims = content['dims']

    coords = get_evenly_spaced_coords(dims, corners)
    return json.dumps(coords)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)