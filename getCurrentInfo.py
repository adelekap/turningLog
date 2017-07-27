import pandas as pd
import os
from tkinter import *

tetrodes = ['TT1','TT2','TT3','TT4','TT5','TT6','TT7','TT8','TT9','TT10','TT11','TT12','R1','R2']



def getInitial():
    master = Tk()
    for tLabel in range(0, 14):
        Label(master, text=tetrodes[tLabel], font=('Helvetica', 16, "bold")).grid(row=tLabel + 1, column=0)
    Label(master, text='Starting Position', font=('Helvetica', 15, "bold")).grid(row=0, column=1)
    tt1Start = Entry(master, width=3)
    tt1Start.grid(row=1, column=1)
    tt2Start = Entry(master, width=3)
    tt2Start.grid(row=2, column=1)
    tt3Start = Entry(master, width=3)
    tt3Start.grid(row=3, column=1)
    tt4Start = Entry(master, width=3)
    tt4Start.grid(row=4, column=1)
    tt5Start = Entry(master, width=3)
    tt5Start.grid(row=5, column=1)
    tt6Start = Entry(master, width=3)
    tt6Start.grid(row=6, column=1)
    tt7Start = Entry(master, width=3)
    tt7Start.grid(row=7, column=1)
    tt8Start = Entry(master, width=3)
    tt8Start.grid(row=8, column=1)
    tt9Start = Entry(master, width=3)
    tt9Start.grid(row=9, column=1)
    tt10Start = Entry(master, width=3)
    tt10Start.grid(row=10,column=1)
    tt11Start = Entry(master, width=3)
    tt11Start.grid(row=11, column=1)
    tt12Start = Entry(master, width=3)
    tt12Start.grid(row=12, column=1)
    r1Start = Entry(master, width=3)
    r1Start.grid(row=13, column=1)
    r2Start = Entry(master, width=3)
    r2Start.grid(row=14, column=1)

    startPos= [tt1Start,tt2Start,tt3Start,tt4Start,tt5Start,tt6Start,tt7Start,tt8Start,tt9Start,tt10Start,
               tt11Start,tt12Start,r1Start,r2Start]

    Button(master, text='Quit', command=master.quit).grid(row=16, column=0, sticky=W, pady=4)
    Button(master, text='Submit', command=master.quit).grid(row=16, column=2 , sticky=W, pady=4)

    mainloop()
    return [l.get() for l in startPos]


def getCurrent(path,rat,date):
    dir = path+rat
    file = path+rat+'/current_'+rat+'.csv'

    if not os.path.isdir(dir):
        os.makedirs(dir)
    if os.path.exists(file):
        info = pd.read_csv(file)
    else:
        with open(file,'w') as create:
            create.write('TT,Direction,Total Turns,Depth,Updated\n')
            starting = getInitial()
            for tetr in range(0,14):
                create.write('{0},{1},0,0,{2}\n'.format(tetrodes[tetr],starting[tetr],date))
        info = pd.read_csv(file)



    depths = list(info['Depth'])
    positions = list(info['Direction'])
    totalTurns = list(info['Total Turns'])

    return (depths,positions,totalTurns)

def total(past,new):
    return int(past)+int(new)

def turnDepth(totalTurns):
    depth = float(totalTurns) * 39.63
    return int(depth)






