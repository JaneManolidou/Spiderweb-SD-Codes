

import os
from sys import path
import glob
scan = '4'
# === USER INPUTS ===
# Path to your analysUtils.py
path_analysisUtils = "/scratch/home/emanolid/data/casa/analysis_scripts"

# List of ms files after atm correction, uid___xxx.ms.atmcor.atmtypeX
# If the conventional pipeline naming is used the glob() should work
#bl_names = glob.glob('*_SI_spw21.bl')
bl_names = [
	'uid___A002_X101e5ab_Xf704.ms.atmcor.atmtype3_SI_spw19.bl',
	'uid___A002_X10239e1_X178c7.ms.atmcor.atmtype2_SI_spw19.bl',
	'uid___A002_X10239e1_X181b9.ms.atmcor.atmtype4_SI_spw19.bl',
	'uid___A002_X10239e1_X18e80.ms.atmcor.atmtype3_SI_spw19.bl',
	'uid___A002_X10275c0_X17ff7.ms.atmcor.atmtype2_SI_spw19.bl',
	'uid___A002_X10305a2_X224e.ms.atmcor.atmtype4_SI_spw19.bl',
	'uid___A002_X10305a2_X2c6c.ms.atmcor.atmtype1_SI_spw19.bl',
	'uid___A002_X103317b_X20c5.ms.atmcor.atmtype3_SI_spw19.bl',
	'uid___A002_X103317b_X2744.ms.atmcor.atmtype4_SI_spw19.bl',
	'uid___A002_X1033b6e_X153b.ms.atmcor.atmtype1_SI_spw19.bl',
	'uid___A002_X1033b6e_X1bbd.ms.atmcor.atmtype1_SI_spw19.bl',
	'uid___A002_X1033b6e_X21ed.ms.atmcor.atmtype4_SI_spw19.bl',
	'uid___A002_X1033b6e_Xfe3.ms.atmcor.atmtype1_SI_spw19.bl',
	'uid___A002_X1034414_X15fc.ms.atmcor.atmtype1_SI_spw19.bl',
	'uid___A002_X1034414_X2139.ms.atmcor.atmtype1_SI_spw19.bl',
	'uid___A002_X1034414_X27c9.ms.atmcor.atmtype3_SI_spw19.bl',
	'uid___A002_X1034414_X2dbd.ms.atmcor.atmtype2_SI_spw19.bl',
	'uid___A002_X1034f36_X119b.ms.atmcor.atmtype1_SI_spw19.bl',
	'uid___A002_X1034f36_Xa80.ms.atmcor.atmtype1_SI_spw19.bl',
	'uid___A002_X1035744_X2f7a.ms.atmcor.atmtype1_SI_spw19.bl',
	'uid___A002_X1035744_X34cd.ms.atmcor.atmtype3_SI_spw19.bl',
	'uid___A002_X1036d05_X2644.ms.atmcor.atmtype1_SI_spw19.bl',
	'uid___A002_X1036d05_X2c62.ms.atmcor.atmtype3_SI_spw19.bl',
	'uid___A002_X1036d05_X33a5.ms.atmcor.atmtype3_SI_spw19.bl',
	'uid___A002_X1036d05_Xb88f.ms.atmcor.atmtype1_SI_spw19.bl'
	]

pathms = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/'
ms_names = [
	pathms+'uid___A002_X101e5ab_Xf704.ms.atmcor.atmtype3',
	pathms+'uid___A002_X10239e1_X178c7.ms.atmcor.atmtype2',
	pathms+'uid___A002_X10239e1_X181b9.ms.atmcor.atmtype4',
	pathms+'uid___A002_X10239e1_X18e80.ms.atmcor.atmtype3',
	pathms+'uid___A002_X10275c0_X17ff7.ms.atmcor.atmtype2',
	pathms+'uid___A002_X10305a2_X224e.ms.atmcor.atmtype4',
	pathms+'uid___A002_X10305a2_X2c6c.ms.atmcor.atmtype1',
	pathms+'uid___A002_X103317b_X20c5.ms.atmcor.atmtype3',
	pathms+'uid___A002_X103317b_X2744.ms.atmcor.atmtype4',
	pathms+'uid___A002_X1033b6e_X153b.ms.atmcor.atmtype1',
	pathms+'uid___A002_X1033b6e_X1bbd.ms.atmcor.atmtype1',
	pathms+'uid___A002_X1033b6e_X21ed.ms.atmcor.atmtype4',
	pathms+'uid___A002_X1033b6e_Xfe3.ms.atmcor.atmtype1',
	pathms+'uid___A002_X1034414_X15fc.ms.atmcor.atmtype1',
	pathms+'uid___A002_X1034414_X2139.ms.atmcor.atmtype1',
	pathms+'uid___A002_X1034414_X27c9.ms.atmcor.atmtype3',
	pathms+'uid___A002_X1034414_X2dbd.ms.atmcor.atmtype2',
	pathms+'uid___A002_X1034f36_X119b.ms.atmcor.atmtype1',
	pathms+'uid___A002_X1034f36_Xa80.ms.atmcor.atmtype1',
	pathms+'uid___A002_X1035744_X2f7a.ms.atmcor.atmtype1',
	pathms+'uid___A002_X1035744_X34cd.ms.atmcor.atmtype3',
	pathms+'uid___A002_X1036d05_X2644.ms.atmcor.atmtype1',
	pathms+'uid___A002_X1036d05_X2c62.ms.atmcor.atmtype3',
	pathms+'uid___A002_X1036d05_X33a5.ms.atmcor.atmtype3',
	pathms+'uid___A002_X1036d05_Xb88f.ms.atmcor.atmtype1'
	]


# Baseline parameters
spw = '19'  # Spw to baseline/image
baseline_support = '0~176;865~1000'  # Channel range(s) to fit baseline
# baseline_support = '10~20;2020~2030'  # Ex. multiple channel ranges
baseline_order = 1  # Polynomial fit order

# Imaging parameters
phasecenter = 'ICRS 11:40:48.35 -026.29.02.252'  # Phase center (weblog)
imsize = [42, 46] # Image size (weblog)
expath = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/baselines/'
troubleshooting = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/baselines/troubleshooting/'

#Using the script to compute imaging parameters

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


          
# Image all baselined spectra
print(f'- Imaging: {", ".join(bl_names)} -> {outimage}')
sdimaging(infiles=bl_names,
          outfile=outimage,
          overwrite=True,
          field=str(field_id),
          intent='OBSERVE_TARGET#ON_SOURCE',
          mode='channel',
          start=0,
          width=1,
          veltype='radio',
          outframe='lsrk',
          gridfunction='SF',
          convsupport=6,
          truncate=-1,
          gwidth=-1,
          jwidth=-1,
          imsize=imsize,
          cell=f'{cellsize}arcsec',
          phasecenter=phasecenter,
          projection='SIN',
          ephemsrcname='',
          pointingcolumn='direction',
          restfreq=f'{frequency}Hz',
          stokes='I',
          minweight=0.1,
          brightnessunit='',
          clipminmax=False )

