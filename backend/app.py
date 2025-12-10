from flask import Flask, request, jsonify
from solver.bfs import solveBFS
from solver.dfs import solveDFS
from solver.common import exist
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route("/solve", methods=["POST"])
def preprocess():
    data = request.get_json()
    start = tuple(data["start"])
    end = tuple(data["end"])
    grid = tuple(data["map"])

    if data["algorithm"] == "BFS":
        x = solveBFS(grid, start, end)
    else:
        x = solveDFS(grid, start, end)
    return jsonify(x)


app.run(port=5000)
