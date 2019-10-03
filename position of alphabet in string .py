#first three lines of code for count of similar letters in para !!
# string = str(input())    
# print(string.count("geeks", 0, 5))   
# print(string.count("geeks", 0, 15))

# position 
print("enter a para \n")
word = str(input())

print("enter a letter from para to find its position!!")

p1=str(input())
result = word.find(p1) 
print ("Substring, "+ p1 + " found at index:", result ) 

print("enter the 2nd letter from para to find its position!!")  
p2=str(input())
result1 = word.find(p2) 
print ("Substring, "+ p2 + " found at index:", result1 ) 
  
#  How to use find() 
print("enter a name from para to check its availaibility!")
p3=str(input())
if (word.find(p3) != -1):
    print ("Name is Present in para") 
else:
    print ("Name is not Present in para..!!") 

