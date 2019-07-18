import csv
import json
import re
import os
import sys
import requests
import base64

PATH  = "./output"

stuff = []

with open('thing.txt', 'w+') as r:
	for path, dirs, files in os.walk(PATH):
		for filename in files:
			fullpath = os.path.join(path, filename)
			with open(fullpath, "r") as f:
				line = f.read()
				values = line.split('\t')
				link = values[4].split('/')
				project = link[3]
				if project.startswith("BPA"):
					program = "bpa"
					proj = project[4:]
				elif project.startswith("JFDI"):
					program = "JFDI"
					proj = project[5:]
				# print(program + "-" +proj)

				s3 = values[4].split('/')
				fName = s3[len(s3)-1]


				dump = json.dumps({"did": values[0], "acl": [program, proj], "file_name": fName, "hashes":{"md5": values[1]}, "size": int(values[2]), "form": "object", "urls":[values[4]]})
				stuff.append(dump)
				r.write(dump)
				r.write(",\n")
			# print(dump)

# url = 'https://qa-bloodpac.planx-pla.net/index/index/'




