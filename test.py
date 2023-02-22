import json

with open('static/data.json') as f:
    data = json.load(f)

# Print the data to verify that it has been loaded correctly
print(data)


for item in data:
    values = (item["title"], item["url"], item["image"])
    print(values)