arr = [3, 5, 9, 4, 6]
x = arr[0]

for i in range(0, len(arr) - 1):
    if arr[i] < x:
        x = arr[i+1]

print(x)
