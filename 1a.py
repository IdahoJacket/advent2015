data = raw_input()

floor = 0
count = 1
for c in data:
  if c == '(':
    floor += 1
  elif c == ')':
    floor -= 1
  
print floor
