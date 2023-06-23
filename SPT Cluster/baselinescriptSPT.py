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
ms_names = glob.glob('*.ms.atmcor.atmtype?')
# ms_names = ['uid___A002_Xf49cca_X2514b.ms.atmcor.atmtype1',
#             'uid___A002_Xf53eeb_X217cd.ms.atmcor.atmtype1',
#            ]

names = ['uid___A002_Xfa2f45_X50e6',
	'uid___A002_Xf53eeb_X1a8ca',
	'uid___A002_Xf9faf1_X402f',
	'uid___A002_Xf8d822_X7fe2',
	'uid___A002_Xfafcc0_X4f42',
	'uid___A002_Xf53eeb_X12997',
	'uid___A002_Xf53eeb_X12338',
	'uid___A002_Xf53eeb_X19feb', 
	'uid___A002_Xf73568_X2c01',
	'uid___A002_Xf53eeb_X4201',
	'uid___A002_Xf53eeb_X11d6b'
	]

print("Got the files")
print(ms_names)
 
merged = '/scratch/home/emanolid/data/SPT/2021.2.00019.S/science_goal.uid___A001_X15a9_X11e8/group.uid___A001_X15a9_X11e9/member.uid___A001_X15a9_X11ec/calibrated/working/combined/'
ms_names2_S = []
for file in ms_names:
	print('Merging:', file)
	outfile = merged + file +'_combined_S.ms'
	mstransform(vis = file, outputvis = outfile, spw = '17,19', intent = 'OBSERVE_TARGET#ON_SOURCE',datacolumn = 'data',combinespws = True,field = '1')
	ms_names2_S.append(outfile)
	
print("In the end we merged:")
print(ms_names2_S)
ms_names2_N = []
for file in ms_names:
	print('Merging:', file)
	outfile = merged + file +'_combined_N.ms'
	mstransform(vis = file, outputvis = outfile, spw = '17,19', intent = 'OBSERVE_TARGET#ON_SOURCE',datacolumn = 'data',combinespws = True,field = '2')
	ms_names2_N.append(outfile)
	
print("In the end we merged:")
print(ms_names2_N)

# Baseline parameters
spw = '0'  # Spw to baseline/image
baseline_support = '0~510;800~990'  # Channel range(s) to fit baseline
# baseline_support = '10~20;2020~2030'  # Ex. multiple channel ranges
baseline_order = 1  # Polynomial fit order

# Imaging parameters
phasecenter='ICRS 23:49:42.71 -056.38.21.673' # Phase center (weblog)
imsize=[32, 34] # Image size (weblog)
expath = '/scratch/home/emanolid/data/SPT/2021.2.00019.S/science_goal.uid___A001_X15a9_X11e8/group.uid___A001_X15a9_X11e9/member.uid___A001_X15a9_X11ec/calibrated/working/baselines/'

# === NO EDITS SHOULD BE NEEDED BELOW ===
# Get imaging parameters with analysisUtils.py and prepare meta data
path.append(path_analysisUtils)
import analysisUtils as aU
es = aU.stuffForScienceDataReduction()

d = aU.representativeSource(ms_names[0])
field_id = next(iter(d.keys())) 
source = next(iter(d.values()))
frequency = aU.restFrequency(ms_names[0], spw='19', source=source)[0]
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
out1 = f'{source}_spw{spw}_S.image.sd'
outimage1 = expath + out1
out2 = f'{source}_spw{spw}_N.image.sd'
outimage2 = expath + out2
# Subtract baseline for all ms
#North
bl_names_N = []
j=0
for i, ms in enumerate(ms_names2_N, start=1):
   if j==i:
   	j=j+1
   outfile = expath+ names[j] + f'_SI_spw{spw}_N.bl'
   print(f'- Substracting baseline {ms} (eb {i}/{len(ms_names)}) -> ' f'{outfile}')
   j = j+1
   sdbaseline(infile = ms,datacolumn='data',blmode='fit',dosubtract=True,maskmode = 'list',blfunc = 'poly', order = baseline_order, spw = f'{spw}:{baseline_support}',outfile=outfile,overwrite=True)
   print(f'  Plotting antenna/pol spectra -> 'f'{outfile+"_AntennaXXX.png"}')
   plotms(vis=outfile,xaxis='chan', yaxis='real',ydatacolumn='data',field=source,intent='OBSERVE_TARGET#ON_SOURCE',averagedata=True,avgtime='1e8',avgscan=True,coloraxis='corr',showgui=False,showatm=False,gridrows=2,gridcols=2,iteraxis='antenna',    xselfscale=True,yselfscale=True,ysharedaxis=True,xsharedaxis=True,showmajorgrid=True,plotfile=outfile+'.png',overwrite=True,highres=True)
   bl_names_N.append(outfile)
print("Baselined North component")
#South
bl_names_S = []
j=0
for i, ms in enumerate(ms_names2_S, start=1):
    outfile = expath+ names[j] + f'_SI_spw{spw}_S.bl'
    print(f'- Substracting baseline {ms} (eb {i}/{len(ms_names)}) -> '
          f'{outfile}')
    j = j+1
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
    bl_names_S.append(outfile)
print("Baselined South component")

#Average Channels

i = 0
bl_names_S2 = []
b ='/scratch/home/emanolid/data/SPT/2021.2.00019.S/science_goal.uid___A001_X15a9_X11e8/group.uid___A001_X15a9_X11e9/member.uid___A001_X15a9_X11ec/calibrated/working/baselines/averaged/'
for file in bl_names_S:
	outfile = b + names[i] +'_S_averaged.bl'
	mstransform(vis = file, outputvis = outfile, chanaverage = True, chanbin = 10,datacolumn = 'data')
	bl_names_S2.append(outfile)
	i = i+1
print("Averaged South")
i = 0
bl_names_N2 = []

for file in bl_names_N:
	outfile = b + names[i] +'_N_averaged.bl'
	mstransform(vis = file, outputvis = outfile, chanaverage = True, chanbin = 10,datacolumn = 'data')
	bl_names_N2.append(outfile)
	i = i+1
	
print("Averaged North")	

d ='/scratch/home/emanolid/data/SPT/2021.2.00019.S/science_goal.uid___A001_X15a9_X11e8/group.uid___A001_X15a9_X11e9/member.uid___A001_X15a9_X11ec/calibrated/working/troubleshooting/'
#Troubleshooting
#South
k = 0
t = []
for file in bl_names_S2:
	outfile = d + names[k] + '_S.png'
	k = k+1
	print(file)
	sdimaging(infiles=file,
        	outfile=outfile,
        	overwrite=True,
        	#field=str(field_id),
        	intent='OBSERVE_TARGET#ON_SOURCE',
        	mode='channel',
        	# nchan=2048,  # The default should create sufficient channels
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
	t.append(outfile)
print("Troubleshooting Images- South")
print(t)

#North
k = 0
l = []
for file in bl_names_S2:
	outfile = d + names[k] + '_N.png'
	k = k+1
	print(file)
	sdimaging(infiles=file,
        	outfile=outfile,
        	overwrite=True,
        	#field=str(field_id),
        	intent='OBSERVE_TARGET#ON_SOURCE',
        	mode='channel',
        	# nchan=2048,  # The default should create sufficient channels
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
	l.append(outfile)
          
     
print("Troubleshooting Images- North")
print(l)






# Image baselined spectra
#South
print(f'- Imaging: {", ".join(bl_names_S2)} -> {outimage1}')
sdimaging(infiles=bl_names_S2,
          outfile=outimage1,
          overwrite=True,
          #field=str(field_id),
          intent='OBSERVE_TARGET#ON_SOURCE',
          mode='channel',
          # nchan=2048,  # The default should create sufficient channels
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
print("Imaged South:")
print(outimage1)

#North
print(f'- Imaging: {", ".join(bl_names_N2)} -> {outimage2}')
sdimaging(infiles=bl_names_N2,
          outfile=outimage2,
          overwrite=True,
          #field=str(field_id),
          intent='OBSERVE_TARGET#ON_SOURCE',
          mode='channel',
          # nchan=2048,  # The default should create sufficient channels
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
          
print("Imaged North:")
print(outimage2)


# Correct the brightness unit in the image header
print(f'- Correct image header unit ({outimage1})')
imhead(imagename = outimage1,
       mode = 'put',
       hdkey = 'bunit',
       hdvalue = 'Jy/beam')
       
print(f'- Correct image header unit ({outimage2})')
imhead(imagename = outimage2,
       mode = 'put',
       hdkey = 'bunit',
       hdvalue = 'Jy/beam')       
      
# Add Restoring Beam Header Information to the Science Image
print(f'- Add restore beam to header ({outimage1})')
myia = iatool()
myia.open(outimage1)
myia.setrestoringbeam(major = str(sfbeam)+'arcsec',
                      minor = str(sfbeam)+'arcsec',
                      pa = '0deg')
myia.done()
 
 
print(f'- Add restore beam to header ({outimage2})')
myia = iatool()
myia.open(outimage2)
myia.setrestoringbeam(major = str(sfbeam)+'arcsec',
                      minor = str(sfbeam)+'arcsec',
                      pa = '0deg')
myia.done()

   
# Export fits file
print(f'- Exporting fits cube {outimage1} -> {outimage1}.fits')
if os.path.isfile(outimage1 + '.fits'):
    os.remove(outimage1 + '.fits')
exportfits(imagename = outimage1,
           fitsimage = outimage1 + '.fits')
           
           
           
print(f'- Exporting fits cube {outimage2} -> {outimage2}.fits')
if os.path.isfile(outimage2 + '.fits'):
    os.remove(outimage2 + '.fits')
exportfits(imagename = outimage2,
           fitsimage = outimage2 + '.fits')

# Create profile map
print(f'- Creating profile map -> {outimage1.replace(".image.sd", "_profilemap.png")}')
plotprofilemap(imagename=outimage1, 
               figfile = outimage1.replace('.image.sd', '_profilemap.png'),
               overwrite=True, 
               separatepanel=False, 
               spectralaxis = 'frequency', 
               transparent = False, 
               showaxislabel = True, 
               showtick = True, 
               showticklabel = True, 
               numpanels='8', 
               figsize='40cm,30cm') 
               
               
               
               
print(f'- Creating profile map -> {outimage2.replace(".image.sd", "_profilemap.png")}')
plotprofilemap(imagename=outimage2, 
               figfile = outimage2.replace('.image.sd', '_profilemap.png'),
               overwrite=True, 
               separatepanel=False, 
               spectralaxis = 'frequency', 
               transparent = False, 
               showaxislabel = True, 
               showtick = True, 
               showticklabel = True, 
               numpanels='8', 
               figsize='40cm,30cm') 
