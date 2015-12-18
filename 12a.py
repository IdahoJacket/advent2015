import itertools

while True:
  try:
   l = raw_input()
  except EOFError:
    break

  inString = False
  sum = 0
  num = 0
  neg = 1
  for c in l:
    if not inString and c.isdigit() or c == '-':
      if c == '-':
        neg = -1
      else:
        num *= 10
        num += int(c)
    else:
      sum += num * neg
      num = 0
      neg = 1
      if c == '"':
        inString = not inString
  sum += num * neg

  print sum
