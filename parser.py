open_file = open('/home/shinigami/Desktop/testing/dump.txt','r')
#write_file = open('/home/shinigami/Desktop/testing/parsed.txt','w')
import json
a = open_file.read()

z = a.split('\n')
z.pop(0)
z.pop(0)
z.pop(0)
z.pop(0)
z.pop(0)

'''for i in z:
  if i.startswith('\n'):
    z.remove(i)
'''
for j in z:
  #write_file.write
    b = json.dumps (j+ '\n')
    print b


