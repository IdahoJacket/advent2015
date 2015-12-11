import itertools

while True:
  try:
   l = raw_input()
  except EOFError:
    break

#test = 10
#while test > 0:
  #test -= 1
while True:
  n = ""
  for i in xrange( len(l) - 1, 0, -1 ):
    if ( l[i] ) == 'z':
      n += 'a'
    else:
      n += chr( ord(l[i]) + 1 )
      n += l[i-1::-1]
      break

  n = n[::-1] 

  print n
  straight = False
  for y in [n[i:i+3] for i in xrange(0,len(n)-2)]:
    if (ord(y[0]) == ord(y[1]) - 1 and ord(y[1]) == ord(y[2]) - 1):
      print y
      straight = True
      break
  #print straight

  banned = reduce( lambda x, y: x or y, [x in "iol" for x in n])
  #print banned

  double = 0
  p = n[0]
  pp = None
  for c in n[1:]:
    if p == c and not pp == c:
      double += 1
    pp = p
    p = c
  print n, double, banned, straight
 
  if double >=2 and not banned and straight:
    break

  l = n

print n
