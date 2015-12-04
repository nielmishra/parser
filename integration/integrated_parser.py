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
