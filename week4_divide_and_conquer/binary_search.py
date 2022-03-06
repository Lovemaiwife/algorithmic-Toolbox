def binary_search(keys, query):
    # write your code here
    high = len(keys)
    low = 1
    if q > keys[-1] or q < keys[0]:
        return -1
    else:
        while True:
            if high < low:
                return -1
                break
            else:
                current_search = (round((high - low)/2) + low - 1)
                if q == keys[current_search]:
                    return current_search
                    break
                elif q > keys[current_search]:
                    low = current_search + 2
                elif q < keys[current_search]:
                    high = current_search

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries
    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')

