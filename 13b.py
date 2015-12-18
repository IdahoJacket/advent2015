import itertools

def score( r, x ):
  s = 0
  for p in xrange(0,len(x)):
    s += r[x[p]][x[(p+1)%len(x)]]
    s += r[x[p]][x[p-1]]
  return s
people = set()
r = {}
people.add( 'me' )
while True:
  try:
   l = raw_input()
  except EOFError:
    break
  l = l.split()

  ( p1, a, p2 ) = ( l[0], int(l[3]), l[10] )
  p2 = p2.strip('.')
  if l[2] == 'lose':
    a = -a
  people.add( p1 )
  if p1 not in r:
    r[p1] = { 'me':0 }
  r[p1][p2] = a

r['me'] = {}
for p in people:
  r['me'][p] = 0

p = itertools.permutations(people)
best = -99999999
for x in p:
  s = score( r, x )
  if s > best:
    best = s

print best
