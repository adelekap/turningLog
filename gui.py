from tkinter import *
from getCurrentInfo import *

path = '/Volumes/TRANS 1/BarnesLab/TurningLogs/'
rat = raw_input('Rat: ')

def show_entry_fields():
    firstname = tt1Turns.get()
    lastname = tt2Turns.get()

    master.quit()

master = Tk()

depths,positions = getCurrent(path,rat)

tetrodes = ['TT1','TT2','TT3','TT4','TT5','TT6','TT7','TT8','TT9','TT10','TT11','TT12','R1','R2']


################## COLUMN 0 ###############################
for tLabel in range(0,14):
    Label(master, text=tetrodes[tLabel]).grid(row=tLabel+1,column=0)


################## COLUMN 1 ###############################
Label(master, text='Current Depth').grid(row=0, column=1)
for t in range(0,14):
    Label(master, text=depths[t]).grid(row=t+1,column=1)


################## COLUMN 2 ###############################
Label(master, text='Current Position').grid(row=0, column=2)
for tt in range(0,14):
    Label(master, text=positions[tt]).grid(row=tt+1,column=2)


################## COLUMN 3 ###############################
Label(master, text='Eighths Turned').grid(row=0, column=3)
tt1Turns = Entry(master, width=3).grid(row=1, column=3)
tt2Turns = Entry(master, width=3).grid(row=2, column=3)
tt3Turns = Entry(master, width=3).grid(row=3, column=3)
tt4Turns = Entry(master, width=3).grid(row=4, column=3)
tt5Turns = Entry(master, width=3).grid(row=5, column=3)
tt6Turns = Entry(master, width=3).grid(row=6, column=3)
tt7Turns = Entry(master, width=3).grid(row=7, column=3)
tt8Turns = Entry(master, width=3).grid(row=8, column=3)
tt9Turns = Entry(master, width=3).grid(row=9, column=3)
tt10Turns= Entry(master, width=3).grid(row=10, column=3)
tt11Turns = Entry(master, width=3).grid(row=11, column=3)
tt12Turns = Entry(master, width=3).grid(row=12, column=3)
r1Turns = Entry(master, width=3).grid(row=13, column=3)
r2Turns = Entry(master, width=3).grid(row=14, column=3)


################## COLUMN 4 ###############################
Label(master, text='New Position').grid(row=0, column=4)
tt1Pos = Entry(master, width=3).grid(row=1, column=4)
tt2Pos = Entry(master, width=3).grid(row=2, column=4)
tt3Pos = Entry(master, width=3).grid(row=3, column=4)
tt4Pos = Entry(master, width=3).grid(row=4, column=4)
tt5Pos = Entry(master, width=3).grid(row=5, column=4)
tt6Pos = Entry(master, width=3).grid(row=6, column=4)
tt7Pos = Entry(master, width=3).grid(row=7, column=4)
tt8Pos = Entry(master, width=3).grid(row=8, column=4)
tt9Pos = Entry(master, width=3).grid(row=9, column=4)
tt10Pos = Entry(master, width=3).grid(row=10, column=4)
tt11Pos = Entry(master, width=3).grid(row=11, column=4)
tt12Pos = Entry(master, width=3).grid(row=12, column=4)
r1Pos = Entry(master, width=3).grid(row=13, column=4)
r2Pos = Entry(master, width=3).grid(row=14, column=4)

################## BUTTONS ###############################
Button(master, text='Quit', command=master.quit).grid(row=15, column=1, sticky=W, pady=4)
Button(master, text='Submit', command=show_entry_fields).grid(row=15, column=3, sticky=W, pady=4)


mainloop( )