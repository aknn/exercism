#pragma once

#include <vector>

// Returns the length of the shortest path (in edges) between src and dst
// in an unweighted, undirected graph with n nodes labeled [0, n).
// Edges is a list of pairs {u, v}. Returns -1 if no path exists.
int shortest_path_unweighted(int n, const std::vector<std::vector<int>>& edges, int src, int dst);

