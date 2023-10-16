import networkx as nx
import matplotlib.pyplot as plt

from collections import defaultdict, deque


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def bfs_longest_path(self, src, destination):
        max_weight = float('-inf')
        max_paths = []

        # Triez les sommets pour toujours commencer par le plus petit indice
        sorted_vertices = sorted(self.graph.keys())

        for start_vertex in sorted_vertices:
            queue = deque([(start_vertex, 0, [])])

            while queue:
                u, current_weight, current_path = queue.popleft()

                for v, weight in self.graph.get(u, []):
                    new_weight = current_weight + weight
                    new_path = current_path + [(u, v, weight)]

                    if v == destination:
                        if new_weight > max_weight:
                            max_weight = new_weight
                            max_paths = [new_path]
                        elif new_weight == max_weight:
                            # En cas d'égalité de poids, conserve les deux chemins
                            max_paths.append(new_path)
                    else:
                        queue.append((v, new_weight, new_path))


        return max_weight, max_paths

    def construct_path(self, src, dst):
        path = [dst]
        node = dst
        while node is not None:
            path.append(self.predecessor[node])
            node = self.predecessor[node]
        path.reverse()
        return path

    def visualize_graph(self):
        G = nx.DiGraph()

        for u, edges in self.graph.items():
            for v, weight in edges:
                G.add_edge(u, v, weight=weight)

        pos = nx.spring_layout(G,k=8)  # You can choose a different layout if needed
        # Nodes
        nx.draw_networkx_nodes(G, pos, node_size=400, node_color='skyblue', alpha=1)

        # Edges
        nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=0.5, alpha=1, edge_color='black')

        # Edge labels
        edge_labels = {(u, v): str(weight) for u, v, weight in G.edges(data='weight')}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # Node labels
        node_labels = {node: str(node) for node in G.nodes}
        nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_color='black')

        plt.title("Weighted Graph Visualization")
        plt.axis('off')
        plt.show()



if __name__ == "__main__":
    g = Graph(22)

    # Adding edges to the graph using cost matrix
    g.add_edge(0, 1, 0)
    g.add_edge(1, 2, 41)
    g.add_edge(2, 3, 0)
    g.add_edge(2, 5, 0)
    g.add_edge(2, 9, 0)
    g.add_edge(3, 4, 29)
    g.add_edge(4, 6, 0)
    g.add_edge(4, 7, 0)
    g.add_edge(5, 10, 32)
    g.add_edge(6, 11, 21)
    g.add_edge(7, 12, 38)
    g.add_edge(8, 13, 45)
    g.add_edge(9, 14, 51)
    g.add_edge(10, 15, 0)
    g.add_edge(10, 16, 0)
    g.add_edge(11,15,0)
    g.add_edge(11, 16, 0)
    g.add_edge(12, 21, 0)
    g.add_edge(13, 21, 0)
    g.add_edge(14, 19, 0)
    g.add_edge(15, 17, 32)
    g.add_edge(16, 18, 36)
    g.add_edge(17, 19, 0)
    g.add_edge(18, 21, 0)
    g.add_edge(19, 20, 50)
    g.add_edge(20, 21, 0)

    g.visualize_graph()
    longest_dist, longest_path = g.bfs_longest_path(0,21)
    print("\nDistances maximales depuis la source:", longest_dist)
    print("\nLe plus long chemin de 0 à 21 est:", longest_path)
