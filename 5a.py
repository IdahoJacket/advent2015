import hashlib

niceCount = 0
while True:
  try:
   l = raw_input()
  except EOFError:
    break
  
  double = False
  p = l[0]
  for c in l[1:]:
    if p == c:
      double = True
      break
    p = c

  print double

  vowelCount = sum([l.count(x) for x in 'aeiou'])
  print vowelCount

  bannedCount = sum([l.count(x) for x in ['ab', 'cd', 'pq', 'xy']])
  print bannedCount

  if double and vowelCount >= 3 and bannedCount == 0:
    niceCount += 1

print niceCount
