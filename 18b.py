import itertools

#size = 6
size = 100
pSize = size + 2
d = [] 
d.append( '.'*pSize )
while True:
  try:
   l = raw_input()
  except EOFError:
    break

  d.append('.' + l + '.')
d.append( '.'*pSize )

loops = 100
for l in xrange( 0, loops):
  g = d
  d = []
  d.append( '.'*pSize )
  for i in xrange( 1, size + 1 ):
    d.append( '.' )
    for j in xrange( 1, size + 1):
      onCount = 0
      if ( i, j ) in ( ( 1, 1 ), (1, size), (size,1), (size,size)):
        d[i] += '#'
      else:
        for k in xrange( -1, 2 ):
          for m in xrange( -1, 2 ):
            if g[i+k][j+m] == '#':
              onCount += 1
        if g[i][j] == '#':
          onCount -= 1
          if onCount in (2,3):
            d[i] += '#'
          else:
            d[i] += '.'
        else:
          if onCount == 3:
            d[i] += '#'
          else:
            d[i] += '.'
    d[i] += '.'
  d.append( '.'*pSize )
print sum((x.count('#') for x in d))
