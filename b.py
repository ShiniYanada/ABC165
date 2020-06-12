x = int(input())
y = 100
count = 0
while (True):
  if y < x:
    y *= 1.01
    y = int(y)
    count += 1
  else:
    break
print(count)
