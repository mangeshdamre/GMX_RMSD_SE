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
## Std. Error.
Now assume having multiple RMSD files from multiple trajectories. Lets consider `(n=5)`. \
The standard error (SE) of a statistic is the approximate standard deviation (SD = **σ**) of a statistical sample population `(n=5)`. The standard error is a statistical term that measures the accuracy with which a sample distribution represents a population by using standard deviation. In statistics, a sample mean deviates from the actual mean of a population (**μ**); this deviation is the standard error of the mean. SE is defined as: \

<img src="https://render.githubusercontent.com/render/math?math={SD}={\sigma}=\sqrt{ \frac{1}{n} \sum_{i=1}^{n} \(x_i-\mu)^2 }"> \
Python comes very handy while performing data operations. By importing `numpy` library, SD and SE calculations can be performed. For example, 
```py
rmsd_std = np.std([trajOne, trajTwo, trajThree, trajFour, trajFive], axis=0)
rmsd_err = rmsd_std / np.sqrt(5)
```
For more details refer to the **<a href="https://github.com/mangeshdamre/GMX_RMSD_SE_PLOT/blob/main/scripts/rmsd_SE.py" target="_blank">rmsd_SE.py</a>** or https://github.com/mangeshdamre/GMX_RMSD_SE_PLOT/blob/238c7f28a668b2f888b4af47e076b2c1ccd0fee5/scripts/rmsd_SE.py#L142-L143.

**How to plot RMSD and SE?**
Now we have basic idea of RMSD and SE. Lets plot them in the graph using Python script.
Assume we have RMSD data file for 5 trajectories. Each RMSD file contains two columns `(time, RMSD)`. Cancatenate all the RMSD data files into one for ease of use.
```sh
paste 1.xvg 2.xvg 3.xvg 4.xvg 5.xvg > abc.xvg  
```
`paste` command will concatenate all the columns into single file which looks like:
```
   0.0000000    0.0520567	   0.0000000    0.0501020	   0.0000000    0.0536470	   0.0000000    0.0520567	   0.0000000    0.0520567
   0.0500000    0.1738762	   0.0500000    0.1738991	   0.0500000    0.1656937	   0.0500000    0.1767206	   0.0500000    0.1733002
   0.1000000    0.2030493	   0.1000000    0.1959478	   0.1000000    0.1833290	   0.1000000    0.2079110	   0.1000000    0.1898366
   0.1500000    0.2113873	   0.1500000    0.2260462	   0.1500000    0.2141280	   0.1500000    0.2258700	   0.1500000    0.2134524
   0.2000000    0.2206186	   0.2000000    0.2318131	   0.2000000    0.2211261	   0.2000000    0.2396275	   0.2000000    0.2169894
   ... ... ... ...
```
Columns `1,3,5,7,9` represents time of the simulation in `ns` and columns `2,4,6,8,10` represents RMSD values for 5 trajectories in `nm` `(nm = 10^-9 m)`.

Pyhton is very convinient to do data operations and graphical plotting. Please use the script (**<a href="https://github.com/mangeshdamre/GMX_RMSD_SE_PLOT/blob/main/scripts/rmsd_SE.py" target="_blank">rmsd_SE.py</a>**) for RMSD+SE plotting.To do so, we will import following libraries in python:
```py
#!/usr/bin/env python3.8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import scipy.stats
import math
import string
import sys
import argparse
```
**How to use rmsd_SE.py?**
```sh
./rmsd_SE.py -h
```
```ruby
usage: rmsd_SE.py [-h] [-x X] -X X [-y Y] -Y Y -f1 F1 -t T -o O

Plot Average RMSD with Std. Error!

optional arguments:
  -h, --help       show this help message and exit
  -x X, --x X      This is the 'xmin' variable : default = 0
  -X X, --X X      This is the 'xmax' variable : default = 25
  -y Y, --y Y      This is the 'ymin' variable : default = 0
  -Y Y, --Y Y      This is the 'Ymax' variable : default = 10
  -f1 F1, --f1 F1  Input RMSD data file name for multiple trajectory data.
  -t T, --t T      Graph Title
  -o O, --o O      Name of output file name (output.png)
```

## Output plot
`rmsd_SE_5traj -x 0 -X 50 -y 0 -Y 7 -f abc.xvg -o output.png -t 'RMSD + SE plot'`
![alt text](https://github.com/mangeshdamre/GMX_RMSD_SE_PLOT/blob/main/demo/output.png?raw=true)
