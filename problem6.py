# You are given an array A=[A1,A2,…,AN], consisting of N integers. In one move, you can take two adjacent numbers Ai and Ai+1, delete them, and then insert the number Ai∧Ai+1 at the deleted position. Here, ∧ denotes bitwise AND. Note that after this operation, the length of the array decreases by one.

# Formally, as long as |A|>1 (where |A| denotes the current length of A), you can pick an index 1≤i<|A| and transform A into [A1,A2,…,Ai−1,Ai∧Ai+1,Ai+2,…,A|A|].

# Find the minimum number of moves required to make all numbers in the resulting array equal.

# Input Format
# The first line of input contains an integer T — the number of test cases you need to solve.
# The first line of each test case contains one integer N, the size of the array.
# The second line of each test case contains N space-separated integers A1,…,AN — the elements of the array A.

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    b = arr[0]
    for i in range(n):
        b&=arr[i]
    r = 0
    for i  in range(n):
        if arr[i] == b:
            continue
        if i == (n-1):
            r = r + 1
            continue
        arr[i + 1] &= arr[i]
        r += 1
    print(r) 