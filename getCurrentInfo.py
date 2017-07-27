import pandas as pd

def getCurrent(path,rat):
    file = path+rat+'/current_'+rat+'.csv'
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






