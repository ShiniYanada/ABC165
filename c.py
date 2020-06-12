n, m , q = list(map(int, input().split()))
lists = []
sequence = [1] * n
output = 0
for i in range(q):
  lists.append(list(map(int, input().split())))
  
while (True):
  score = 0
  limit_digit = -1
  for i in range(q):
    if sequence[lists[i][1] - 1] - sequence[lists[i][0] - 1] == lists[i][2]:
      score += lists[i][3]
  if output < score:
    output = score
  for i in range(n):
    if sequence[n - i - 1] == m:
      limit_digit = n - i - 1
  if limit_digit == 0:
    break
  elif limit_digit == -1:
    sequence[n - 1] += 1
  else:
    if limit_digit == 1:
      sequence = [sequence[0] + 1] * n
    else:
      sequence[limit_digit - 1] += 1
      for k in range(limit_digit, n):
        sequence[k] = sequence[limit_digit - 1]

print(output)
      
