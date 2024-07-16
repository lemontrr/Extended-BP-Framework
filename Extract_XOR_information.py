def extract_XOR_NOTs(n,m,filename):
    with open('code_formal/'+filename+'.py','r') as f:
        head,body,tail = f.read().split('        ################### Here is your code !! ###################')
    lines = body.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].replace(' ','')

    pure_XORs = dict()
    XORs = dict()
    NLs = []
    k = 0
    new_lines = []
    for i in range(2,len(lines)-1):
        Y,X = lines[i].split('=')
        if Y in {f'y[{_}]' for _ in range(m)}:
            XORs[Y] = [X]
        elif ('&' in X) or ('|' in X):
            for j in range(i+1,len(lines)-1):
                lines[j] = lines[j].replace(Y,f'g[{k}]')
            new_lines.append(f'g[{k}]={X}')
            if '&' in X: r0,r1 = X.split('&'); NLs.append('&')
            elif '|' in X: r0,r1 = X.split('|'); NLs.append('|')
            XORs[f'r[{2*k}]'] = [r0]
            XORs[f'r[{2*k+1}]'] = [r1]
            k += 1

        elif '^' in X:
            pure_XORs[Y] = X.split('^')
            new_lines.append(lines[i])
        else:
            pure_XORs[Y] = [X]
            new_lines.append(lines[i])
    for r in XORs:
        There_is_not_x_g = True
        while(There_is_not_x_g):
            There_is_not_x_g = False
            for X in XORs[r]:
                if X not in {f'x[{_}]' for _ in range(n)}|{f'g[{_}]' for _ in range(k)}|{'1'}:
                    There_is_not_x_g = True
                    break
            if There_is_not_x_g:
                XORs[r].remove(X)
                for x in pure_XORs[X]:
                    if x in XORs[r]:
                        XORs[r].remove(x)
                    else:
                        XORs[r].append(x)

    NOTs = []
    for r in XORs:
        if '1' in XORs[r]:
            XORs[r].remove('1')
            NOTs.append(r)
    return XORs,NLs,NOTs