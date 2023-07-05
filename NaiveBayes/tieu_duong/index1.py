import csv
import random
import math
import sys

# Load datas from CSV

def load_data(filename):
  lines = csv.reader(open(filename,"rb"))
  dataset = list(lines) # danh sach n bo gia tri , moi element la 1 bo gia tri 
  for i in range(len(dataset)):
    dataset[i] = [float(x) for x in dataset[i]]
    
  return dataset

