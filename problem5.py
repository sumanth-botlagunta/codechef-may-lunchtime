# You are given an array A containing N integers, and a positive integer M. Find the maximum value of
# Ai+Aj+((Ai−Aj)modM)
# across all pairs 1≤i,j≤N.

# Note that xmodM refers to the smallest non-negative integer obtained as the remainder upon dividing x by M. For example, 4mod3=1 and (−10)mod3=2.

# Input Format
# The first line of input will contain a single integer T, the number of test cases. The description of test cases follows.
# Each test case consists of two lines of input.
# The first line of each test case contains two space-separated integers N and M.
# The second line of each test case contains N space-separated integers  A1,A2,…,AN .

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    max_sum = -1
    mx = max(arr)
    for i in range(n):
        sum = arr[i] + mx + ((arr[i] - mx) % m)
        if sum > max_sum:
            max_sum = sum 
    print(max_sum)