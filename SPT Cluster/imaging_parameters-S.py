
path='/scratch/home/emanolid/data/SPT/2021.2.00019.S/science_goal.uid___A001_X15a9_X11e8/group.uid___A001_X15a9_X11e9/member.uid___A001_X15a9_X11ec/calibrated/working/'

files_split=[
	path+'uid___A002_Xf53eeb_X11d6b.ms',
	path+'uid___A002_Xf53eeb_X12338.ms',
	path+'uid___A002_Xf53eeb_X12997.ms',
	path+'uid___A002_Xf53eeb_X19feb.ms',
	path+'uid___A002_Xf53eeb_X1a8ca.ms',
	path+'uid___A002_Xf53eeb_X4201.ms',
	path+'uid___A002_Xf73568_X2c01.ms',
	path+'uid___A002_Xf8d822_X7fe2.ms',
	path+'uid___A002_Xf9faf1_X402f.ms',
	path+'uid___A002_Xfa2f45_X50e6.ms',
	path+'uid___A002_Xfafcc0_X4f42.ms'
	]
diameter=12
spw=21
mean_freq=[]
theory_beam=[]
cell_list=[]
imsize_list=[]
msize=[]
field = '1'

#commands to determine imaging parameters
for file in files_split:
	
	print(file)
	
	xsampling,ysampling,maxsize = au.getTPSampling(vis=file,showplot=False)
	msize.append(maxsize)
	print(maxsize)
	msmd.open(file)
	freq=msmd.meanfreq(spw)
	msmd.close()
	mean_freq.append(freq)
	theorybeam=au.primaryBeamArcsec(frequency=freq*1e-9,diameter=diameter)
	theory_beam.append(theorybeam)
	cell=theorybeam/9.0
	cell_list.append(cell)
	imsize=int(round(maxsize/cell)*2)
	imsize_list.append(imsize)
print("mean_frequency=",mean_freq,"\ntheorybeam=",theory_beam,"\ncell=",cell_list,"\nimsize=",imsize_list)
