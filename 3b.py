totalArea = 0
while True:
  try:
   l = raw_input()
  except EOFError:
    break
  x = [0,0]
  y = [0,0]
  used = set()
  used.add( ( x[0], y[0] ) )
  i = 0
  for d in l:
    index = i % 2
    if d == '<':
      x[index] -= 1
    elif d == '>':
      x[index] += 1
    elif d == 'v' or d == 'V':
      y[index] -= 1
    elif d == '^':
      y[index] += 1
    used.add( (x[index],y[index]) )
    i += 1

  print len(used)

