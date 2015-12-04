import hashlib

totalArea = 0
while True:
  try:
   l = raw_input()
  except EOFError:
    break

  o = hashlib.md5()

  o.update( l )

  n = o.copy()
  i = -1

  while ( n.hexdigest()[:5] != '000000' ):
    i += 1
    n = o.copy()
    n.update( str( i ) )

  print i

