# main.py

def count_power_groups(stations, lines):
    """
    Count the number of connected groups of power stations.

    Parameters
    ----------
    stations : list of str
        List of station names.
    lines : list of tuple(str, str)
        Each tuple represents a connection (undirected) between two stations.

    Returns
    -------
    int
        Number of connected groups (connected components).
    """
    if not stations:
        return 0

    # Build adjacency list
    graph = {station: set() for station in stations}
    for a, b in lines:
        if a in graph and b in graph:
            graph[a].add(b)
            graph[b].add(a)

    visited = set()

    def dfs(node):
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                stack.extend(graph[current] - visited)

    groups = 0
    for station in stations:
        if station not in visited:
            dfs(station)
            groups += 1

    return groups


if __name__ == "__main__":
    # Example usage
    stations = ["A", "B", "C", "D", "E"]
    lines = [("A", "B"), ("C", "D")]
    print(count_power_groups(stations, lines))  # Output: 3