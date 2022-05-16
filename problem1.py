# // Our Chef is currently practicing on CodeChef and is a beginner. The count of ‘All Problems’ in the Beginner section is X. Our Chef has already ‘Attempted’ Y problems among them. How many problems are yet ‘Un-attempted’?

string = input()
array = string.split(" ");

for i in range(0,len(array)):
    array[i] = int(array[i])

print(array[0]-array[1])