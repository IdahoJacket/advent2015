import itertools

#t = 1000
t = 2503

best = 0
r = {}
d = {}
g = {}
w = {}
p = {}
while True:
  try:
   l = raw_input()
  except EOFError:
    break

  l = l.split()

  
  x = ( int(l[3]), int(l[6]), int(l[13]) )
  r[l[0]] = x
  d[l[0]] = 0
  g[l[0]] = x[1]
  w[l[0]] = x[2]
  p[l[0]] = 0

for s in xrange( 0, t ):
  bestD = 0
  for j in r:
    if g[j] > 0:
      g[j] -= 1
      d[j] += r[j][0]
    else:
      w[j] -= 1
      if w[j] == 0:
        g[j] = r[j][1]
        w[j] = r[j][2]
    if d[j] > bestD:
      bestD = d[j]

  for j in r:
    if d[j] == bestD:
      p[j] += 1

print p
