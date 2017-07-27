from getCurrentInfo import *


path = '/Volumes/TRANS 1/BarnesLab/TurningLogs/'
rat = raw_input('Rat: ')
date = raw_input('Date {YYYY-MM-DD}: ')

depths,positions,totTurns = getCurrent(path,rat,date)
tetrodes = ['TT1','TT2','TT3','TT4','TT5','TT6','TT7','TT8','TT9','TT10','TT11','TT12','R1','R2']


def save_turn_data():
    currentFile = path + rat + '/current_' + rat + '.csv'
    logFile = path + rat + '/' + rat + '_'+date+'.csv'
    turns=[tt1Turns.get(),tt2Turns.get(),tt3Turns.get(),tt4Turns.get(),tt5Turns.get(),tt6Turns.get(),
           tt7Turns.get(),tt8Turns.get(),tt9Turns.get(),tt10Turns.get(),tt11Turns.get(),tt12Turns.get(),
           r1Turns.get(),r2Turns.get()]
    newPositions=[tt1Pos.get(),tt2Pos.get(),tt3Pos.get(),tt4Pos.get(),tt5Pos.get(),tt6Pos.get(),
                  tt7Pos.get(),tt8Pos.get(),tt9Pos.get(),tt10Pos.get(),tt11Pos.get(),tt12Pos.get(),
                  r1Pos.get(),r2Pos.get()]
    notes = [tt1Notes.get(),tt2Notes.get(),tt3Notes.get(),tt4Notes.get(),tt5Notes.get(),tt6Notes.get(),tt7Notes.get(),
             tt8Notes.get(),tt9Notes.get(),tt10Notes.get(),tt11Notes.get(),tt12Notes.get(),r1Notes.get(),r2Notes.get()]
    with open(currentFile,'w') as current:
        with open(logFile,'w') as log:
            current.write('TT,Direction,Total Turns,Depth,Updated\n')
            log.write('TT,Old Depth,Old Direction,Turns,New Direction,Total Turns,New Depth,Notes\n')
            for tet in range(0,14):
                newTotal = total(totTurns[tet],turns[tet])
                newDepth = turnDepth(newTotal)
                current.write('{0},{1},{2},{3},{4}\n'.format(tetrodes[tet],newPositions[tet],newTotal,newDepth,date))
                log.write('{0},{1},{2},{3},{4},{5},{6},{7}\n'.format(tetrodes[tet],depths[tet],positions[tet],turns[tet],
                                                                 newPositions[tet],newTotal,newDepth,notes[tet]))

    master.quit()


master = Tk()


################## COLUMN 0 ###############################
for tLabel in range(0,14):
    Label(master, text=tetrodes[tLabel],font=('Helvetica',16, "bold")).grid(row=tLabel+1,column=0)


################## COLUMN 1 ###############################
Label(master, text='Current Depth',font=('Helvetica',15, "bold")).grid(row=0, column=1)
for t in range(0,14):
    Label(master, text=depths[t],font=('Helvetica',14)).grid(row=t+1,column=1)


################## COLUMN 2 ###############################
Label(master, text='Current Position',font=('Helvetica',15, "bold")).grid(row=0, column=2)
for tt in range(0,14):
    Label(master, text=positions[tt],font=('Helvetica',14)).grid(row=tt+1,column=2)


################## COLUMN 3 ###############################
Label(master, text='Eighths Turned',font=('Helvetica',15, "bold")).grid(row=0, column=3)
tt1Turns = Entry(master, width=3)
tt1Turns.grid(row=1, column=3)
tt2Turns = Entry(master, width=3)
tt2Turns.grid(row=2, column=3)
tt3Turns = Entry(master, width=3)
tt3Turns.grid(row=3, column=3)
tt4Turns = Entry(master, width=3)
tt4Turns.grid(row=4, column=3)
tt5Turns = Entry(master, width=3)
tt5Turns.grid(row=5, column=3)
tt6Turns = Entry(master, width=3)
tt6Turns.grid(row=6, column=3)
tt7Turns = Entry(master, width=3)
tt7Turns.grid(row=7, column=3)
tt8Turns = Entry(master, width=3)
tt8Turns.grid(row=8, column=3)
tt9Turns = Entry(master, width=3)
tt9Turns.grid(row=9, column=3)
tt10Turns= Entry(master, width=3)
tt10Turns.grid(row=10, column=3)
tt11Turns = Entry(master, width=3)
tt11Turns.grid(row=11, column=3)
tt12Turns = Entry(master, width=3)
tt12Turns.grid(row=12, column=3)
r1Turns = Entry(master, width=3)
r1Turns.grid(row=13, column=3)
r2Turns = Entry(master, width=3)
r2Turns.grid(row=14, column=3)


################## COLUMN 4 ###############################
Label(master, text='New Position',font=('Helvetica',15, "bold")).grid(row=0, column=4)
tt1Pos = Entry(master, width=3)
tt1Pos.grid(row=1, column=4)
tt2Pos = Entry(master, width=3)
tt2Pos.grid(row=2, column=4)
tt3Pos = Entry(master, width=3)
tt3Pos.grid(row=3, column=4)
tt4Pos = Entry(master, width=3)
tt4Pos.grid(row=4, column=4)
tt5Pos = Entry(master, width=3)
tt5Pos.grid(row=5, column=4)
tt6Pos = Entry(master, width=3)
tt6Pos.grid(row=6, column=4)
tt7Pos = Entry(master, width=3)
tt7Pos.grid(row=7, column=4)
tt8Pos = Entry(master, width=3)
tt8Pos.grid(row=8, column=4)
tt9Pos = Entry(master, width=3)
tt9Pos.grid(row=9, column=4)
tt10Pos = Entry(master, width=3)
tt10Pos.grid(row=10, column=4)
tt11Pos = Entry(master, width=3)
tt11Pos.grid(row=11, column=4)
tt12Pos = Entry(master, width=3)
tt12Pos.grid(row=12, column=4)
r1Pos = Entry(master, width=3)
r1Pos.grid(row=13, column=4)
r2Pos = Entry(master, width=3)
r2Pos.grid(row=14, column=4)


################## COLUMN 5 ###############################
Label(master, text='Notes',font=('Helvetica',15, "bold")).grid(row=0, column=5)
tt1Notes = Entry(master, width=10)
tt1Notes.grid(row=1, column=5)
tt2Notes = Entry(master, width=10)
tt2Notes.grid(row=2, column=5)
tt3Notes = Entry(master, width=10)
tt3Notes.grid(row=3, column=5)
tt4Notes = Entry(master, width=10)
tt4Notes.grid(row=4, column=5)
tt5Notes = Entry(master, width=10)
tt5Notes.grid(row=5, column=5)
tt6Notes = Entry(master, width=10)
tt6Notes.grid(row=6, column=5)
tt7Notes = Entry(master, width=10)
tt7Notes.grid(row=7, column=5)
tt8Notes = Entry(master, width=10)
tt8Notes.grid(row=8, column=5)
tt9Notes = Entry(master, width=10)
tt9Notes.grid(row=9,column=5)
tt10Notes = Entry(master, width=10)
tt10Notes.grid(row=10, column=5)
tt11Notes= Entry(master, width=10)
tt11Notes.grid(row=11, column=5)
tt12Notes = Entry(master, width=10)
tt12Notes.grid(row=12, column=5)
r1Notes = Entry(master, width=10)
r1Notes.grid(row=13, column=5)
r2Notes = Entry(master, width=10)
r2Notes.grid(row=14, column=5)



################## BUTTONS ###############################
Button(master, text='Quit', command=master.quit).grid(row=16, column=2, sticky=W, pady=4)
Button(master, text='Submit', command=save_turn_data).grid(row=16, column=4, sticky=W, pady=4)


mainloop()