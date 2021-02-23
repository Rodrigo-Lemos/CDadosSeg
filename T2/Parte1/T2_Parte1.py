#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os
import sys

# In[12]:
if len(sys.argv) != 2:
    print('checar numero de parametros')
    exit()

manifests = os.listdir(sys.argv[1])
answerDict = {}
permissionDict = {}
for manifest in manifests:
    apk = manifest.strip('AndroidManifest_')
    with open(sys.argv[1]+'/'+manifest, 'r') as f:
        for line in f:
            if '<uses-permission' in line:
                permission = line.split('"')[1].split('.')[-1]
                if permission in permissionDict.keys():
                    permissionDict[permission]+=1
                else:
                    permissionDict[permission]=1
                if apk in answerDict.keys():
                    answerDict[apk].append(permission)
                else:
                    answerDict[apk] = [permission]
print('====================================\n\nPermissões por APK\n\n====================================')
i=1
for key in answerDict:
    print(str(i)+') '+key+' : '+str(answerDict[key]))
    print('\n')
    i+=1


# In[13]:


uniqueDict = {}
for key in answerDict:
    uniqueDict[key] = []
    for permission in answerDict[key]:
        if permissionDict[permission] == 1:
            uniqueDict[key].append(permission)
print('====================================\n\nPermissões únicas por APK\n\n====================================')
i=1
for key in uniqueDict:
    print(str(i)+') '+key+' : '+str(uniqueDict[key]))
    print('\n')
    i+=1
print('====================================\n\nPermissões comuns de todas APKs\n\n====================================')
numberOfApks = len(answerDict)
mutualPermissions = []
for permission in permissionDict:
    if permissionDict[permission] == numberOfApks:
        mutualPermissions.append(permission)
print(str(mutualPermissions))


# In[ ]:




