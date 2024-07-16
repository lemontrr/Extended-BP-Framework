def circuit_formal(n,m,filename):
    with open('code_target_imps/'+filename+'.py','r') as f:
        head,body,tail = f.read().split('        ################### Here is your code !! ###################')
    lines = body.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].replace(' ','').replace(';','')

    new_lines = []; cnt = 0; len_lines = len(lines)
    for i in range(len_lines):
        if '#' in lines[i]: continue
        if '=' not in lines[i]: continue

        if ('^=' in lines[i]) or ('&=' in lines[i]) or ('|=' in lines[i]):
            Y_op,X = lines[i].split('=')
            Y,op = Y_op[:-1],Y_op[-1]
            for j in range(i+1,len_lines):
                lines[j] = lines[j].replace(Y,f'DJ_master[{cnt+1}]')
            new_lines.append(f'DJ_master[{cnt}]={X}')
            new_lines.append(f'DJ_master[{cnt+1}]={Y}{op}DJ_master[{cnt}]')
            cnt += 2
        else:
            new_lines.append(lines[i])
    
    new2_lines = []; len_lines = len(new_lines)
    for i in range(len_lines):
        if '#' in new_lines[i]: continue
        if '=' not in new_lines[i]: continue

        Y,X = new_lines[i].split('=')
        if Y not in {f'y[{_}]'for _ in range(m)}:
            for j in range(i+1,len_lines):
                new_lines[j] = new_lines[j].replace(Y,f'DJ_master[{cnt}]')
            new2_lines.append(f'DJ_master[{cnt}]={X}')
            cnt += 1
        else: 
            new2_lines.append(new_lines[i])
        
    new3_lines = []; len_lines = len(new2_lines)
    for i in range(len_lines):
        Y,X = new2_lines[i].split('=')
        if Y in {f'y[{_}]'for _ in range(m)}:
            for j in range(i+1,len_lines):
                new2_lines[j] = new2_lines[j].replace(Y,f'DJ_master[{cnt}]')
            new3_lines.append(f'DJ_master[{cnt}]={X}')
            new3_lines.append(f'{Y}=DJ_master[{cnt}]')
            cnt += 1
        else:
            new3_lines.append(new2_lines[i])
    with open('code_formal/'+filename+'.py','w') as f:
        f.write(head)
        f.write('        ################### Here is your code !! ###################\n')
        f.write(f'        DJ_master = [0]*{cnt}\n')
        for line in new3_lines:
            f.write('        '+line.replace('=',' = ').replace('^',' ^ ').replace('&', ' & ').replace('|',' | ')+'\n')
        f.write('        ################### Here is your code !! ###################\n')
        f.write(tail)
    print('')