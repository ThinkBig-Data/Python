EXCEPTION HANDLING
In [1]:


try:
  print(x)
except:
  print("An exception occurred")



An exception occurred
In [4]:


a=5
b=0   
try: 
    print(a/b) 
except: 
    print("A number is not divisible by zero")



A number is not divisible by zero
In [12]:


   # Program to depict else clause with try-except 
  
# Function which returns a/b 
def AbyB(a , b): 
    try: 
        c = ((a+b) / (a-b)) 
    except ZeroDivisionError:
        print("a/b result in 0")
    else: 
        print(c) 
  
# Driver program to test above function 
AbyB(2.0, 3.0) 
AbyB(3.0, 3.0) 



-5.0
a/b result in 0
In [14]:


# Python program to handle simple runtime error 
  
a = [1, 2, 3] 
try:
    print ("Second element = %d" %(a[1])) 
  
    # Throws error since there are only 3 elements in array 
    print ("Fourth element = %d" %(a[3]))    
​
except IndexError:
     print ("An error occurred")



Second element = 2
An error occurred
