import json
from os import listdir
from os.path import isfile, join

data = json.load(open("instances_train2014.json"))

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk("/home/sunand/sunandFastMask/data"):
    f.extend(filenames)
    break

count = 0
tempList = []
info = data["info"]
newJson = open("tempJson.json", "w")
json.dump(info, newJson)
for i in range(500):

	if data["images"][i]["images"] in f:
		tempList.append(data["images"][i])
	count += 1
	if count == len(f):
		break

print(tempList)

