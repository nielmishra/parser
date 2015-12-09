#!/usr/bin/python
__name__ = '__main__'
import os
import sys
import numpy as np

import matplotlib
import matplotlib.pyplot as plt


def get_plot_files(file):
    open_file = open(os.path.realpath(file),'r')
    raw_data = open_file.read()
    array = raw_data.split('* ')
    
    array.pop(0)
    dict_data = {}
    parameters = []
    parsed_files = []
    
for i in range(len(array)):
  dict_data[i] = array[i]
  sample = dict_data[i].split('\n')
  write_file = open('/home/shinigami/Desktop/parser_%s'%(i),'w')
  for j in sample:
    if j.startswith('Index') or j.startswith('--') or j.startswith('/home') or j.startswith('Tra'):
      continue
    else:   
      write_file.write(j+'\n')
      
      
for i in range(len(array)):
        dict_data[i] = array[i]
        
        sample = dict_data[i].split('\n')

        write_file = open('parsed_%s.txt'%(i),'w')      
      
      
      
