#!/usr/bin/env python
# coding: utf-8

# In[39]:


"""
A= @
S= $
H= #
I=!
E = 3
4 = +
G = 6

"""


# In[59]:


securepasswd = (('s','$'),('h','#'),('i','!'),('a','@'),('e','3'),('4','+'),('g','6'))


# In[60]:


def pass_secure(create):
  for a,b in securepasswd: 
   create = create.replace(a,b)
  return create


# In[61]:


if __name__=="__main__":
    create = input("Enter your password")
    create = pass_secure(create) 
print(f"Secured form of your password is {create} ")


# In[ ]:




