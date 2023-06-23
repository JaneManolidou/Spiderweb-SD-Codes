#This python script will combine spectral windows for CO and CI and give out two new files, one for each. Then it will baseline them and store them in a directory.

#path to thecalibrated measurement sets
pathCal = '/scratch/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/'


#old measurement sets:
pathms = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/'

MeasSetsCO=[
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
	
MeasSetsCI = []
for file in MeasSetsCO:
	MeasSetsCI.append(file)
#blank names:

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

#path to new measurement sets:
#path to the calibrated measurement sets
pathnew = '/scratch/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/combined/'

#CO
COfiles = []
i=0
for file in MeasSetsCO:
	outfile = pathnew + names[i]+'_newCO.ms.atmcor.atmtype'
	mstransform(vis = file, outputvis = outfile, spw = '17,19', intent = 'OBSERVE_TARGET#ON_SOURCE',datacolumn = 'data',combinespws = True)
	COfiles.append(outfile)
	i=i+1
	
#CI
CIfiles = []
i=0
for file in MeasSetsCI:
	outfile = pathnew + names[i]+'_newCI.ms.atmcor.atmtype'
	mstransform(vis = file, outputvis = outfile, spw = '21,23', intent = 'OBSERVE_TARGET#ON_SOURCE',datacolumn = 'data',combinespws = True)
	CIfiles.append(outfile)
	i=i+1	
	
