# python3


def get_euclidean_cycle(edges, m):
    edge_count = {}

    for i in range(len(edges)):
        edge_count[i] = len(edges[i])

    curr_path = [0]
    circuit = []
    curr_v = 0

    while len(curr_path):
        if edge_count[curr_v]:
            curr_path.append(curr_v)
            edge_count[curr_v] -= 1
            next_v = edges[curr_v][edge_count[curr_v]]
            curr_v = next_v
        else:
            circuit.append(curr_v)
            curr_v = curr_path.pop()

    circuit.pop()
    return circuit[::-1]


if __name__ == '__main__':
    n, m = map(int, input().split())

    edges = [[] for _ in range(n)]
    degree = [0 for _ in range(n)]
    num = 0
    for i in range(m):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        num += 1
        degree[a - 1] += 1
        degree[b - 1] -= 1

    if any(degree):
        print(0)
    else:
        print(1)
        print(' '.join(map(lambda x: str(x + 1), get_euclidean_cycle(edges, m))))

