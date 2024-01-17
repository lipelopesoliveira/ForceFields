# DREIDING Force Field

This folder contains the necessary parameters for the use of the DREIDING force field by the RASPA program. In addition to the parameters of the DREIDING force field, which are used for the framework atoms, some specific parameters taken from the TraPPE model and others were added to treate the gas atoms.

## DREIDING Parameters

Parameters taken from **Table II** of *MAYO, Stephen L.; OLAFSON, Barry D.; GODDARD, William A. DREIDING: a generic force field for molecular simulations. Journal of Physical chemistry, v. 94, n. 26, p. 8897-8909, 1990.*

| Atom | R<sub>min</sub> (A)  | D<sub>0</sub> (kcal/mol) | σ (A)   | ε (K)      |
|------|---------|---------------|---------|------------|
| H    | 3.19500 | 0.01520       | 2.84642 | 7.648938   |
| B    | 4.02000 | 0.09500       | 3.58141 | 47.805859  |
| C    | 3.89830 | 0.09510       | 3.47299 | 47.856181  |
| N    | 3.66210 | 0.07740       | 3.26256 | 38.949195  |
| O    | 3.40460 | 0.09570       | 3.03315 | 48.158113  |
| F    | 3.47200 | 0.07250       | 3.09320 | 36.483419  |
| Al   | 4.39000 | 0.31000       | 3.91105 | 155.998068 |
| Si   | 4.27000 | 0.31000       | 3.80414 | 155.998068 |
| P    | 4.15000 | 0.32000       | 3.69723 | 161.030264 |
| S    | 4.03000 | 0.34400       | 3.59032 | 173.107533 |
| Cl   | 3.95030 | 0.28330       | 3.51932 | 142.562105 |
| Ga   | 4.39000 | 0.40000       | 3.91105 | 201.287829 |
| Ge   | 4.27000 | 0.40000       | 3.80414 | 201.287829 |
| As   | 4.15000 | 0.41000       | 3.69723 | 206.320025 |
| Se   | 4.03000 | 0.43000       | 3.59032 | 216.384417 |
| Br   | 3.95000 | 0.37000       | 3.51905 | 186.191242 |
| In   | 4.59000 | 0.55000       | 4.08923 | 276.770766 |
| Sn   | 4.47000 | 0.55000       | 3.98232 | 276.770766 |
| Sb   | 4.35000 | 0.55000       | 3.87541 | 276.770766 |
| Te   | 4.23000 | 0.57000       | 3.76850 | 286.835157 |
| I    | 4.15000 | 0.51000       | 3.69723 | 256.641983 |

## Gas Parameters

| Atom   | σ (A)   | ε (K)      |    Charge   |   Source   |
|--------|---------|------------|-------------|------------| 
| He     | 2.64000 | 10.900000  |   0.0000    |    [1]     |
| O_co2  | 3.05000 | 79.000000  |  -0.3500    |    [2]     |
| C_co2  | 2.80000 | 27.000000  |   0.7000    |    [2]     |
| N_n2   | 3.30600 | 38.298000  |  -0.4050    |    [3]     |
| N_com  |    -    |     -      |   0.8100    |    [3]     |
| O_o2   | 3.04500 |  53.023000 |  -0.1120    |    [3]     |
| O_com  |    -    |     -      |   0.2240    |    [3]     |
| Ar     | 3.380000| 124.070000 |   0.0000    |    [3]     |
| CH4    | 3.73000 | 148.000000 |   0.0000    |    [4]     |
| H_h2   |    -    |     -      |   0.4680    |    [5]     |
| H_com  | 2.72000 | 10.0000000 |  -0.9360    |    [5]     |
| C_co   | 3.63600 | 16.1410000 |  -0.2424    |    [6]     |
| CO_com |    -    |     -      |   0.5168    |    [6]     |
| O_co   | 2.97900 | 98.0140000 |  -0.2744    |    [6]     |
| Ow     | 3.09700 | 89.5730841 |   0.0000    |    [7]     |
| Lw     |    -    |     -      |  -0.2410    |    [7]     |
| Hw     |    -    |     -      |   0.2410    |    [7]     |
| O_so2  |  73.8   |    3.39    |  −0.295     |    [8]     |
| S_so2  |  79.0   |    3.05    |   0.59      |    [8]     |

### References
1. J.O. Hirschfelder et al., Molecular Theory of Gases and Liquids, Wiley, New York, 1954, p. 1114.
2. J. Potoff, and J.I. Siepmann, AIChE J. 47, 1676-1682 (2001).
3. A. Martin-Calvo et al. , Phys. Chem. Chem. Phys. 2011, 13, 11165-11174.
4. M.G. Martin, and J.I. Siepmann, J. Phys. Chem. B 102, 2569-2577 (1998).
5. Q. Yang., and C. Zhong, J. Phys. Chem. B 2005, 109, 24, 11862–11864
6. A. Martin-Calvo et al. , J. Phys. Chem. C. 2012, 116, 6655.
7. S.W. Rick, J. Chem. Phys. 2004, 120 (13), 6085-6093.
8. J. Phys. Chem. B 2011, 115, 17, 4949–4954

## Conversion method

The Lennard-Jones potential has it minumum at a ditance R<sub>min</sub> = 2<sup>1/6</sup> . σ, so the conversion from R<sub>min</sub> to sigma is made dividing R<sub>min</sub> by 2<sup>1/6</sup>.

The conversion from kcal/mol to K is made dividing by the Boltzman constant (K<sub>b</sub>) in kcal/[mol.K] = 0.0019872041

## Instalation 

To install this force field you can create a new folder on the compiled raspa forcefield directory, usually on the folder: `${RASPA_DIR}/share/raspa/forcefield/`, and put the tree files on this new folder. You can put any name that you want, just remember to put this same name on the script to run the RASPA simulation under the `Forcefield` variable tag. 

You can also just put these tree files on the folder that you are running the RASPA, with the variable `Local` as the force field tag `Forcefield`. The program always search for force field files on the local folder first. 

Finally, you can put the folder with the molecule definition files (you can find these files on the `Molecules/Generic` directory of this repository) on the `${RASPA_DIR}/share/raspa/molecules/` directory. This folder contains the molecule definitions (i.e. atomic type, positions and thermodynamic informations) for the program to run the simmulations. These informations are taken from the [TraPPE](http://trappe.oit.umn.edu/) database. You can also change the gas molecules parameters to some other files on the `Molecules` folder on this repository, just remenber to change the parameters on force field files. 
