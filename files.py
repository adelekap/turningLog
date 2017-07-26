import os
import pandas as pd

directory = '/Users/adelekap/Documents'

rat = '10441'

current = '{0}/current_{1}.csv'.format(directory,rat)

if os.path.exists(current):
    curStats = pd.read_csv(current)

else:
    with open(current,'w') as newCurrent:
        newCurrent.write('TT,Direction,Total Turns,Depth\n')
        for tt in ['1','2','3','4','5','6','7','8','9','10','11','12','R1','R2']:
            direction = raw_input("Starting Direction of TT"+tt+": ")
            newCurrent.write('{0},{1},0,0\n'.format(tt,direction))

    curStats = pd.read_csv(current)




