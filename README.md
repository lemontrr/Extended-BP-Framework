# Extended-BP-Framework
This repository includes a tool for optimizing S-box circuits while maintaining nonlinear gates and AND-depth.
You can access all folders and files once you unzip the Extended_BP_Framework.zip file.
For more details, please refer to the paper.

## How to Upload Circuits
The circuit you want to optimize must be uploaded as a Python file in the 'code_target_imps' folder.
The detailed code of the circuit should be placed between the lines '################### Here is your code !! ###################'.
The types of input and output variables must be list-type variable names 'x' and 'y'.
For details, please follow the file format already in the 'code_target_imps' folder.

## Options
mode : Choosing whether to optimize ('opt') or analyze ('anal') [default 'opt']

**-f** : Circuit filename to optimize (except '.py') [default : 'AES_32ANDs']

**-n** : Input size of the S-box [default : 8]

**-m** : Output size of the S-box [default : 8]

**-M** : The number of cores for multi threading (if 1, single core) [default : 1]

**-A** : BP based algorithm to be incorporated ('RNBP' or 'BPD') [default : 'RNBP']

**-H** : The depth limit [default : 23]

**-R** : Random circuit mofidication mode (True or False) [default : False]



**--AR** : Result filename to analyze performance (except '.py')

**--ALD** : Log filename to analyze changes in Dist (except '.txt')

**--ALI** : Log filename to analyze many informations (except '.txt')



## Usage Examples
Run the command below.
>python main.py opt
>
>python main.py opt -f AES_depth16
>
>python main.py opt -f AES_depth16 -M 12 -A BPD -H 15
>
>python main.py opt -n 5 -m 5 -f Ascon
>
>python main.py opt -n 5 -m 5 -f Ascon -M 4 -A BPD -H 5 -R
>
>python main.py opt -n 16 -m 16 -f Saturnin -M 8 -A RNBP
>
>python main.py anal -AR AES_32ANDs_BPD_best_23D_6AD_32NLs_82XORs
>
>python main.py anal -ALD log_example
>
>python main.py anal -ALI log_example
>

## Files Generated
**In 'code_results' folder** : result python file

**In 'code_formal' folder** : temporary Python file to extract XOR information

**In 'log' folder** : log file recording the optimization process



## Points for Analyzing the Results
Using the 'anal -AR' option the following measures are analyzed: depth (with NOTs), depth, AND-depth, ANDs, ORs, XORs, NOTs.
This measure ignores the implementation of the XNOR gates, and the NOT gates can be combined with the XOR gates to become the XNOR gates.
When all NOT gates are combined into an XNOR gate, the latency of the circuit follows 'depth' rather than 'depth (with NOTs)'.
