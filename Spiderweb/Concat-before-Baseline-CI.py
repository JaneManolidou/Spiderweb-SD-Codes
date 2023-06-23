
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
expath = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/combined/concat_baselines/'


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

b = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/combined/concat_baselines/'
print("Averaging...", new)
outfile = b+ 'Spiderweb_concatenated_averaged_CI.ms.bl'
mstransform(vis = new, outputvis = outfile, chanaverage = True, chanbin = 20,datacolumn = 'data')
print("Averaged", outfile)

inimage = outfile

# Image all baselined spectra

sdimaging(infiles=[inimage],
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
               numpanels='8', 
               figsize='40cm,30cm') 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


