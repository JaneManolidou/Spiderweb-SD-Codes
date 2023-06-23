import os
import sys
sys.path.append("/scratch/home/emanolid/data/casa/analysis_scripts") 
import analysisUtils as au 
from sys import path
import glob

path_analysisUtils = "/scratch/home/emanolid/data/casa/analysis_scripts"

ms_names = glob.glob('*.ms.atmcor.atmtype?')

# Baseline parameters
spw = '21'  # Spw to baseline/image
baseline_support = '0~750;900~1023'  # Channel range(s) to fit baseline

baseline_order = 1  # Polynomial fit order



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
outimage = f'{source}_spw{spw}.image.sd'

# Subtract baseline for all ms
global bl_files
bl_files = []
for i, ms in enumerate(ms_names, start=1):
    outfile = ms + f'_SI_spw{spw}.bl'
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

