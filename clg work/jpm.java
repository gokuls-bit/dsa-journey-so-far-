import java.util.Arrays;

class DijkstraSimple {
    static final int INF = Integer.MAX_VALUE; // Represents infinity

    static void dijkstra(int[][] graph, int source) {
        int V = graph.length;
        int[] distance = new int[V]; // Stores shortest distances
        boolean[] visited = new boolean[V]; // Keeps track of visited nodes

        // Step 1: Initialize distances
        Arrays.fill(distance, INF);
        distance[source] = 0;

        // Step 2: Find shortest paths for all vertices
        for (int i = 0; i < V - 1; i++) {
            int u = findMinDistance(distance, visited, V);
            visited[u] = true;

            // Step 3: Update distances of neighboring nodes
            for (int v = 0; v < V; v++) {
                if (!visited[v] && graph[u][v] != 0 && distance[u] != INF &&
                    distance[u] + graph[u][v] < distance[v]) {
                    distance[v] = distance[u] + graph[u][v];
                }
            }
        }

        // Step 4: Print the shortest distances
        System.out.println("Vertex \t Distance from Source");
        for (int i = 0; i < V; i++) {
            System.out.println(i + " \t " + (distance[i] == INF ? "∞" : distance[i]));
        }
    }

    // Helper function to find the node with the smallest distance
    static int findMinDistance(int[] distance, boolean[] visited, int V) {
        int min = INF, minIndex = -1;
        for (int i = 0; i < V; i++) {
            if (!visited[i] && distance[i] < min) {
                min = distance[i];
                minIndex = i;
            }
        }
        return minIndex;
    }

    public static void main(String[] args) {
        int[][] graph = {
            {0, 10, 20, 0, 0},
            {10, 0, 5, 1, 0},
            {20, 5, 0, 2, 8},
            {0, 1, 2, 0, 3},
            {0, 0, 8, 3, 0}
        };

        dijkstra(graph, 0); // Start from node 0
    }
}
