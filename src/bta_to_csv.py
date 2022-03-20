__author__ = "Sanjay Somanath"

import Grasshopper as gh
import os
import csv
from os.path import exists
#Geth the local directory
gh_path = str(os.path.dirname(gh.Instances.DocumentServer.Document[0].FilePath))+'\csv'
if not os.path.exists(gh_path):
    os.makedirs(gh_path)
csv_key = []
for i in range(len(units)):
    csv_key.append('unit '+ str(i))
csv_value = []
csv_block = []
for i in bta:
    csv_block.append('Block ' + str(active_curve))
#csv_value.append(active_curve)
for i in bta:
    csv_value.append(i)
if write_csv:
    filepath = gh_path + "\\" + "block_" + str(active_curve) + '.csv'
    file = open(filepath, "wb")
    writer = csv.writer(file)
    for w in range(len(units)):
      writer.writerow([csv_block[w], csv_key[w], csv_value[w]])
    file.close()