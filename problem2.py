# Bob has X rupees and goes to a market. The cost of apples is Rs. A per kg and the cost of oranges is Rs. B per kg.

# Determine whether he can buy at least 1 kg each of apples and oranges.

money = int(input())
costarray = str(input()).split(" ")
    

cost = int(costarray[0]) + int(costarray[1])

if money >= cost:
    print("Yes")
else:
    print("No")

