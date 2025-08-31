#include "solution.h"

#include <queue>
#include <unordered_map>
#include <unordered_set>

int shortest_path_unweighted(int n, const std::vector<std::vector<int>>& edges, int src, int dst) {
    if (src == dst) return 0;
    if (src < 0 || dst < 0 || src >= n || dst >= n) return -1;

    std::vector<std::vector<int>> adj(n);
    adj.reserve(n);
    for (const auto& e : edges) {
        if (e.size() != 2) continue;
        int u = e[0], v = e[1];
        if (u < 0 || v < 0 || u >= n || v >= n) continue;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    std::queue<int> q;
    std::vector<int> dist(n, -1);
    dist[src] = 0;
    q.push(src);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            if (dist[v] != -1) continue;
            dist[v] = dist[u] + 1;
            if (v == dst) return dist[v];
            q.push(v);
        }
    }
    return -1;
}

