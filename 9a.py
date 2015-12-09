import itertools

table = {}
while True:
  try:
   l = raw_input().split()
  except EOFError:
    break

  src = l[0]
  dest = l[2]
  dist = l[4]
  
  if src not in table:
    table[src] = {}
  if dest not in table:
    table[dest] = {}

  table[src][dest] = int(dist)
  table[dest][src] = int(dist)

p = []
p.append( src )
for d in table[src]:
  p.append( d )

mincost = 999999
for x in itertools.permutations(p):
  print x
  cost = 0
  for i in xrange(0, len(x) - 1):
    cost += table[x[i]][x[i+1]]
  mincost = min( cost, mincost )

print mincost
