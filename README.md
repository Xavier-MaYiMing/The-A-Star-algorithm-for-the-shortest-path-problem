### The A* Algorithm for the Shortest Path Problem

##### Reference: Hart P E, Nilsson N J, Raphael B. A formal basis for the heuristic determination of minimum cost paths[J]. IEEE Transactions on Systems Science and Cybernetics, 1968, 4(2): 100-107.

| Variables   | Meaning                                                      |
| ----------- | ------------------------------------------------------------ |
| network     | A two-dimensional array, in which 0 denotes the obstacle, and 1 denotes that the node is accessible |
| source      | The source node                                              |
| destination | The destination node                                         |
| dim1        | Dimension 1                                                  |
| dim2        | Dimension 2                                                  |
| f_list      | The list of f_values (f = g + h)                             |
| g_list      | The list of g_values (g equals the length)                   |
| path_list   | The list of paths                                            |

#### Example

![](https://github.com/Xavier-MaYiMing/The-A-Star-algorithm-for-the-shortest-path-problem/blob/main/A-star%20example.png)

```python
if __name__ == '__main__':
    # Example
    test_network = [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1],
    ]
    s = [0, 0]
    d = [2, 6]
    print(main(test_network, s, d))
```

##### Output: 

```python
{
    'path': [[0, 0], [1, 0], [1, 1], [1, 2], [2, 2], [3, 2], [3, 3], [3, 4], [3, 5], [2, 5], [2, 6]], 
    'length': 10.0
}
```
