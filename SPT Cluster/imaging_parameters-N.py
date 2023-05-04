#mini script to test:
#ms.split.cal
#path
path='/scratch/home/emanolid/data/SPT/'

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
spw=19
mean_freq_split=[]
theory_beam_split=[]
cell_list_split=[]
imsize_list_split=[]
field='2'
#commands to determine imaging parameters
for file in files_split:
	
	print(file)
	
	#imagename=outresult+'spw%s.image'%(spw)
	#determining maxsize
	xsampling,ysampling,maxsize=aU.getTPSampling(vis=file,showplot=False)
	#determining theory beam and imsize and cell
	msmd.open(file)
	freq=msmd.meanfreq(spw)
	msmd.close()
	mean_freq_split.append(freq)
	theorybeam=aU.primaryBeamArcsec(frequency=freq*1e-9,diameter=diameter)
	cell=theorybeam/9.0
	cell_list_split.append(cell)
	imsize=int(round(maxsize/cell)*2)
	imsize_list_split.append(imsize)
print("mean_frequency=",mean_freq_split,"\ntheorybeam=",theory_beam_split,"\ncell=",cell_list_split,"\nimsize=",imsize_list_split)
