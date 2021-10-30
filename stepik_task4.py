import requests

with open('file.txt') as inf:
    line = inf.readline().strip()

file = requests.get(line)
lst = file.text.splitlines()
print(len(lst))
