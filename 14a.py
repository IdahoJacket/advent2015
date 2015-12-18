import itertools

t = 2503

best = 0

while True:
  try:
   l = raw_input()
  except EOFError:
    break

  s = t
  l = l.split()

  ( speed, go, rest ) = ( int(l[3]), int(l[6]), int(l[13]) )

  d = 0
  while s > 0:
    d += speed * min(go,s)
    s -= go + rest
  if d > best:
    best = d
print best
