# Method 1

x = [10, 8, -1, 100, 200, 35]
mx = x[0]
for i in range(0,len(x)):
    if mx < x[i]:
        mx = x[i]
print("x =",x)
print("The maximum value of x is",mx)

# Method 2

x = [10, 8, -1, 100, 200, 35]
mx = x[0]
for y in x:
    if mx < y:
        mx = y
print("x =",x)
print("The maximum value of x is",mx)

# Method 3
x = [10, 8, -1, 100, 200, 35]
mx = x[0]
i = 0
while i < len(x):
    if mx < x[i]:
        mx = x[i]
    i = i + 1
print("x =",x)
print("The maximum value of x is",mx)

# Method 4

x = [10, 8, -1, 100, 200, 35]
mx = x[0]
i = len(x)-1
while i >= 0:
    if mx < x[i]:
        mx = x[i]
    i = i - 1
print("x =",x)
print("The maximum value of x is", mx)