# Alice has a bucket of water initially having W litres of water in it. The maximum capacity of the bucket is X liters.

# Alice turned on the tap and the water starts flowing into the bucket at a rate of Y litres/hour. She left the tap running for exactly Z hours. Determine whether the bucket has been overflown, filled exactly, or is still left unfilled.

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases. The description of the test cases follows.
# Each test case consists of a single line of input containing four space-separated integers  W, X, Y, Z .

def bucket(arr):
    for i in range(0,len(arr)-1):
        arr[i] = int(arr[i])

    filled = (arr[2]*arr[3]) + arr[0];
    capacity = arr[1]

    if filled > capacity:
        return("overFlow")
    elif filled == capacity:
        return("filled")
    else:
        return("Unfilled")

while True:  
    try: 
        for i in range(int(input())):
            a, b, c, d = map(int,input().split())
            if a + c*d >b:
                print("overFlow")
            elif a + c*d == b:
                print("filled")
            else:
                print("Unfilled")        
    except :
        break

    