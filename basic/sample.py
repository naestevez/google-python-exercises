import re

filename = open('/Users/Alex/Documents/google-python-exercises/basic/small.txt')
f = filename.read().lower()
f = re.findall(r"[\w']+|[.,!?;]", f)
f = sorted(f)
dict = {}
count = 0

while count < len(f):
  if f[count] not in dict.keys():
    dict[f[count]] = 1
  elif f[count] in dict.keys():
    dict[f[count]] += 1
  count += 1

print dict
filename.close()
