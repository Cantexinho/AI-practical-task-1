from bfs_dfs_algorithms.operations.graph import GraphOperations
import timeit


def process_bfs(graph_name: str) -> None:
    operations = GraphOperations()

    graph = operations.load_graph(f"src/bfs_dfs_algorithms/graphs/{graph_name}")
    report = operations.bfs(graph, 0)
    report["operation_time"] = timeit.timeit(lambda: operations.bfs(graph, 0), number=1)

    print(report)

    operations.visualize(graph)


def process_dfs(graph_name: str) -> None:
    operations = GraphOperations()

    graph = operations.load_graph(f"src/bfs_dfs_algorithms/graphs/{graph_name}")
    report = operations.dfs(graph, 0)
    report["operation_time"] = timeit.timeit(lambda: operations.dfs(graph, 0), number=1)

    print(report)

    operations.visualize(graph)


def main():
    algorythm = input("Enter what algorythm you want to use (bfs/dfs): ")
    graph = input("Enter graph name from graphs folder: ")
    if algorythm == "bfs":
        process_bfs(graph)
    if algorythm == "dfs":
        process_dfs(graph)


if __name__ == "__main__":
    main()


# graph = operations.create_undirected_graph(20, 12)
# operations.save_graph(graph, "graphs/directed_graph_test")
