import math
from numpy import random
from seaborn import displot

points = {
    'TAXI': 2,
    'CARGO': {
        'AUTO': {
            'TOP': 4,
            'BOTTOM': 2
        },
        'TELEOP': {
            'TOP': 2,
            'BOTTOM': 1
        }
    },
    'HANGER': {
        'LOW': 4,
        'MID': 6,
        'HIGH': 10,
        'TRAVERSAL': 15
    }
}

climbPoints = 15
totTime = 215

def main():
    avgClimbTime = 20
    stdClimbTime = 2
    pClimbSuccess = 0.75
    avgCycleTime = 10
    stdCycleTime = 1
    pCycleSuccess = 0.8
    pointDict = []
    for x in range(100):
        totPoints, remainingTime = simulationNormDict(avgClimbTime, stdClimbTime, pClimbSuccess, avgCycleTime, stdCycleTime, pCycleSuccess)
        pointDict.append(math.floor(totPoints))
    displot()
    print(pointDict)

def simulation(climbTime, cycleTime):
    totPoints = 0

    shootTime = totTime - climbTime

    shootAttempts = math.floor(shootTime / cycleTime)
    shootPoints = shootAttempts * 2

    totPoints = totPoints + shootPoints + climbPoints

    return totPoints

def simulationNormDict(avgClimbTime, stdClimbTime, pClimbSuccess, avgCycleTime, stdCycleTime, pCycleSuccess):
    totTime = 215
    totPoints = 0

    totTime -= random.normal(avgClimbTime, stdClimbTime)
    totPoints += 15 if (random.geometric(pClimbSuccess) == 1) else 0

    curCycleTime = 0

    while (totTime-curCycleTime > 0):
        totTime -= curCycleTime
        totPoints += 2 if (random.geometric(pCycleSuccess) == 1 ) else 0
        curCycleTime = random.normal(avgCycleTime, stdCycleTime)


    return totPoints, totTime
        

if __name__ == '__main__': 
    main()