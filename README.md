[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/jfx4QqAl)
# hw03 – Power Grid Groups (Graphs)

## Story
A city has many **power stations**. Some stations are connected by power lines. If there is a path of power lines between two stations, they are in the **same power group**. If there is no path, they are in different groups.

City engineers want to know:

> How many separate power groups are there?

You will take a set of stations and the power lines between them and return the number of connected groups.

---

## Function Specification
Write a function:

```python
def count_power_groups(stations, lines):
    """Return the number of connected groups (components) of stations.

    stations: list[str] - station names.
    lines: list[tuple[str, str]] - undirected connections between stations.
    """
    ...  # implement
```

### Parameters
- `stations`: list of station names (strings)
- `lines`: list of pairs `(a, b)` meaning an undirected power line between `a` and `b`

### Return
An integer: how many connected groups of stations exist.

### Example
```python
stations = ["A", "B", "C", "D"]
lines = [("A", "B"), ("B", "C")]  # D is alone

count_power_groups(stations, lines)  # -> 2
# Group 1: {A, B, C}
# Group 2: {D}
```

---

## Constraints
- `len(stations)` in `[0, 10_000]`
- `len(lines)` in `[0, 50_000]`
- All station names in `lines` appear in `stations`
- Stations may have no lines (isolated)
- Multiple identical lines may appear; treat them as a single connection

## Expected Complexity
- Time: `O(n + m)` where `n = len(stations)`, `m = len(lines)`
- Space: `O(n + m)` for adjacency structure + visited set

Use a graph structure that lets you find neighbors quickly (adjacency list).

---

## Implementation Guidance (8-Step Scaffold)
1. Clarify: A "power group" is a connected component in the undirected graph.
2. Rephrase: If all stations connect (one component) return `1`; if none connect, return `len(stations)`.
3. Inputs / Outputs / Structures:
   - Adjacency list: `dict[str, set[str]]`
   - Visited tracking: `set[str]`
4. Pseudocode sketch:
   - Build adjacency list (include isolated stations with empty set)
   - Initialize `groups = 0`
   - For each station: if not visited, traverse (DFS/BFS), mark visited, `groups += 1`
5. Code: Implement traversal (stack or queue or recursion)
6. Debug: Test tiny cases (empty, single, chain, disconnected)
7. Optimize: Ensure linear construction & traversal; avoid duplicate neighbor inserts
8. Final check: Complexity meets `O(n + m)`; no unnecessary work

---

## Hints
- Adjacency list (`dict` mapping station -> `set` or `list` of neighbors) is typical.
- Use a `visited` set to skip already processed stations.
- Each new traversal started from an unvisited station counts one new group.
- Either DFS or BFS works; pick what you’re comfortable with.

---

## Running Tests

```bash
python -m pytest -q
```


---

## FAQ
**Q1: Are lines directed or undirected?** Undirected. `("A", "B")` allows travel both ways.

**Q2: What if there are no stations?** Return `0`.

**Q3: What if there are stations but no lines?** Every station is isolated → return `len(stations)`.

**Q4: Multiple lines between the same pair?** Treat them as one connection; duplicates should not break your logic.

**Q5: Do I have to use recursion?** No. Iterative stack/queue is fine.

**Q6: Expected Big-O?** About `O(n + m)` time, `O(n + m)` space.

**Q7: How to debug graph code?** Print adjacency list & visited progress on tiny examples.

---

Happy coding!