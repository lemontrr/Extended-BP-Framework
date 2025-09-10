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
import os
import sys


def Read_sizes(filename):
    with open(filename, 'r') as fp:
        lines = fp.read().split(
            '################### Here is your code !! ###################')[1].split('\n')
    all_Vars = set()
    for line in lines:
        line = line.replace(' ', '').replace(';', '')
        if '#' in line[:3]:
            continue
        if '=' not in line:
            continue
        if line.count('=') > 1:
            continue
        # print(line)
        C, AB = line.split('=')
        all_Vars.add(C.replace('^', '').replace('&', '').replace('|', ''))
        if '&' in AB:
            all_Vars.update(AB.split('&'))
        elif '|' in AB:
            all_Vars.update(AB.split('|'))
        elif '^' in AB:
            all_Vars.update(AB.split('^'))
        else:
            all_Vars.add(AB)
    n = 0
    for i in range(100, -1, -1):
        if f'x[{i}]' in all_Vars:
            n = i+1
            break
    m = 0
    for i in range(100, -1, -1):
        if f'y[{i}]' in all_Vars:
            m = i+1
            break
    return n, m


def optimizer_with_BPD(n, m, XORs, NLs, NOTs, filename, pc_name, H):
    st = time.time()
    add_on_logname = f'_{H}H_{pc_name}'
    circuit, XORnum = Optimizer_BPD.Optimizer_with_BPD(
        n, m, XORs, NLs, NOTs, log_filename=filename + add_on_logname, H=H)

    add_on_name = f'_{H}H_{XORnum}XORs_{pc_name}_{int(time.time()-st)}s'
    Write_Circuit.Write_Circuit(filename, add_on_name, circuit)
    print(f'Write {filename} (H = {H}) by using {XORnum}XORs in {pc_name} (time : {time.time()-st:.2f}s)')
    return 1


def optimizer_with_BPD_for_modified_circuit(n, m, XORs, NLs, NOTs, filename, pc_name, H):
    st = time.time()
    new_XORs, new_NLs, new_NOTs, _ = Modification_Circuits.Modify_circuits(
        n, m, XORs, NLs, NOTs)

    add_on_logname = f'_{H}H_{pc_name}'
    circuit, XORnum = Optimizer_BPD.Optimizer_with_BPD(
        n, m, new_XORs, new_NLs, new_NOTs, log_filename=filename + add_on_logname, H=H)

    add_on_name = f'_{H}H_{XORnum}XORs_{pc_name}_{int(time.time()-st)}s'
    Write_Circuit.Write_Circuit(filename, add_on_name, circuit)
    print(f'Write {filename} (H = {H}) by using {XORnum}XORs in {pc_name} (time : {time.time()-st:.2f}s)')
    return 1


def optimizer_with_RNBP(n, m, XORs, NLs, NOTs, filename, pc_name):
    st = time.time()
    add_on_logname = f'_RNBP_{pc_name}'
    circuit, XORnum = Optimizer_RNBP.Optimizer_with_RNBP(
        n, m, XORs, NLs, NOTs, log_filename=filename + add_on_logname)

    add_on_name = f'_RNBP_{XORnum}XORs_{pc_name}_{int(time.time()-st)}s'
    Write_Circuit.Write_Circuit(filename, add_on_name, circuit)
    print(f'Write {filename} by using {XORnum}XORs in {pc_name} (time : {time.time()-st:.2f}s)')
    return 1


def optimizer_with_RNBP_for_modified_circuit(n, m, XORs, NLs, NOTs, filename, pc_name):
    st = time.time()
    new_XORs, new_NLs, new_NOTs, _ = Modification_Circuits.Modify_circuits(
        n, m, XORs, NLs, NOTs)

    add_on_logname = f'_RNBP_{pc_name}'
    circuit, XORnum = Optimizer_RNBP.Optimizer_with_RNBP(
        n, m, new_XORs, new_NLs, new_NOTs, log_filename=filename + add_on_logname)

    add_on_name = f'_RNBP_{XORnum}XORs_{pc_name}_{int(time.time()-st)}s'
    Write_Circuit.Write_Circuit(filename, add_on_name, circuit)
    print(f'Write {filename} by using {XORnum}XORs in {pc_name} (time : {time.time()-st:.2f}s)')
    return 1


if __name__ == '__main__':
    descript = "This is the tool to optimize S-box circuit."
    # descript += "The main paper is 'A Framework for Generating S-Box Circuits with Boyer-Peralta Algorithm-Based Heuristics, and Its Applications to AES and Saturnin'\n"

    parser = argparse.ArgumentParser(description=descript)

    parser.add_argument(
        "-f", "--filename", help="Circuit to optimize (default 'AES10')", type=str, default='AES10')
    parser.add_argument(
        "-m", "--multi", help="The number of cores for multi threading (default 1)", type=int, default=1)
    parser.add_argument(
        "-a", "--algorithm", help="BP based algorithm to be incorporated (default 'RNBP')", type=str, default='RNBP')
    parser.add_argument("-H", "-d", "--depth_limit",
                        help="The depth limit (default : 23)", type=int, default=23)
    parser.add_argument(
        "-r", "--random", help="Random circuit modification mode (default : False)", type=bool, default=False)

    subparser = parser.add_subparsers(
        dest="command", help="Available commands")
    srch_parser = subparser.add_parser(
        "search", help="Search an S-box circuit (default)")
    anal_parser = subparser.add_parser("analyze", help="Analyze the data")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()

    elif args.command == "analyze":
        filenames = os.listdir('./code_results')
        text = ''
        for filename in filenames:
            if filename == 'CODE_RESULTS.txt':
                continue
            n, m = Read_sizes('./code_results/'+filename)
            DN, D, AD, ANDs, ORs, XORs, NOTs = Code_spac_analysis.check_implementation_spec_in_results(
                filename, n, m)
            text += f'Performance of {filename[:-3]} ::: depth(with NOTs) : {DN} / depth : {D} / AND-depth : {AD} / ANDs : {ANDs} / ORs : {ORs} / XORs : {XORs} / NOTs : {NOTs}\n'
        with open('./code_results/CODE_RESULTS.txt', 'w') as fp:
            fp.write(text)

        if not os.path.exists('./log/view_Dist'):
            os.makedirs('./log/view_Dist')
        if not os.path.exists('./log/view_all_Info'):
            os.makedirs('./log/view_all_Info')
        filenames = os.listdir('./log')
        for filename in filenames:
            if '.txt' not in filename:
                continue
            text = log_reader.anal_Dist(filename[:-4])
            with open('./log/view_Dist/'+filename[:-4]+'.txt', 'w') as fp:
                fp.write(text)
            text = log_reader.anal_Informations(filename[:-4])
            with open('./log/view_all_Info/'+filename[:-4]+'.txt', 'w') as fp:
                fp.write(text)

    else:
        n, m = Read_sizes('./code_target_imps/'+args.filename+'.py')
        if args.multi == 1:
            multi_proc = 'a single core'
        else:
            multi_proc = f'{args.multi} multi cores'
        if args.algorithm == 'RNBP':
            algorithm = 'RNBP'
        elif args.algorithm == 'BPD':
            algorithm = f'BPD (H = {args.depth_limit})'
        if args.random == True:
            modify = ' with randomly modificatons'
        elif args.random == False:
            modify = ''
        print(f'I will optimize {args.filename} ({n}-bit -> {m}-bit) on {multi_proc} using {algorithm}' + modify)

        Change_Circuit_Formal.circuit_formal(n, m, args.filename)
        XORs, NLs, NOTs = Extract_XOR_information.extract_XOR_NOTs(
            n, m, args.filename)
        if args.multi == 1:
            if (args.algorithm == 'RNBP') and (args.random == False):
                optimizer_with_RNBP(n, m, XORs, NLs, NOTs,
                                    args.filename, 'single')
            elif (args.algorithm == 'RNBP') and (args.random == True):
                optimizer_with_RNBP_for_modified_circuit(
                    n, m, XORs, NLs, NOTs, args.filename, 'single')
            elif (args.algorithm == 'BPD') and (args.random == False):
                optimizer_with_BPD(n, m, XORs, NLs, NOTs,
                                   args.filename, 'single', args.depth_limit)
            elif (args.algorithm == 'BPD') and (args.random == True):
                optimizer_with_BPD_for_modified_circuit(
                    n, m, XORs, NLs, NOTs, args.filename, 'single', args.depth_limit)
        elif args.multi > 1:
            p = Pool(args.multi)
            ret = [0]*args.multi
            if (args.algorithm == 'RNBP') and (args.random == False):
                for pc_cnt in range(args.multi):
                    ret[pc_cnt] = p.apply_async(optimizer_with_RNBP, [
                                                n, m, XORs, NLs, NOTs, args.filename, f'core{pc_cnt:02d}'])
            elif (args.algorithm == 'RNBP') and (args.random == True):
                for pc_cnt in range(args.multi):
                    ret[pc_cnt] = p.apply_async(optimizer_with_RNBP_for_modified_circuit, [
                                                n, m, XORs, NLs, NOTs, args.filename, f'core{pc_cnt:02d}'])
            elif (args.algorithm == 'BPD') and (args.random == False):
                for pc_cnt in range(args.multi):
                    ret[pc_cnt] = p.apply_async(optimizer_with_BPD, [
                                                n, m, XORs, NLs, NOTs, args.filename, f'core{pc_cnt:02d}', args.depth_limit])
            elif (args.algorithm == 'BPD') and (args.random == True):
                for pc_cnt in range(args.multi):
                    ret[pc_cnt] = p.apply_async(optimizer_with_BPD_for_modified_circuit, [
                                                n, m, XORs, NLs, NOTs, args.filename, f'core{pc_cnt:02d}', args.depth_limit])
            [r.get() for r in ret]
            p.close()
            p.join()

