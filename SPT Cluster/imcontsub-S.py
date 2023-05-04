#mini script to test:
#ms.split.cal
#path
path='/scratch/home/emanolid/data/SPT/2021.2.00019.S/science_goal.uid___A001_X15a9_X11e8/group.uid___A001_X15a9_X11e9/member.uid___A001_X15a9_X11ec/calibrated/'


images=[path+'uid___A002_Xf53eeb_X11d6b.ms.split.cal.png',path+ 'uid___A002_Xf53eeb_X12338.ms.split.cal.png',path+'uid___A002_Xf53eeb_X12997.ms.split.cal.png',path+'uid___A002_Xf53eeb_X19feb.ms.split.cal.png',path+ 'uid___A002_Xf53eeb_X4201.ms.split.cal.png', path+'uid___A002_Xf73568_X2c01.ms.split.cal.png', path+'uid___A002_Xf8d822_X7fe2.ms.split.cal.png', path+'uid___A002_Xf9faf1_X402f.ms.split.cal.png', path+'uid___A002_Xfa2f45_X50e6.ms.split.cal.png', path+'uid___A002_Xfafcc0_X4f42.ms.split.cal.png']
tot = path+'collectedsdimaging.png'
diameter=12
spw='19'


for file in images:
	
	print(file)
	cont = file.split('.ms')[0]+'_cont.png'
	sub = file.split('.ms')[0]+'_subcont.png'
	imcontsub(imagename=file, linefile=sub,contfile=cont,fitorder=1, chans='202~273',stokes='I')
print(tot)
imcontsub(imagename=tot,linefile=tot.split('.png')[0]+'_sub.png',contfile=tot.split('.png')[0]+'_cont.png',fitorder=1,chans='208~273',stokes='I')
