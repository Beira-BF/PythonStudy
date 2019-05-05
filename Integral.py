def f(x,sigma,miu):
    exp = 2.7182818284590452353
    pi = 3.1415926535897932384
    part1 = 1.0/(sigma*((2.0*pi)**0.5))
    part2 = -(x-miu)**2.0/(2.0*sigma**2.0)
    return part1*(exp**part2)

a = f(-2,1.5,1.0)
print("f 在-2的取值：",a)

def integralf(xa,xb,n,sigma,miu):
    s = (xb-xa)/n
    ret = 0.0
    for i in range(0,n):
        ret += (f((xa+i*s),sigma,miu)+f((xa+(i+1)*s),sigma,miu))*s/2.0
    return ret

b = integralf(-2,4,1000,1.5,1.0)
print("f 在-2到4之间的积分：",b)

def integall(sigma,miu):
    xa = -5
    xb = 5
    n = 1000
    esp = 1e-8
    while True:
        I1 = integralf(xa,xb,n, sigma,miu)
        I2 = integralf(2*xa,2*xb,4*n,sigma,miu)
        ans = abs(I2-I1)
        n = 4*n
        xa = 2*xa
        xb = 2*xb
        if ans < esp:
            return I2

c = integall(1.5,1.0)
print("f 在正负无穷之间的积分：","%10.5f" % c, end=" ")
