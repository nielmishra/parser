import os
import sys
import numpy as np

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def get_plot_files(file):
    open_file = open(os.path.realpath(file),'r')
    raw_data = open_file.read()
    array = raw_data.split('* ')
    
    array.pop(0)
    dict_data = {}
    parameters = []
    parsed_files = []
    dir1 = str(file)
        
    os.mkdir(dir1[:-4])
    for i in range(len(array)):
        dict_data[i] = array[i]
        
        sample = dict_data[i].split('\n')
        write_file = open(os.path.realpath(dir1[:-4])+'/parsed_%s.txt'%(i),'w')
      
        for j in sample[3:]:
            if j.startswith('Index'):
                items = j.split()
                parameters.append(items) if len(parameters) < i+1 else None
                continue
            if j.startswith('--'): 
                continue
            else:   
                write_file.write(j+'\n')

        parsed_files.append(os.path.realpath(dir1[:-4])+'/parsed_%s.txt'%(i))
    return parameters, parsed_files    

def loudew(file):
    parameters, parsed_files = get_plot_files(file)  

    for plot_file, parameter in zip(parsed_files, parameters):
        data = np.loadtxt(plot_file, unpack=True, dtype=str)
        for i in range(2, len(data)):

            plt.plot([x.strip(',') for x in data[1]], [y.strip(',') for y in data[i]])
            try:
                plt.xlabel(parameter[1]), plt.ylabel(parameter[i]) 
                plt.title('%s  vs  %s'%(parameter[1], parameter[i]))
                plt.savefig(plot_file+str(i)+'.png'), plt.clf()
            except IndexError:
                plt.xlabel(parameter[1]), plt.ylabel('missing y label')
                plt.title('%s  vs  missing y label'%(parameter[1], ))
                plt.savefig(plot_file+str(i)+'.png'), plt.clf()
          

def main():

    files = sys.argv[1:]
    for fi in files:
        loudew(fi)
              
if __name__ == '__main__':
    main()
