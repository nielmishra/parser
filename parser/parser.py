open_file = open('/home/shinigami/Desktop/test/dump.txt','r')
#write_file = open('/home/shinigami/Desktop/test/parsed.txt','w')

raw_data = open_file.read()
array = raw_data.split('* ')

array.pop(0)

dict_data = {}

for i in range(len(array)):
  dict_data[i] = array[i]
  sample = dict_data[i].split('\n')
  write_file = open('/home/shinigami/Desktop/test/parsed_%s.txt'%(i),'w')
  for j in sample:
    if j.startswith('Index') or j.startswith('--') or j.startswith('/home') or j.startswith('Tra'):
      continue
    else:   
      write_file.write(j+'\n')



