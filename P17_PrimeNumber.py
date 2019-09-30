# Python program to check if given number is prime or not 
  

no = 11
# If given number is greater than 1 
if no > 1: 
      
   # check from 2 to n / 2  
   for i in range(2, no//2): 
         
       # If no. is divisible by any number between  
       # 2 and n / 2, it is not prime  
       if (no % i) == 0: 
           print(no, "is not a prime number.") 
           break
   else: 
       print(no, "is a prime number.") 
  
else: 
   print(no, "is not a prime number.")
