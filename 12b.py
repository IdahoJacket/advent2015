import itertools
import json

def sumStr( l ):
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
  return sum

def isRed( d ):
  for y in d.items():
    if ( y[1] == 'red' ):
      print d, y
      return True

def sum( j ):
  val = 0
  if isinstance(j, dict):
    if isRed(j):
      return 0
    j = j.items()
  elif isinstance(j,int):
    return j
  elif isinstance(j,basestring):
    return 0


  
  for x in j:
    print x
    if isinstance(x, dict):
      if not isRed(x):
        val += sum( x.items() )
    elif isinstance(x,int):
      val += x
    elif isinstance(x,basestring):
      val += 0
    else:
      for k in x: 
        val += sum( k )
  return val     

while True:
  try:
   l = raw_input()
  except EOFError:
    break

  j = json.loads(l)
  print sum( j )
