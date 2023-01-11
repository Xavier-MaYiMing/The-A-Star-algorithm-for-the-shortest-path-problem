#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 8:35
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : A_Star.py
# @Statement : The A* algorithm for the shortest path problem
# @Reference: Hart P E, Nilsson N J, Raphael B. A formal basis for the heuristic determination of minimum cost paths[J]. IEEE Transactions on Systems Science and Cybernetics, 1968, 4(2): 100-107.
import math


def heuristic(node, destination):
    """
    Calculate the heuristic destination between node and destination (Manhattan distance)
    :param node:
    :param destination:
    :return:
    """
    return abs(node[0] - destination[0]) + abs(node[1] - destination[1])


def find_neighbors(network, node, dim1, dim2):
    # Find the neighbors of node
    neighbors = []
    if node[0] - 1 >= 0 and network[node[0] - 1][node[1]] == 1:
        neighbors.append([node[0] - 1, node[1]])
    if node[0] + 1 < dim1 and network[node[0] + 1][node[1]] == 1:
        neighbors.append([node[0] + 1, node[1]])
    if node[1] - 1 >= 0 and network[node[0]][node[1] - 1] == 1:
        neighbors.append([node[0], node[1] - 1])
    if node[1] + 1 < dim2 and network[node[0]][node[1] + 1] == 1:
        neighbors.append([node[0], node[1] + 1])
    return neighbors


def cal_dis(node1, node2):
    # Calculate the distance between node1 and node2
    return math.sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2)


def main(network, source, destination):
    """
    The main function of the A*
    :param network: A two-dimensional array, in which 0 denotes the obstacle, and 1 denotes that the node is accessible
    :param source: The source node
    :param destination: The destination node
    :return:
    """
    # Step 1. Initialization
    dim1 = len(network)
    dim2 = len(network[0])
    open_list = []
    closed_list = []
    f_list = []
    g_list = []
    path_list = []
    open_list.append(source)
    temp_h = heuristic(source, destination)
    f_list.append(temp_h)
    g_list.append(0)
    path_list.append([source])

    # Step 2. The main loop
    while open_list:

        # Step 2.1. Pop the node in the open_list with the minimum f (f=g+h) value
        ind = f_list.index(min(f_list))
        node = open_list.pop(ind)
        f_list.pop(ind)
        g = g_list.pop(ind)
        path = path_list.pop(ind)
        closed_list.append(node)

        # Step 2.2. Termination judgment
        if node == destination:
            return {'path': path, 'length': g}

        # Step 2.3. Extend to the eight surrounding nodes
        neighbors = find_neighbors(network, node, dim1, dim2)
        for temp_node in neighbors:
            if temp_node in closed_list:
                continue
            elif temp_node in open_list:
                ind = open_list.index(temp_node)
                temp_g = g + cal_dis(node, temp_node)
                if temp_g < g_list[ind]:
                    temp_path = path.copy()
                    temp_path.append(temp_node)
                    f_list[ind] = temp_g + heuristic(temp_node, destination)
                    g_list[ind] = temp_g
                    path_list[ind] = temp_path
            else:
                open_list.append(temp_node)
                temp_path = path.copy()
                temp_path.append(temp_node)
                temp_g = g + cal_dis(node, temp_node)
                temp_h = heuristic(temp_node, destination)
                f_list.append(temp_g + temp_h)
                g_list.append(temp_g)
                path_list.append(temp_path)

    # Step 3. Sort the results
    return {}


if __name__ == '__main__':
    # Example
    test_network = [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1],
    ]
    s = [0, 0]
    d = [2, 6]
    print(main(test_network, s, d))
