# Uses python3

def get_optimal_value(capacity, weights, values, indices):
    value = 0.
    i = 0
    while (capacity > 0)and(i < len(values)):
        index = indices[i]
        value += min(capacity, weights[index]) * values[index] / weights[index]
        capacity -= min(capacity, weights[index])
        i += 1
    # write your code here

    return value


if __name__ == "__main__":
    n, capacity = map(int, input().split())
    values = []
    weights = []
    for i in range(n):
        v, w = map(int, input().split())
        values.append(v)
        weights.append(w)

    indices = sorted(range(n), reverse=True, key=lambda x: values[x] / weights[x])
    opt_value = get_optimal_value(capacity, weights, values, indices)
    print("{:.10f}".format(opt_value))
