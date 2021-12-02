# ForceFields
 A repository to hold my personal developed forcefields for molecular mechanics calculations

This force field is built by combining the main parameters from `DREIDING` force field for light elements, such as C, N, H, O, and others, and parameters from `UFF` for heavy elements, both used for frameworks atoms. 

For the adsorbate atoms the parameters is taken from different sources, all documented in the `force_field_mixing_rules.def` file.

# DREIDING Parameters

| Atom | R0 (A) | D0 (kcal/mol) |
|------|--------|---------------|
| H    | 3.195  | 0.0152        |
| B    | 4.02   | 0.095         |
| C    | 3.8983 | 0.0951        |
| N    | 3.6621 | 0.0774        |
| O    | 3.4046 | 0.0957        |
| F    | 3.4720 | 0.0725        |
| Al   | 4.39   | 0.31          |
| Si   | 4.27   | 0.31          |
| P    | 4.15   | 0.32          |
| S    | 4.03   | 0.344         |
| Cl   | 3.9503 | 0.2833        |
| Ga   | 4.39   | 0.40          |
| Ge   | 4.27   | 0.40          |
| As   | 4.15   | 0.41          |
| Se   | 4.03   | 0.43          |
| Br   | 3.95   | 0.37          |
| In   | 4.59   | 0.55          |
| Sn   | 4.47   | 0.55          |
| Sb   | 4.35   | 0.55          |
| Te   | 4.23   | 0.57          |
| I    | 4.15   | 0.51          |

## Instalation 

To install this force field you can create a new folder on the compiled raspa forcefield directory, usually on the folder: `${RASPA_DIR}/share/raspa/forcefield/`, and put the tree files in the `DREIDING-UFF-TRAPPE` on this new folder. You can put any name that you want, just remember to put this same name on the script to run the RASPA simulation under the `Forcefield` variable tag. 

You can also just put these tree files on the folder that you are running the RASPA, with the variable `Local` as the force field. The program always search for force field files on the local folder first. 

Finally, you can put the folder `Trappe` on the `${RASPA_DIR}/share/raspa/molecules/` directory. This folder contains the molecule definitions (i.e. atomic type, positions and thermodynamic informations) for the program to run the simmulations. These informations are taken from the [TraPPE](http://trappe.oit.umn.edu/) database. 
