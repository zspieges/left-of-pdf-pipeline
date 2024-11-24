#Pull JSON
from urllib.request import urlopen
import json
from operator import itemgetter
url = ‘<>A URL GOES HERE’
response = urlopen(url)
data = json.loads(response.read())

#Create dicitonary of all value pairs
dict = {}

#Add all key value pairs
for obj in data['keyValuePairs']:
  if 'value' in obj:
    dict[obj['key']['content']] = obj['value']['content']
  else: 
    dict[obj['key']['content']] = None

#Find the right and left most points on the page then use them to calculate middle
left_most_x_list = []
right_most_x_list = []
for obj in data['keyValuePairs']:
  if 'value' in obj:
    left_most_x = max(obj['key']['boundingRegions'][0]['boundingBox'][0], 
                      obj['key']['boundingRegions'][0]['boundingBox'][6],
                      obj['value']['boundingRegions'][0]['boundingBox'][0],
                      obj['value']['boundingRegions'][0]['boundingBox'][6])
  else:
    left_most_x = max(obj['key']['boundingRegions'][0]['boundingBox'][0], 
                      obj['key']['boundingRegions'][0]['boundingBox'][6])
  left_most_x_list.append(left_most_x)

  if 'value' in obj:
    right_most_x = max(obj['key']['boundingRegions'][0]['boundingBox'][2], 
                      obj['key']['boundingRegions'][0]['boundingBox'][4],
                      obj['value']['boundingRegions'][0]['boundingBox'][2],
                      obj['value']['boundingRegions'][0]['boundingBox'][4])
  else:
    right_most_x = max(obj['key']['boundingRegions'][0]['boundingBox'][2], 
                      obj['key']['boundingRegions'][0]['boundingBox'][4])
  right_most_x_list.append(right_most_x)

left_boundary = min(left_most_x_list)
right_boundary = max(right_most_x_list)
dist = right_boundary - left_boundary
middle = dist/2

#Check that all the boxes at least START ('boundingBox'][0]) before the middle. 
#If yes, add key to final list
final = []
for obj in data['keyValuePairs']:
  start_x = obj['key']['boundingRegions'][0]['boundingBox'][0]
  if start_x < middle:
    final.append(obj['key']['content'])

print(final)



