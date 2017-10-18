import json
from os import listdir
from os.path import isfile, join

data = json.load("instances_train2014.json")

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk("/home/sunand/sunandFastMask/data"):
    f.extend(filenames)
    break

count = 0
tempList = []
for i in range(500):

	if data["images"][i]["images"] in f:
		tempList.append(data["images"][i])
	count += 1
	if count == len(f):
		break

print(tempList)

