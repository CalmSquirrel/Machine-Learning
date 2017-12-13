import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

def grabData(strArray):
    resultArray = []
    stringValue = ""
    for i in strArray:
        if i != '[' and i != ']' and i != ' ':
            if i != ',':
                stringValue+=i
            else:
                resultArray.append(float("".join(stringValue)))
                stringValue = ""
    return resultArray

def grabFirstFifteen(grabData, dataArray):
    FirstFifteen = np.zeros(15)
    for i in dataArray:
        Temp = grabData(i)[0:15]
        if len(Temp) == 0:
            Temp = np.zeros(15)
        elif len(Temp) < 15:
            Temp = np.pad(Temp, (0, 15-len(Temp)), 'constant', constant_values = 0)
        FirstFifteen = np.vstack((FirstFifteen, Temp))
    FirstFifteen = np.delete(FirstFifteen, 0, 0)
    return FirstFifteen

LoL = pd.read_csv('D:\Downloads\_LeagueofLegends.csv')
LoL = LoL[LoL.redMiddleChamp != 'Azir']
LoL = LoL[LoL.blueMiddleChamp != 'Azir']
goldDiff15 = grabFirstFifteen(grabData, np.array(LoL['golddiff'])) #blueteam - redteam
BlueTurrets = grabFirstFifteen(grabData, np.array(LoL['bTowers']))
RedTurrets = grabFirstFifteen(grabData, np.array(LoL['rTowers']))

np.place(BlueTurrets, BlueTurrets == 0, [50])
np.place(BlueTurrets, BlueTurrets <= 15, [1])
np.place(BlueTurrets, BlueTurrets > 15, [0])

np.place(RedTurrets, RedTurrets == 0, [50])
np.place(RedTurrets, RedTurrets <= 15, [1])
np.place(RedTurrets, RedTurrets > 15, [0])

NumBlueTurrets = np.sum(BlueTurrets, axis = 1)
NumRedTurrets = np.sum(RedTurrets, axis = 1)

plt.scatter(NumRedTurrets, NumBlueTurrets)
plt.show()
