#path to thecalibrated measurement sets
pathCal = '/scratch/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated_old/combined/'

#this time our list must contain calibrated measurements sets
MeasSetsCO=[
	pathCal+'uid___A002_X101c3b2_X42b1_newCO.ms.split.cal',
	pathCal+'uid___A002_X101e5ab_Xf704_newCO.ms.split.cal',
	pathCal+'uid___A002_X10239e1_X178c7_newCO.ms.split.cal',
	pathCal+'uid___A002_X10239e1_X181b9_newCO.ms.split.cal',
	pathCal+'uid___A002_X10239e1_X18e80_newCO.ms.split.cal',
	pathCal+'uid___A002_X10275c0_X17ff7_newCO.ms.split.cal',
	pathCal+'uid___A002_X10305a2_X224e_newCO.ms.split.cal',
	pathCal+'uid___A002_X10305a2_X2c6c_newCO.ms.split.cal',
	pathCal+'uid___A002_X103317b_X20c5_newCO.ms.split.cal',
	pathCal+'uid___A002_X103317b_X2744_newCO.ms.split.cal',
	pathCal+'uid___A002_X1033b6e_X153b_newCO.ms.split.cal',
	pathCal+'uid___A002_X1033b6e_X1bbd_newCO.ms.split.cal',
	pathCal+'uid___A002_X1033b6e_X21ed_newCO.ms.split.cal',
	pathCal+'uid___A002_X1033b6e_Xfe3_newCO.ms.split.cal',
	pathCal+'uid___A002_X1034414_X15fc_newCO.ms.split.cal',
	pathCal+'uid___A002_X1034414_X2139_newCO.ms.split.cal',
	pathCal+'uid___A002_X1034414_X27c9_newCO.ms.split.cal',
	pathCal+'uid___A002_X1034414_X2dbd_newCO.ms.split.cal',
	pathCal+'uid___A002_X1034f36_X119b_newCO.ms.split.cal',
	pathCal+'uid___A002_X1034f36_Xa80_newCO.ms.split.cal',
	pathCal+'uid___A002_X1035744_X2f7a_newCO.ms.split.cal',
	pathCal+'uid___A002_X1035744_X34cd_newCO.ms.split.cal',
	pathCal+'uid___A002_X1036d05_X2644_newCO.ms.split.cal',
	pathCal+'uid___A002_X1036d05_X2c62_newCO.ms.split.cal',
	pathCal+'uid___A002_X1036d05_X33a5_newCO.ms.split.cal',
	pathCal+'uid___A002_X1036d05_Xb88f_newCO.ms.split.cal'
	]
	
MeasSetsCI =[
	pathCal+'uid___A002_X101c3b2_X42b1_newCI.ms.split.cal',
	pathCal+'uid___A002_X101e5ab_Xf704_newCI.ms.split.cal',
	pathCal+'uid___A002_X10239e1_X178c7_newCI.ms.split.cal',
	pathCal+'uid___A002_X10239e1_X181b9_newCI.ms.split.cal',
	pathCal+'uid___A002_X10239e1_X18e80_newCI.ms.split.cal',
	pathCal+'uid___A002_X10275c0_X17ff7_newCI.ms.split.cal',
	pathCal+'uid___A002_X10305a2_X224e_newCI.ms.split.cal',
	pathCal+'uid___A002_X10305a2_X2c6c_newCI.ms.split.cal',
	pathCal+'uid___A002_X103317b_X20c5_newCI.ms.split.cal',
	pathCal+'uid___A002_X103317b_X2744_newCI.ms.split.cal',
	pathCal+'uid___A002_X1033b6e_X153b_newCI.ms.split.cal',
	pathCal+'uid___A002_X1033b6e_X1bbd_newCI.ms.split.cal',
	pathCal+'uid___A002_X1033b6e_X21ed_newCI.ms.split.cal',
	pathCal+'uid___A002_X1033b6e_Xfe3_newCI.ms.split.cal',
	pathCal+'uid___A002_X1034414_X15fc_newCI.ms.split.cal',
	pathCal+'uid___A002_X1034414_X2139_newCI.ms.split.cal',
	pathCal+'uid___A002_X1034414_X27c9_newCI.ms.split.cal',
	pathCal+'uid___A002_X1034414_X2dbd_newCI.ms.split.cal',
	pathCal+'uid___A002_X1034f36_X119b_newCI.ms.split.cal',
	pathCal+'uid___A002_X1034f36_Xa80_newCI.ms.split.cal',
	pathCal+'uid___A002_X1035744_X2f7a_newCI.ms.split.cal',
	pathCal+'uid___A002_X1035744_X34cd_newCI.ms.split.cal',
	pathCal+'uid___A002_X1036d05_X2644_newCI.ms.split.cal',
	pathCal+'uid___A002_X1036d05_X2c62_newCI.ms.split.cal',
	pathCal+'uid___A002_X1036d05_X33a5_newCI.ms.split.cal',
	pathCal+'uid___A002_X1036d05_Xb88f_newCI.ms.split.cal'
	]
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
#because this script is meant to be run after mstransform, we check the new spws with a list obs, and the channels with a plotms over channels
spwCO='0'
spwCI = '0'

#baseline support:
baseline_support_CO = '40~400;1600~1700'
baseline_support_CI = '40~200;1300~1700'
#iteration variable
i = 0


#CO
i=0
for file in MeasSetsCO:
	sdbaseline(infile=file, datacolumn='data',  spw = f'{spwCO}:{baseline_support_CO}', blfunc = 'poly', order = 1, overwrite = True,outfile = pathCal+'baselines/'+names[i]+'_combined_CO.bl',clipniter = 0, maskmode = 'auto',intent='OBSERVE_TARGET#ON_SOURCE',sigmavalue='rms',dosubtract=True,thresh=10,avg_limit  = 20,minwidth =4)
	i=i+1
	
	
#CI
i=0
for file in MeasSetsCI:
	sdbaseline(infile=file, datacolumn='data',  spw = f'{spwCI}:{baseline_support_CI}', blfunc = 'poly', order = 1, overwrite = True,outfile = pathCal+'baselines/'+names[i]+'_combined_CI.bl',clipniter = 0, maskmode = 'auto',intent='OBSERVE_TARGET#ON_SOURCE',sigmavalue='rms',dosubtract=True,thresh=10,avg_limit  = 20,minwidth =4)
	i=i+1
	
	
#casalog from scriptforpi:

#sdbaseline( infile='uid___A002_X1033b6e_X1bbd.ms.atmcor.atmtype1', datacolumn='data', antenna='', field='', spw='', timerange='', scan='', pol='', intent='', reindex=True, maskmode='list', thresh=5.0, avg_limit=4, minwidth=4, edge=[0, 0], blmode='fit', dosubtract=True, blformat='table', bloutput='uid___A002_X1033b6e_X1bbd.ms.atmcor.atmtype1.s9_6.bl.tbl', bltable='', blfunc='variable', order=5, npiece=2, applyfft=True, fftmethod='fft', fftthresh=3.0, addwn=[0], rejwn=[], clipthresh=3.0, clipniter=0, blparam='uid___A002_X1033b6e_X1bbd.ms.atmcor.atmtype1_blparam_stage9.txt', verbose=False, updateweight=False, sigmavalue='stddev', showprogress=False, minnrow=1000, outfile='uid___A002_X1033b6e_X1bbd.ms.atmcor.atmtype1_bl', overwrite=True )
	
	
	
#flagdata( vis='uid___A002_X101c3b2_X42b1.ms.atmcor.atmtype1_bl', mode='summary', autocorr=False, inpfile='', reason='any', tbuff=0.0, spw='', field='Spiderweb_galaxy', antenna='', uvrange='', timerange='', correlation='', scan='', intent='OBSERVE_TARGET#ON_SOURCE', array='', observation='', feed='', clipminmax=[], datacolumn='DATA', clipoutside=True, channelavg=False, chanbin=1, timeavg=False, timebin='0s', clipzeros=False, quackinterval=1.0, quackmode='beg', quackincrement=False, tolerance=0.0, addantenna='', lowerlimit=0.0, upperlimit=90.0, ntime='scan', combinescans=False, timecutoff=4.0, freqcutoff=3.0, timefit='line', freqfit='poly', maxnpieces=7, flagdimension='freqtime', usewindowstats='none', halfwin=1, extendflags=True, winsize=3, timedev='', freqdev='', timedevscale=5.0, freqdevscale=5.0, spectralmax=1000000.0, spectralmin=0.0, antint_ref_antenna='', minchanfrac=0.6, verbose=False, extendpols=True, growtime=50.0, growfreq=50.0, growaround=False, flagneartime=False, flagnearfreq=False, minrel=0.0, maxrel=1.0, minabs=0, maxabs=-1, spwchan=False, spwcorr=True, basecnt=False, fieldcnt=True, name='before', action='apply', display='', flagbackup=True, savepars=False, cmdreason='', outfile='', overwrite=True, writeflags=True )

