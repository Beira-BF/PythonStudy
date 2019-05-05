import random
a = []
for i in range(0,1000):
    x = random.randint(-105,105)
    a.append(x)
print(a)
print(len(a))
xp = (sum(a))/1000
print(xp)
m = 0
for i in a:
    m += (i-xp)**2
s = (1/(1000-1)*m)**0.5
print(s)

b=[[]for _ in range(21)]
#print(b)
#类似于归一化法，按照比例把数字映射到对应的区间
a1=-105
b1=106
a2=0
b2=21
for i in a:
    n=(i-a1)/(b1-a1)*(b2-a2)
    #print(int(n))
    b[int(n)].append(i)
    
print(b)

# for i in b:
#     print(i)
for i in b:
    for j in i:
        xp = sum(i)/(len(i))
        m += (j-xp)**2
        s = (1/(len(i)-1)*m)**0.5
    print("Sequence：",i,"Average：",xp,"Standard deviation:","%10.4f" % s)
