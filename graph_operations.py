from collections import defaultdict, deque
import matplotlib.pyplot as plt
import networkx as nx
import random


class GraphOperations:
    def visualize(self, graph: nx.graph) -> None:
        nx.draw(graph, with_labels=True, node_color="skyblue", node_size=800)
        plt.show()

    def bfs(self, graph: nx.graph, start_node: int) -> dict:
        visited_nodes = []
        queue = [start_node]
        visited = set()

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                visited_nodes.append(node)
                queue.extend(graph.neighbors(node))

        unvisited_nodes = set(graph.nodes()) - visited
        unvisited_nodes_len = graph.number_of_nodes() - len(visited_nodes)

        return {
            "visited_nodes": visited_nodes,
            "visited_nodes_len": len(visited_nodes),
            "unvisited_nodes": unvisited_nodes,
            "unvisited_nodes_len": unvisited_nodes_len,
        }

    def dfs(self, graph: nx.Graph, start_node: int) -> dict:
        visited_nodes = []
        unvisited_nodes = set(graph.nodes())
        stack = [start_node]
        visited = set()

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                visited_nodes.append(node)
                unvisited_nodes.discard(node)
                stack.extend(reversed(list(graph.neighbors(node))))

        return {
            "visited_nodes": visited_nodes,
            "visited_nodes_len": len(visited_nodes),
            "unvisited_nodes": unvisited_nodes,
            "unvisited_nodes_len": len(unvisited_nodes),
        }

    def create_undirected_graph(self, nodes: int, edges: int) -> nx.Graph:
        graph = nx.Graph()
        graph.add_nodes_from(range(nodes))
        possible_edges = [(i, j) for i in range(nodes) for j in range(i + 1, nodes)]
        edges_to_add = random.sample(possible_edges, edges)
        graph.add_edges_from(edges_to_add)
        return graph

    def create_directed_graph(self, nodes: int, branching_factor: int) -> nx.DiGraph:
        graph = nx.DiGraph()
        for i in range(nodes):
            graph.add_node(i)
        for i in range(nodes):
            num_branches = random.randint(1, branching_factor)
            branches = random.sample(range(nodes), num_branches)
            for branch in branches:
                graph.add_edge(i, branch)
        return graph

    def save_graph(self, graph: nx.graph, file_path: str) -> None:
        nx.write_graphml(graph, file_path)

    def load_graph(self, file_path: str) -> nx.graph:
        return nx.read_graphml(file_path, int)
