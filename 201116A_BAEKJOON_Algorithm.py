#에라토스테네스의 체 
#1 부터 100사이의 소수 구해보기

n = 100
def isPrime(a):
    if(a<2):
        return False
    for i in range(2,a):
        if(a%1==0):
            return False
    return True

for i in range(n+1):
    if(isPrime(i)):
        print(i)

        n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)