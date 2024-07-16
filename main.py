from multiprocessing import Pool
import multiprocessing as mp
import Change_Circuit_Formal
import Extract_XOR_information
import Modification_Circuits
import Optimizer_BPD
import Optimizer_RNBP
import Write_Circuit
import Code_spac_analysis
import time
import argparse
import log_reader

def optimizer_with_BPD(n,m,XORs,NLs,NOTs,filename,pc_name,H):
    st = time.time()
    add_on_logname = f'_{H}H_{pc_name}'
    circuit,XORnum = Optimizer_BPD.Optimizer_with_BPD(n,m,XORs,NLs,NOTs,log_filename = filename + add_on_logname,H = H)

    add_on_name = f'_{H}H_{XORnum}XORs_{pc_name}_{int(time.time()-st)}s'
    Write_Circuit.Write_Circuit(filename,add_on_name,circuit)
    print(f'Write {filename} (H = {H}) by using {XORnum}XORs in {pc_name} (time : {time.time()-st:.2f}s)')
    return 1

def optimizer_with_BPD_for_modified_circuit(n,m,XORs,NLs,NOTs,filename,pc_name,H):
    st = time.time()
    new_XORs,new_NLs,new_NOTs,_ = Modification_Circuits.Modify_circuits(n,m,XORs,NLs,NOTs)

    add_on_logname = f'_{H}H_{pc_name}'
    circuit,XORnum = Optimizer_BPD.Optimizer_with_BPD(n,m,new_XORs,new_NLs,new_NOTs,log_filename = filename + add_on_logname,H = H)

    add_on_name = f'_{H}H_{XORnum}XORs_{pc_name}_{int(time.time()-st)}s'
    Write_Circuit.Write_Circuit(filename,add_on_name,circuit)
    print(f'Write {filename} (H = {H}) by using {XORnum}XORs in {pc_name} (time : {time.time()-st:.2f}s)')
    return 1

def optimizer_with_RNBP(n,m,XORs,NLs,NOTs,filename,pc_name):
    st = time.time()
    add_on_logname = f'_RNBP_{pc_name}'
    circuit,XORnum = Optimizer_RNBP.Optimizer_with_RNBP(n,m,XORs,NLs,NOTs,log_filename = filename + add_on_logname)

    add_on_name = f'_RNBP_{XORnum}XORs_{pc_name}_{int(time.time()-st)}s'
    Write_Circuit.Write_Circuit(filename,add_on_name,circuit)
    print(f'Write {filename} by using {XORnum}XORs in {pc_name} (time : {time.time()-st:.2f}s)')
    return 1

def optimizer_with_RNBP_for_modified_circuit(n,m,XORs,NLs,NOTs,filename,pc_name):
    st = time.time()
    new_XORs,new_NLs,new_NOTs,_ = Modification_Circuits.Modify_circuits(n,m,XORs,NLs,NOTs)

    add_on_logname = f'_RNBP_{pc_name}'
    circuit,XORnum = Optimizer_RNBP.Optimizer_with_RNBP(n,m,new_XORs,new_NLs,new_NOTs,log_filename = filename + add_on_logname)

    add_on_name = f'_RNBP_{XORnum}XORs_{pc_name}_{int(time.time()-st)}s'
    Write_Circuit.Write_Circuit(filename,add_on_name,circuit)
    print(f'Write {filename} by using {XORnum}XORs in {pc_name} (time : {time.time()-st:.2f}s)')
    return 1

if __name__ == '__main__':
    descript = "This is the tool to optimize S-box circuit."
    # descript += "The main paper is 'A Framework for Generating S-Box Circuits with Boyer-Peralta Algorithm-Based Heuristics, and Its Applications to AES and Saturnin'\n"

    parser = argparse.ArgumentParser(description=descript)

    parser.add_argument("mode",help="Choosing whether to optimize ('opt') or analyze ('anal') (default 'opt')",type=str,default='opt')

    parser.add_argument("-f", "--filename",help="Circuit to optimize (default 'Imp_32ANDs')",type=str,default='Imp_32ANDs')
    parser.add_argument("-n", "--insize",help="Input size of the S-box (default 8)",type=int,default=8)
    parser.add_argument("-m", "--outsize",help="Output size of the S-box (default 8)",type=int,default=8)
    parser.add_argument("-M", "--multi",help="The number of cores for multi threading (default 1)",type = int,default=1)
    parser.add_argument("-A", "--algorithm",help="BP based algorithm to be incorporated (default 'RNBP')",type=str,default='RNBP')
    parser.add_argument("-H", "--depth_limit",help="The depth limit (default : 23)",type = int,default=23)
    parser.add_argument("-R", "--random",help="Random circuit mofidication mode (default : False)",type = bool,default=False)

    parser.add_argument("-AR", "--anal_result",help="Result filename to analyze performance",type=str,default='')
    parser.add_argument("-ALD", "--anal_log_Dist",help="Log filename to analyze changes in Dist",type=str,default='')
    parser.add_argument("-ALI", "--anal_log_I",help="Log filename to analyze many informations",type=str,default='')
    
    args = parser.parse_args()

    if args.mode == 'opt':
        if args.multi == 1:           multi_proc = 'a single core'
        else:                         multi_proc = f'{args.multi} multi cores'
        if args.algorithm == 'RNBP':  algorithm = 'RNBP'
        elif args.algorithm == 'BPD': algorithm = f'BPD (H = {args.depth_limit})'
        if args.random == True:       modify = ' with randomly modificatons'
        elif args.random == False:    modify = ''
        print(f'I will optimize {args.filename} ({args.insize}-bit -> {args.outsize}-bit) on {multi_proc} using {algorithm}' + modify)

        Change_Circuit_Formal.circuit_formal(args.insize,args.outsize,args.filename)
        XORs,NLs,NOTs = Extract_XOR_information.extract_XOR_NOTs(args.insize,args.outsize,args.filename)
        if args.multi == 1:
            if (args.algorithm == 'RNBP') and (args.random == False): 
                optimizer_with_RNBP(args.insize,args.outsize,XORs,NLs,NOTs,args.filename,'single')
            elif (args.algorithm == 'RNBP') and (args.random == True): 
                optimizer_with_RNBP_for_modified_circuit(args.insize,args.outsize,XORs,NLs,NOTs,args.filename,'single')
            elif (args.algorithm == 'BPD') and (args.random == False): 
                optimizer_with_BPD(args.insize,args.outsize,XORs,NLs,NOTs,args.filename,'single',args.depth_limit)
            elif (args.algorithm == 'BPD') and (args.random == True):
                optimizer_with_BPD_for_modified_circuit(args.insize,args.outsize,XORs,NLs,NOTs,args.filename,'single',args.depth_limit)
        elif args.multi > 1:
            p = Pool(args.multi); ret = [0]*args.multi
            if (args.algorithm == 'RNBP') and (args.random == False): 
                for pc_cnt in range(args.multi): ret[pc_cnt] = p.apply_async(optimizer_with_RNBP,[args.insize,args.outsize,XORs,NLs,NOTs,args.filename,f'core{pc_cnt:02d}'])
            elif (args.algorithm == 'RNBP') and (args.random == True): 
                for pc_cnt in range(args.multi): ret[pc_cnt] = p.apply_async(optimizer_with_RNBP_for_modified_circuit,[args.insize,args.outsize,XORs,NLs,NOTs,args.filename,f'core{pc_cnt:02d}'])
            elif (args.algorithm == 'BPD') and (args.random == False): 
                for pc_cnt in range(args.multi): ret[pc_cnt] = p.apply_async(optimizer_with_BPD,[args.insize,args.outsize,XORs,NLs,NOTs,args.filename,f'core{pc_cnt:02d}'],args.depth_limit)
            elif (args.algorithm == 'BPD') and (args.random == True):
                for pc_cnt in range(args.multi): ret[pc_cnt] = p.apply_async(optimizer_with_BPD_for_modified_circuit,[args.insize,args.outsize,XORs,NLs,NOTs,args.filename,f'core{pc_cnt:02d}'],args.depth_limit)
            [r.get() for r in ret]; p.close(); p.join()

    elif args.mode == 'anal':
        if (args.anal_result != '') + (args.anal_log_Dist != '') + (args.anal_log_I != '') > 1:
            print('Please use only one option among AR, ALD, and ALS.')
        elif args.anal_result != '':
            print(args.anal_result)
            DN,D,AD,ANDs,ORs,XORs,NOTs = Code_spac_analysis.check_implementation_spec_in_results(args.anal_result+'.py',args.insize,args.outsize)
            print(f'Performance of {args.anal_result} ::: depth(wtih NOTs) : {DN} / depth : {D} / AND-depth : {AD} / ANDs : {ANDs} / ORs : {ORs} / XORs : {XORs} / NOTs : {NOTs}')
        elif args.anal_log_Dist != '':
            log_reader.anal_Dist(args.anal_log_Dist)
        elif args.anal_log_I != '':
            log_reader.anal_Informations(args.anal_log_I)
    else:
        print("You entered the mode incorrectly. (Only 'opt' or 'anal' are possible.)")
    