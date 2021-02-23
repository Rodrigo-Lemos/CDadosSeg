#!/usr/bin/env python
# coding: utf-8

# In[1]:

import sys
import pefile
if len(sys.argv)!=3:
    print('checar numero de argumentos')
    exit()
path = [sys.argv[1], sys.argv[2]]
answerDict = {}
for file in path:
    answerDict[file] = []
    pe=pefile.PE(file)
    for section in pe.sections:
        answerDict[file].append(section.Name.decode('utf-8').strip('\x00'))
intersection = [value for value in answerDict[path[0]] if value in answerDict[path[1]]] 
file1 = [value for value in answerDict[path[0]] if value not in answerDict[path[1]]]
file2 = [value for value in answerDict[path[1]] if value not in answerDict[path[0]]]
print('Seções comuns aos 2 arquivos: '+str(intersection)+'\n')
print('Seções apenas em '+path[0]+': '+str(file1)+'\n')
print('Seções apenas em '+path[1]+': '+str(file2)+'\n')


# In[ ]:




