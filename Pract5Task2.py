def longest_repeating_subsequence_length(S):
    n = len(S)
    c = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if S[i - 1] == S[j - 1] and i != j:
                c[i][j] = 1 + c[i - 1][j - 1]
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

    return c[n][n]


string = "AABCBDC"
length = longest_repeating_subsequence_length(string)
print(length)
