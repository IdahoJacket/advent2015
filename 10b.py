import itertools

while True:
  try:
   l = raw_input().split()
  except EOFError:
    break

l = l[0]
loop = 50

for q in xrange(0,loop):
  result = ""
  prev = l[0]
  count = 0
  for j in xrange(0,len(l)):
    i = l[j]
    if ( i == prev ):
      count += 1
    else:
      result += str( count ) + prev
      count = 1
      prev = i
    j += 1
  

  result += str( count ) + i
  l = result

print len(result)
    
