""" Strongly Connected Algorithm - Kosaraju's Algo
1) DFS through graph
2) stack nodes by ending time (decreasing)
3) DFS through Transpose Graph
4) it is a scc if no connections are made

Youtube: https://www.youtube.com/watch?v=RpgcYiky7uw
"""
from pythonds import Graph
def scc(graph) -> List[set]:
    