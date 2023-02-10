import numpy as np
from TabletoANF import ANF2TruthTable, AlltruTable, comb
# from scipy import comb


def vectorSplit(varsNum):
    k_vec = {}
    for i in range(varsNum+1):
        k_vec['k=' + str(i)] = []
    allTable = AlltruTable(varsNum)
    for i in allTable:
        count = 0
        for j in i:
            if j == 1:
                count = count + 1
            else:
                continue
        k_vec['k=' + str(count)].append(i)
    return k_vec

def k_vector(k,varsNum):
    k_Table = vectorSplit(varsNum)['k=' + str(k)]
    return k_Table
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1]
def f(x,truthTable):
    xi = 0   #x向量对应的十进制数
    x_1=x.copy()
    x_1.reverse()
    for i in range(len(x_1)):
        xi =  xi + x_1[i]*pow(2,i)
    return truthTable[xi]



def k_Walshcomp(k,varsNum, truthTable):
    x = k_vector(k,varsNum)
    allTable = AlltruTable(varsNum)
    Walsh_res = []

    for i in allTable:
        sum = 0
        for j in x:
            tmp = np.inner(np.array(i),np.array(j))%2
            sum = sum +pow(-1,(f(j,truthTable)+tmp)%2)
        Walsh_res.append(sum)
    return Walsh_res

def k_nonlinearity(k,varsNum,WalshTable):

    for i in range(len(WalshTable)):
        WalshTable[i] = abs(WalshTable[i])
    Walsh_max = max(WalshTable)
    k_non = (comb(varsNum,k))/2-Walsh_max/2
    return k_non

def allmultipy(varsNum):
    allTable = AlltruTable(varsNum)
    oneTerm = {}
    for i in range(varsNum):
        oneTerm['x_' + str(i + 1)] = 0
    # print(oneTerm) # {'x_1': [False, 1], 'x_2': [False, 1], 'x_3': [False, 1]}
    resTable = []
    for table in allTable:
        ret = 1
        for i in range(int(varsNum/2)):
            oneTerm['x_' + str(i + 1)] = table[varsNum - i - 1]
            oneTerm['x_' + str(i + 1 + int(varsNum / 2))] = table[varsNum - (i + 1 + int(varsNum / 2))]
            restmp = (oneTerm['x_' + str(i + 1)] + oneTerm['x_' + str(i + 1 + int(varsNum / 2))] + 1) % 2
            ret *= int(restmp)
        resTable.append(ret)
    return resTable

# def g_create(varsNum,ftruthTable):
#     multiTable = allmultipy(varsNum)
#     gtruthTable = [0] * pow(2,varsNum)
#     print(gtruthTable)
#     if varsNum == 2 | varsNum == 4:
#         gtruthTable = ANF2TruthTable(varsNum,AlltruTable(varsNum))
#     elif varsNum > 4 :
#         for i in range(pow(2,varsNum)):
#             if i > 3:
#                 gi = i / 4
#             else: gi = i
#             onetruth = ftruthTable[i] + g_create(int(varsNum/4),ftruthTable[:pow(2,int(varsNum/4))])[gi]*multiTable[i]
#             onetruth = onetruth % 2
#             gtruthTable[i] = onetruth
#     return gtruthTable

def g_create(varsNum,ftruthTable):
    if varsNum == 1:
        return [0,1]
    multiTable = allmultipy(varsNum)
    gtruthTable = [0] * pow(2, varsNum)
    g_m_1table = g_create(int(varsNum/2),ANF2TruthTable(int(varsNum/2),AlltruTable(int(varsNum/2))))
    print(g_m_1table)
    for i in range(pow(2, varsNum)):
        gi = int(i / int(pow(2, int(varsNum/2))))
        onetruth = ftruthTable[i] + g_m_1table[gi] * multiTable[i]
        onetruth = onetruth % 2
        gtruthTable[i] = onetruth
    return gtruthTable



if __name__ == '__main__':
    varsNum = int(input("The varnum is:"))
    #ftruthTable = ANF2TruthTable(varsNum, AlltruTable(varsNum))
    # please input the truetable of Boolean function as fallow
    ftruthTable =
    #truthTable = g_create(varsNum,ftruthTable)
    while 1:
        k = int(input("Please input the weight k :"))
        if k == -1 :
            break
        WalshTable = k_Walshcomp(k,varsNum,ftruthTable)
       # print(WalshTable)
        k_non = k_nonlinearity(k,varsNum,WalshTable)
        print(k_non)