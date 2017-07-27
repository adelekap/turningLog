import pandas as pd

def getCurrent(path,rat):
    file = path+rat+'/current_'+rat+'.csv'
    info = pd.read_csv(file)

    depths = list(info['Depth'])
    positions = list(info['Direction'])

    return (depths,positions)


