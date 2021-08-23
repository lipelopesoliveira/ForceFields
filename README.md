# ForceFields
 A repository to hold my personal developed forcefields for molecular mechanics calculations

This force field is built by combining the main parameters from `DREIDING` force field for light elements, such as C, N, H, O, and others, and parameters from `UFF` for heavy elements, both used for frameworks atoms. 

For the adsorbate atoms the parameters is taken from different sources, all documented in the `force_field_mixing_rules.def` file.

## Instalation 

To install this force field you can create a new folder on the compiled raspa forcefield directory, usually on the folder: `${RASPA_DIR}/share/raspa/forcefield/`, and put the tree files in the `DREIDING-UFF-TRAPPE` on this new folder. You can put any name that you want, just remember to put this same name on the script to run the RASPA simulation under the `Forcefield` variable tag. 

You can also just put these tree files on the folder that you are running the RASPA, with the variable `Local` as the force field. The program always search for force field files on the local folder first. 

Finally, you can put the folder `Trappe` on the `${RASPA_DIR}/share/raspa/molecules/` directory. This folder contains the molecule definitions (i.e. atomic type, positions and thermodynamic informations) for the program to run the simmulations. These informations are taken from the (TraPPE)[http://trappe.oit.umn.edu/] database. 
