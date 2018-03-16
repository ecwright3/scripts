import os
import json


test = os.popen('powershell.exe "get-process').read()
print(test[0])
#names = list(map(lambda x: x["Name"], test) )
#print(names)
