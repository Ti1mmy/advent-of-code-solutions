original = [int(s) for s in input().split(',')]
o = original.copy()
input = 5
outputs = []
go = True


def assignpara(oc, ocpos, opos):
    print(opos)
    if oc[ocpos] == 0:
        return o[o[n + opos]]
    elif oc[ocpos] == 1:
        return o[n + opos]


def parse(n):
    oc = str(o[n])
    if len(oc) < 5:
        oc = (5-len(oc))*'0' + oc
    oc = [int(s) for s in oc]
    if oc[-1] == 1 or oc[-1] == 2:
        a = 0
        b = 0
        a = assignpara(oc, -3, 1)
        b = assignpara(oc, -4, 2)
        if oc[-1] == 1:
            c = a + b 
        elif oc[-1] == 2:
            c = a * b
        o[o[n + 3]] = c
        return n + 4

    elif oc[-1] == 3:
        o[o[n + 1]] = input
        return n + 2

    elif oc[-1] == 4:
        a = assignpara(oc, -3, 1)
        outputs.append(a)
        return n + 2
    
    elif oc[-1] == 5 or oc[-1] == 6:
        a = 0
        b = 0
        a = assignpara(oc, -3, 1)
        b = assignpara(oc, -4, 2)
        
        if oc[-1] == 5:
            if a != 0:
                return b
        elif oc[-1] == 6:
            if a == 0:
                return b
        return n + 3

    elif oc[-1] == 7:
        a = 0
        b = 0
        a = assignpara(oc, -3, 1)
        b = assignpara(oc, -4, 2)
        if a < b:
            o[o[n+3]] = 1
        else: 
            o[o[n+3]] = 0
        return n + 4
    
    elif oc[-1] == 8:
        a = 0
        b = 0
        a = assignpara(oc, -3, 1)
        b = assignpara(oc, -4, 2)
        if a == b:
            o[o[n+3]] = 1
        else:
            o[o[n+3]] = 0
        return n + 4

    elif oc[-1] == 9 and oc[-2] == 9:
        global go
        go = False
        return n + 1
n = 0
while go:
    n = parse(n)
    print(outputs)
print(outputs)