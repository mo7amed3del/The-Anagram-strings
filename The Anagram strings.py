#!/usr/bin/env python
# coding: utf-8

# In[2]:


#this function is checking if the string is in english language # stack over flow link (https://stackoverflow.com/questions/27084617/detect-strings-with-non-english-characters-in-python) 

def isEnglish(s): 
    try: 
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError: 
        return False 
    else: 
        return True


# In[4]:


def compare(s,t):
    assert len(s) >= 1,"S should not be empty" 
    assert len(t) <= 5*10**4, "T's length should not smaller than 5x10^4" 
    assert s.islower() and t.islower(), "S and T should be lower case" 
    assert isEnglish(s) and isEnglish(t) , "input must be in english" 
    #return true if t is an anagram of s 
    return sorted(s)== sorted(t) 
    
print(compare(s = "rat", t = "car"))


# In[ ]:




