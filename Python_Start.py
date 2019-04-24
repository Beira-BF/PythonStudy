#Example 1

x = [1,2,3,4.1,7.1]
s = 0
for i in x:
    s = s + i
a = s / len(x)
print("x=",x)
print("Total",len(x),"elements.")
print("The sum of these elements is ", s)
print("The mean value of these elements is", a)

#Example 2

y = range(1,101)
m = 0
for j in y:
    m = m + j
print("1+2+3+...+100 =",m)

#Example 3

z = range(1,100,2)
n = 0
for k in z:
    n = n + k
print("1+3+5+...+99 =",n)

#Example 4

a = range(10,0,-1)
l = 0
for i in a:
    l = l + i
print("10+9+8+...+1 =",l)

