"""Module to solve the code-kata https://www.codewars.com/kata/biggest-sum/

We define a helper functions:

    bellman_ford():
    uses to helper functions, initialize and relax to find the shortest path

    make_node_matrix():
    to make a matrix holding tuples of node names and values to be inputted
    into a graph

    make_graph_from_matrix():
    convert a matrix into a graph to be inputted into a shortest path algorith
"""

import timeit
from sys import version_info
from collections import OrderedDict

py = version_info[0]

if py < 3:
    from itertools import izip

def initialize(graph, source):
    """Set up each node within the graph where we assume that rest of the nodes
    are very far away."""
    d = {}
    p = {}
    for node in graph:
        d[node] = float('Inf')
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    return d, p


def relax(node, neighbour, graph, d, p):
    """Check if the distance between node and neighbour is lower than the one
    we know of and record if it is."""
    if d[neighbour] > d[node] + graph[node][neighbour]:
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node


def bellman_ford(graph, source):
    """Returns two dictionaries, d and p where d holds all nodes and the cost
    to reach each one and p holds the predecessors which show which path
    to take each node with the lost cost."""
    d, p = initialize(graph, source)
    for u in graph:
        for v in graph[u]:
            relax(u, v, graph, d, p)

    #check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]

    return d, p


def make_node_matrix(matrix):
    """Convert input matrix to matrix of tuples with node name and value to be
    input into function to convert to graph. Values are inverted for input
    into shortest path algorithm."""
    node_names = ['n{0}'.format(p) for p in range(1, len(matrix)**2 + 1)]
    if py < 3:
        nodes = izip(node_names, [ -n for row in matrix for n in row])
    else:
        nodes = zip(node_names, [ -n for row in matrix for n in row])
    node_matrix = []
    for i in range(len(matrix)):
        sub_list = []
        for idx, t in enumerate(nodes):
            sub_list.append(t)
            if idx == len(matrix) - 1:
                break
        node_matrix.append(sub_list)
    return node_matrix


def make_graph_from_matrix(grid):
    """Convert an input matrix of tuples into a graph where we assume the
    direction of traversal in the matrix only allowed to be one to the right
    or down."""
    graph= OrderedDict()
    for row_count, row in enumerate(grid):
        for col, node in enumerate(row):
            vertex = {}
            ref, value = node
            if col == len(row) - 1:
                if row_count == len(grid) - 1:
                    key, value = grid[len(grid) - 1][len(grid) -1]
                    graph[key] = vertex
                    break
                key, value = grid[row_count + 1][col]
                vertex[key] = value
            elif row_count == len(grid) - 1:
                key, value = grid[row_count][col + 1]
                vertex[key] = value
            else:
                vertex.update([grid[row_count][col + 1], grid[row_count + 1][col]])
            graph[ref] = vertex
    return graph


def find_sum(m):
    """Find the highest sum in a matrix from top left to bottom right."""
    node_matrix = make_node_matrix(m)
    graph = make_graph_from_matrix(node_matrix)
    last_node = 'n' + str(len(m) ** 2)
    d, p = bellman_ford(graph, 'n1')
    return abs(d[last_node]) + m[0][0]

m = [[191, 171, 128, 162, 158, 110, 171, 93, 127, 176, 190, 150, 176, 190, 121, 143, 89, 87, 105, 179, 48, 112, 56, 199, 132, 135, 124, 149, 135, 18, 57, 152, 27, 27, 42, 117, 118, 111, 119, 89, 46, 191, 26, 38, 121, 57, 66, 10, 107, 67, 147, 85, 187],
[164, 12, 20, 169, 122, 20, 68, 191, 61, 155, 162, 165, 118, 80, 18, 177, 122, 144, 125, 182, 52, 66, 37, 44, 156, 51, 117, 161, 192, 44, 194, 58, 107, 158, 67, 91, 112, 150, 132, 74, 106, 53, 110, 175, 50, 143, 168, 118, 138, 29, 93, 60, 11],
[128, 148, 142, 124, 171, 137, 28, 47, 135, 38, 89, 73, 44, 62, 139, 127, 103, 85, 188, 63, 114, 51, 20, 35, 124, 139, 33, 139, 104, 93, 140, 114, 22, 61, 12, 175, 186, 20, 80, 18, 136, 143, 108, 133, 167, 171, 200, 187, 140, 68, 185, 72, 174],
[197, 17, 80, 152, 61, 173, 122, 84, 38, 192, 106, 111, 39, 65, 114, 166, 114, 129, 162, 116, 44, 190, 67, 192, 176, 157, 94, 67, 163, 20, 63, 125, 137, 149, 189, 68, 31, 43, 63, 51, 50, 55, 74, 32, 84, 134, 189, 199, 53, 145, 54, 50, 165],
[12, 113, 74, 74, 182, 125, 161, 104, 197, 15, 133, 184, 107, 102, 84, 64, 115, 122, 56, 20, 26, 21, 104, 192, 170, 200, 87, 18, 141, 48, 34, 143, 38, 169, 21, 158, 23, 142, 130, 125, 197, 29, 33, 66, 190, 34, 32, 162, 64, 95, 127, 28, 79],
[96, 28, 104, 89, 82, 200, 171, 132, 123, 51, 145, 134, 70, 82, 129, 52, 198, 67, 150, 200, 12, 57, 35, 51, 54, 192, 165, 114, 70, 85, 86, 42, 22, 144, 167, 156, 141, 190, 100, 63, 26, 103, 161, 20, 54, 110, 181, 153, 177, 129, 72, 159, 35],
[17, 51, 165, 193, 92, 11, 122, 127, 52, 152, 32, 69, 116, 147, 53, 140, 91, 91, 188, 75, 28, 185, 188, 99, 73, 152, 155, 183, 199, 157, 142, 144, 99, 167, 104, 194, 127, 109, 147, 48, 120, 85, 100, 200, 120, 174, 71, 152, 66, 16, 83, 96, 109],
[128, 190, 123, 105, 110, 18, 93, 134, 26, 100, 141, 182, 57, 38, 119, 68, 75, 92, 133, 16, 69, 77, 114, 63, 17, 35, 32, 22, 112, 150, 12, 183, 143, 56, 154, 185, 26, 39, 72, 55, 88, 37, 155, 189, 62, 25, 140, 60, 35, 104, 14, 27, 90],
[163, 153, 16, 141, 82, 27, 160, 162, 110, 83, 43, 74, 35, 37, 200, 68, 26, 11, 22, 84, 199, 43, 68, 67, 77, 98, 29, 92, 197, 149, 175, 176, 130, 51, 200, 54, 78, 17, 159, 26, 37, 85, 183, 56, 83, 46, 74, 159, 101, 174, 161, 44, 151],
[149, 183, 138, 79, 68, 22, 116, 143, 38, 191, 163, 96, 136, 200, 125, 183, 55, 169, 199, 74, 92, 53, 20, 63, 126, 93, 200, 196, 40, 124, 55, 101, 30, 159, 43, 83, 59, 132, 49, 121, 62, 193, 120, 141, 37, 128, 96, 181, 184, 76, 107, 44, 13],
[102, 191, 20, 96, 68, 93, 108, 75, 130, 101, 139, 62, 53, 168, 127, 142, 143, 102, 24, 55, 38, 103, 21, 73, 178, 94, 85, 146, 122, 52, 111, 102, 200, 45, 123, 108, 165, 136, 195, 145, 93, 113, 80, 192, 124, 140, 12, 70, 137, 46, 159, 78, 72],
[86, 151, 11, 128, 32, 75, 79, 183, 64, 100, 144, 129, 126, 28, 76, 78, 68, 179, 151, 101, 90, 102, 105, 36, 172, 138, 160, 73, 102, 43, 76, 119, 40, 15, 47, 90, 128, 98, 91, 38, 64, 19, 12, 26, 149, 162, 97, 200, 194, 51, 140, 37, 70],
[116, 112, 137, 134, 186, 151, 104, 160, 20, 180, 158, 77, 144, 94, 81, 60, 90, 99, 30, 100, 59, 36, 80, 77, 29, 164, 68, 178, 17, 26, 141, 50, 33, 137, 67, 166, 63, 99, 121, 136, 159, 173, 58, 153, 124, 41, 106, 106, 197, 122, 116, 191, 133],
[46, 102, 154, 187, 152, 73, 157, 42, 121, 49, 101, 91, 71, 87, 165, 45, 200, 75, 198, 65, 167, 192, 147, 161, 143, 173, 30, 142, 132, 109, 110, 183, 180, 95, 126, 153, 81, 171, 125, 175, 12, 128, 126, 105, 24, 192, 186, 74, 167, 148, 60, 153, 25],
[189, 44, 83, 94, 180, 112, 148, 12, 168, 26, 190, 57, 123, 51, 183, 65, 11, 39, 46, 198, 164, 168, 192, 14, 42, 148, 96, 161, 20, 65, 190, 164, 117, 51, 120, 179, 24, 44, 118, 102, 77, 50, 198, 76, 123, 35, 42, 31, 146, 66, 33, 76, 99],
[139, 194, 113, 166, 42, 127, 26, 50, 92, 30, 119, 180, 52, 71, 132, 109, 190, 143, 187, 15, 75, 18, 118, 11, 136, 114, 92, 182, 183, 159, 197, 132, 132, 46, 139, 77, 198, 198, 101, 89, 124, 84, 175, 155, 169, 70, 110, 18, 65, 175, 59, 38, 40],
[24, 67, 174, 181, 19, 127, 60, 177, 92, 155, 53, 47, 132, 36, 121, 93, 130, 24, 40, 196, 79, 58, 18, 42, 146, 89, 131, 22, 85, 140, 198, 23, 35, 118, 72, 90, 123, 150, 34, 127, 109, 94, 24, 58, 45, 118, 30, 170, 96, 123, 114, 159, 153],
[10, 126, 114, 86, 29, 52, 184, 146, 164, 62, 125, 158, 35, 24, 198, 99, 88, 55, 63, 71, 151, 179, 42, 52, 99, 185, 73, 18, 162, 185, 174, 23, 121, 110, 182, 26, 37, 166, 128, 80, 100, 197, 130, 52, 52, 46, 185, 21, 11, 145, 79, 62, 188],
[149, 100, 104, 162, 80, 144, 63, 99, 142, 97, 173, 144, 137, 58, 193, 30, 129, 21, 42, 195, 133, 115, 23, 176, 48, 147, 149, 51, 97, 52, 166, 110, 55, 39, 136, 94, 155, 143, 160, 16, 141, 114, 160, 66, 46, 72, 91, 79, 148, 171, 154, 63, 132],
[156, 84, 75, 130, 157, 112, 109, 63, 27, 186, 72, 94, 186, 65, 73, 62, 63, 86, 66, 40, 77, 166, 69, 191, 18, 84, 120, 44, 81, 34, 131, 26, 33, 120, 168, 88, 67, 180, 11, 175, 65, 37, 10, 33, 32, 160, 177, 81, 171, 28, 103, 135, 111],
[114, 189, 17, 150, 155, 198, 154, 135, 139, 197, 131, 19, 15, 89, 35, 122, 177, 25, 152, 27, 135, 55, 113, 93, 72, 133, 131, 62, 80, 119, 120, 108, 117, 153, 168, 197, 146, 95, 112, 163, 124, 177, 185, 184, 23, 195, 169, 184, 120, 154, 129, 50, 86],
[138, 62, 23, 164, 173, 139, 194, 17, 47, 68, 194, 119, 95, 31, 136, 109, 35, 137, 104, 52, 91, 90, 190, 173, 151, 169, 15, 187, 187, 105, 120, 95, 160, 151, 156, 82, 181, 73, 104, 170, 112, 69, 94, 150, 178, 24, 48, 54, 137, 95, 81, 189, 104],
[39, 183, 19, 161, 98, 22, 50, 172, 151, 166, 15, 65, 155, 24, 133, 70, 72, 162, 64, 175, 23, 116, 89, 165, 127, 195, 90, 96, 197, 156, 134, 46, 91, 106, 123, 19, 48, 170, 126, 178, 162, 71, 35, 89, 129, 47, 102, 32, 57, 42, 192, 167, 167],
[20, 77, 82, 40, 165, 165, 117, 40, 73, 26, 108, 97, 82, 112, 132, 72, 180, 111, 85, 108, 175, 71, 166, 91, 116, 39, 48, 194, 29, 154, 123, 157, 62, 88, 90, 148, 190, 200, 121, 115, 174, 84, 160, 106, 38, 185, 37, 77, 124, 133, 59, 182, 83],
[184, 133, 133, 69, 40, 104, 22, 114, 196, 37, 73, 194, 57, 153, 103, 105, 31, 88, 44, 138, 137, 138, 132, 30, 58, 62, 161, 175, 117, 119, 149, 69, 46, 173, 56, 172, 161, 102, 190, 56, 143, 26, 118, 108, 156, 11, 130, 135, 118, 187, 100, 81, 175],
[96, 37, 22, 41, 110, 118, 88, 10, 154, 13, 59, 187, 92, 32, 140, 137, 55, 190, 79, 63, 88, 129, 100, 128, 22, 62, 106, 61, 103, 143, 63, 153, 83, 98, 51, 150, 170, 149, 46, 98, 71, 113, 137, 163, 53, 20, 153, 178, 191, 35, 195, 18, 136],
[79, 124, 29, 199, 55, 94, 157, 133, 178, 133, 29, 182, 89, 129, 171, 15, 126, 44, 13, 140, 129, 35, 186, 13, 155, 153, 197, 147, 157, 65, 165, 79, 47, 49, 117, 114, 153, 31, 94, 21, 14, 92, 188, 197, 131, 197, 33, 140, 35, 151, 193, 87, 94],
[154, 127, 135, 162, 150, 101, 62, 45, 62, 167, 145, 54, 119, 67, 103, 18, 90, 70, 129, 68, 69, 47, 15, 161, 52, 72, 43, 43, 65, 123, 86, 77, 125, 103, 78, 68, 188, 192, 45, 176, 54, 188, 33, 37, 24, 185, 186, 157, 70, 27, 44, 180, 139],
[93, 20, 43, 159, 194, 143, 199, 99, 101, 185, 149, 138, 46, 52, 14, 30, 35, 152, 180, 92, 134, 76, 198, 44, 121, 84, 65, 118, 198, 174, 95, 70, 67, 116, 168, 46, 156, 175, 171, 62, 80, 191, 77, 152, 66, 167, 82, 150, 13, 157, 42, 194, 129],
[196, 133, 158, 48, 33, 195, 192, 185, 134, 33, 134, 35, 195, 64, 155, 133, 98, 85, 193, 126, 20, 19, 133, 99, 13, 155, 151, 72, 10, 106, 67, 74, 174, 100, 89, 118, 19, 179, 131, 183, 39, 185, 48, 25, 97, 158, 189, 49, 52, 173, 121, 34, 135],
[23, 196, 86, 143, 90, 44, 65, 145, 18, 16, 11, 166, 165, 60, 47, 140, 112, 152, 171, 180, 88, 187, 159, 58, 12, 182, 27, 35, 18, 66, 74, 144, 62, 25, 48, 40, 65, 190, 168, 132, 132, 147, 132, 60, 112, 114, 60, 60, 119, 17, 166, 76, 108],
[12, 140, 134, 142, 152, 195, 117, 156, 161, 39, 162, 84, 138, 59, 104, 159, 149, 85, 98, 158, 168, 104, 112, 54, 162, 20, 146, 119, 70, 152, 15, 106, 94, 154, 144, 61, 156, 194, 86, 193, 67, 36, 170, 148, 16, 137, 87, 200, 140, 182, 113, 133, 78],
[133, 182, 83, 86, 193, 195, 11, 78, 98, 198, 175, 148, 72, 10, 105, 61, 156, 189, 107, 85, 196, 170, 91, 117, 58, 85, 105, 83, 71, 113, 36, 161, 64, 144, 170, 62, 120, 153, 56, 92, 70, 182, 11, 66, 66, 134, 14, 177, 141, 39, 174, 90, 107],
[180, 75, 166, 45, 162, 133, 194, 154, 143, 51, 162, 41, 40, 173, 16, 15, 129, 126, 181, 63, 122, 167, 135, 184, 116, 92, 144, 20, 168, 83, 106, 63, 195, 88, 190, 145, 184, 120, 132, 114, 98, 128, 97, 120, 11, 50, 47, 189, 79, 159, 32, 77, 182],
[36, 124, 164, 60, 56, 54, 166, 25, 157, 93, 88, 10, 191, 39, 197, 197, 135, 21, 124, 196, 36, 54, 191, 178, 191, 64, 199, 13, 133, 146, 71, 36, 89, 166, 152, 191, 20, 90, 26, 115, 17, 180, 105, 111, 83, 70, 170, 175, 71, 74, 41, 45, 141],
[66, 164, 142, 10, 142, 174, 71, 154, 143, 68, 115, 100, 17, 10, 28, 82, 55, 45, 26, 185, 81, 92, 153, 76, 23, 73, 172, 169, 110, 159, 181, 191, 17, 99, 160, 142, 176, 66, 92, 71, 125, 78, 131, 46, 195, 49, 58, 148, 92, 10, 104, 135, 30],
[188, 177, 151, 138, 123, 194, 106, 177, 44, 10, 67, 118, 23, 28, 39, 197, 23, 31, 149, 45, 31, 107, 60, 92, 102, 171, 53, 141, 46, 46, 89, 19, 86, 39, 52, 56, 155, 63, 98, 43, 119, 89, 10, 22, 161, 66, 148, 82, 122, 61, 116, 95, 152],
[116, 110, 128, 156, 40, 114, 81, 34, 103, 80, 126, 19, 31, 101, 174, 154, 140, 87, 24, 52, 101, 90, 105, 24, 30, 84, 97, 147, 159, 111, 186, 89, 20, 112, 123, 121, 178, 20, 163, 74, 20, 62, 54, 24, 169, 42, 40, 119, 125, 183, 157, 82, 172],
[172, 176, 100, 186, 179, 147, 195, 163, 102, 196, 18, 177, 89, 122, 166, 131, 99, 153, 48, 141, 145, 137, 79, 11, 111, 100, 159, 114, 19, 171, 153, 154, 22, 197, 145, 145, 66, 76, 164, 79, 116, 149, 112, 67, 29, 28, 28, 155, 190, 163, 168, 178, 67],
[112, 161, 24, 179, 72, 88, 32, 145, 154, 63, 190, 93, 192, 185, 144, 106, 20, 115, 69, 141, 177, 173, 182, 161, 97, 107, 152, 180, 129, 193, 149, 51, 50, 40, 55, 13, 164, 180, 22, 121, 160, 74, 62, 85, 42, 177, 120, 168, 35, 17, 135, 47, 12],
[61, 137, 137, 65, 25, 87, 96, 80, 67, 166, 25, 18, 110, 44, 172, 178, 48, 33, 36, 180, 51, 124, 187, 39, 57, 113, 163, 88, 190, 66, 103, 140, 133, 188, 85, 164, 59, 193, 104, 162, 132, 173, 55, 22, 41, 105, 110, 85, 179, 177, 94, 44, 54],
[66, 30, 184, 124, 143, 23, 105, 181, 187, 186, 66, 50, 10, 101, 20, 94, 171, 174, 144, 29, 24, 33, 118, 191, 177, 154, 170, 127, 29, 52, 60, 165, 63, 55, 145, 137, 135, 124, 59, 64, 111, 141, 110, 37, 95, 45, 25, 34, 96, 196, 47, 26, 118],
[108, 182, 37, 125, 85, 127, 126, 148, 131, 22, 36, 77, 149, 21, 89, 77, 47, 137, 119, 156, 200, 172, 56, 85, 178, 85, 128, 11, 64, 24, 196, 133, 63, 97, 189, 197, 50, 35, 39, 69, 173, 200, 59, 155, 191, 62, 49, 190, 134, 64, 149, 172, 191],
[143, 117, 191, 87, 19, 55, 17, 125, 70, 175, 136, 11, 106, 99, 84, 89, 14, 140, 189, 58, 158, 192, 68, 157, 63, 72, 114, 158, 83, 118, 195, 30, 145, 164, 79, 39, 135, 187, 165, 193, 64, 20, 168, 125, 164, 40, 152, 195, 78, 132, 11, 48, 93],
[80, 129, 39, 137, 33, 194, 67, 84, 11, 157, 48, 47, 169, 166, 156, 18, 50, 190, 193, 12, 11, 53, 166, 55, 27, 135, 159, 191, 75, 101, 176, 129, 96, 14, 98, 141, 82, 143, 39, 98, 128, 151, 153, 21, 53, 118, 88, 97, 188, 105, 33, 157, 114],
[30, 80, 93, 87, 110, 83, 184, 183, 190, 104, 163, 107, 157, 184, 110, 120, 117, 56, 30, 163, 128, 73, 35, 166, 104, 40, 183, 75, 89, 14, 64, 124, 38, 81, 133, 10, 42, 57, 74, 92, 100, 198, 95, 198, 155, 115, 189, 157, 18, 10, 41, 135, 126],
[168, 83, 182, 182, 12, 184, 156, 59, 56, 96, 80, 18, 52, 81, 112, 86, 17, 85, 120, 92, 134, 62, 151, 103, 107, 12, 136, 40, 63, 108, 194, 129, 189, 187, 134, 188, 28, 176, 53, 139, 76, 101, 22, 36, 177, 18, 45, 161, 100, 182, 66, 186, 186],
[137, 195, 38, 91, 157, 177, 148, 106, 46, 112, 178, 10, 97, 75, 60, 92, 151, 60, 115, 135, 155, 41, 127, 183, 178, 108, 154, 10, 97, 128, 17, 137, 34, 36, 109, 156, 164, 52, 81, 163, 54, 162, 55, 100, 139, 175, 60, 13, 109, 140, 69, 55, 159],
[121, 178, 49, 142, 143, 92, 14, 186, 144, 91, 56, 67, 200, 177, 132, 55, 28, 147, 89, 176, 103, 123, 78, 117, 36, 162, 195, 83, 128, 187, 190, 132, 42, 149, 154, 168, 189, 43, 140, 190, 127, 162, 68, 89, 110, 157, 170, 158, 21, 110, 186, 101, 187],
[178, 191, 120, 38, 72, 14, 122, 19, 115, 91, 58, 161, 19, 121, 92, 26, 32, 180, 60, 152, 68, 138, 99, 165, 53, 91, 47, 166, 10, 59, 131, 139, 138, 136, 182, 156, 196, 120, 109, 138, 34, 101, 178, 119, 197, 181, 105, 121, 117, 72, 39, 113, 90],
[77, 118, 148, 124, 187, 177, 190, 163, 40, 195, 156, 23, 93, 173, 132, 150, 184, 188, 82, 70, 161, 192, 27, 179, 56, 34, 63, 79, 175, 35, 23, 179, 58, 187, 185, 31, 89, 89, 78, 184, 176, 102, 72, 40, 52, 190, 109, 93, 50, 95, 198, 87, 114],
[139, 101, 31, 79, 38, 121, 48, 147, 120, 79, 108, 163, 72, 21, 96, 29, 12, 154, 115, 180, 89, 153, 53, 157, 24, 53, 121, 135, 26, 183, 82, 20, 47, 39, 28, 162, 32, 187, 36, 71, 150, 125, 47, 167, 143, 186, 200, 68, 185, 123, 85, 25, 20],
[175, 137, 84, 59, 41, 192, 140, 131, 145, 61, 86, 167, 171, 93, 178, 81, 138, 169, 191, 45, 55, 19, 190, 179, 51, 158, 37, 144, 189, 161, 40, 130, 55, 12, 30, 135, 124, 122, 99, 137, 111, 46, 73, 56, 120, 146, 64, 85, 147, 11, 184, 30, 187]]

if __name__ == '__main__':
    print(timeit.timeit(stmt="find_sum_bellman_ford(m)", setup="from find_sum import find_sum_bellman_ford, m", number=1))
