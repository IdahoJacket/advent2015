totalArea = 0
while True:
  try:
    (x,y,z) = [int(x) for x in raw_input().split('x')]
  except EOFError:
    break
  
  area = 2 * ((x*y)+(x*z)+(y*z))
  smallestSideArea = (x*y*z) / (max(x,y,z))

  totalArea += area + smallestSideArea

print totalArea
