
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
expath = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/combined/antenna_baselines/'


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
out1 = f'{source}_spw{spw}_CI_PM01.image.sd'
outimage1 = expath + out1
out2 = f'{source}_spw{spw}_CI_PM02.image.sd'
outimage2 = expath + out2
out3 = f'{source}_spw{spw}_CI_PM03.image.sd'
outimage3 = expath + out3
out4 = f'{source}_spw{spw}_CI_PM04.image.sd'
outimage4 = expath + out4
#Concatenation:

print('Concatenating...')

concat(vis = ms_names, concatvis= 'Spiderweb_concatenated_Second_Try_CI.ms',respectname=True)
ms = 'Spiderweb_concatenated_Second_Try_CI.ms'
outfile = expath+ ms + f'.bl'
print(f'- Substracting baseline {ms} -> 'f'{outfile}')
sdbaseline(infile = ms, datacolumn='data', blmode='fit', dosubtract=True, maskmode = 'list', blfunc = 'poly',  order = baseline_order,  spw = f'{spw}:{baseline_support}',outfile=outfile, overwrite=True)
print(f'  Plotting antenna/pol spectra -> ' f'{outfile+"_AntennaXXX.png"}')
plotms(vis=outfile,xaxis='chan',yaxis='real',ydatacolumn='data',field=source,intent='OBSERVE_TARGET#ON_SOURCE',averagedata=True,avgtime='1e8',avgscan=True,coloraxis='corr',showgui=False,showatm=False, gridrows=2,gridcols=2, iteraxis='antenna',xselfscale=True, yselfscale=True,ysharedaxis=True,xsharedaxis=True, showmajorgrid=True, plotfile=outfile+'.png', overwrite=True, highres=True)
    
    
new = outfile 

#Averaging channels:

b = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/combined/antenna_baselines/'
print("Averaging...", new)
outfile = b+ 'Spiderweb_concatenated_averaged_CI.ms.bl'
mstransform(vis = new, outputvis = outfile, chanaverage = True, chanbin = 20,datacolumn = 'data')
print("Averaged", outfile)

inimage = outfile

# Image all baselined spectra
#PM01
sdimaging(infiles=[inimage],
          outfile=outimage1,
          overwrite=True,
          field=str(field_id),
          intent='OBSERVE_TARGET#ON_SOURCE',
          mode='channel',
          start=0,
          antenna='PM01',
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
#PM02
sdimaging(infiles=[inimage],
          outfile=outimage2,
          overwrite=True,
          field=str(field_id),
          intent='OBSERVE_TARGET#ON_SOURCE',
          mode='channel',
          start=0,
          width=1,
          antenna='PM02',
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
#PM03

sdimaging(infiles=[inimage],
          outfile=outimage3,
          overwrite=True,
          field=str(field_id),
          intent='OBSERVE_TARGET#ON_SOURCE',
          mode='channel',
          start=0,
          width=1,
          antenna = 'PM03',
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
#PM04

sdimaging(infiles=[inimage],
          outfile=outimage4,
          overwrite=True,
          field=str(field_id),
          intent='OBSERVE_TARGET#ON_SOURCE',
          mode='channel',
          start=0,
          width=1,
          antenna = 'PM04',
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
print(f'- Correct image header unit ({outimage1})')
imhead(imagename = outimage1,
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
    
# Export fits file
print(f'- Exporting fits cube {outimage1} -> {outimage1}.fits')
if os.path.isfile(outimage1 + '.fits'):
    os.remove(outimage1 + '.fits')
exportfits(imagename = outimage1,
           fitsimage = outimage1 + '.fits')

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
               numpanels='4', 
               figsize='40cm,30cm') 
    
    

          
# Correct the brightness unit in the image header
print(f'- Correct image header unit ({outimage2})')
imhead(imagename = outimage2,
       mode = 'put',
       hdkey = 'bunit',
       hdvalue = 'Jy/beam')
      
# Add Restoring Beam Header Information to the Science Image
print(f'- Add restore beam to header ({outimage2})')
myia = iatool()
myia.open(outimage2)
myia.setrestoringbeam(major = str(sfbeam)+'arcsec',
                      minor = str(sfbeam)+'arcsec',
                      pa = '0deg')
myia.done()
    
# Export fits file
print(f'- Exporting fits cube {outimage2} -> {outimage2}.fits')
if os.path.isfile(outimage2 + '.fits'):
    os.remove(outimage2 + '.fits')
exportfits(imagename = outimage2,
           fitsimage = outimage2 + '.fits')

# Create profile map
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
               numpanels='4', 
               figsize='40cm,30cm') 
    
    
          
# Correct the brightness unit in the image header
print(f'- Correct image header unit ({outimage3})')
imhead(imagename = outimage3,
       mode = 'put',
       hdkey = 'bunit',
       hdvalue = 'Jy/beam')
      
# Add Restoring Beam Header Information to the Science Image
print(f'- Add restore beam to header ({outimage3})')
myia = iatool()
myia.open(outimage3)
myia.setrestoringbeam(major = str(sfbeam)+'arcsec',
                      minor = str(sfbeam)+'arcsec',
                      pa = '0deg')
myia.done()
    
# Export fits file
print(f'- Exporting fits cube {outimage3} -> {outimage3}.fits')
if os.path.isfile(outimage3 + '.fits'):
    os.remove(outimage3 + '.fits')
exportfits(imagename = outimage3,
           fitsimage = outimage3 + '.fits')

# Create profile map
print(f'- Creating profile map -> {outimage3.replace(".image.sd", "_profilemap.png")}')
plotprofilemap(imagename=outimage3, 
               figfile = outimage3.replace('.image.sd', '_profilemap.png'),
               overwrite=True, 
               separatepanel=False, 
               spectralaxis = 'frequency', 
               transparent = False, 
               showaxislabel = True, 
               showtick = True, 
               showticklabel = True, 
               numpanels='4', 
               figsize='40cm,30cm') 
    
    
          
# Correct the brightness unit in the image header
print(f'- Correct image header unit ({outimage4})')
imhead(imagename = outimage4,
       mode = 'put',
       hdkey = 'bunit',
       hdvalue = 'Jy/beam')
      
# Add Restoring Beam Header Information to the Science Image
print(f'- Add restore beam to header ({outimage4})')
myia = iatool()
myia.open(outimage4)
myia.setrestoringbeam(major = str(sfbeam)+'arcsec',
                      minor = str(sfbeam)+'arcsec',
                      pa = '0deg')
myia.done()
    
# Export fits file
print(f'- Exporting fits cube {outimage4} -> {outimage4}.fits')
if os.path.isfile(outimage4 + '.fits'):
    os.remove(outimage4 + '.fits')
exportfits(imagename = outimage4,
           fitsimage = outimage4 + '.fits')

# Create profile map
print(f'- Creating profile map -> {outimage4.replace(".image.sd", "_profilemap.png")}')
plotprofilemap(imagename=outimage4, 
               figfile = outimage4.replace('.image.sd', '_profilemap.png'),
               overwrite=True, 
               separatepanel=False, 
               spectralaxis = 'frequency', 
               transparent = False, 
               showaxislabel = True, 
               showtick = True, 
               showticklabel = True, 
               numpanels='4', 
               figsize='40cm,30cm') 
    
    
    
    
    
    
    
    
    
    


