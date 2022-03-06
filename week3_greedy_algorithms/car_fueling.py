# python3

# 0 200 375 550 750 900

import sys

def compute_min_refills(distance, tank, stops):
    num_refills = 0
    stops.insert(0,0)
    stops.append(distance)
    stops.append(distance + 1)
    current_fill = 0
    last_fill = 0
    while stops[current_fill] < distance:
        if stops[current_fill + 1] - stops[current_fill] <= tank:
            while stops[current_fill] < distance and stops[current_fill + 1] - stops[last_fill] <= tank:
                current_fill += 1
            last_fill = current_fill
            num_refills += 1
            # print(current_fill)
        else:
            return -1
           
    return num_refills -1

if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
