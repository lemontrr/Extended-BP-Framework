def Write_Circuit(filename,add_on_name,Circuit):
    with open('code_target_imps/'+filename+'.py','r') as f:
        head,body,tail = f.read().split('        ################### Here is your code !! ###################')
    tcnt = len([_ for _ in Circuit if 't' in _.split('=')[0]])
    rcnt = len([_ for _ in Circuit if 'r' in _.split('=')[0]])
    with open('code_results/'+filename+add_on_name+'.py','w') as f:
        f.write(head)
        f.write('        ################### Here is your code !! ###################\n')
        f.write(f'        t = [0]*{tcnt}; r = [0]*{rcnt}\n')
        for line in Circuit:
            f.write('        '+line.replace('=',' = ').replace('^',' ^ ').replace('&', ' & ').replace('|',' | ')+'\n')
        f.write('        ################### Here is your code !! ###################\n')
        f.write(tail)
