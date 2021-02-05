# RMSD with Std. Error plot
Use the script to calculate the RMSD of a protein from molecular dynamics simulations performed by GROMACS.
`gmx rms -h` is used to calculate the rmsd of a protein with given selection.
Having multiple simulations of similar setup, it is worth while to look into RMSDs and Std. Error related to it.
## RMSD
**Root Mean Square Deviation.** The Root Mean Squared Deviation (RMSD) is a numerical measure of the difference between two structures/selections and is defined as: \
\
<img src="https://render.githubusercontent.com/render/math?math={RMSD}=\sqrt{\frac{1}{N_{atoms}}\sum_{i=1}^{N_{atoms}}\(r_i(t_1)-r_i(t_2))^2}"> \
where __*N<sub>atoms</sub>*__ is the number of atoms whose positions are being compared, and __*r<sub>i</sub>(t)*__ is the position of atom __*i*__ at time __*t*__.

**How to calculate RMSD using GROMACS?** \
`gmx rms -h` will guide through the usage of the command with elaborate description.
```sh
gmx rms -s abc.tpr -f abc.xtc -o abc.xvg -tu ns -n index.ndx
```
The above command in terminal will allow you to select an option listed in the `index.ndx` file. For example:
```sh
Select group for least squares fit
Group     0 (         System) has 420972 elements
Group     1 (        Protein) has 18864 elements
Group     2 (      Protein-H) has 14748 elements
Group     3 (        C-alpha) has  1902 elements
Group     4 (       Backbone) has  5706 elements
Group     5 (      MainChain) has  7614 elements
Group     6 (   MainChain+Cb) has  9396 elements
Group     7 (    MainChain+H) has  9450 elements
Group     8 (      SideChain) has  9414 elements
Group     9 (    SideChain-H) has  7134 elements
Group    10 (    Prot-Masses) has 18864 elements
Group    11 (    non-Protein) has 402108 elements
Group    12 (          Water) has 402066 elements
Group    13 (            SOL) has 402066 elements
Group    14 (      non-Water) has 18906 elements
Group    15 (            Ion) has    42 elements
Group    16 (             NA) has    42 elements
Group    17 ( Water_and_ions) has 402108 elements
```
To calculate RMSD for `Backbone` atoms for every frame we select a group `4` first to align all the frames in the trajectory with respect to first frame. Later it will ask to make second selection to calculate the RMSD next group (again select group `4`).
```sh
Select a group: 4
Selected 4: 'Backbone'
Select group for RMSD calculation
Group     0 (         System) has 420972 elements
Group     1 (        Protein) has 18864 elements
Group     2 (      Protein-H) has 14748 elements
Group     3 (        C-alpha) has  1902 elements
Group     4 (       Backbone) has  5706 elements
Group     5 (      MainChain) has  7614 elements
Group     6 (   MainChain+Cb) has  9396 elements
Group     7 (    MainChain+H) has  9450 elements
Group     8 (      SideChain) has  9414 elements
Group     9 (    SideChain-H) has  7134 elements
Group    10 (    Prot-Masses) has 18864 elements
Group    11 (    non-Protein) has 402108 elements
Group    12 (          Water) has 402066 elements
Group    13 (            SOL) has 402066 elements
Group    14 (      non-Water) has 18906 elements
Group    15 (            Ion) has    42 elements
Group    16 (             NA) has    42 elements
Group    17 ( Water_and_ions) has 402108 elements
```
