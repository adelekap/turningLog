import os
import pandas as pd
from datetime import date
from turns import *


rat = raw_input("Rat: ")

dateStamp = raw_input("Date {YYYY-MM-DD}: ")

directory = '/Volumes/TRANS 1/BarnesLab/TurningLogs/'+rat


current = '{0}/current_{1}.csv'.format(directory,rat)

tetrodes = ['1','2','3','4','5','6','7','8','9','10','11','12','R1','R2']

def getCurrent():
    if os.path.exists(current):
        return pd.read_csv(current)

    else:
        with open(current,'w') as newCurrent:
            newCurrent.write('TT,Direction,Total Turns,Depth\n')
            for tt in tetrodes:
                direction = raw_input("Starting Direction of TT"+tt+": ")
                newCurrent.write('{0},{1},0,0\n'.format(tt,direction))

        return pd.read_csv(current)


def updateCurrent(curStats1):
    file = '{0}/{1}_{2}.csv'.format(directory,rat,dateStamp)
    curStats2 = curStats1.set_index('TT')
    curStats = curStats2.transpose()
    confirm = 'N'

    while(confirm == 'N'):
        with open(file,'w') as logFile:
            with open(current,'w') as currentFile:
                logFile.write('TT,Old Direction,Turns,New Direction,Total Turns,Depth\n')
                currentFile.write('TT,Direction,Total Turns,Depth\n')
                for tt in tetrodes:
                    info = list(curStats[tt])
                    turnTT = int(raw_input("Eighths turned on "+tt+": "))
                    oldDir = info[0]
                    newDir = raw_input("New Direction of "+tt+": ")
                    totTurns,depth = turn(int(turnTT),int(info[1]))

                    logFile.write('{0},{1},{2},{3},{4},{5}\n'.format(tt,oldDir,turnTT,newDir,totTurns,depth))
                    currentFile.write('{0},{1},{2},{3}\n'.format(tt,newDir,totTurns,depth))
                confirm = raw_input("Confirm input? (Y/N)")


updateCurrent(getCurrent())
