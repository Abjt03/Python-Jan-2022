# Find Positive Numbers in the List input by the User

# List input
list = []
n = int(input("Enter number of list members : "))
print("Enter list members : ")
for i in range(0, n):
    list.append(int(input()))

# Print positive members
print("Print positive list members : ")
for i in range(0, n):
    if list[i] >= 0:
        print(list[i], end=' ')
