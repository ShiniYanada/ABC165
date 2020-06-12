k = int(input())
a, b = list(map(int, input().split()))
output = 'NG'
for i in range(a, b + 1):
  if i % k == 0:
    output = 'OK'
    break
print(output)
