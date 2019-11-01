
# coding: utf-8

# # Lists

# What is List?
# 1. It is Data Structure.
# 2. It is of Mutable type i.e. changeable (we can change the data in List).
# 3. Every element in List is known as Item.
# 4. Elements in List are ordered.
# 5. List can be created by putting values in square brackets i.e. [v1,v2,v3....] 
# 6. Index starts from 0 in Lists.

# In[3]:


my_list= [1,2,3,4,5,6] #lets make the first list named as my_list and put numeric values form 1 to 6 in it.


# In[4]:


print(my_list) # we can print by using print function


# In[5]:


my_list #or we can print the values by directly writting the list name.


# In[6]:


#slicing of lists.
#slicing is the process in which we can extract items from list by using index values.
my_list[1]


# In[7]:


my_list[:]#this is the use of slicing. Colon divide the starting index value from ending index.


# In[8]:


my_list[0:4]#attention
# The output of this line shows that we provide strating index as 0 and ending index as 4 i.e. we want to print 5 values.
# But here we are getting 4 values in output only.
# This implies the last index value is not included.


# In[9]:


my_list[1:2]
#Here we are starting from 1 index value and ending at 2 index. So we are getting the item at index at 1 i.e. 2.


# In[10]:


my_list[::]
#Here we are proving two colons
# [starting index : ending index : next printing value]


# In[13]:


my_list[1:5:1]
# Here staring index is 1, ending index is 5 and next printing value is 1.
# i.e. why output is 2, 3, 4, 5.


# In[14]:


my_list[1:5:2]
# Here next priting value is 2. i.e. we are priting each 2nd value. 
# i.e. leaving 1 and printing 2 similarly leaving 3 and priting 4.


# In[18]:


my_list[::-1]
#Here -1 signifies starting from last
# In any list 
# [a,b,c,d]
# [0,1,2,3] index values for list from starting.
#[-4,-3,-2,-1] index va;ue for list from last.


# In[25]:


for i in my_list[0:5:2]: #we can use the slicing of lists in loops also.
    print(i)
    print(i*i)


# In[26]:


my_list=[1,'hasrhit',2,'gupta'] # we can add integer as well as strings at the same time in lists.
my_list


# In[27]:


my_list=[1,1.001,2.002,'harshit'] # we can add any data type value in Lists.


# In[28]:


my_list

