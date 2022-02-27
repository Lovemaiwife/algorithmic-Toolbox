# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    worthiest = []
    while capacity > 0:
        
        idx = -1
        unit_value = 0 
        for i in range(len(weights)):
            if i not in worthiest and values[i] / weights[i] >= unit_value:
                unit_value = values[i] / weights[i]
                idx = i
        worthiest.append(idx)
        item_weight = min(weights[idx], capacity)
        capacity -= item_weight
        value += item_weight * unit_value
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
