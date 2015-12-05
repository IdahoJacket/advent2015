import hashlib

niceCount = 0
while True:
  try:
   l = raw_input()
  except EOFError:
    break
  
  double = False

  pairs = zip(l,l[1:])
  i = 0
  for p in pairs:
    if p in pairs[i+2:]:
      double = True
      break
    i += 1
  print double

  i = 0
  repeat = False
  for c in l[:-2]:
    if l[i + 2] == c:
      repeat = True
      break
    i += 1
  print repeat

  if double and repeat:
    niceCount += 1

print niceCount
