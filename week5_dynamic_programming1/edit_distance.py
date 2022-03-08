# Uses python3
def edit_distance(s, t):
    #write your code here
    s = '#' + s
    t = '#' + t
    n = len(s)
    m = len(t)
    dp = [[float('inf')] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = i
    for j in range(m):
        dp[0][j] = j
    for i in range(1, n):
        for j in range(1, m):
            insert = dp[i][j-1] + 1
            delete = dp[i-1][j] + 1
            match = dp[i-1][j-1]
            mismatch = dp [i-1][j-1] + 1
            if s[i] == t[j]:
                dp[i][j] = min(insert, delete, match)
            else:
                dp[i][j] = min(insert, delete, mismatch)


    return dp[n-1][m-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
