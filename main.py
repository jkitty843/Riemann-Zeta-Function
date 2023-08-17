def rzf(s):
  y = 0
  for d in range(1000):
    y += (1 / pow((d + 1), s))
  return y


while True:
  print('Enter a value for the RZF: \n')
  s = float(input())
  print(f'Output: {str(rzf(s))}')
