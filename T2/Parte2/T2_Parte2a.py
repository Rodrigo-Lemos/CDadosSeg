#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pefile
import sys

# In[21]:
if len(sys.argv) != 2:
    print('checar numero de parametros')
    exit()

path = os.listdir(sys.argv[1])
answerDict = {}
for file in path:
    answerDict[file] = []
    pe=pefile.PE(sys.argv[1]+'/'+file)
    for section in pe.sections:
        answerDict[file].append(section.Name.decode('utf-8').strip('\x00'))
i=1
for file in answerDict:
    print(str(i)+') '+file+' : '+str(answerDict[file]))
    i+=1


# In[ ]:




