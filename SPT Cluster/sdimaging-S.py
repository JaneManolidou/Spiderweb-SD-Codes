#mini script to test:
#ms.split.cal
#path
path='/scratch/home/emanolid/data/SPT/2021.2.00019.S/science_goal.uid___A001_X15a9_X11e8/group.uid___A001_X15a9_X11e9/member.uid___A001_X15a9_X11ec/calibrated/'

files_split=[
	path+'uid___A002_Xf53eeb_X11d6b.ms.split.cal',
	path+'uid___A002_Xf53eeb_X12338.ms.split.cal',
	path+'uid___A002_Xf53eeb_X12997.ms.split.cal',
	path+'uid___A002_Xf53eeb_X19feb.ms.split.cal',
	path+'uid___A002_Xf53eeb_X4201.ms.split.cal',
	path+'uid___A002_Xf73568_X2c01.ms.split.cal',
	path+'uid___A002_Xf8d822_X7fe2.ms.split.cal',
	path+'uid___A002_Xf9faf1_X402f.ms.split.cal',
	path+'uid___A002_Xfa2f45_X50e6.ms.split.cal',
	path+'uid___A002_Xfafcc0_X4f42.ms.split.cal'
	]

diameter=12
spw='19'
field='1'
i = 0
imsize_list= [98, 86, 100, 100, 106, 102, 106, 106, 104, 102]
cell_list = [6.978215056818556, 6.978216435414547, 6.978217631126456, 6.978204935999371, 6.978229023952952, 6.977719236417349, 6.977609062092598, 6.97763661686913, 6.977648578410993, 6.977736666649563]


for file in files_split:
		
	a = imsize_list[i]
	b = cell_list[i]
	c = str(b)+'arcsec'
	print(file)
	out = file+'.png'
	sdimaging(infiles=[file],outfile=out, overwrite=True, spw=spw, gridfunction='SF',convsupport=6,imsize=[a,a],cell=[c,c],field=field, stokes='I',veltype='radio',outframe='lsrk')
	i = i+1
sdimaging(infiles=files_split,outfile=path+'collectedsdimaging.png', overwrite=True, spw=spw, field=field, gridfunction='SF',convsupport=6,imsize=[101,101],cell=['6.98arcsec','6.98arcsec'],stokes='I',veltype='radio',outframe='lsrk')

