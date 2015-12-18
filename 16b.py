import itertools

def score( x, y ):
  s = 1
  for p in xrange( 0, len(x[0]) ):
    propS = 0
    for i in xrange( 0, len(y) ):
      propS += x[i][p] * y[i]
    propS = max( propS, 0 )
    s *= propS
  return s

def genX( x, y ):
  if y > 1:
    for i in xrange( 0, x + 1 ):
      a = x - i
      r = []
      r.append( a )
      for j in genX( x - a, y - 1 ):
        q = r + j
        yield q
  elif y == 1:
    yield [x]
  elif y ==0:
    yield [0]
  
d = {} 
while True:
  try:
   l = raw_input()
  except EOFError:
    break
  l = l.split()

  n = l[1].strip(':')
  d[n] = {}
  for i in xrange( 2, len(l ), 2 ):
    d[n][l[i].strip(':')] = int(l[i+1].strip(','))

o = dict( 
children= 3,
cats= 7,
samoyeds= 2,
pomeranians= 3,
akitas= 0,
vizslas= 0,
goldfish= 5,
trees= 3,
cars= 2,
perfumes= 1
)

for a in d.items():
  found = True
  for i in a[1].items():
    if i[0] in ( 'cats', 'trees' ):
      if i[1] <= o[i[0]]:
        found = False
        break
    elif i[0] in ( 'pomeranians', 'goldfish' ):
		  if i[1] >= o[i[0]]:
			  found = False
		 	  break
    elif i[1] != o[i[0]]:
      found = False
      break
  if found:
    print a[0]
