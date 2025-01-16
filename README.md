# Extended-BP-Framework
This text provides guidance on using a tool is developed in *A Framework for Generating S-Box Circuits with Boyar–Peralta Algorithm-Based Heuristics, and Its Applications to AES, SNOW3G, and Saturnin*, a paper accepted to CHES 2025. 
(Paper URL : https://tches.iacr.org/index.php/TCHES/article/view/11940/11800)
This tool optimizes the number of XOR gates and depth in S-box circuits by using algorithms that extends BPD and RNBP, which are algorithms for optimizing circuits of linear layers.
So, RNBP option optimizes only the number of XOR gates, while BPD option optimizes the number of XOR gates within a depth specified by the user.
The tool preserves nonlinear gates and AND-depth.

This tool includes the results (for AES, SNOW3G, and Saturnin) presented in the paper and the Ascon S-box circuit for quick testing.

## Options of main.py
**-h** : Show the help message and exit.  
**search** : Search for optimized circuits. (default)  
**analyze** : Generates files by analyzing the result and log files.  

##### Search Options
**-f** : Specifies the circuit filename to optimize (excluding the **.py** extension). [default : **AES10**]  
**-m** : Indicates the number of cores for multi-threading. Each core runs independently to optimize the target circuit. If set to 1, a single core is used. [default : 1]  
**-a** : Selects the BP-based algorithm to apply (**RNBP** or **BPD**). [default : **RNBP**]  
**-d** or **-H** : Sets the depth limit. [default : 23]  
**-r** : Enable or disables random circuit modification mode (```True``` or ```False```). [default : ```False```]  

## Usage Examples
This section provides example commands along with explanations of their outcomes.

>python main.py search

This command performs the optimization process for the circuit specified in 
**code_target_imps/AES10.py**, utilizing eRNBP.

>python main.py -f AES12

The optimization process targets the circuit in **code_target_imps/AES12.py**, utilizing eRNBP.

>python main.py -f AES12 -m 12 -a BPD -H 15

Here, the optimization focuses on the circuit in **code_target_imps/AES12.py**, using eBPD with 12 cores and a depth limit of 15.

>python main.py -f Ascon

In this case, the circuit in **code_target_imps/Ascon.py** is optimized with eRNBP.

>python main.py -f Ascon -m 4 -a BPD -H 5 -r True

This command applies optimization to the circuit in **code_target_imps/Ascon.py** using eBPD with 4 cores, a depth limit of 5, and random circuit modification mode enabled.

>python main.py -f Saturnin -m 8 -a RNBP

The optimization is applied to the circuit in **code_target_imps/Saturnin.py**, utilizing eRNBP on 8 cores.

>python main.py analyze

The analysis processes all results stored in the **code_results** directory, generating a summary in **code_results/CODE_RESULTS.txt**. Log files in the **log** directory are reviewed, with changes in Dist saved to **log/view_Dist** and additional information stored in **log/view_all_Info**.

## Included Circuit Files
**code_target_imps/AES10.py** : AES S-box circuit in [BP10]  
**code_target_imps/AES12.py** : AES S-box circuit in [BP12]  
**code_target_imps/AES10v2.py** and **code_target_imps/AES10v3.py** : AES S-box circuits made in Section 4.1 based on [BP10]  
**code_target_imps/AES12v2.py** and **code_target_imps/AES12v3.py** : AES S-box circuits made in Section 4.1 based on [BP12]  
**code_target_imps/Ascon.py** : Ascon S-box circuit in [DEMS21]  
**code_target_imps/Saturnin.py** : Saturnin super S-box circuit in [CDL+20]  
**code_target_imps/SNOW_up.py** : Front part of SNOW3G S-box in [BHNS10]  
**code_target_imps/SNOW_dn.py** : Back part of SNOW3G S-box in [BHNS10]  
**code_formal/AES10.py** : Formal type (XOR information) of **code_target_imps/AES10.py**  
Files in **code_results** directory : Results included in the paper.  

## How to Upload Circuits
To optimize a circuit, it must be uploaded as a Python file in the **code_target_imps** directory.
The implementation of the circuit must be inserted at the position marked by the following comment in the file:

```################### Here is your code !! ###################```

The input and output variables must be listed as ```x``` and ```y```, respectively.
For further instructions, refer to the example file provided in the **code_target_imps** directory.

## Generated Files by Our Tool
The **code_results** directory includes the result **.py** files.  
The **code_formal** directory includes temporary **.py** files to extract XOR information.  
The **log** directory includes log files recording the optimization process.  
The **log/view_Dist** directory includes log files that record changes to *Dist*.  
The **log/view_all_Info** directory includes log files containing information other than *Dist*.  

## Notes on the Resulting Circuit Files
When this tool runs to optimize the circuit, a file or files are generated in **core_results**.
The file name is written in the order of [original file name], [RNBP or limited depth], [number of XOR gates], [core name], and [time].
For example, if you run ```python main.py -f Ascon -a BPD -H 5```, a file called **core_results/Ascon_5H_11XORs_single_0s.py** is generated.
The optimized circuit is written in Python format in the generated file(s).

## Notes on Analyzing the Results
Using the **analyze** option, in **code_results/CODE_RESULTS.txt**, the following metrics are analyzed: depth (with NOTs), depth (without NOTs), AND-depth, ANDs, ORs, XORs, and NOTs.
When all NOT gates are combined into an XNOR gate, the latency of the circuit follows *depth (without NOTs)* rather than *depth (with NOTs)*.

## Running Time
Our multi-threading option does not improve the speed of one search, but it enables multiple searches to run concurrently. The following shows the time taken for one search per circuit with the AMD Ryzen 9 7950X:  
Ascon S-box : Less than 1s,  
AES S-box : 3h - 20h,  
Saturnin super S-box : About a week,  
A part of SNOW3G S-box : 12h - a day (when applying the technique to reduce the size of ```W``` as written in the paper.)  

## References
[BP10] Joan Boyar and René Peralta. A new combinational logic minimization technique with applications to cryptology. In Paola Festa, editor, Experimental Algorithms, 9th International Symposium, SEA 2010, Ischia Island, Naples, Italy, May 20-22, 2010. Proceedings, volume 6049 of Lecture Notes in Computer Science, pages 178–189. Springer, 2010.  
[BHNS10] Billy Bob Brumley, Risto M. Hakala, Kaisa Nyberg, and Sampo Sovio. Consecutive s-box lookups: A timing attack on SNOW 3g. In Miguel Soriano, Sihan Qing, and Javier López, editors, Information and Communications Security - 12th International Conference, ICICS 2010, Barcelona, Spain, December 15-17, 2010. Proceedings, volume 6476 of Lecture Notes in Computer Science, pages 171–185. Springer, 2010.  
[BP12] Joan Boyar and René Peralta. A small depth-16 circuit for the AES s-box. In Dimitris Gritzalis, Steven Furnell, and Marianthi Theoharidou, editors, Information Security and Privacy Research - 27th IFIP TC 11 Information Security and Privacy Conference, SEC 2012, Heraklion, Crete, Greece, June 4-6, 2012. Proceedings, volume 376 of IFIP Advances in Information and Communication Technology, pages 287–298. Springer, 2012.  
[CDL+20] Anne Canteaut, Sébastien Duval, Gaëtan Leurent, María Naya-Plasencia, Léo Perrin, Thomas Pornin, and André Schrottenloher. Saturnin: a suite of lightweight symmetric algorithms for post-quantum security. IACR Transactions on Symmetric Cryptology, 2020(S1):160–207, 2020.  
[DEMS21] Christoph Dobraunig, Maria Eichlseder, Florian Mendel, and Martin Schläffer. Ascon v1. 2: Lightweight authenticated encryption and hashing. Journal of Cryptology, 34:1–42, 2021.  
