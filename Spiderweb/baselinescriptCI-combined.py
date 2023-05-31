# Script for SD supplemental imaging with manual baseline subtraction
# and imaging of a Spw/Source.
#
# Usage: CASA> execfile('scriptForSDSupplementalImaging.py') 
# 
# Inputs
# - user path to analysisUtils.py
# Baseline:
# - ms data sets after atmospheric correction (before pipeline baseline)
# - spw (spectral window)
# - channels to be used for baseline support
# - baseline order
# baseline command can be modified further as needed
#
# Imaging: Take minimum parameters from the weblog step 13. hsd_imaging
#          casa.log (linked at the bottom of the weblog page) for the
#          respective mous/spw.
# - phase center
# - imsize
# Remaining imaging parameters are inferred with analysisUtils, or can
# be modified in the imaging step.
#
# Outputs
# .png image per antenna/pol of baselined spectra for each eb
# casa (.image.sd) and fits (.image.sd.fits) image cubes

import os
from sys import path
import glob
scan = '4'
# === USER INPUTS ===
# Path to your analysUtils.py
path_analysisUtils = "/scratch/home/emanolid/data/casa/analysis_scripts"

# List of ms files after atm correction, uid___xxx.ms.atmcor.atmtypeX
# If the conventional pipeline naming is used the glob() should work
ms_names = glob.glob('*_newCI.ms.atmcor.atmtype')
# ms_names = ['uid___A002_Xf49cca_X2514b.ms.atmcor.atmtype1',
#             'uid___A002_Xf53eeb_X217cd.ms.atmcor.atmtype1',
#            ]

# Baseline parameters
spw = '0'  # Spw to baseline/image
baseline_support = '0~300;900~1700'  # Channel range(s) to fit baseline
# baseline_support = '10~20;2020~2030'  # Ex. multiple channel ranges
baseline_order = 1  # Polynomial fit order

# Imaging parameters
phasecenter = 'ICRS 11:40:48.35 -026.29.02.252'  # Phase center (weblog)
imsize =  [44, 50] # Image size (weblog)
expath = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/combined/baselines/'

# === NO EDITS SHOULD BE NEEDED BELOW ===
# Get imaging parameters with analysisUtils.py and prepare meta data
path.append(path_analysisUtils)
import analysisUtils as aU
es = aU.stuffForScienceDataReduction()

d = aU.representativeSource(ms_names[0])
field_id = next(iter(d.keys())) 
source = next(iter(d.values()))
frequency = aU.restFrequency(ms_names[0], spw=spw, source=source)[0]
theorybeam = aU.primaryBeamArcsec(frequency=frequency*1e-9,
                                  fwhmfactor=1.131,
                                  diameter=12)
cellsize = theorybeam / 9.0
sfbeam = aU.sfBeam(frequency=frequency*1e-9,
                   pixelsize=cellsize,
                   convsupport=6,
                   img=None,
                   stokes='both',
                   fwhmfactor=1.131,
                   diameter=12)[0]
out = f'{source}_spw{spw}.image.sd'
outimage = expath + out
# Subtract baseline for all ms
bl_files = []
for i, ms in enumerate(ms_names, start=1):
    outfile = expath+ ms + f'_CI.bl'
    print(f'- Substracting baseline {ms} (eb {i}/{len(ms_names)}) -> '
          f'{outfile}')
    sdbaseline(infile = ms,
               datacolumn='data',
               blmode='fit',
               dosubtract=True,
               maskmode = 'list',
               blfunc = 'poly',  # Baseline function
               order = baseline_order,  # Baseline order
               spw = f'{spw}:{baseline_support}',
               outfile=outfile,
               overwrite=True)
    print(f'  Plotting antenna/pol spectra -> '
          f'{outfile+"_AntennaXXX.png"}')
    plotms(vis=outfile,
           xaxis='chan',
           yaxis='real',
           ydatacolumn='data',
           field=source,
           intent='OBSERVE_TARGET#ON_SOURCE',
           # spw='0',  # For single spw it should be no 0
           averagedata=True,
           avgtime='1e8',
           avgscan=True,
           coloraxis='corr',
           showgui=False,
           showatm=False,
           gridrows=2,
           gridcols=2,
           iteraxis='antenna',
           xselfscale=True,
           yselfscale=True,
           ysharedaxis=True,
           xsharedaxis=True,
           showmajorgrid=True,
           plotfile=outfile+'.png',
           overwrite=True,
           highres=True)
    bl_files.append(outfile)


