# Like most users, Chef didn’t know that he could add problems to a personal to-do list by clicking on the magic '+' symbol on the top-right of each problem page. But once he found out about it, he went crazy and added loads of problems to his to-do list without looking at their difficulty rating.

# Chef is a beginner and should ideally try and solve only problems with difficulty rating strictly less than 1000. Given a list of difficulty ratings for problems in the Chef’s to-do list, please help him identify how many of those problems Chef should remove from his to-do list, so that he is only left with problems of difficulty rating less than  1000 .

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    count = 0
    for j in range(n):
        if arr[j] >= 1000:
            count += 1
    print(count)