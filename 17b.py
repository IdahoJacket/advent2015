import itertools

minC = 9999
minCCount = 0

def fill( d, v, c ):
  global minC
  global minCCount
  if len(d) == 0:
    return 0
  elif d[0] == v:
    if ( c + 1 ) < minC:
      minC = c + 1
    if ( c + 1 ) == minC:
      minCCount += 1
    return 1 + fill( d[1:], v, c )
  elif d[0] < v:
    return fill( d[1:], v, c) + fill( d[1:], v - d[0], c + 1 )
  else:
    return fill( d[1:], v, c)

d = [] 
while True:
  try:
   l = raw_input()
  except EOFError:
    break

  d.append(int(l))

v = 150
#v = 25
d = sorted(d)

print fill(d,v,0)
print minC, minCCount
