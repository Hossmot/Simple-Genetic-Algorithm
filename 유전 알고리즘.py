import random as rd
R = int(0) 

def randint():
    R = rd.randrange(1, 6)
    return(R)
HMaccord = int(input('최댓값 유지의 최소횟수를 입력해 주세요'))
MaxCount = int(0)
food_cost = [1, 2 ,3 ,4, 5]
food_sacri = [2, 3, 5, 7, 9]
rdgroup = []
ExGroup = []
descendantGroup = []
Sacri_List = []
SacriPut = int(0)
SvGroup = []
Calculate_Group = []
SvPoint = int(0)
Sum = int(0)
NumCount = 0;

while NumCount != 36 :                #초기 그룹 설정
    k = randint()
    if(Sum+k)<10:
        rdgroup.append(k)
        Sum += k
    if(Sum+k)==10:
        rdgroup.append(k)
        ExGroup.append(rdgroup)
        rdgroup = []
        Sum = 0
        NumCount += 1

for i in range(36):
    for k in range(len(ExGroup[i])):
        SacriPut += food_sacri[ExGroup[i][k]-1]          #만족도 측정
    Sacri_List.append(SacriPut)
    SacriPut = 0
           
Sacri_List.sort()
SvPoint = Sacri_List[31]


for i in range(36):
    for k in range(len(ExGroup[i])):
        SacriPut += food_sacri[ExGroup[i][k]-1]
    if SacriPut >= SvPoint:
        SvGroup.append(ExGroup[i])           #1차 자연선택
    SacriPut = 0
for i in range(len(SvGroup)):
    for k in range(len(SvGroup[i])):
        SacriPut += food_sacri[SvGroup[i][k]-1]
    if SacriPut == max(Sacri_List):
        Max_List = SvGroup[i]
        Max_Sacri = SacriPut
        break
    else:
        SacriPut = 0   


print(Sacri_List)
print(SvGroup)     
print(Max_List)
print(Max_Sacri)

while MaxCount != HMaccord:                  #세대 반복
    while len(SvGroup) != 36:
        A1 = rd.randrange(1, len(SvGroup))
        A2 = rd.randrange(1, len(SvGroup))
        while A1 == A2:
            A2 = rd.randrange(1, len(SvGroup))                    

        Sum_List = SvGroup[A1] + SvGroup[A2]       #번식, 자손
    
        Sum = 0

        while True:
            k = rd.randrange(1, len(Sum_List))
            InputNum = Sum_List[k]
            if(Sum+InputNum)<10:
                descendantGroup.append(Sum_List[k])
                Sum += Sum_List[k]
            if(Sum+InputNum)==10:
                descendantGroup.append(Sum_List[k])
                SvGroup.append(descendantGroup)
                descendantGroup = []
                Sum_List = []
                Sum = 0
                break     

    Sacri_List = []
    SacriPut = 0
    for i in range(36):
        for k in range(len(SvGroup[i])):
            SacriPut += food_sacri[SvGroup[i][k]-1]
        Sacri_List.append(SacriPut)
        SacriPut = 0           
   

    if max(Sacri_List) == Max_Sacri:
        MaxCount += 1
    if max(Sacri_List) > Max_Sacri:
        for i in range(len(SvGroup)):
            for k in range(len(SvGroup[i])):
                SacriPut += food_sacri[SvGroup[i][k]-1]
            if SacriPut == max(Sacri_List):
                Max_List = SvGroup[i]
                Max_Sacri = SacriPut
                SacriPut = 0
                break
            else:
                SacriPut = 0    

    Sacri_List.sort()
    SvPoint = Sacri_List[25]              #n차 자연선택

    for i in range(36):
        for k in range(len(SvGroup[i])):
            SacriPut += food_sacri[SvGroup[i][k]-1]
        if SacriPut >= SvPoint:
            Calculate_Group.append(SvGroup[i])
    SvGroup = Calculate_Group
    Calculate_Group = []


print(Sacri_List)
print(SvGroup)     
print(Max_List)
print(Max_Sacri)

    


