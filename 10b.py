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
  j = 0
  prev = int(l[0])
  count = 0
  while j < len(l):
    #print "j=",j,"l[j]=",l[j]
    i = int(l[j])
    if ( i == prev ):
      count += 1
      #print "inc"
    else:
      result += str( count ) + str( prev )
      #print result
      count = 1
      prev = i
    j += 1
  

  result += str( count ) + str( i )
  #print "Result ", result
  l = result

print len(result)
    
