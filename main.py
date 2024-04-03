from graph_operations import GraphOperations
import timeit


def bfs(graph_name: str) -> None:
    operations = GraphOperations()

    graph = operations.load_graph(f"graphs/{graph_name}")
    report = operations.bfs(graph, 0)
    report["operation_time"] = timeit.timeit(lambda: operations.bfs(graph, 0), number=1)

    print(report)

    operations.visualize(graph)


def dfs(graph_name: str) -> None:
    operations = GraphOperations()

    graph = operations.load_graph(f"graphs/{graph_name}")
    report = operations.dfs(graph, 0)
    report["operation_time"] = timeit.timeit(lambda: operations.dfs(graph, 0), number=1)

    print(report)

    operations.visualize(graph)


if __name__ == "__main__":
    algorythm = input("Enter what algorythm you want to use (bfs/dfs): ")
    graph = input("Enter graph name from graphs folder: ")
    if algorythm == "bfs":
        bfs(graph)
    if algorythm == "dfs":
        dfs(graph)


# graph = operations.create_undirected_graph(20, 12)
# operations.save_graph(graph, "graphs/directed_graph_test")
