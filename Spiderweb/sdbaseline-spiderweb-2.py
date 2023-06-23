#path to thecalibrated measurement sets
pathCal = '/scratch/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated_old/'

#this time our list must contain calibrated measurements sets
MeasSetsCO=[
	pathCal+'uid___A002_X101c3b2_X42b1.ms.split.cal',
	pathCal+'uid___A002_X101e5ab_Xf704.ms.split.cal',
	pathCal+'uid___A002_X10239e1_X178c7.ms.split.cal',
	pathCal+'uid___A002_X10239e1_X181b9.ms.split.cal',
	pathCal+'uid___A002_X10239e1_X18e80.ms.split.cal',
	pathCal+'uid___A002_X10275c0_X17ff7.ms.split.cal',
	pathCal+'uid___A002_X10305a2_X224e.ms.split.cal',
	pathCal+'uid___A002_X10305a2_X2c6c.ms.split.cal',
	pathCal+'uid___A002_X103317b_X20c5.ms.split.cal',
	pathCal+'uid___A002_X103317b_X2744.ms.split.cal',
	pathCal+'uid___A002_X1033b6e_X153b.ms.split.cal',
	pathCal+'uid___A002_X1033b6e_X1bbd.ms.split.cal',
	pathCal+'uid___A002_X1033b6e_X21ed.ms.split.cal',
	pathCal+'uid___A002_X1033b6e_Xfe3.ms.split.cal',
	pathCal+'uid___A002_X1034414_X15fc.ms.split.cal',
	pathCal+'uid___A002_X1034414_X2139.ms.split.cal',
	pathCal+'uid___A002_X1034414_X27c9.ms.split.cal',
	pathCal+'uid___A002_X1034414_X2dbd.ms.split.cal',
	pathCal+'uid___A002_X1034f36_X119b.ms.split.cal',
	pathCal+'uid___A002_X1034f36_Xa80.ms.split.cal',
	pathCal+'uid___A002_X1035744_X2f7a.ms.split.cal',
	pathCal+'uid___A002_X1035744_X34cd.ms.split.cal',
	pathCal+'uid___A002_X1036d05_X2644.ms.split.cal',
	pathCal+'uid___A002_X1036d05_X2c62.ms.split.cal',
	pathCal+'uid___A002_X1036d05_X33a5.ms.split.cal',
	pathCal+'uid___A002_X1036d05_Xb88f.ms.split.cal'
	]
	
MeasSetsCI = []
for file in MeasSetsCO:
	MeasSetsCI.append(file)

names=[
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
	'uid___A002_X1036d05_X33a5',
	'uid___A002_X1036d05_Xb88f'
	]
	

#redefining the parameters

diameter=12
#spw must be strings for these CASA commands
spwCO='19'
spwCI = '21'

#baseline support:
baseline_support_CO = '200~600'
baseline_support_CI = '0~500'
#iteration variable
i = 0



#All
i=0
for file in MeasSetsCO:
	sdbaseline(infile=file, datacolumn='data',  spw = '17:400~800,19:200~600,21:0~200,23:200~800' , blfunc = 'poly', order = 1, overwrite = True, outfile = pathCal+'baselines/'+names[i]+'.bl',clipniter = 100, maskmode = 'auto', intent='OBSERVE_TARGET#ON_SOURCE',sigmavalue='rms',dosubtract=True,thresh=10,avg_limit  = 20,minwidth =4)
	i = i+1


#Both together (to be safe):
i=0
for file in MeasSetsCO:
	sdbaseline(infile=file, datacolumn='data',  spw = '19:200~600,21:0~200' , blfunc = 'poly', order = 1, overwrite = True, outfile = pathCal+'baselines/'+names[i]+'_ALL.bl',clipniter = 100, maskmode = 'auto', intent='OBSERVE_TARGET#ON_SOURCE',sigmavalue='rms',dosubtract=True,thresh=10,avg_limit  = 20,minwidth =4)
	i = i+1



#CO
i=0
for file in MeasSetsCO:
	sdbaseline(infile=file, datacolumn='data',  spw = f'{spwCO}:{baseline_support_CO}', blfunc = 'poly', order = 1, overwrite = True,outfile = pathCal+'baselines/'+names[i]+'_CO.bl',clipniter = 100, maskmode = 'auto',intent='OBSERVE_TARGET#ON_SOURCE',sigmavalue='rms',dosubtract=True,thresh=10,avg_limit  = 20,minwidth =4)
	i=i+1
	
	
#CI
i=0
for file in MeasSetsCI:
	sdbaseline(infile=file, datacolumn='data',  spw = f'{spwCI}:{baseline_support_CI}', blfunc = 'poly', order = 1, overwrite = True,outfile = pathCal+'baselines/'+names[i]+'_CI.bl',clipniter = 100, maskmode = 'auto',intent='OBSERVE_TARGET#ON_SOURCE',sigmavalue='rms',dosubtract=True,thresh=10,avg_limit  = 20,minwidth =4)
	i=i+1
	
	
#casalog from scriptforpi:

#sdbaseline( infile='uid___A002_X1033b6e_X1bbd.ms.atmcor.atmtype1', datacolumn='data', antenna='', field='', spw='', timerange='', scan='', pol='', intent='', reindex=True, maskmode='list', thresh=5.0, avg_limit=4, minwidth=4, edge=[0, 0], blmode='fit', dosubtract=True, blformat='table', bloutput='uid___A002_X1033b6e_X1bbd.ms.atmcor.atmtype1.s9_6.bl.tbl', bltable='', blfunc='variable', order=5, npiece=2, applyfft=True, fftmethod='fft', fftthresh=3.0, addwn=[0], rejwn=[], clipthresh=3.0, clipniter=0, blparam='uid___A002_X1033b6e_X1bbd.ms.atmcor.atmtype1_blparam_stage9.txt', verbose=False, updateweight=False, sigmavalue='stddev', showprogress=False, minnrow=1000, outfile='uid___A002_X1033b6e_X1bbd.ms.atmcor.atmtype1_bl', overwrite=True )
	
	
	
#flagdata( vis='uid___A002_X101c3b2_X42b1.ms.atmcor.atmtype1_bl', mode='summary', autocorr=False, inpfile='', reason='any', tbuff=0.0, spw='', field='Spiderweb_galaxy', antenna='', uvrange='', timerange='', correlation='', scan='', intent='OBSERVE_TARGET#ON_SOURCE', array='', observation='', feed='', clipminmax=[], datacolumn='DATA', clipoutside=True, channelavg=False, chanbin=1, timeavg=False, timebin='0s', clipzeros=False, quackinterval=1.0, quackmode='beg', quackincrement=False, tolerance=0.0, addantenna='', lowerlimit=0.0, upperlimit=90.0, ntime='scan', combinescans=False, timecutoff=4.0, freqcutoff=3.0, timefit='line', freqfit='poly', maxnpieces=7, flagdimension='freqtime', usewindowstats='none', halfwin=1, extendflags=True, winsize=3, timedev='', freqdev='', timedevscale=5.0, freqdevscale=5.0, spectralmax=1000000.0, spectralmin=0.0, antint_ref_antenna='', minchanfrac=0.6, verbose=False, extendpols=True, growtime=50.0, growfreq=50.0, growaround=False, flagneartime=False, flagnearfreq=False, minrel=0.0, maxrel=1.0, minabs=0, maxabs=-1, spwchan=False, spwcorr=True, basecnt=False, fieldcnt=True, name='before', action='apply', display='', flagbackup=True, savepars=False, cmdreason='', outfile='', overwrite=True, writeflags=True )


#SDIMAGING



#sdimaging( infiles=['uid___A002_X101c3b2_X42b1.ms.atmcor.atmtype1_bl', 'uid___A002_X103317b_X20c5.ms.atmcor.atmtype3_bl', 'uid___A002_X103317b_X2744.ms.atmcor.atmtype4_bl', 'uid___A002_X1033b6e_Xfe3.ms.atmcor.atmtype1_bl', 'uid___A002_X1033b6e_X153b.ms.atmcor.atmtype1_bl', 'uid___A002_X1033b6e_X1bbd.ms.atmcor.atmtype1_bl', 'uid___A002_X1033b6e_X21ed.ms.atmcor.atmtype4_bl', 'uid___A002_X1034414_X15fc.ms.atmcor.atmtype1_bl', 'uid___A002_X1034414_X2139.ms.atmcor.atmtype1_bl', 'uid___A002_X1034414_X27c9.ms.atmcor.atmtype3_bl', 'uid___A002_X1034414_X2dbd.ms.atmcor.atmtype2_bl', 'uid___A002_X1034f36_Xa80.ms.atmcor.atmtype1_bl', 'uid___A002_X1034f36_X119b.ms.atmcor.atmtype1_bl', 'uid___A002_X1035744_X2f7a.ms.atmcor.atmtype1_bl', 'uid___A002_X1035744_X34cd.ms.atmcor.atmtype3_bl', 'uid___A002_X1036d05_X2644.ms.atmcor.atmtype1_bl', 'uid___A002_X1036d05_X2c62.ms.atmcor.atmtype3_bl', 'uid___A002_X1036d05_X33a5.ms.atmcor.atmtype3_bl', 'uid___A002_X1036d05_Xb88f.ms.atmcor.atmtype1_bl', 'uid___A002_X101e5ab_Xf704.ms.atmcor.atmtype3_bl', 'uid___A002_X10239e1_X178c7.ms.atmcor.atmtype2_bl', 'uid___A002_X10239e1_X181b9.ms.atmcor.atmtype4_bl', 'uid___A002_X10239e1_X18e80.ms.atmcor.atmtype3_bl', 'uid___A002_X10275c0_X17ff7.ms.atmcor.atmtype2_bl'], outfile='uid___A001_X2d20_X3bdd.s13_0.Spiderweb_galaxy_sci.spw17.cube.I.PM03.iter0.image.sd', overwrite=False, field='1', spw='17', antenna=['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '1', '1', '1', '1'], scan='', intent='OBSERVE_TARGET#ON_SOURCE', mode='channel', nchan=1024, start=0, width=1, veltype='radio', outframe='lsrk', gridfunction='SF', convsupport=6, truncate=-1, gwidth=-1, jwidth=-1, imsize=[42, 46], cell=['4.484877499arcsec', '4.484877499arcsec'], phasecenter='ICRS 11:40:48.35 -026.29.02.252', projection='SIN', ephemsrcname='', pointingcolumn='direction', restfreq='455261899920.000183105Hz', stokes='I', minweight=0.1, brightnessunit='', clipminmax=False )

#sdimaging( infiles=['uid___A002_X101c3b2_X42b1.ms.atmcor.atmtype1_bl', 'uid___A002_X103317b_X20c5.ms.atmcor.atmtype3_bl', 'uid___A002_X103317b_X2744.ms.atmcor.atmtype4_bl', 'uid___A002_X1033b6e_Xfe3.ms.atmcor.atmtype1_bl', 'uid___A002_X1033b6e_X153b.ms.atmcor.atmtype1_bl', 'uid___A002_X1033b6e_X1bbd.ms.atmcor.atmtype1_bl', 'uid___A002_X1033b6e_X21ed.ms.atmcor.atmtype4_bl', 'uid___A002_X1034414_X15fc.ms.atmcor.atmtype1_bl', 'uid___A002_X1034414_X2139.ms.atmcor.atmtype1_bl', 'uid___A002_X1034414_X27c9.ms.atmcor.atmtype3_bl', 'uid___A002_X1034414_X2dbd.ms.atmcor.atmtype2_bl', 'uid___A002_X1034f36_Xa80.ms.atmcor.atmtype1_bl', 'uid___A002_X1034f36_X119b.ms.atmcor.atmtype1_bl', 'uid___A002_X1035744_X2f7a.ms.atmcor.atmtype1_bl', 'uid___A002_X1035744_X34cd.ms.atmcor.atmtype3_bl', 'uid___A002_X1036d05_X2644.ms.atmcor.atmtype1_bl', 'uid___A002_X1036d05_X2c62.ms.atmcor.atmtype3_bl', 'uid___A002_X1036d05_X33a5.ms.atmcor.atmtype3_bl', 'uid___A002_X1036d05_Xb88f.ms.atmcor.atmtype1_bl', 'uid___A002_X101e5ab_Xf704.ms.atmcor.atmtype3_bl', 'uid___A002_X10239e1_X178c7.ms.atmcor.atmtype2_bl', 'uid___A002_X10239e1_X181b9.ms.atmcor.atmtype4_bl', 'uid___A002_X10239e1_X18e80.ms.atmcor.atmtype3_bl', 'uid___A002_X10275c0_X17ff7.ms.atmcor.atmtype2_bl'], outfile='uid___A001_X2d20_X3bdd.s13_19.Spiderweb_galaxy_sci.spw19.cube.I.PM03.iter0.image.sd', overwrite=False, field='1', spw='19', antenna=['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '1', '1', '1', '1'], scan='', intent='OBSERVE_TARGET#ON_SOURCE', mode='channel', nchan=1024, start=0, width=1, veltype='radio', outframe='lsrk', gridfunction='SF', convsupport=6, truncate=-1, gwidth=-1, jwidth=-1, imsize=[42, 46], cell=['4.438720587arcsec', '4.438720587arcsec'], phasecenter='ICRS 11:40:48.35 -026.29.02.252', projection='SIN', ephemsrcname='', pointingcolumn='direction', restfreq='459995899920.000183105Hz', stokes='I', minweight=0.1, brightnessunit='', clipminmax=False )

#sdimaging(infiles=['uid___A002_X101c3b2_X42b1.ms.atmcor.atmtype1_bl', 'uid___A002_X103317b_X20c5.ms.atmcor.atmtype3_bl', 'uid___A002_X103317b_X2744.ms.atmcor.atmtype4_bl', 'uid___A002_X1033b6e_Xfe3.ms.atmcor.atmtype1_bl', 'uid___A002_X1033b6e_X153b.ms.atmcor.atmtype1_bl', 'uid___A002_X1033b6e_X1bbd.ms.atmcor.atmtype1_bl', 'uid___A002_X1033b6e_X21ed.ms.atmcor.atmtype4_bl', 'uid___A002_X1034414_X15fc.ms.atmcor.atmtype1_bl', 'uid___A002_X1034414_X2139.ms.atmcor.atmtype1_bl', 'uid___A002_X1034414_X27c9.ms.atmcor.atmtype3_bl', 'uid___A002_X1034414_X2dbd.ms.atmcor.atmtype2_bl', 'uid___A002_X1034f36_Xa80.ms.atmcor.atmtype1_bl', 'uid___A002_X1034f36_X119b.ms.atmcor.atmtype1_bl', 'uid___A002_X1035744_X2f7a.ms.atmcor.atmtype1_bl', 'uid___A002_X1035744_X34cd.ms.atmcor.atmtype3_bl', 'uid___A002_X1036d05_X2644.ms.atmcor.atmtype1_bl', 'uid___A002_X1036d05_X2c62.ms.atmcor.atmtype3_bl', 'uid___A002_X1036d05_X33a5.ms.atmcor.atmtype3_bl', 'uid___A002_X1036d05_Xb88f.ms.atmcor.atmtype1_bl', 'uid___A002_X101e5ab_Xf704.ms.atmcor.atmtype3_bl', 'uid___A002_X10239e1_X178c7.ms.atmcor.atmtype2_bl', 'uid___A002_X10239e1_X181b9.ms.atmcor.atmtype4_bl', 'uid___A002_X10239e1_X18e80.ms.atmcor.atmtype3_bl', 'uid___A002_X10275c0_X17ff7.ms.atmcor.atmtype2_bl'], outfile='uid___A001_X2d20_X3bdd.s13_38.Spiderweb_galaxy_sci.spw21.cube.I.PM03.iter0.image.sd', field='1', spw='21', antenna=['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '1', '1', '1', '1'], intent='OBSERVE_TARGET#ON_SOURCE', mode='channel', nchan=1024, start=0, width=1, outframe='lsrk', gridfunction='SF', convsupport=6, truncate=-1, gwidth=-1, jwidth=-1, imsize=[44, 50], cell=['4.152608662arcsec', '4.152608662arcsec'], phasecenter='ICRS 11:40:48.35 -026.29.02.252', restfreq='491578560000.000122070Hz', stokes='I')

#sdimaging(infiles=['uid___A002_X101c3b2_X42b1.ms.atmcor.atmtype1_bl', 'uid___A002_X103317b_X20c5.ms.atmcor.atmtype3_bl', 'uid___A002_X103317b_X2744.ms.atmcor.atmtype4_bl', 'uid___A002_X1033b6e_Xfe3.ms.atmcor.atmtype1_bl', 'uid___A002_X1033b6e_X153b.ms.atmcor.atmtype1_bl', 'uid___A002_X1033b6e_X1bbd.ms.atmcor.atmtype1_bl', 'uid___A002_X1033b6e_X21ed.ms.atmcor.atmtype4_bl', 'uid___A002_X1034414_X15fc.ms.atmcor.atmtype1_bl', 'uid___A002_X1034414_X2139.ms.atmcor.atmtype1_bl', 'uid___A002_X1034414_X27c9.ms.atmcor.atmtype3_bl', 'uid___A002_X1034414_X2dbd.ms.atmcor.atmtype2_bl', 'uid___A002_X1034f36_Xa80.ms.atmcor.atmtype1_bl', 'uid___A002_X1034f36_X119b.ms.atmcor.atmtype1_bl', 'uid___A002_X1035744_X2f7a.ms.atmcor.atmtype1_bl', 'uid___A002_X1035744_X34cd.ms.atmcor.atmtype3_bl', 'uid___A002_X1036d05_X2644.ms.atmcor.atmtype1_bl', 'uid___A002_X1036d05_X2c62.ms.atmcor.atmtype3_bl', 'uid___A002_X1036d05_X33a5.ms.atmcor.atmtype3_bl', 'uid___A002_X1036d05_Xb88f.ms.atmcor.atmtype1_bl', 'uid___A002_X101e5ab_Xf704.ms.atmcor.atmtype3_bl', 'uid___A002_X10239e1_X178c7.ms.atmcor.atmtype2_bl', 'uid___A002_X10239e1_X181b9.ms.atmcor.atmtype4_bl', 'uid___A002_X10239e1_X18e80.ms.atmcor.atmtype3_bl', 'uid___A002_X10275c0_X17ff7.ms.atmcor.atmtype2_bl'], outfile='uid___A001_X2d20_X3bdd.s13_57.Spiderweb_galaxy_sci.spw23.cube.I.PM03.iter0.image.sd', field='1', spw='23', antenna=['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '1', '1', '1', '1'], intent='OBSERVE_TARGET#ON_SOURCE', mode='channel', nchan=1024, start=0, width=1, outframe='lsrk', gridfunction='SF', convsupport=6, truncate=-1, gwidth=-1, jwidth=-1, imsize=[46, 50], cell=['4.113007416arcsec', '4.113007416arcsec'], phasecenter='ICRS 11:40:48.35 -026.29.02.252', restfreq='496312560000.000122070Hz', stokes='I')
