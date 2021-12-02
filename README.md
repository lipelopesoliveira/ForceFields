# ForceFields
 A repository to hold my personal developed forcefields for molecular mechanics calculations

This force field is built by combining the main parameters from `DREIDING` force field for light elements, such as C, N, H, O, and others, and parameters from `UFF` for heavy elements, both used for frameworks atoms. 

For the adsorbate atoms the parameters is taken from different sources, all documented in the `force_field_mixing_rules.def` file.

# DREIDING Parameters

| Atom | R0 (A)  | D0 (kcal/mol) | σ (A)   | ε (K)      |
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

## Instalation 

To install this force field you can create a new folder on the compiled raspa forcefield directory, usually on the folder: `${RASPA_DIR}/share/raspa/forcefield/`, and put the tree files in the `DREIDING-UFF-TRAPPE` on this new folder. You can put any name that you want, just remember to put this same name on the script to run the RASPA simulation under the `Forcefield` variable tag. 

You can also just put these tree files on the folder that you are running the RASPA, with the variable `Local` as the force field. The program always search for force field files on the local folder first. 

Finally, you can put the folder `Trappe` on the `${RASPA_DIR}/share/raspa/molecules/` directory. This folder contains the molecule definitions (i.e. atomic type, positions and thermodynamic informations) for the program to run the simmulations. These informations are taken from the [TraPPE](http://trappe.oit.umn.edu/) database. 
