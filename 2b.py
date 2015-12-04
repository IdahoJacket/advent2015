totalArea = 0
while True:
  try:
    (x,y,z) = [int(x) for x in raw_input().split('x')]
  except EOFError:
    break
  
  volume = (x*y*z)
  smallestPerimeter = (x+x+y+y+z+z) - (max(x,y,z)*2)

  totalArea += volume + smallestPerimeter

print totalArea
