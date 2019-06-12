x1=int(input())
x2=int(input())
global v
def change(x1, x2):
    v=['0']
    for i in range(x1):
        v.append('1')
    v.append('*')
    for i in range(x2):
        v.append('1')
    v.append('=')
    v.append('0')
    return v
v=change(x1, x2)

def rule1(v):
    i=0
    while v[i]!='*':
        i=i+1
    print(v)
    rule2(v, i)
def rule2(v, i):
    i=i+1
    v[i]='a'
    print(v)
    rule3(v, i)
def rule3(v, i):
    while v[i]!='*':
        i=i-1
    print(v)
    rule3_1(v, i)
def rule3_1(v, i):
    while True:
        i=i-1
        if v[i]=='1' or v[i]=='0':
            break
    print(v)
    if v[i]=='1':
        rule4(v, i)
    if v[i]=='0':
        rule7(v, i)
def rule4(v, i):
    v[i]='a'
    print(v)
    rule5(v, i)
def rule5(v, i):
    while v[i]!='0':
        i=i+1
    v[i]='1'
    print(v)
    rule6(v, i)
def rule6(v, i):
    v.append('0')
    i=i+1
    print(v)
    rule3(v, i)
def rule7(v, i):
    while True:
        i=i+1
        if v[i]=='*':
            break
        v[i]='1'
        print(v)
    rule8(v, i)
def rule8(v, i):
    while True:
        i=i+1
        if v[i]=='1' or v[i]=='=':
            break
    if v[i]=='1':
        v[i]='a'
        print(v)
        rule3(v, i)
    else: ruleend(v);
def ruleend(v):
    print(v)
    j=len(v)-1
    while v[j]!='=':
        j=j-1
    ans=len(v)-2-j
    print('ans:', ans)
rule1(v)
