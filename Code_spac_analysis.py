# import Reader
import math

def check_depth_with_NOT(lines,base):
    VAR_depth = {B:0 for B in base}
    VAR_depth['1'] = 0
    for X_line in lines:
        if '=' not in X_line: continue
        if '#' in X_line: continue
        X_line = X_line.replace(' ','')
        C,AB = X_line.split('=')
        if '^' in AB:
            ABs = AB.split('^')
            d = 0
            for A in ABs:
                d += 1<<VAR_depth[A]
            VAR_depth[C] = math.ceil(math.log2(d))
        elif '&' in AB:
            A,B = AB.split('&')
            VAR_depth[C] = max([VAR_depth[A],VAR_depth[B]]) + 1
        elif '|' in AB:
            A,B = AB.split('|')
            VAR_depth[C] = max([VAR_depth[A],VAR_depth[B]]) + 1
        else:
            VAR_depth[C] = VAR_depth[AB]
    depth = 0
    for V in VAR_depth:
        if VAR_depth[V] > depth:
            depth = VAR_depth[V]
    return depth

def check_depth_without_NOT(lines,base):
    VAR_depth = {B:0 for B in base}
    VAR_depth['1'] = 0
    for X_line in lines:
        if '=' not in X_line: continue
        if '#' in X_line: continue
        X_line = X_line.replace(' ','')
        C,AB = X_line.split('=')
        if '^' in AB:
            ABs = AB.split('^')
            d = 0
            for A in ABs:
                if A == '1': continue
                d += 1<<VAR_depth[A]
            VAR_depth[C] = math.ceil(math.log2(d))
        elif '&' in AB:
            A,B = AB.split('&')
            VAR_depth[C] = max([VAR_depth[A],VAR_depth[B]]) + 1
        elif '|' in AB:
            A,B = AB.split('|')
            VAR_depth[C] = max([VAR_depth[A],VAR_depth[B]]) + 1
        else:
            VAR_depth[C] = VAR_depth[AB]
    depth = 0
    for V in VAR_depth:
        if VAR_depth[V] > depth:
            depth = VAR_depth[V]
    return depth

def check_ANDdepth(lines,base):
    VAR_depth = {B:0 for B in base}
    VAR_depth['1'] = 0
    for X_line in lines:
        if '=' not in X_line: continue
        if '#' in X_line: continue
        X_line = X_line.replace(' ','')
        C,AB = X_line.split('=')
        if '^' in AB:
            ABs = AB.split('^')
            VAR_depth[C] = max([VAR_depth[A] for A in ABs])
        elif '&' in AB:
            A,B = AB.split('&')
            VAR_depth[C] = max([VAR_depth[A],VAR_depth[B]]) + 1
        elif '|' in AB:
            A,B = AB.split('|')
            VAR_depth[C] = max([VAR_depth[A],VAR_depth[B]]) + 1
        else:
            VAR_depth[C] = VAR_depth[AB]
    depth = 0
    for V in VAR_depth:
        if VAR_depth[V] > depth:
            depth = VAR_depth[V]
    return depth

def check_ANDgates(lines):
    cnt = 0
    for X_line in lines:
        if '=' not in X_line: continue
        X_line = X_line.replace(' ','')
        C,AB = X_line.split('=')
        if '&' in AB:
            cnt += AB.count('&')
    return cnt

def check_ORgates(lines):
    cnt = 0
    for X_line in lines:
        if '=' not in X_line: continue
        X_line = X_line.replace(' ','')
        C,AB = X_line.split('=')
        if '|' in AB:
            cnt += AB.count('|')
    return cnt

def check_XORgates(lines):
    cnt = 0
    for X_line in lines:
        if '=' not in X_line: continue
        X_line = X_line.replace(' ','')
        C,AB = X_line.split('=')
        if '^' in AB:
            ab = AB.split('^')
            cnt += AB.count('^') - ab.count('1')
    return cnt

def check_NOTgates(lines):
    cnt = 0
    for X_line in lines:
        if '=' not in X_line: continue
        X_line = X_line.replace(' ','')
        C,AB = X_line.split('=')
        if '^' in AB:
            ab = AB.split('^')
            cnt += ab.count('1')
    return cnt

def check_implementation_spec_in_results(filename,n,m):
    with open('code_results/'+filename,'r') as f:
        head,body,tail = f.read().split('        ################### Here is your code !! ###################')
    lines = body.split('\n')[2:-1]
    base = [f'x[{i}]' for i in range(n)] + ['1']
    DN = check_depth_with_NOT(lines,base)
    D = check_depth_without_NOT(lines,base)
    AD = check_ANDdepth(lines,base)
    ANDs = check_ANDgates(lines)
    ORs = check_ORgates(lines)
    XORs = check_XORgates(lines)
    NOTs = check_NOTgates(lines)
    return DN,D,AD,ANDs,ORs,XORs,NOTs
