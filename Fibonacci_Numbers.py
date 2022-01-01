# Fibonacci numbers output = (1, 1, 2, 3, 5, 8 ,13, 21, 34, 55)
array = []
b, c = 0, 0
while c < 55:
  if len(array) < 2:
    array.append(1)
  else:
      c = array[(b + 1)] + array[b]
      b += 1
      array.append(c)
print(array)