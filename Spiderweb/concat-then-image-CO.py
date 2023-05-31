
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
a = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/combined/baselines/'
bl_names = [
	a+'uid___A002_X101c3b2_X42b1_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X101e5ab_Xf704_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X10239e1_X178c7_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X10239e1_X181b9_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X10239e1_X18e80_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X10275c0_X17ff7_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X10305a2_X224e_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X10305a2_X2c6c_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X103317b_X20c5_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X103317b_X2744_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X1033b6e_X153b_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X1033b6e_X1bbd_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X1033b6e_X21ed_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X1033b6e_Xfe3_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X1034414_X15fc_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X1034414_X2139_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X1034414_X27c9_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X1034414_X2dbd_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X1034f36_X119b_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X1034f36_Xa80_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X1035744_X2f7a_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X1035744_X34cd_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X1036d05_X2644_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X1036d05_X2c62_newCO.ms.atmcor.atmtype_CO.bl',
	a+'uid___A002_X1036d05_X33a5_newCO.ms.atmcor.atmtype_CO.bl'
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
	
names = [
	'uid___A002_X101c3b2_X42b1',
	'uid___A002_X101e5ab_Xf704',
	'uid___A002_X10239e1_X178c7',
	'uid___A002_X10239e1_X181b9',
	'uid___A002_X10239e1_X18e80',
	'uid___A002_X10275c0_X17ff7',
	'uid___A002_X10305a2_X224e',
	'uid___A002_X10305a2_X2c6c',
	'uid___A002_X103317b_X20c5',
	'uid___A002_X103317b_X2744',
	'uid___A002_X1033b6e_X153b',
	'uid___A002_X1033b6e_X1bbd',
	'uid___A002_X1033b6e_X21ed',
	'uid___A002_X1033b6e_Xfe3',
	'uid___A002_X1034414_X15fc',
	'uid___A002_X1034414_X2139',
	'uid___A002_X1034414_X27c9',
	'uid___A002_X1034414_X2dbd',
	'uid___A002_X1034f36_X119b',
	'uid___A002_X1034f36_Xa80',
	'uid___A002_X1035744_X2f7a',
	'uid___A002_X1035744_X34cd',
	'uid___A002_X1036d05_X2644',
	'uid___A002_X1036d05_X2c62',
	'uid___A002_X1036d05_X33a5'
	]
	


#Averaging channels:
i = 0
bl_names2 = []
b = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/combined/baselines/averaged/'
for file in bl_names:
	print("Averaging...", file)
	outfile = b+ names[i] +'_CO_averaged'
	mstransform(vis = file, outputvis = outfile, chanaverage = True, chanbin = 20,datacolumn = 'data')
	bl_names2.append(outfile)
	i = i+1
print("Averaged", bl_names2)

# Baseline parameters
spw = '19'  # Spw to baseline/image

# Imaging parameters
phasecenter = 'ICRS 11:40:48.35 -026.29.02.252'  # Phase center (weblog)
imsize =  [42, 46] # Image size (weblog)
expath = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/combined/'
troubleshooting = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/combined/baselines/troubleshooting/'
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
outimage = expath +'Concatenated_' + out

print('Concatenating...')

concat(vis = bl_names2, concatvis= 'Spiderweb_concatenated_CO.ms',respectname=True)

print('Imaging full spectra...')

        
# Image all baselined spectra

sdimaging(infiles=['Spiderweb_concatenated_CO.ms'],
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


# Correct the brightness unit in the image header
print(f'- Correct image header unit ({outimage})')
imhead(imagename = outimage,
       mode = 'put',
       hdkey = 'bunit',
       hdvalue = 'Jy/beam')
      
# Add Restoring Beam Header Information to the Science Image
print(f'- Add restore beam to header ({outimage})')
myia = iatool()
myia.open(outimage)
myia.setrestoringbeam(major = str(sfbeam)+'arcsec',
                      minor = str(sfbeam)+'arcsec',
                      pa = '0deg')
myia.done()
    
# Export fits file
print(f'- Exporting fits cube {outimage} -> {outimage}.fits')
if os.path.isfile(outimage + '.fits'):
    os.remove(outimage + '.fits')
exportfits(imagename = outimage,
           fitsimage = outimage + '.fits')

# Create profile map
print(f'- Creating profile map -> {outimage.replace(".image.sd", "_profilemap.png")}')
plotprofilemap(imagename=outimage, 
               figfile = outimage.replace('.image.sd', '_profilemap.png'),
               overwrite=True, 
               separatepanel=False, 
               spectralaxis = 'frequency', 
               transparent = False, 
               showaxislabel = True, 
               showtick = True, 
               showticklabel = True, 
               numpanels='4', 
               figsize='40cm,30cm') 
  
