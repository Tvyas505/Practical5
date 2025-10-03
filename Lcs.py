def find_lcs_from_algo(a, b): 
    m = len(a) 
    n = len(b) 

    c = [[[0, 'n'] for _ in range(n + 1)] for _ in range(m + 1)] 

    for i in range(1, m + 1): 
        for j in range(1, n + 1): 
            if a[i - 1] == b[j - 1]: 
                c[i][j][0] = c[i - 1][j - 1][0] + 1 
                c[i][j][1] = 'd' 
            elif c[i - 1][j][0] >= c[i][j - 1][0]: 
                c[i][j][0] = c[i - 1][j][0] 
                c[i][j][1] = 'u' 
            else: 
                c[i][j][0] = c[i][j - 1][0] 
                c[i][j][1] = 's' 

    print(" Cost and Direction Matrix\n") 
    print("      ", end="") 
    for char in b: 
        print(f" {char}  ", end="") 
    print() 

    for i in range(m + 1): 
        if i == 0: 
            print("  ", end="") 
        else: 
            print(f"{a[i-1]} ", end="") 
        for j in range(n + 1): 
            val = c[i][j][0] 
            direction = c[i][j][1] 
            print(f"{val:>2}{direction} ", end="") 
        print() 

    lcs_string = [] 
    i, j = m, n 
    while i > 0 and j > 0: 
        direction = c[i][j][1] 
        if direction == 'd': 
            lcs_string.append(a[i - 1]) 
            i -= 1 
            j -= 1 
        elif direction == 'u': 
            i -= 1 
        else: 
            j -= 1 

    lcs_result = "".join(reversed(lcs_string)) 

    print("\n--------------------\n") 
    print(" Final Result") 
    print(f"Length of LCS = {c[m][n][0]}") 
    print(f"LCS = {lcs_result}") 


if __name__ == "__main__": 
    X = "AGCCCTAAGGGCTACCTAGCTT" 
    Y = "GACAGCCTACAAGCGTTAGCTTG" 

    print(f"Sequence X: {X}") 
    print(f"Sequence Y: {Y}\n") 

    find_lcs_from_algo(X, Y)
