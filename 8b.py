result = 0
while True:
  try:
   l = raw_input()
  except EOFError:
    break

  quotes = l.count('"')
  slash = l.count('\\')

  result += 2 + slash + quotes

print result
