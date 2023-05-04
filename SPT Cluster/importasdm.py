path1='/scratch/home/emanolid/data/SPT/2021.2.00019.S/science_goal.uid___A001_X15a9_X11e8/group.uid___A001_X15a9_X11e9/member.uid___A001_X15a9_X11ec/raw/'

path2='/scratch/home/emanolid/data/SPT/2021.2.00019.S/science_goal.uid___A001_X15a9_X11e8/group.uid___A001_X15a9_X11e9/member.uid___A001_X15a9_X11ec/msfiles/'


names = ['uid___A002_Xf53eeb_X11d6b',
	'uid___A002_Xf53eeb_X12338',
	'uid___A002_Xf53eeb_X12997',
	'uid___A002_Xf53eeb_X19feb',
	'uid___A002_Xf53eeb_X1a8ca',
	'uid___A002_Xf53eeb_X4201',
	'uid___A002_Xf73568_X2c01',
	'uid___A002_Xf8d822_X7fe2',
	'uid___A002_Xf9faf1_X402f',
	'uid___A002_Xfa2f45_X50e6',
	'uid___A002_Xfafcc0_X4f42'
	]





asdm_files = [
	path1+'uid___A002_Xf53eeb_X11d6b.asdm.sdm',
	path1+'uid___A002_Xf53eeb_X12338.asdm.sdm',
	path1+'uid___A002_Xf53eeb_X12997.asdm.sdm',
	path1+'uid___A002_Xf53eeb_X19feb.asdm.sdm',
	path1+'uid___A002_Xf53eeb_X1a8ca.asdm.sdm',
	path1+'uid___A002_Xf53eeb_X4201.asdm.sdm',
	path1+'uid___A002_Xf73568_X2c01.asdm.sdm',
	path1+'uid___A002_Xf8d822_X7fe2.asdm.sdm',
	path1+'uid___A002_Xf9faf1_X402f.asdm.sdm',
	path1+'uid___A002_Xfa2f45_X50e6.asdm.sdm',
	path1+'uid___A002_Xfafcc0_X4f42.asdm.sdm'
	]
	
i=0	
for file in asdm_files:
	print(file)
	out = path2 + names[i]+'.ms'
	importasdm(asdm = file, vis = out, verbose= True)

	i=i+1	
