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
Following is the quick bash script to calculate the RMSD:
```sh
#!/bin/sh
tpr=abc.tpr
xtc=abc.xtc
output=abc.xvg
index=index.ndx

echo 4 4 | gmx rms -s $tpr -f $xtc -o $output -tu ns -n $index
```
**Std. Error.**
Now assume having multiple RMSD files from multiple trajectories. Lets consider `(n=5)`. \
The standard error (SE) of a statistic is the approximate standard deviation (SD = **σ**) of a statistical sample population `(n=5)`. The standard error is a statistical term that measures the accuracy with which a sample distribution represents a population by using standard deviation. In statistics, a sample mean deviates from the actual mean of a population (**μ**); this deviation is the standard error of the mean. SE is defined as:
<img src="https://render.githubusercontent.com/render/math?math={SD}={\sigma}=\sqrt{ \frac{1}{n} \sum_{i=1}^{n} \(x_i-\mu)^2 }"> \

**How to plot RMSD and SE?**
Now we have basic idea of RMSD and SE. Lets plot them in the graph using Python script.
Assume we have RMSD data file for 5 trajectories which looks like:
```
   0.0000000    0.0520567	   0.0000000    0.0501020	   0.0000000    0.0536470	   0.0000000    0.0520567	   0.0000000    0.0520567
   0.0500000    0.1738762	   0.0500000    0.1738991	   0.0500000    0.1656937	   0.0500000    0.1767206	   0.0500000    0.1733002
   0.1000000    0.2030493	   0.1000000    0.1959478	   0.1000000    0.1833290	   0.1000000    0.2079110	   0.1000000    0.1898366
   0.1500000    0.2113873	   0.1500000    0.2260462	   0.1500000    0.2141280	   0.1500000    0.2258700	   0.1500000    0.2134524
   0.2000000    0.2206186	   0.2000000    0.2318131	   0.2000000    0.2211261	   0.2000000    0.2396275	   0.2000000    0.2169894
   ... ... ... ...
```
Columns `1,3,5,7,9` represents time of the simulation in `ns` and columns `2,4,6,8,10` represents RMSD values for 5 trajectories in `nm` (nm = 10^-9 m).
 
