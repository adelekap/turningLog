from tkinter import *

def show_entry_fields():
    firstname = tt1Turns.get()
    lastname = tt2Turns.get()

    master.quit()

master = Tk()

################## COLUMN 1 ###############################
Label(master, text='Eighths Turned').grid(row=0, column=1)
Label(master, text="TT1").grid(row=1)
Label(master, text="TT2").grid(row=2)
Label(master, text='TT3').grid(row=3)
Label(master, text='TT4').grid(row=4)
Label(master, text='TT5').grid(row=5)
Label(master, text='TT6').grid(row=6)
Label(master, text='TT7').grid(row=7)
Label(master, text = 'TT8').grid(row=8)
Label(master, text = 'TT9').grid(row=9)
Label(master, text='TT10').grid(row=10)
Label(master, text='TT11').grid(row=11)
Label(master, text='TT12').grid(row=12)
Label(master, text='R1').grid(row=13)
Label(master, text='R2').grid(row=14)

################## COLUMN 2 ###############################
Label(master, text='Current Depth').grid(row=0, column=2)


tt1Turns = Entry(master, width=3).grid(row=1, column=1)
tt2Turns = Entry(master, width=3).grid(row=2, column=1)
tt3Turns = Entry(master, width=3).grid(row=3, column=1)
tt4Turns = Entry(master, width=3).grid(row=4, column=1)
tt5Turns = Entry(master, width=3).grid(row=5, column=1)
tt6Turns = Entry(master, width=3).grid(row=6, column=1)
tt7Turns = Entry(master, width=3).grid(row=7, column=1)
tt8Turns = Entry(master, width=3).grid(row=8, column=1)
tt9Turns = Entry(master, width=3).grid(row=9, column=1)
tt10Turns= Entry(master, width=3).grid(row=10, column=1)
tt11Turns = Entry(master, width=3).grid(row=11, column=1)
tt12Turns = Entry(master, width=3).grid(row=12, column=1)
r1Turns = Entry(master, width=3).grid(row=13, column=1)
r2Turns = Entry(master, width=3).grid(row=14, column=1)


Button(master, text='Quit', command=master.quit).grid(row=15, column=0, sticky=W, pady=4)
Button(master, text='Submit', command=show_entry_fields).grid(row=15, column=1, sticky=W, pady=4)

mainloop( )