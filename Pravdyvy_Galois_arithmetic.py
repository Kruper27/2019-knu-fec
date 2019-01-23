GF=2**8
g=2
pol_8=[1,0,0,0,1,1,1,0,1]
def pol_mod(pol):
    if len(pol)==8:
        return pol
    else:
        for i in range(len(pol_8)):
            pol[i]^=pol_8[i]
        return pol[1:]
def move(pol):
    if pol[0]==1:
        pol=[0]+pol
    for i in range(1,len(pol)):
        pol[i-1]=pol[i]
    pol[-1]=0
    return pol
gfilog={}
gfilog[0]=1
pol=[0,0,0,0,0,0,0,1]
for i in range(1,GF):
    pol=pol_mod(move(pol))
    count=0
    for j in range(len(pol)):
        if pol[j]!=0:
            count+=2**(len(pol)-j-1)
    gfilog[i]=count
gflog={}
gflog[0]=None
for i in gfilog.keys():
    if i!=255:
        gflog[gfilog[i]]=i
def add(a,b):
    return a^b
def sub(a,b):
    return a^b
def mul(a,b):
    if (a==0) or (b==0):
        return 0
    else:
        return gfilog[(gflog[a]+gflog[b])%GF]
def div(a,b):
    if (a==0):
        return 0
    if (b==0):
        raise ZeroDivisionError
    if gflog[a]<gflog[b]:
        return gfilog[(gflog[a]-gflog[b])+GF-1]
    return gfilog[(gflog[a]-gflog[b])]
if __name__=='__main__':
    print('Starting performance tests')
    from timeit import timeit
    print('123+78 run 1000000 times',timeit('add(123,78)','from Galois_arithmetic import add'))
    print('123-78 run 1000000 times',timeit('sub(123,78)','from Galois_arithmetic import sub'))
    print('123*78 run 1000000 times',timeit('mul(123,78)','from Galois_arithmetic import mul'))
    print('123/78 run 1000000 times',timeit('div(123,78)','from Galois_arithmetic import div'))
