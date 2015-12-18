import itertools

def fill( d, v ):
  if len(d) == 0:
    return 0
  elif d[0] == v:
    return 1 + fill( d[1:], v )
  elif d[0] < v:
    return fill( d[1:], v) + fill( d[1:], v - d[0] )
  else:
    return fill( d[1:], v)

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

print fill(d,v)
