import itertools

def score( x, y ):
  s = 1
  for p in xrange( 0, len(x[0]) ):
    propS = 0
    for i in xrange( 0, len(y) ):
      propS += x[i][p] * y[i]
    propS = max( propS, 0 )
    s *= propS
  return s

def genX( x, y ):
  if y > 1:
    for i in xrange( 0, x + 1 ):
      a = x - i
      r = []
      r.append( a )
      for j in genX( x - a, y - 1 ):
        q = r + j
        yield q
  elif y == 1:
    yield [x]
  elif y ==0:
    yield [0]
  
 
i = 0
x = []

while True:
  try:
   l = raw_input()
  except EOFError:
    break
  l = l.split()

  x.append([])
  for y in xrange( 2, 10, 2 ):
    x[i].append(int(l[y].strip(',')))
  i += 1
print x

best = 0

for q in genX( 100, i ):
  s = score( x, q )
  print q, s
  if s > best:
    best = s

print best
