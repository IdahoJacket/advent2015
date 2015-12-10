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

  while ( n.hexdigest()[:6] != '000000' ):
    n = hashlib.md5()
    i += 1
    n.update( l + str( i ) )

  print i

