#  Finding area of the circle

#  Input Radius
rad = float(input("Enter Radius of the Circle : "))

#  Calculate Area assuming Pi=3.14
area = 3.14*rad*rad
print("Area of the Circle is : ", area)

# To take in a filename and print its extension (File Type)

# Get extension
f_name = input("Enter filename : ")
string = ""
for i in f_name:
    if i == '.':
        for x in range(f_name.find(i)+1, len(f_name)):
            string += f_name[x]

# Print filetype
if(string == "py"):
    print("Extension is : Python")
elif(string == "cpp"):
    print("Extension is : C++")
elif(string == "java"):
    print("Extension is : Java")
elif(string == "xml"):
    print("Extension is : XML")
else:
    print("Unrecognized Extension")
