

def turn(turns,curTurns):
    totalTurns = curTurns + turns
    depth = float(totalTurns) * 39.626
    return (totalTurns,int(depth))