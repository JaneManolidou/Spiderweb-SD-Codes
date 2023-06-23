#split antennas

import os
from sys import path
import glob
scan = '4'
# === USER INPUTS ===
# Path to your analysUtils.py
path_analysisUtils = "/scratch/home/emanolid/data/casa/analysis_scripts"

# List of ms files after atm correction, uid___xxx.ms.atmcor.atmtypeX
# If the conventional pipeline naming is used the glob() should work
ms_names = glob.glob('*.ms.atmcor.atmtype?')
# ms_names = ['uid___A002_Xf49cca_X2514b.ms.atmcor.atmtype1',
#             'uid___A002_Xf53eeb_X217cd.ms.atmcor.atmtype1',
#            ]
print(ms_names)

path1 = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/antennas/'
path2 = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/antennas/'
path3 = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/antennas/'
path4 = '/home/emanolid/data/Spiderweb/Data/science_goal.uid___A001_X2d20_X3bd9/group.uid___A001_X2d20_X3bda/member.uid___A001_X2d20_X3bdd/calibrated/working/antennas/'


for file in ms_names:
	
	output1 = path1+file.split('.ms')[0]+'_antenna1.ms.atmcor.atmtype'
	print(output1)
	split(vis = file, outputvis = output1, antenna = 'PM01',datacolumn='data',scan='')
	
	
for file in ms_names:
	
	
	output2 = path2+file.split('.ms')[0]+'_antenna2.ms.atmcor.atmtype'
	print(output2)
	split(vis = file, outputvis = output2, antenna = 'PM02',datacolumn='data',scan='')
	
	
for file in ms_names:
	
	
	output3 = path3+file.split('.ms')[0]+'_antenna3.ms.atmcor.atmtype'

	print(output3)
	split(vis = file, outputvis = output3, antenna = 'PM03',datacolumn='data',scan='')
	
for file in ms_names:
	
	
	output4 = path4+file.split('.ms')[0]+'_antenna4.ms.atmcor.atmtype'
	print(output4)
	split(vis = file, outputvis = output4, antenna = 'PM04', datacolumn='data',scan='')
