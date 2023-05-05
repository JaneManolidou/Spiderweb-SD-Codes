#information taken for the Spiderweb Galaxy (can be imported after running parameter computation)
freqspw19 = [145748837254.38898, 145748797072.0478, 145748330072.86047, 145748253653.68744, 145748135367.5736, 145747833252.0432, 145743490037.62573, 145743415718.10825, 145742577587.41736, 145742500066.20404, 145742430725.73068, 145742357462.65536, 145742281116.0432, 145742495677.51657, 145742284247.60843, 145742215998.78055, 145742141163.13956, 145742065493.85486, 145741951499.57443, 145742024339.7153, 145741869485.67624, 145741803939.56253, 145741448285.30142, 145741382879.54318, 145741309444.87204, 145741201561.89432] 
TBCO = [39.98950098906066, 39.98951201400085, 39.98964014630674, 39.98966111379798, 39.98969356856383, 39.98977646178573, 39.99096817315229, 39.990988565905155, 39.99121854451148, 39.99123981605397, 39.99125884284999, 39.99127894601463, 39.99129989531391, 39.99124102029472, 39.991299036020635, 39.99131776332807, 39.99133829806068, 39.991359061564694, 39.99139034141345, 39.99137035418932, 39.99141284592658, 39.991430831718056, 39.99152842319221, 39.99154637057398, 39.991566521113775, 39.991596124336716] 
CellsCO = [4.443277887673407, 4.443279112666762, 4.443293349589638, 4.443295679310887, 4.443299285395981, 4.44330849575397, 4.443440908128032, 4.443443173989461, 4.443468727167943, 4.443471090672663, 4.443473204761109, 4.44347543844607, 4.44347776614599, 4.443471224477191, 4.443477670668959, 4.443479751480897, 4.443482033117854, 4.443484340173855, 4.443487815712605, 4.443485594909925, 4.443490316214064, 4.443492314635339, 4.443503158132468, 4.443505152285997, 4.4435073912348635, 4.443510680481857] 
ImsizeCO= [92, 94, 94, 96, 92, 80, 164, 92, 102, 94, 424, 94, 92, 92, 92, 102, 94, 92, 94, 416, 92, 94, 90, 98, 94, 98]
#mean frequencies are in Hz but are not needed for the code
#TheoreticalBeam size is also not needed in the computations
freqspw21=  [155790833439.68832, 155790793257.34702, 155790326258.1597, 155790249838.98895, 155790131552.87494, 155789829437.34396, 155785486222.93408, 155785411903.40884, 155784573772.71857, 155784496251.50327, 155784426911.03143, 155784353647.95563, 155784277301.34396, 155784491862.8158, 155784280432.90903, 155784212184.0808, 155784137348.44016, 155784061679.15607, 155783947684.87506, 155784020525.0138, 155783865670.9817, 155783800124.86444, 155783444470.6069, 155783379064.84393, 155783305630.17374, 155783197747.19855] 
TBCI= [37.4118498685303, 37.4118595179819, 37.411971664277566, 37.41199001582303, 37.412018421466385, 37.412090972748146, 37.41313400144456, 37.41315184988314, 37.413353134965654, 37.41337175253463, 37.41338840542414, 37.41340600038697, 37.41342433591369, 37.41337280652655, 37.41342358383155, 37.41343997459597, 37.413457947277884, 37.4134761201869, 37.41350349734849, 37.41348600386761, 37.413523194042206, 37.4135389358021, 37.413624351068506, 37.41364005920542, 37.41365769561586, 37.41368360532093] 
CellsCI = [4.1568722076144775, 4.156873279775767, 4.1568857404752855, 4.156887779535892, 4.156890935718487, 4.156898996972016, 4.157014889049396, 4.157016872209238, 4.157039237218406, 4.157041305837181, 4.157043156158238, 4.157045111154108, 4.157047148434854, 4.157041422947395, 4.157047064870173, 4.157048886066218, 4.157050883030876, 4.157052902242989, 4.157055944149833, 4.157054000429735, 4.157058132671356, 4.157059881755789, 4.1570693723409455, 4.157071117689491, 4.157073077290651, 4.15707595614677] 
ImsizeCI = [98, 100, 102, 102, 100, 86, 174, 100, 108, 100, 454, 102, 100, 100, 98, 110, 102, 98, 100, 444, 100, 102, 96, 104, 100, 104]

#path to thecalibrated measurement sets
pathCal = '/scratch/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/'

#this time our list must contain calibrated measurements sets
MeasSets=[
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
#Storing what we excluded for good measure
outnamesCO = []
outnamesCI = []
outCellsCO = []
outCellsCI = []
outImCO = []
outImCI = []
pathex = '/scratch/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/excluded-data/Auto '

#redefining the parameters

diameter=12
#spw must be strings for these CASA commands
spwCO='19'
spwCI = '21'
#iteration variable
i = 0

#to find the median cellsize and imsize for later:
cellsumCO = 0
imsumCO = 0 
cellsumCI = 0
imsumCI = 0 
MeasSetsCO = MeasSets
namesCO = names
MeasSetsCI = MeasSets
namesCI= names
j = 0
a = len(CellsCO)
while j < len(CellsCO): #all are the same length cause we have the same number of files:
	if j>=a:
		break
	#The problem is usually found in imsize because it is a result of a computation using maxsize
	if j < a-1: 
		if ImsizeCO[j+1] > ImsizeCO[j]+20 or  ImsizeCO[j+1] < ImsizeCO[j]-20:
			outnamesCO.append(namesCO[j+1])
			outCellsCO.append(CellsCO[j+1])
			outImCO.append(ImsizeCO[j+1])
			ImsizeCO.pop(j+1)
			CellsCO.pop(j+1)
			MeasSetsCO.pop(j+1)
			namesCO.pop(j+1)
			a = a - 1
			continue
	cellsumCO = cellsumCO + CellsCO[j]
	imsumCO = imsumCO + ImsizeCO[j]
	j = j+1
	
j = 0
a = len(CellsCI)
while j < len(CellsCI):
	if j>=a:
		break
	if j < a-1:
		if ImsizeCI[j+1] > ImsizeCI[j]+20 or  ImsizeCI[j+1] < ImsizeCI[j]-20:
			outnamesCI.append(namesCI[j+1])
			outCellsCI.append(CellsCI[j+1])
			outImCI.append(ImsizeCI[j+1])
			ImsizeCI.pop(j+1)
			CellsCI.pop(j+1)
			MeasSetsCI.pop(j+1)
			namesCI.pop(j+1)
			a = a -1
			continue
	imsumCI = imsumCI + ImsizeCI[j]
	cellsumCI = cellsumCI + CellsCI[j]
	j = j+1
	



#we will be storing the troubleshooting images in a separate directory
impath='/scratch/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/troubleshooting_images/Auto/'

#First we will image each one separately
for file in MeasSetsCO:
	#CO	
	a = ImsizeCO[i]
	b =round(CellsCO[i],3)
	c = str(b)+'arcsec'
	cellsumCO =cellsumCO + b
	imsumCO = imsumCO + a
	print(file)
	outCO = impath+names[i]+'_CO'+'.png'
	
	sdimaging(infiles=[file],outfile=outCO, overwrite=True, spw=spwCO, gridfunction='SF',convsupport=6,imsize=[a,a],cell=[c,c], stokes='I',veltype='radio',outframe='lsrk')
i = 0	
for file in MeasSetsCI:	
	#now for the CI line
	a = ImsizeCI[i]
	outCI = impath+names[i]+'_CI'+'.png'
	b =round(CellsCI[i],3)
	c = str(b)+'arcsec'
	cellsumCI =cellsumCI + b
	imsumCI = imsumCI + a
	sdimaging(infiles=[file],outfile=outCI, overwrite=True, spw=spwCI, gridfunction='SF',convsupport=6,imsize=[a,a],cell=[c,c], stokes='I',veltype='radio',outframe='lsrk')
	i = i+1

#now to create one image using all measurement sets:

#First for CO:
print("CO")
Cellcalc = cellsumCO/len(CellsCO)
cell = str(Cellcalc)+'arcsec'
Im = int(imsumCO/len(ImsizeCO))
print(cell)
print(im)

sdimaging(infiles=MeasSetsCO,outfile=pathCal+'collectedsdimaging_CO.png', overwrite=True, spw=spwCO,  gridfunction='SF',convsupport=6,imsize=[Im,Im],cell=[cell,cell],stokes='I',veltype='radio',outframe='lsrk')
#Including the excluded ones (with the median value we got for the ones we kept):
sdimaging(infiles=MeasSets,outfile=pathCal+'collectedsdimaging_CO_unfiltered.png', overwrite=True, spw=spwCO,  gridfunction='SF',convsupport=6,imsize=[Im,Im],cell=[cell,cell],stokes='I',veltype='radio',outframe='lsrk')

#Then for CI:

print("CI")
Cellcalc = cellsumCO/len(CellsCI)
cell = str(Cellcalc)+'arcsec'
Im = int(imsumCO/len(ImsizeCI))
print(cell)
print(Im)

sdimaging(infiles=MeasSetsCI,outfile=pathCal+'collectedsdimaging_CI.png', overwrite=True, spw=spwCI,  gridfunction='SF',convsupport=6,imsize=[Im,Im],cell=[cell,cell],stokes='I',veltype='radio',outframe='lsrk')
#Including the excluded ones (with the median value we got for the ones we kept):
sdimaging(infiles=MeasSets,outfile=pathCal+'collectedsdimaging_CI_unfiltered.png', overwrite=True, spw=spwCI,  gridfunction='SF',convsupport=6,imsize=[Im,Im],cell=[cell,cell],stokes='I',veltype='radio',outframe='lsrk')

#Imaging Excluded Data by themselves:
i = 0
for file in outnamesCO:
	a = outImCO[i]
	b =round(outCellsCO[i],3)
	c = str(b)+'arcsec'
	
	print(file)
	outCO = pathex + outnamesCO[i]+'_ex_CO'+'.png'
	
	sdimaging(infiles=[file],outfile=outCO, overwrite=True, spw=spwCO, gridfunction='SF',convsupport=6,imsize=[a,a],cell=[c,c], stokes='I',veltype='radio',outframe='lsrk')
	
	
i = 0
for file in outnamesCI:
	a = outImCI[i]
	b =round(outCellsCI[i],3)
	c = str(b)+'arcsec'
	
	print(file)
	outCI = pathex + outnamesCI[i]+'_ex_CI'+'.png'
	
	sdimaging(infiles=[file],outfile=outCI, overwrite=True, spw=spwCI, gridfunction='SF',convsupport=6,imsize=[a,a],cell=[c,c], stokes='I',veltype='radio',outframe='lsrk')
