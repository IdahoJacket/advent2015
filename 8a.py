result = 0
while True:
  try:
   l = raw_input()
  except EOFError:
    break

  result += len(l) - len(eval(l))

print result
