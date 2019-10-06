#Python code to find occurrences 
#of a substring in a string 
#defining a string
str = "I live in India, India is a great country"
#finding occurrences of 'India'
#in complete string
print(str.count("India"))
#finding occurrences of 'India'
#from 0 to 15 index
print(str.count("India",0,15))
#finding occurrences of 'i' (small 'i')
#in complete string
print(str.count("i"))
