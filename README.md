# Force Fields for RASPA

This repository contains files with DREIDING and UFF force field parameters for simulations using the RASPA program. 

The general definition of the van der Waals parameters is done as follows:

![lennard_jones_potential](https://github.com/lipelopesoliveira/ForceFields/assets/33868364/dbdc9411-036f-49ec-8295-5915adfd1433)

![CodeCogsEqn](https://user-images.githubusercontent.com/33868364/144495206-9dd075db-1c04-4969-98fc-3cb84b82e332.png)


The Lennard-Jones potential has it minumum at a ditance R<sub>min</sub> = 2<sup>1/6</sup> . σ, so the conversion from R<sub>min</sub> to sigma is made dividing R<sub>min</sub> by 2<sup>1/6</sup>.

The conversion from kcal/mol to K is made dividing by the Boltzman constant (K<sub>b</sub>) in kcal/[mol.K] = 0.0019872041


## Instalation 

To install this force field you can create a new folder on the compiled raspa forcefield directory, usually on the folder: `${RASPA_DIR}/share/raspa/forcefield/`, and put the tree files in the chosed force field on this new folder. You can put any name that you want, just remember to put this same name on the script to run the RASPA simulation under the `Forcefield` variable tag. 

You can also just put these tree files on the folder that you are running the RASPA, with the variable `Local` as the force field. The program always search for force field files on the local folder first. 

