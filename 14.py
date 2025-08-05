n = 0
arr = [1,5,7,2,6,5,4,9,8,12,14,16,18]
for i in range(0 ,len(arr)):
  if arr[i] % 2 ==0:
    n = n+arr[i]
print(n)