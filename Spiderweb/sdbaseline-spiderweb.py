
#path to thecalibrated measurement sets
pathCal = '/scratch/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/'

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
#iteration variable
i = 0


#Both together (to be safe):
i=0
for file in MeasSetsCO:
	sdbaseline(infile=file, datacolumn='data',  spw = '19,21' , blfunc = 'poly', order = 1, overwrite = True, outfile = pathCal+'baselines/'+names[i]+'_ALL.bl',clipniter = 100)
	i = i+1



#CO
i=0
for file in MeasSetsCO:
	sdbaseline(infile=file, datacolumn='data',  spw = spwCO, blfunc = 'poly', order = 2, overwrite = True,outfile = pathCal+'baselines/'+names[i]+'_CO.bl',clipniter = 100)
	i=i+1
	
	
#CI
i=0
for file in MeasSetsCI:
	sdbaseline(infile=file, datacolumn='data',  spw = spwCI, blfunc = 'poly', order = 1, overwrite = True,outfile = pathCal+'baselines/'+names[i]+'_CI.bl',clipniter = 100)
	i=i+1
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

