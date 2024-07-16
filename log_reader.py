import re
import math

def read_log(log_filename):
    with open(f'./log/{log_filename}.txt','r') as f:
        readlines = f.read()

    readlines = readlines.split('\n')
    infos = []
    info = []
    for i in range(len(readlines)):
        if readlines[i] == '':
            infos.append(info)
            info = []
        else:
            info.append(readlines[i])
    infos.append(info)

    if 'RNBP' in log_filename:
        n = eval(infos[0][0].split(' : ')[1])
        m = eval(infos[0][1].split(' : ')[1])
        Y = eval(infos[0][2].split(' : ')[1])
        XORs = eval(infos[0][3].split(' : ')[1])
        H = -1; HY = []
    else:
        n = eval(infos[0][0].split(' : ')[1])
        m = eval(infos[0][1].split(' : ')[1])
        H = eval(infos[0][2].split(' : ')[1])
        Y = eval(infos[0][3].split(' : ')[1])
        XORs = eval(infos[0][4].split(' : ')[1])
        HY = eval(infos[0][5].split(' : ')[1])
    
    Sname = [f'x[{i}]' for i in range(n)]
    S = [1<<i for i in range(n)]
    D = [0 for i in range(n)]
    Dist = eval(infos[1][0].split(' : ')[1])
    
    name_tag = n
    status = {name_tag:[Sname[:],S[:],D[:],Dist[:]]}
    for info in infos[2:-1]:
        if len(info) < 2: continue
        name_tag += 1
        if 'RNBP' in log_filename:
            new_Sname, new_S = info[0].split(' : ')[1].split(', ')
        else:
            new_Sname, new_S, new_D = info[0].split(' : ')[1].split(', ')
        Sname += [new_Sname]
        S     += [int(new_S)]
        if 'RNBP' in log_filename:
            if bin(S[-1]).count('1') == 1:
                i = int(math.log2(S[-1]))-n
                new_D = max(min([D[_] for _ in range(len(S)) if S[_] == Y[2*i]]), min([D[_] for _ in range(len(S)) if S[_] == Y[2*i+1]]))+1
            else:
                new_D = 999
                for i in range(len(S)-1):
                    for j in range(i+1,len(S)-1):
                        if S[-1] == S[i]^S[j]:
                            new_D = min(new_D,max(D[i],D[j])+1)
        D     += [int(new_D)]
        Dist = eval(info[1].split(' : ')[1])
        status[name_tag] = [Sname[:],S[:],D[:],Dist[:]]
    name_tags = list(status.keys())

    Circuit = eval(infos[-1][1].split(' : ')[1])

    return n,m,name_tags,XORs,Y,HY,status,Circuit

def print_imp(stat,Y,Circuit):
    Sname,S,D,Dist = stat
    NLs,NOTs,k = extract_NLs_NOTs(Circuit)
    n = len([_ for _ in Sname if 'x' in _])
    XORs = 1
    for _ in range(n,len(S)):
        if bin(S[_]).count('1')>1:
            for i in range(_):
                for j in range(i+1,_):
                    if S[i]^S[j] == S[_]:
                        if max(D[i],D[j])+1 == D[_]:
                            print(f'{Sname[_]} = {Sname[i]} + {Sname[j]} (depth : {D[_]} = {D[i]} + {D[j]}) - {XORs}th XOR'); XORs += 1
        else:
            i = int(math.log2(S[_]))-n
            print(f'{Sname[_]} = {Sname[S.index(Y[2*i])]} {NLs[i]} {Sname[S.index(Y[2*i+1])]} (depth : {D[_]} = {D[S.index(Y[2*i])]} {NLs[i]} {D[S.index(Y[2*i+1])]})')

def print_only_Dists(status):
    name_tags = list(status.keys())
    bef_tag = 0
    for name_tag in name_tags:
        Sname,S,D,Dist = status[name_tag]
        if name_tag == len([_ for _ in Sname if 'x' in _]):
            bef_Dist = Dist[:]

        text = ''; changed = []
        for i in range(len(Dist)):
            if i > 0:
                # if Dist[i] != bef_Dist[i]: 
                #     if Dist[i] == 0:       text += ' ' + '\033[96m' + f'_' + '\033[0m'; changed.append(i)
                #     else:                  text += ' ' + '\033[96m' + f'{Dist[i]}' + '\033[0m'; changed.append(i)
                if Dist[i] == 999:       text += f' ?'
                elif Dist[i] == 0:         text += f' _'
                else:                      text += f' {Dist[i]}'
            else:
                # if Dist[i] != bef_Dist[i]:
                #     if Dist[i] == 0:       text += '\033[96m' + f'_' + '\033[0m'; changed.append(i)
                #     else:                  text += '\033[96m' + f'{Dist[i]}' + '\033[0m'; changed.append(i)
                if Dist[i] == 999:       text += f'?'
                elif Dist[i] == 0:         text += f'_'
                else:                      text += f'{Dist[i]}'
        print(text)
        bef_Dist = Dist[:]

def extract_NLs_NOTs(Circuit):
    NLs_dict = dict()
    NOTs = []
    for line in Circuit:
        C,AB = line.split('=')
        if 'g' in C:
            c = int(re.findall(r'\d+',C)[0])
            NLs_dict[c] = AB.split(']')[1].split('r[')[0]
        elif '^' in AB:
            if '1' in AB.split('^'):
                NOTs.append(C)
    k = len(list(NLs_dict.keys()))
    NLs = []
    for i in range(k):
        NLs.append(NLs_dict[i])
    return NLs,NOTs,k

def anal_Dist(log_filename):
    n,m,tags,XORs,Y,HY,status,Circuit = read_log(log_filename)
    print_only_Dists(status)

def anal_Informations(log_filename):
    n,m,tags,XORs,Y,HY,status,Circuit = read_log(log_filename)
    Sname,S,D,Dist = status[tags[-1]]
    NLs,NOTs,k = extract_NLs_NOTs(Circuit)
    print(f'n = {n}')
    print(f'm = {m}')
    print(f'k = {k}')
    if 'RNBP' not in log_filename:
        print(f'H = {max(D)}')
    print(f'Sname = {Sname}')
    print(f'S = {S}')
    print(f'D = {D}')
    print(f'Y = {Y}')
    if 'RNBP' not in log_filename:
        print(f'HY = {HY}')
    print(f'NLs = {NLs}')
    print(f'NOTs = {NOTs}')
    print('')
    print('Circuit')
    print_imp(status[tags[-1]],Y,Circuit)
