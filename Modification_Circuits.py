import math
import random
import copy
import time
def Modify_circuits(n,m,origin_XORs,origin_NLs,origin_NOTs,mode = 'modified'):
    origin_depth = estimate_depth(n,m,origin_XORs,origin_NLs,origin_NOTs)
    origin_XORnum = sum([len(origin_XORs[r])-1 for r in origin_XORs])
    if mode == 'modified':
        while(True):
            XORs = copy.deepcopy(origin_XORs); NLs = origin_NLs[:]; NOTs = origin_NOTs[:] 
            new_NL = [random.choice(['&','|','!&','!|']) for _ in range(len(NLs))]
            for i in range(len(NLs)):
                if (NLs[i] == '&') and (new_NL[i] == '!&'):
                    XORs,NLs,NOTs = AND_to_NAND(XORs,NLs,NOTs,i)
                elif (NLs[i] == '&') and (new_NL[i] == '|'):
                    XORs,NLs,NOTs = AND_to_OR(XORs,NLs,NOTs,i)
                elif (NLs[i] == '&') and (new_NL[i] == '!|'):
                    XORs,NLs,NOTs = AND_to_NOR(XORs,NLs,NOTs,i)
                elif (NLs[i] == '!&') and (new_NL[i] == '&'):
                    XORs,NLs,NOTs = NAND_to_AND(XORs,NLs,NOTs,i)
                elif (NLs[i] == '!&') and (new_NL[i] == '|'):
                    XORs,NLs,NOTs = NAND_to_OR(XORs,NLs,NOTs,i)
                elif (NLs[i] == '!&') and (new_NL[i] == '!|'):
                    XORs,NLs,NOTs = NAND_to_NOR(XORs,NLs,NOTs,i)
                elif (NLs[i] == '|') and (new_NL[i] == '&'):
                    XORs,NLs,NOTs = OR_to_AND(XORs,NLs,NOTs,i)
                elif (NLs[i] == '|') and (new_NL[i] == '!&'):
                    XORs,NLs,NOTs = OR_to_NAND(XORs,NLs,NOTs,i)
                elif (NLs[i] == '|') and (new_NL[i] == '!|'):
                    XORs,NLs,NOTs = OR_to_NOR(XORs,NLs,NOTs,i)
                elif (NLs[i] == '!|') and (new_NL[i] == '&'):
                    XORs,NLs,NOTs = NOR_to_AND(XORs,NLs,NOTs,i)
                elif (NLs[i] == '!|') and (new_NL[i] == '!&'):
                    XORs,NLs,NOTs = NOR_to_NAND(XORs,NLs,NOTs,i)
                elif (NLs[i] == '!|') and (new_NL[i] == '|'):
                    XORs,NLs,NOTs = NOR_to_OR(XORs,NLs,NOTs,i)
            
            new_ver = [random.choice(['1','2','3']) for _ in range(len(NLs))]
            for i in range(len(NLs)):
                if new_ver[i] == '2':
                    if (NLs[i] == '&') or (NLs[i] == '!&'):
                        XORs,NLs,NOTs = AND_NAND_ver2(XORs,NLs,NOTs,i)
                    elif (NLs[i] == '|') or (NLs[i] == '!|'):
                        XORs,NLs,NOTs = OR_NOR_ver2(XORs,NLs,NOTs,i)
                if new_ver[i] == '3':
                    if (NLs[i] == '&') or (NLs[i] == '!&'):
                        XORs,NLs,NOTs = AND_NAND_ver3(XORs,NLs,NOTs,i)
                    elif (NLs[i] == '|') or (NLs[i] == '!|'):
                        XORs,NLs,NOTs = OR_NOR_ver3(XORs,NLs,NOTs,i)
            depth = estimate_depth(n,m,XORs,NLs,NOTs)
            XORnum = sum([len(XORs[r])-1 for r in XORs])
            if depth <= origin_depth:
                if XORnum <= int(origin_XORnum*1.15):
                    break
    else:
        XORs = copy.deepcopy(origin_XORs); NLs = origin_NLs[:]; NOTs = origin_NOTs[:] 
        depth = origin_depth

    return XORs,NLs,NOTs,depth

def estimate_depth(n,m,XORs,NLs,NOTs):
    D = {f'x[{_}]':0 for _ in range(n)}
    k = len(NLs)
    for i in range(k):
        D[f'r[{2*i}]'] = math.ceil(math.log2(sum([1<<D[X] for X in XORs[f'r[{2*i}]']])))
        D[f'r[{2*i+1}]'] = math.ceil(math.log2(sum([1<<D[X] for X in XORs[f'r[{2*i+1}]']])))
        D[f'g[{i}]'] = max(D[f'r[{2*i}]'], D[f'r[{2*i+1}]']) + 1
    for i in range(m):
        D[f'y[{i}]'] = math.ceil(math.log2(sum([1<<D[X] for X in XORs[f'y[{i}]']])))
    d = max([D[f'y[{i}]'] for i in range(m)])
    return d

def AND_to_OR(XORs,NLs,NOTs,i):
    new_XORs = copy.deepcopy(XORs)
    new_NLs = NLs[:]
    new_NOTs = NOTs[:]

    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            for x in new_XORs[f'r[{2*i}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            for x in new_XORs[f'r[{2*i+1}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            if (f'r[{2*i}]' in new_NOTs) ^ (f'r[{2*i+1}]' in new_NOTs):
                if r in new_NOTs:
                    new_NOTs.remove(r)
                else:
                    new_NOTs.append(r)
    new_NLs[i] = '|'
    return new_XORs, new_NLs, new_NOTs

def AND_to_NAND(XORs,NLs,NOTs,i):
    new_XORs = copy.deepcopy(XORs)
    new_NLs = NLs[:]
    new_NOTs = NOTs[:]
    
    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            if r in new_NOTs:
                new_NOTs.remove(r)
            else:
                new_NOTs.append(r)
    new_NLs[i] = '!&'
    return new_XORs, new_NLs, new_NOTs

def AND_to_NOR(XORs,NLs,NOTs,i):
    new_XORs = copy.deepcopy(XORs)
    new_NLs = NLs[:]
    new_NOTs = NOTs[:]

    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            for x in new_XORs[f'r[{2*i}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            for x in new_XORs[f'r[{2*i+1}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            if (f'r[{2*i}]' in new_NOTs) ^ (f'r[{2*i+1}]' in new_NOTs):
                if r in new_NOTs:
                    new_NOTs.remove(r)
                else:
                    new_NOTs.append(r)
    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            if r in new_NOTs:
                new_NOTs.remove(r)
            else:
                new_NOTs.append(r)
    new_NLs[i] = '!|'
    return new_XORs, new_NLs, new_NOTs

def OR_to_AND(XORs,NLs,NOTs,i):
    new_XORs = copy.deepcopy(XORs)
    new_NLs = NLs[:]
    new_NOTs = NOTs[:]

    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            for x in new_XORs[f'r[{2*i}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            for x in new_XORs[f'r[{2*i+1}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            if (f'r[{2*i}]' in new_NOTs) ^ (f'r[{2*i+1}]' in new_NOTs):
                if r in new_NOTs:
                    new_NOTs.remove(r)
                else:
                    new_NOTs.append(r)
    new_NLs[i] = '&'
    return new_XORs, new_NLs, new_NOTs

def OR_to_NAND(XORs,NLs,NOTs,i):
    new_XORs = copy.deepcopy(XORs)
    new_NLs = NLs[:]
    new_NOTs = NOTs[:]

    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            for x in new_XORs[f'r[{2*i}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            for x in new_XORs[f'r[{2*i+1}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            if (f'r[{2*i}]' in new_NOTs) ^ (f'r[{2*i+1}]' in new_NOTs):
                if r in new_NOTs:
                    new_NOTs.remove(r)
                else:
                    new_NOTs.append(r)
    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            if r in new_NOTs:
                new_NOTs.remove(r)
            else:
                new_NOTs.append(r)
    new_NLs[i] = '!&'
    return new_XORs, new_NLs, new_NOTs

def OR_to_NOR(XORs,NLs,NOTs,i):
    new_XORs = copy.deepcopy(XORs)
    new_NLs = NLs[:]
    new_NOTs = NOTs[:]

    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            if r in new_NOTs:
                new_NOTs.remove(r)
            else:
                new_NOTs.append(r)
    new_NLs[i] = '!|'
    return new_XORs, new_NLs, new_NOTs

def NAND_to_AND(XORs,NLs,NOTs,i):
    new_XORs = copy.deepcopy(XORs)
    new_NLs = NLs[:]
    new_NOTs = NOTs[:]
    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            if r in new_NOTs:
                new_NOTs.remove(r)
            else:
                new_NOTs.append(r)
    new_NLs[i] = '&'
    return new_XORs, new_NLs, new_NOTs

def NAND_to_OR(XORs,NLs,NOTs,i):
    new_XORs = copy.deepcopy(XORs)
    new_NLs = NLs[:]
    new_NOTs = NOTs[:]

    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            for x in new_XORs[f'r[{2*i}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            for x in new_XORs[f'r[{2*i+1}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            if (f'r[{2*i}]' in new_NOTs) ^ (f'r[{2*i+1}]' in new_NOTs):
                if r in new_NOTs:
                    new_NOTs.remove(r)
                else:
                    new_NOTs.append(r)
    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            if r in new_NOTs:
                new_NOTs.remove(r)
            else:
                new_NOTs.append(r)
    new_NLs[i] = '|'
    return new_XORs, new_NLs, new_NOTs

def NAND_to_NOR(XORs,NLs,NOTs,i):
    new_XORs = copy.deepcopy(XORs)
    new_NLs = NLs[:]
    new_NOTs = NOTs[:]

    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            for x in new_XORs[f'r[{2*i}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            for x in new_XORs[f'r[{2*i+1}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            if (f'r[{2*i}]' in new_NOTs) ^ (f'r[{2*i+1}]' in new_NOTs):
                if r in new_NOTs:
                    new_NOTs.remove(r)
                else:
                    new_NOTs.append(r)
    new_NLs[i] = '!|'
    return new_XORs, new_NLs, new_NOTs

def NOR_to_AND(XORs,NLs,NOTs,i):
    new_XORs = copy.deepcopy(XORs)
    new_NLs = NLs[:]
    new_NOTs = NOTs[:]

    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            for x in new_XORs[f'r[{2*i}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            for x in new_XORs[f'r[{2*i+1}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            if (f'r[{2*i}]' in new_NOTs) ^ (f'r[{2*i+1}]' in new_NOTs):
                if r in new_NOTs:
                    new_NOTs.remove(r)
                else:
                    new_NOTs.append(r)
    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            if r in new_NOTs:
                new_NOTs.remove(r)
            else:
                new_NOTs.append(r)
    new_NLs[i] = '&'
    return new_XORs, new_NLs, new_NOTs

def NOR_to_NAND(XORs,NLs,NOTs,i):
    new_XORs = copy.deepcopy(XORs)
    new_NLs = NLs[:]
    new_NOTs = NOTs[:]

    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            for x in new_XORs[f'r[{2*i}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            for x in new_XORs[f'r[{2*i+1}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            if (f'r[{2*i}]' in new_NOTs) ^ (f'r[{2*i+1}]' in new_NOTs):
                if r in new_NOTs:
                    new_NOTs.remove(r)
                else:
                    new_NOTs.append(r)
    new_NLs[i] = '!&'
    return new_XORs, new_NLs, new_NOTs

def NOR_to_OR(XORs,NLs,NOTs,i):
    new_XORs = copy.deepcopy(XORs)
    new_NLs = NLs[:]
    new_NOTs = NOTs[:]

    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            if r in new_NOTs:
                new_NOTs.remove(r)
            else:
                new_NOTs.append(r)
    new_NLs[i] = '|'
    return new_XORs, new_NLs, new_NOTs

def AND_NAND_ver2(XORs,NLs,NOTs,i):
    new_XORs = copy.deepcopy(XORs)
    new_NLs = NLs[:]
    new_NOTs = NOTs[:]

    for x in new_XORs[f'r[{2*i}]']:
        if x in new_XORs[f'r[{2*i+1}]']:
            new_XORs[f'r[{2*i+1}]'].remove(x)
        else:
            new_XORs[f'r[{2*i+1}]'].append(x)
    if f'r[{2*i}]' in new_NOTs:
        if f'r[{2*i+1}]' in new_NOTs:
            new_NOTs.remove(f'r[{2*i+1}]')
        else:
            new_NOTs.append(f'r[{2*i+1}]')
    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            for x in new_XORs[f'r[{2*i}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            if f'r[{2*i}]' in new_NOTs:
                if r in new_NOTs:
                    new_NOTs.remove(r)
                else:
                    new_NOTs.append(r)
    return new_XORs, new_NLs, new_NOTs

def AND_NAND_ver3(XORs,NLs,NOTs,i):
    new_XORs = copy.deepcopy(XORs)
    new_NLs = NLs[:]
    new_NOTs = NOTs[:]

    for x in new_XORs[f'r[{2*i+1}]']:
        if x in new_XORs[f'r[{2*i}]']:
            new_XORs[f'r[{2*i}]'].remove(x)
        else:
            new_XORs[f'r[{2*i}]'].append(x)
    if f'r[{2*i+1}]' in new_NOTs:
        if f'r[{2*i}]' in new_NOTs:
            new_NOTs.remove(f'r[{2*i}]')
        else:
            new_NOTs.append(f'r[{2*i}]')
    for r in new_XORs:
        if f'g[{i}]' in new_XORs[r]:
            for x in new_XORs[f'r[{2*i+1}]']:
                if x in new_XORs[r]:
                    new_XORs[r].remove(x)
                else:
                    new_XORs[r].append(x)
            if f'r[{2*i+1}]' in new_NOTs:
                if r in new_NOTs:
                    new_NOTs.remove(r)
                else:
                    new_NOTs.append(r)
    return new_XORs, new_NLs, new_NOTs

def OR_NOR_ver2(XORs,NLs,NOTs,i):
    new_XORs = copy.deepcopy(XORs)
    new_NLs = NLs[:]
    new_NOTs = NOTs[:]

    for x in new_XORs[f'r[{2*i}]']:
        if x in new_XORs[f'r[{2*i+1}]']:
            new_XORs[f'r[{2*i+1}]'].remove(x)
        else:
            new_XORs[f'r[{2*i+1}]'].append(x)
    return new_XORs, new_NLs, new_NOTs

def OR_NOR_ver3(XORs,NLs,NOTs,i):
    new_XORs = copy.deepcopy(XORs)
    new_NLs = NLs[:]
    new_NOTs = NOTs[:]

    for x in new_XORs[f'r[{2*i+1}]']:
        if x in new_XORs[f'r[{2*i}]']:
            new_XORs[f'r[{2*i}]'].remove(x)
        else:
            new_XORs[f'r[{2*i}]'].append(x)
    return new_XORs, new_NLs, new_NOTs
