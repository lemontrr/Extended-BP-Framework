import random
import math
import time
import re
import os

S_XORs_2PD = []
S_XORs_2PD_for_new_pair = [dict()]*5

def Optimizer_with_RNBP(n,m,XORs,NLs,NOTs,log_filename = 'log'):
    logs = os.listdir('./log')
    i = 0
    while(True):
        if log_filename+f'_{i:03d}.txt' in logs:
            i += 1
        else:
            log_file = log_filename+f'_{i:03d}.txt'
            break

    k = len(NLs); t = 0; st = time.time(); bst = st
    S,_,Y,Sname = initialize_S_D_Y_Sname(n,m,k,XORs)
    Dist = initialize_Dist(n,Y)
    initialize_SXORs(S)
    with open('./log/'+log_file,'a') as flog:
        flog.write(f'n : {n}\nm : {m}\nY : {Y}\nXORs : {XORs}\n\n')
    
    with open('./log/'+log_file,'a') as flog:
        flog.write(f'Dist : {Dist}\n' + f'time : {time.time()-st:.2f} (+{time.time()-bst:.2f})\n\n')
    
    while(max(Dist)>0):
        start = time.time()
        is_there_g = -1
        for i in range(k):
            if 1<<(n+i) not in S:
                if Y[2*i] in S:
                    if Y[2*i+1] in S:
                        is_there_g = i
                        break
        if is_there_g >= 0:
            Sname.append(f'g[{i}]')
            S.append(1<<(n+i))
            pre_emp = True
            end_pre_emptive = time.time()

        elif min([d for d in Dist if d > 0]) == 999:
            i = Dist.index(999)
            text = bin(Y[i])[2:][::-1]
            Xs = []
            for j in range(len(text)):
                if text[j] == '1':
                    Xs.append(1<<j)
                    
            while(True):
                v0,v1 = Xs[0],Xs[1]
                w = v0^v1
                if w not in S:
                    break
                else:
                    Xs.remove(v0)
                    Xs.remove(v1)
                    Xs.append(w)
            pre_emp = True
            end_pre_emptive = time.time()
            Sname.append(f't[{t}]'); t += 1
            S.append(w)
        elif 1 not in Dist:
            pre_emp = False
            WD = make_WD(S) # Filtering (depth under H)
            end_make_WD = time.time()

            # strategy
            ## Filtering (Reduce Dist)
            tuple_Dist = tuple(Dist)
            WD_Dist = dict()
            for w in WD:
                update_S_XORs_for_new_pair(w)
                test_Dist = Dist[:]
                for i in range(len(Y)):
                    if Dist[i] == 0 : continue
                    test_Dist[i] = update_distance_for_new_pair(S+[w],Y[i],Dist[i])
                if tuple_Dist != tuple(test_Dist): 
                    WD_Dist[w] = test_Dist

            end_Filtering_2 = time.time()

            ## Minimize Sum of Dist
            W_sum = set(); min_sum = 999
            for w in WD_Dist:
                s = sum([i for i in WD_Dist[w] if i != 999])
                if min_sum > s:
                    W_sum = {w}
                    min_sum = s
                elif min_sum == s:
                    W_sum.add(w)
            end_Sum_Dist = time.time()

            ## Maximize Euclidean norm of Dist
            W_Enm = []; max_Enm = 0
            for w in W_sum:
                e = sum([i*i for i in WD_Dist[w] if i != 999])
                if max_Enm < e:
                    W_Enm = [w]
                    max_Enm = e
                elif max_Enm == e:
                    W_Enm.append(w)
            end_Enm_Dist = time.time()

            ## Random
            w = random.choice(W_Enm)

            Sname.append(f't[{t}]'); t += 1
            S.append(w)
        else:
            pre_emp = True
            y = Y[Dist.index(1)]
            w = pre_emptive(S,y)
            end_pre_emptive = time.time()

            Sname.append(f't[{t}]'); t += 1
            S.append(w)
        update_S_XORs_for_new_pair(S[-1])
        update_SXORs()

        for i in range(len(Y)):
            if Dist[i] == 0 : continue
            Dist[i] = update_distance(S,Y[i],Dist[i])
        
        end_Update = time.time()

        with open('./log/'+log_file,'a') as flog:
            flog.write(f'{len(Sname)}th Add (Sname, S) : {Sname[-1]}, {S[-1]}\n' + f'Dist : {Dist}\n')
            if pre_emp:
                flog.write(f'time : {time.time()-st:.2f} (+{time.time()-bst:.2f} = {end_pre_emptive - start:.2f} + {end_Update - end_pre_emptive:.2f})\n\n'); bst = time.time()
            else:
                flog.write(f'time : {time.time()-st:.2f} (+{time.time()-bst:.2f} = {end_make_WD - start:.2f} + {end_Filtering_2 - end_make_WD:.2f} + {end_Sum_Dist-end_Filtering_2:.2f} + {end_Enm_Dist-end_Sum_Dist:.2f} + {end_Update-end_Enm_Dist:.2f})\n\n'); bst = time.time()
        
    with open('./log/'+log_file,'a') as flog:
        flog.write(f'XOR : {len(S)-n-k}\n')

    C = make_Circuit(n,m,k,S,Y,NLs,NOTs)
    with open('./log/'+log_file,'a') as flog:
        flog.write(f'Circuit : {C}')

    Zerorize_S_XORs()
    return C,len(S)-n-k

def initialize_S_D_Y_Sname(n,m,k,XORs):
    S = [1<<i for i in range(n)]
    Y = []
    for i in range(2*k):
        v = 0
        for j in range(n):
            if f'x[{j}]' in XORs[f'r[{i}]']:
                v |= 1<<j
        for j in range(k):
            if f'g[{j}]' in XORs[f'r[{i}]']:
                v |= 1<<(n+j)
        Y.append(v)    
    for i in range(m):
        v = 0
        for j in range(n):
            if f'x[{j}]' in XORs[f'y[{i}]']:
                v |= 1<<j
        for j in range(k):
            if f'g[{j}]' in XORs[f'y[{i}]']:
                v |= 1<<(n+j)
        Y.append(v)
    return S,[0]*n,Y,[f'x[{i}]' for i in range(n)]

def initialize_Dist(n,Y):
    Dist = []
    for i in range(len(Y)):
        if Y[i] >= (1<<n):
            Dist.append(999)
        else:
            Dist.append(bin(Y[i]).count('1')-1)
    return Dist

def initialize_SXORs(S):
    S_XORs_2PD.append({0})
    S_XORs_2PD.append({s for s in S})
    S_XORs_2PD.append(set())
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            S_XORs_2PD[-1].add(S[i]^S[j])
    S_XORs_2PD.append(set())
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            for k in range(j+1,len(S)):
                S_XORs_2PD[-1].add(S[i]^S[j]^S[k])
    S_XORs_2PD.append(set())
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            for k in range(j+1,len(S)):
                for l in range(k+1,len(S)):
                    S_XORs_2PD[-1].add(S[i]^S[j]^S[k]^S[l])

def update_distance(S,y,dist):
    Mk = 0 # mask
    for s in S:
        Mk |= s
    if (Mk&y) != y: 
        return 999
    len_S = len(S)
    if dist != 999:
        if rec(S,len_S,0,y,0,dist):
            return dist-1
        else:
            return dist
    else:
        dist = bin(y).count('1') - 1
        for dist_ in range(9):
            if rec(S,len_S,0,y,0,dist_):
                return dist_-1
        return 999

def rec(S,len_S,i,y,v,dist):
    if len_S-i < dist:
        return False
    if dist <= 4: 
        if y^v in S_XORs_2PD[dist]:
            return True
        else:
            return False
    
    if rec(S,len_S,i+1,y,v^S[i],dist-1):
        return True
    if rec(S,len_S,i+1,y,v,dist):
        return True
    return False
    
def update_distance_for_new_pair(S,y,dist):
    Mk = 0 # mask
    for s in S:
        Mk |= s
    if (Mk&y) != y: 
        return 999
    len_S = len(S)
    if dist != 999:
        if rec_for_new_pair(S,len_S,0,y,0,dist):
            return dist-1
        else:
            return dist
    else:
        return 999

def rec_for_new_pair(S,len_S,i,y,v,dist):
    if len_S-i < dist:
        return False
    if dist <= 4: 
        if y^v in S_XORs_2PD_for_new_pair[dist]:
            return True
        else:
            return False
    
    if rec_for_new_pair(S,len_S,i+1,y,v^S[i],dist-1):
        return True
    if rec_for_new_pair(S,len_S,i+1,y,v,dist):
        return True
    return False

def update_SXORs():
    for i in range(1,5):
        S_XORs_2PD[i].update(S_XORs_2PD_for_new_pair[i])

def update_S_XORs_for_new_pair(w):
    S_XORs_2PD_for_new_pair[0] = dict()
    S_XORs_2PD_for_new_pair[1] = {w}
    S_XORs_2PD_for_new_pair[2] = {w^s for s in S_XORs_2PD[1]}
    S_XORs_2PD_for_new_pair[3] = {w^s for s in S_XORs_2PD[2]}
    S_XORs_2PD_for_new_pair[4] = {w^s for s in S_XORs_2PD[3]}
    
def make_WD(S):
    WD = set()
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            w = S[i]^S[j]
            if w in S: continue
            WD.add(w)
    return WD

def pre_emptive(S,y):
    for i in range(len(S)):
        if S[i]^y in S:
            return y

def make_Circuit(n,m,k,S,Y,NLs,NOTs):
    B_match = dict(); g_cnt = 0; t_cnt = 0
    for i in range(len(S)):
        b = S[i]
        if bin(b).count('1') == 1:
            if i < n:
                B_match[b] = f'x[{i}]'
            else:
                B_match[b] = f'g[{int(math.log2(b))-n}]'
                g_cnt += 1
        else:
            B_match[b] = f't[{t_cnt}]'
            t_cnt += 1

    Circuit = []; r_not_fin = [i for i in range(2*k)]; y_not_fin = [i for i in range(m)]
    for i in range(len(S)):
        b = S[i]
        if 'x' in B_match[b]: pass
        elif 'g' in B_match[b]: 
            j = int(re.findall(r'\d+',B_match[b])[0])
            if '!' in NLs[j]:
                Circuit.append(f'{B_match[b]}=r[{2*j}]{NLs[j][1]}r[{2*j+1}]^1')
            else:
                Circuit.append(f'{B_match[b]}=r[{2*j}]{NLs[j]}r[{2*j+1}]')
        else:
            Fin = False
            for i0 in range(i):
                for i1 in range(i0+1,i):
                    if b == S[i0]^S[i1]:
                        Circuit.append(f'{B_match[b]}={B_match[S[i0]]}^{B_match[S[i1]]}')
                        Fin = True
                        break
                if Fin:
                    break
        if b in Y:
            remover = []
            for j in r_not_fin:
                if b == Y[j]:
                    if f'r[{j}]' in NOTs:
                        Circuit.append(f'r[{j}]={B_match[b]}^1')
                    else:
                        Circuit.append(f'r[{j}]={B_match[b]}')
                    remover.append(j)
            for j in remover:
                r_not_fin.remove(j)
            remover = []
            for j in y_not_fin:
                if b == Y[2*k+j]:
                    if f'y[{j}]' in NOTs:
                        Circuit.append(f'y[{j}]={B_match[b]}^1')
                    else:
                        Circuit.append(f'y[{j}]={B_match[b]}')
                    remover.append(j)
            for j in remover:
                y_not_fin.remove(j)
    return Circuit

def Zerorize_S_XORs():
    del S_XORs_2PD[:]
    for i in range(5):
        S_XORs_2PD_for_new_pair[i] = dict()