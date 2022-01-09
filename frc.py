import math
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

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
    pointArray = []
    for x in range(1000):
        totPoints, remainingTime = simulationNormDict(avgClimbTime, stdClimbTime, pClimbSuccess, avgCycleTime, stdCycleTime, pCycleSuccess)
        #totPoints, remainingTime = simulationNormDictNoClimb(avgCycleTime, stdCycleTime, pCycleSuccess)
        pointArray.append(math.floor(totPoints))
    data = {}
    data['Points'] = pointArray
    sns.set_theme(style="darkgrid")
    sns.displot(data, x='Points', discrete=True)
    plt.show()

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

def simulationNormDictNoClimb(avgCycleTime, stdCycleTime, pCycleSuccess):
    totTime = 215
    totPoints = 0
    curCycleTime = 0

    while (totTime-curCycleTime > 0):
        totTime -= curCycleTime
        totPoints += 2 if (random.geometric(pCycleSuccess) == 1 ) else 0
        curCycleTime = random.normal(avgCycleTime, stdCycleTime)

    return totPoints, totTime

if __name__ == '__main__': 
    main()