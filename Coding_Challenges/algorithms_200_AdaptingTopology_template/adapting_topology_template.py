#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml

graph = {
    0: [1],
    1: [0, 2, 3, 4],
    2: [1],
    3: [1],
    4: [1, 5, 7, 8],
    5: [4, 6],
    6: [5, 7],
    7: [4, 6],
    8: [4],
}


def n_swaps(cnot):
    """Count the minimum number of swaps needed to create the equivalent CNOT.

    Args:
        - cnot (qml.Operation): A CNOT gate that needs to be implemented on the hardware
        You can find out the wires on which an operator works by asking for the 'wires' attribute: 'cnot.wires'

    Returns:
        - (int): minimum number of swaps
    """

    # QHACK #
    # https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/
    start = cnot.wires[0]
    goal = cnot.wires[1]
    seen = []
    Q = [[start]]

    while Q:
        path = Q.pop(0)
        vertex = path[-1]

        if vertex not in seen:
            neighbours = graph[vertex]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                Q.append(new_path)

                if neighbour == goal:
                    middles_nodes = len(new_path) - 2  # remove start and goal
                    return middles_nodes * 2  # need to flip before and after
            seen.append(vertex)
    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    output = n_swaps(qml.CNOT(wires=[int(i) for i in inputs]))
    print(f"{output}")
