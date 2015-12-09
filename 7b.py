values = {}
formulas = {}

while True:
  try:
   l = raw_input().split()
  except EOFError:
    break

  if len(l) == 3:
    if ( l[0].isdigit() ):
      values[l[2]] = int( l[0] )
    else:
      formulas[l[2]] = ( 'ASSIGN', l[0] )
  elif len(l) == 4:
    formulas[l[3]] = ( l[0], l[1] )
  else:
    formulas[l[4]] = ( l[1], l[0], l[2] )

values['b'] = 16076

oldlen = len( formulas ) + 1
while len( formulas ) < oldlen:
  newFormulas = {}
  oldlen = len( formulas )
  for k, v in formulas.items():
    foundAll = True

    count = 2
    if v[0] == 'NOT':
      count = 1
    elif v[0] == 'LSHIFT':
      count = 1
    elif v[0] == 'RSHIFT':
      count = 1
    elif v[0] == 'ASSIGN':
      count = 1
   
    for v2 in v[1:count + 1]:
      if not v2.isdigit() and v2 not in values:
          foundAll = False
          break       

    if foundAll:
      if v[0] == 'NOT':
        if ( v[1].isdigit() ):
          values[k] = ~int(v[1])
        else:
          values[k] = ~values[v[1]]
      elif v[0] == 'AND':
        if ( v[1].isdigit() ):
          val1 = int(v[1])
        else:
          val1 = values[v[1]]
        if ( v[2].isdigit() ):
          val2 = int(v[2])
        else:
          val2 = values[v[2]]
        values[k] = val1 & val2
      elif v[0] == 'OR':
        if ( v[1].isdigit() ):
          val1 = int(v[1])
        else:
          val1 = values[v[1]]
        if ( v[2].isdigit() ):
          val2 = int(v[2])
        else:
          val2 = values[v[2]]
        values[k] = val1 | val2
      elif v[0] == 'LSHIFT':
        values[k] = values[v[1]] << int(v[2])
      elif v[0] == 'RSHIFT':
        values[k] = values[v[1]] >> int(v[2])
      elif v[0] == 'ASSIGN':
        values[k] = values[v[1]]
        
    else:
      newFormulas[k] = v
  
  formulas = newFormulas

for k,v in values.items():
  if v < 0:
    values[k] = ( 2**16) + v
print values['a']
