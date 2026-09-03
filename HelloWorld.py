import sys

#This is an integer
x = 5
#This is a string
"""
This is a comment so 
ignore
"""
y = "Python" #Comment on the side
#print("Hello World outside main.", end=" "); print("Same line", end=" ")
#print("Double quotes text", end=" ");print('Single quotes text')
#print(x, " " , y, " Mixing text and strings")
def __main__():
    print("Hello World inside main");
    if 5 > 2:
        print("5 greater than 2")

x = "Python reverse"
y = 5
#print(x, end=" "); print(y)
x = str(3);
y = int("5")
z = float("7.2")
print(x, "(int to string)", y, "(string to int)", z, "(string to float)")
print(x,"(", type(x), ")", y, "(", type(y), ")", z,"(", type(z),")")
