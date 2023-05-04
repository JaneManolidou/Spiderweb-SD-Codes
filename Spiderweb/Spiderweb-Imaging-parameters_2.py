path='/scratch/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/raw/msfiles/'

files_split=[
	path+'uid___A002_X101c3b2_X42b1.ms',
	path+'uid___A002_X101e5ab_Xf704.ms',
	path+'uid___A002_X10239e1_X178c7.ms',
	path+'uid___A002_X10239e1_X181b9.ms',
	path+'uid___A002_X10239e1_X18e80.ms',
	path+'uid___A002_X10275c0_X17ff7.ms',
	path+'uid___A002_X10305a2_X224e.ms',
	path+'uid___A002_X10305a2_X2c6c.ms',
	path+'uid___A002_X103317b_X20c5.ms',
	path+'uid___A002_X103317b_X2744.ms',
	path+'uid___A002_X1033b6e_X153b.ms',
	path+'uid___A002_X1033b6e_X1bbd.ms',
	path+'uid___A002_X1033b6e_X21ed.ms',
	path+'uid___A002_X1033b6e_Xfe3.ms',
	path+'uid___A002_X1034414_X15fc.ms',
	path+'uid___A002_X1034414_X2139.ms',
	path+'uid___A002_X1034414_X27c9.ms',
	path+'uid___A002_X1034414_X2dbd.ms',
	path+'uid___A002_X1034f36_X119b.ms',
	path+'uid___A002_X1034f36_Xa80.ms',
	path+'uid___A002_X1035744_X2f7a.ms',
	path+'uid___A002_X1035744_X34cd.ms',
	path+'uid___A002_X1036d05_X2644.ms',
	path+'uid___A002_X1036d05_X2c62.ms',
	path+'uid___A002_X1036d05_X33a5.ms',
	path+'uid___A002_X1036d05_Xb88f.ms'
	]
	

	
diameter=12
spwCO=19
spwCI = 21
mean_freq_CO=[]
theory_beam_CO=[]
cell_list_CO=[]
imsize_list_CO=[]
msize=[]
mean_freq_CI=[]
theory_beam_CI=[]
cell_list_CI=[]
imsize_list_CI=[]


#commands to determine imaging parameters
for file in files_split:
	
	print(file)
	
	xsampling,ysampling,maxsize = au.getTPSampling(vis=file,showplot=False)
	msize.append(maxsize)
	print(maxsize)
	
	msmd.open(file)
	freq_CO=msmd.meanfreq(spwCO)
	freq_CI=msmd.meanfreq(spwCI)
	msmd.close()
	
	mean_freq_CO.append(freq_CO)
	mean_freq_CI.append(freq_CI)
	
	theorybeamCO=au.primaryBeamArcsec(frequency=freq_CO*1e-9,diameter=diameter,taper=10.0,fwhmfactor=None)
	theory_beam_CO.append(theorybeamCO)
	cellCO=theorybeamCO/9.0
	cell_list_CO.append(cellCO)
	imsizeCO=int(round(maxsize/cellCO)*2)
	imsize_list_CO.append(imsizeCO)
	
	
	theorybeamCI=au.primaryBeamArcsec(frequency=freq_CI*1e-9,diameter=diameter,taper=10.0,fwhmfactor=None)
	theory_beam_CI.append(theorybeamCI)
	cellCI=theorybeamCI/9.0
	cell_list_CI.append(cellCI)
	imsizeCI=int(round(maxsize/cellCI)*2)
	imsize_list_CI.append(imsizeCI)
print("Information for CO:")
print("Mean frequency for spw 19: ",mean_freq_CO,"\nTheory beam for CO =",theory_beam_CO,"\nSize of cells =",cell_list_CO,"\nImsize=",imsize_list_CO)
print("and now")
print("Information for CI:")
print("Mea frequency for spw 21: ",mean_freq_CI,"\nTheory beam for CI =",theory_beam_CI,"\nSize of cells=",cell_list_CI,"\nImsize=",imsize_list_CI)



