# -*- coding: utf-8 -*-

"""Tests for sandbox package."""

import sandbox
import numpy as np
import networkx as nx
import igraph as ig
# Both networkx and igraph store node properties on a per node basis, not as an array.
# networkz is a Python only implementation, igraph is a binary extension module. There is
# probably a trade-off between flexibility and speed. A reasonably good approach could be
# to first do node computations on numpy arrays, tben use them to set the node properrties
# and do the graph computation.


def test_nx0():
    G = nx.Graph()
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    print(G.nodes)
    values = [1,2,3]
    values = np.array(values)
    nx.set_node_attributes(G, {'values': values})
    print(f"{nx.get_node_attributes(G, 'values')=}")

def test_ig1():
    g = ig.Graph()
    g.add_vertices(3)
    g.add_edges([(0,1),(0,2)])
    g.vs['value'] = [1,2,3]
    v = g.vs['value']
    print(type(v),id(v))
    v2 = g.vs['value']
    print(type(v2),id(v2))

def test_ig2():
    g = ig.Graph()
    g.add_vertices(3)
    g.add_edges([(0,1),(0,2)])
    values = [1,2,3]
    g.vs['value'] = values
    print(f"{g.vs['value']=}")
    values[0] = 10
    print(f'{values=}')
    print(f"{g.vs['value']=}")
    print("Setting vertex attribute implies copying them.")
    assert g.vs[0]['value'] == 10

def test_ig3():
    g = ig.Graph()
    g.add_vertices(3)
    g.add_edges([(0,1),(0,2)])
    values = [1,2,3]
    g.vs['value'] = values
    print(f"{g.vs['value']=}")
    values = np.array(values)
    g.vs['value'] = values
    print(f"{g.vs['value']=}")
    print("Can set vertex attribute from numpy array.")


# ==============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (otherwise all tests are normally run with pytest)
# Make sure that you run this code with the project directory as CWD, and
# that the source directory is on the path
# ==============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_nx0

    print("__main__ running", the_test_you_want_to_debug)
    the_test_you_want_to_debug()
    print('-*# finished #*-')

# eof