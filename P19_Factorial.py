# Python program calculate factorial of a number . 



n=int(input("Enter any number "))      #User input any integer number. 
fact=1 
for i in range(1,n+1):  #for loop 1 to n+1

    # if number is 1 so it will print 1 . No need for if statement. 
    fact=fact*i
    
    
print("Factorial of ", n, "is",fact)      # Factorial Result. 
