import pytest

from graph import Graph


def test_graph():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    assert g.graph == {1: {2}, 2: {1, 3}, 3: {2}}