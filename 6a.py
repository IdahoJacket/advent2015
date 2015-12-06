import hashlib

size = 1000
niceCount = 0
grid = [[0 for x in xrange(size)] for x in xrange(size)]
while True:
  try:
   l = raw_input().split()
  except EOFError:
    break

  
  start = 2
  stop = 4
  if l[0] == 'toggle':
    start = 1
    stop = 3
    op = 2
  elif l[1] == 'on':
    op = 1
  else:
    op = 0

  startX, startY = [int(x) for x in l[start].split(',')]
  stopX, stopY = [int(x) for x in l[stop].split(',')]
  
  for x in xrange(startX,stopX+1):
    for y in xrange(startY,stopY+1):
      if op != 2:
        grid[x][y] = op
      elif grid[x][y] == 0:
        grid[x][y] = 1
      else:
        grid[x][y] = 0

  # print grid

print sum( [sum(x) for x in grid] )
