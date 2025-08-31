#include "solution.h"

#include <cassert>
#include <iostream>

static void run_tests() {
    // Triangle 0-1-2-0, shortest 0->2 is 1
    {
        int n = 3;
        std::vector<std::vector<int>> edges{{0,1},{1,2},{2,0}};
        assert(shortest_path_unweighted(n, edges, 0, 2) == 1);
    }
    // Line 0-1-2-3, shortest 0->3 is 3
    {
        int n = 4;
        std::vector<std::vector<int>> edges{{0,1},{1,2},{2,3}};
        assert(shortest_path_unweighted(n, edges, 0, 3) == 3);
    }
    // Disconnected, no path
    {
        int n = 4;
        std::vector<std::vector<int>> edges{{0,1},{2,3}};
        assert(shortest_path_unweighted(n, edges, 0, 3) == -1);
    }
    // Invalid vertices
    {
        int n = 3;
        std::vector<std::vector<int>> edges{{0,1}};
        assert(shortest_path_unweighted(n, edges, -1, 2) == -1);
        assert(shortest_path_unweighted(n, edges, 0, 3) == -1);
    }
    // Trivial src==dst
    {
        int n = 5;
        std::vector<std::vector<int>> edges{};
        assert(shortest_path_unweighted(n, edges, 2, 2) == 0);
    }
}

int main() {
    run_tests();
    std::cout << "All tests passed\n";
    return 0;
}

