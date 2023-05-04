#mini script to test:
#ms.split.cal
#path
path='/scratch/home/emanolid/data/SPT/2021.2.00019.S/science_goal.uid___A001_X15a9_X11e8/group.uid___A001_X15a9_X11e9/member.uid___A001_X15a9_X11ec/calibrated/'


images2=[path+'uid___A002_Xf53eeb_X11d6b_N.png', path+'uid___A002_Xf53eeb_X12338_N.png',path+'uid___A002_Xf53eeb_X12997_N.png',path+'uid___A002_Xf53eeb_X19feb_N.png', path+'uid___A002_Xf53eeb_X4201_N.png', path+'uid___A002_Xf73568_X2c01_N.png', path+'uid___A002_Xf8d822_X7fe2_N.png', path+'uid___A002_Xf9faf1_X402f_N.png', path+'uid___A002_Xfa2f45_X50e6_N.png', path+'uid___A002_Xfafcc0_X4f42_N.png']

tot = path+'collectedsdimaging_N.png'
diameter=12
spw='19'


for file in images2:
	
	print(file)
	cont = file.split('.png')[0]+'_cont.png'
	sub = file.split('.png')[0]+'_subcont.png'
	imcontsub(imagename=file, linefile=sub,contfile=cont,fitorder=1, chans='208~273',stokes='I')
print(tot)
imcontsub(imagename=tot,linefile=tot.split('.png')[0]+'_sub.png',contfile=tot.split('.png')[0]+'_cont.png',fitorder=1,chans='208~273',stokes='I')
