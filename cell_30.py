#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def palindrome(word,num,test):
  if num == (len(word) // 2): return True
  if word[num] == word[(len(word)-1)-num]: return palindrome(word,num+1,True)
  else: return False
x = input("word to check palindrome ")
print (palindrome(x,0,True))

