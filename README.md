# ESO: March 25th - June 25th 2023

This repository contains all the code that was used during my time at the European Sout Observatory Headquarters in Garching, Munich. All code is written in Python but is meant to be run through CASA (the Common Astronomy Software Application). It concerns imaging and baselining data from the Atacama Large Millimeter Array (ALMA). There are two main branches, one containing code for the Spiderweb galaxy (z = 2.163), project under the guidance of Carlos De bBreuk and Paola Andreani, and the other for the SPT galaxy Cluster (z=4.3), for Allison Man's project on large redshift clusters. 

## Spiderweb - 

The spiderweb galaxy is located at z = 2.163. Our observations were taken at band four, and therefore we seek lines for Carbon Monoxide (CO(4->3)) and Atomic Carbon (CI(1->0)) which are at this frequency inside the band. This set consists of:

* Computation of imaging Parameters - using .ms files produced by scriptforpy
* Computation of imaging Parameters - using .ms files produced manually with importasdm
* sdimaging for the parameters of the first code
* sdimaging for the parameters of the second code



## SPT Cluster - 

The SPT Cluster is found at z=4.3. We are searching for the line of CI(1->0) which is redshifted to 92 GHz. Our observations are in Band 3 of ALMA. Unlike Spiderweb, this cluster is separated into a northern and souther region, and so our data have 2 fields which we can examine. This set consists of:

* Computation of imaging Parameters for the Southern Region - using .ms files produced by scriptforpy
* Computation of imaging Parameters for the Southern Region - using .ms files produced manually with importasdm
* Computation of imaging Parameters for the Northern Region - using .ms files produced manuallu with importasdm
* sdimaging code for the southern region
* sdimaging code for the northern region

Normally the data is baselined before imaging, either using sdbasline on CASA or automatically during the run of scriptforpy. However, the line in this case was too faint. These codes offer a workaround, but they must be run AFTER sdimaging:

* Continuum subtraction for the images of the Southern Cluster
* Continuum Subtraction for the images of the Northern Cluster


## Necessary Installments

To run this code, one must have:

* the latest pipeline version of CASA (12.4.1.12 as of this moment): https://casa.nrao.edu/casa_obtaining.shtml
* NumPy 1.24.2 (imported as np) : https://numpy.org/
* the Analysis Utilities package (imported as au): https://casaguides.nrao.edu/index.php/Analysis_Utilities
