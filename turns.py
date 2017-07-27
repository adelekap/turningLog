

def turn(turns,curTurns):
    totalTurns = curTurns + turns
    depth = float(totalTurns) * 39.63
    return (totalTurns,int(depth))