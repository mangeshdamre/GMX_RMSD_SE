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
