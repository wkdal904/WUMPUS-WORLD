import random
import turtle                      
t=turtle.Turtle()
t.hideturtle()

    
# 1. 웜푸스 구덩이 위치(0.15확률)
wumpus_list_x=[] #wumpus좌표리스트 생성
for i in range(16):
    wumpus_list_y=[]
    for j in range(2):
        wumpus_list_y.append(0)
    wumpus_list_x.append(wumpus_list_y)

pitch_list_x=[] #구덩이 좌표리스트 생성
for i in range(16):
    pitch_list_y=[]
    for j in range(2):
        pitch_list_y.append(0)
    pitch_list_x.append(pitch_list_y)

y_value=150
for j in range(0,16,4):
    x_value=-150
    for i in range(j,j+4,1):
              # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
        wumpus=[1,1,1,0,0,0,0,0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        pitch= [1,1,1,0,0,0,0,0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        wumpus_random_choice=random.choice(wumpus)
        pitch_random_choice=random.choice(pitch)
        
        if x_value==-150 and y_value==-150:  #[1,1] 제외
            x_value+=100
            continue

        
        if wumpus_random_choice==1 and pitch_random_choice!=1: # wumpus가 나타날 확률 15%
                                                 # pitch와 겹치면 안됨
                                         
            #골드의 위치와 중복을 피하기 위해 wumpus가 생성된 위치 좌표를 리스트에 저장한다.
            wumpus_list_x[i][0]=x_value
            wumpus_list_x[i][1]=y_value
            
        
                    
        if wumpus_random_choice!=1 and pitch_random_choice==1: # 구덩이가 나타날 확률 15%
                                         # wumpus와 겹치면 안됨
          
            #골드의 위치와 중복을 피하기 위해 구덩이가 생성된 위치 좌표를 리스트에 저장한다.
            pitch_list_x[i][0]=x_value
            pitch_list_x[i][1]=y_value    

        x_value+=100
    y_value-=100

            
print("wumpus 위치 데이더")##############################################
print("==")
print(wumpus_list_x)
print("")

print("구덩이 위치 데이더 : ")##############################################
print("==")
print(pitch_list_x)
print("")

# 2.구덩이와, wumpus의 주변 환경
stench_list_x=[] #breeze좌표리스트 생성
for i in range(16):
    stench_list_y=[]
    for j in range(2):
        stench_list_y.append(0)
    stench_list_x.append(stench_list_y)

breeze_list_x=[] #breeze좌표리스트 생성
for i in range(16):
    breeze_list_y=[]
    for j in range(2):
        breeze_list_y.append(0)
    breeze_list_x.append(breeze_list_y)


##wumpus가 위치한 좌표의 주변에 S(냄새)의 좌표를 저장한다.
def save_S_xy(x,y,num):
    if x+100<200:
            num_1=num+1
            stench_list_x[num_1][0]=x+100
            stench_list_x[num_1][1]=y

    if x-100>-200:
            num_2=num-1
            stench_list_x[num_2][0]=x-100
            stench_list_x[num_2][1]=y
       
    if y+100<200:
            num_3=num-4
            stench_list_x[num_3][0]=x
            stench_list_x[num_3][1]=y+100
   
    if y-100>-200:
            num_4=num+4
            stench_list_x[num_4][0]=x
            stench_list_x[num_4][1]=y-100
  
        
##구덩이가 위치한 좌표의 주변에 B(바람)의 좌표를 저장한다.
def save_B_xy(x,y,num):
    if x+100<200:
             num_1=num+1
             breeze_list_x[num_1][0]=x+100
             breeze_list_x[num_1][1]=y
        
    if x-100>-200:
            num_2=num-1
            breeze_list_x[num_2][0]=x-100
            breeze_list_x[num_2][1]=y
        
    if y+100<200:
            num_3=num-4
            breeze_list_x[num_3][0]=x
            breeze_list_x[num_3][1]=y+100
        
    if y-100>-200:
            num_4=num+4
            breeze_list_x[num_4][0]=x
            breeze_list_x[num_4][1]=y-100

##wumpus 리스트에 저장된 wumpus 위치를 탐색하고 wumpus가 존재하면 그 wumpus 주변에 냄새가 나게한다.        
if wumpus_list_x[0][0]==-150 and wumpus_list_x[0][1]==150:
    save_S_xy(wumpus_list_x[0][0],wumpus_list_x[0][1],0)
if wumpus_list_x[1][0]==-50 and wumpus_list_x[1][1]==150:
    save_S_xy(wumpus_list_x[1][0],wumpus_list_x[1][1],1)
if wumpus_list_x[2][0]==50 and wumpus_list_x[2][1]==150:
    save_S_xy(wumpus_list_x[2][0],wumpus_list_x[2][1],2)
if wumpus_list_x[3][0]==150 and wumpus_list_x[3][1]==150:
    save_S_xy(wumpus_list_x[3][0],wumpus_list_x[3][1],3)
    
if wumpus_list_x[4][0]==-150 and wumpus_list_x[4][1]==50:
    save_S_xy(wumpus_list_x[4][0],wumpus_list_x[4][1],4)
if wumpus_list_x[5][0]==-50 and wumpus_list_x[5][1]==50:
    save_S_xy(wumpus_list_x[5][0],wumpus_list_x[5][1],5)
if wumpus_list_x[6][0]==50 and wumpus_list_x[6][1]==50:
    save_S_xy(wumpus_list_x[6][0],wumpus_list_x[6][1],6)
if wumpus_list_x[7][0]==150 and wumpus_list_x[7][1]==50:
    save_S_xy(wumpus_list_x[7][0],wumpus_list_x[7][1],7)

if wumpus_list_x[8][0]==-150 and wumpus_list_x[8][1]==-50:
    save_S_xy(wumpus_list_x[8][0],wumpus_list_x[8][1],8)
if wumpus_list_x[9][0]==-50 and wumpus_list_x[9][1]==-50:
    save_S_xy(wumpus_list_x[9][0],wumpus_list_x[9][1],9)
if wumpus_list_x[10][0]==50 and wumpus_list_x[10][1]==-50:
    save_S_xy(wumpus_list_x[10][0],wumpus_list_x[10][1],10)
if wumpus_list_x[11][0]==150 and wumpus_list_x[11][1]==-50:
    save_S_xy(wumpus_list_x[11][0], wumpus_list_x[11][1],11)
    
if wumpus_list_x[12][0]==-150 and wumpus_list_x[12][1]==-150:
    save_S_xy(wumpus_list_x[12][0],wumpus_list_x[12][1],12)
if wumpus_list_x[13][0]==-50 and wumpus_list_x[13][1]==-150:
    save_S_xy(wumpus_list_x[13][0],wumpus_list_x[13][1],13)
if wumpus_list_x[14][0]==50 and wumpus_list_x[14][1]==-150:
    save_S_xy(wumpus_list_x[14][0],wumpus_list_x[14][1],14)
if wumpus_list_x[15][0]==150 and wumpus_list_x[15][1]==-150:
    save_S_xy(wumpus_list_x[15][0],wumpus_list_x[15][1],15)


##구덩이 리스트에 저장된 구덩이 위치를 탐색하고 구덩이가 존재하면 그 구덩이 주변에 바람이 불게한다.
if pitch_list_x[0][0]==-150 and pitch_list_x[0][1]==150:
    save_B_xy(pitch_list_x[0][0],pitch_list_x[0][1],0)
if pitch_list_x[1][0]==-50 and pitch_list_x[1][1]==150:
    save_B_xy(pitch_list_x[1][0], pitch_list_x[1][1],1)
if pitch_list_x[2][0]==50 and pitch_list_x[2][1]==150:
    save_B_xy(pitch_list_x[2][0],pitch_list_x[2][1],2)
if pitch_list_x[3][0]==150 and pitch_list_x[3][1]==150:
    save_B_xy(pitch_list_x[3][0],pitch_list_x[3][1],3)
    
if pitch_list_x[4][0]==-150 and pitch_list_x[4][1]==50:
    save_B_xy(pitch_list_x[4][0],pitch_list_x[4][1],4)
if pitch_list_x[5][0]==-50 and pitch_list_x[5][1]==50:
    save_B_xy(pitch_list_x[5][0],pitch_list_x[5][1],5)
if pitch_list_x[6][0]==50 and pitch_list_x[6][1]==50:
    save_B_xy(pitch_list_x[6][0],pitch_list_x[6][1],6)
if pitch_list_x[7][0]==150 and pitch_list_x[7][1]==50:
    save_B_xy(pitch_list_x[7][0],pitch_list_x[7][1],7)

if pitch_list_x[8][0]==-150 and pitch_list_x[8][1]==-50:
    save_B_xy(pitch_list_x[8][0],pitch_list_x[8][1],8)
if pitch_list_x[9][0]==-50 and pitch_list_x[9][1]==-50:
    save_B_xy(pitch_list_x[9][0],pitch_list_x[9][1],9)
if pitch_list_x[10][0]==50 and pitch_list_x[10][1]==-50:
    save_B_xy(pitch_list_x[10][0],pitch_list_x[10][1],10)
if pitch_list_x[11][0]==150 and pitch_list_x[11][1]==-50:
    save_B_xy(pitch_list_x[11][0],pitch_list_x[11][1],11)
    
if pitch_list_x[12][0]==-150 and pitch_list_x[12][1]==-150:
    save_B_xy(pitch_list_x[12][0],pitch_list_x[12][1],12)
if pitch_list_x[13][0]==-50 and pitch_list_x[13][1]==-150:
    save_B_xy(pitch_list_x[13][0],pitch_list_x[13][1],13)
if pitch_list_x[14][0]==50 and pitch_list_x[14][1]==-150:
    save_B_xy(pitch_list_x[14][0],pitch_list_x[14][1],14)
if pitch_list_x[15][0]==150 and pitch_list_x[15][1]==-150:
    save_B_xy(pitch_list_x[15][0],pitch_list_x[15][1],15)


print("냄새 위치 데이더 ")##############################################
print("==")
print(stench_list_x)
print("")

print("바람 위치 데이터  ")##############################################
print("==")
print(breeze_list_x)
print("")

# 3. 골드의 위치
#골드는 무조건 한개가 나타나야한다.

gold_list_x=[] #gold의 좌표리스트 생성
for i in range(16):
    gold_list_y=[]
    for j in range(2):
        gold_list_y.append(0)
    gold_list_x.append(gold_list_y)

while gold_list_x==[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]: #골드가 나올때까지 무한 반복한다.
    gold=random.randint(0,14) #15개 칸중에 1개를 랜덤으로 축출
    print(gold)
    y_value=150
    for j in range(0,16,4):
        x_value=-150
        for i in range(j,j+4,1):
                if x_value==-150 and y_value==150 and wumpus_list_x[0][0]!=-150 and wumpus_list_x[0][1]!=150 and pitch_list_x[0][0]!=-150 and pitch_list_x[0][1]!=150: #wumpus리스트의 좌표와 , 웅덩이리스트에 존재하는  좌표를 현재 위치 좌표와 비교한다.
                    if gold==0:
                     #골드와 바람, 냄새의 중복을 피하기 위해 골드의 위치를 저장해놓는다.
                        gold_list_x[gold][0]=x_value
                        gold_list_x[gold][1]=y_value
                                
                if x_value==-50 and y_value==150 and wumpus_list_x[1][0]!=-50 and wumpus_list_x[1][1]!=150 and pitch_list_x[1][0]!=-50 and pitch_list_x[1][1]!=150: #wumpus리스트의 좌표와 , 웅덩이리스트에 존재하는  좌표를 현재 위치 좌표와 비교한다.
                    if gold==1:
                        gold_list_x[gold][0]=x_value
                        gold_list_x[gold][1]=y_value
                                
                if x_value==50 and y_value==150 and wumpus_list_x[2][0]!=50 and wumpus_list_x[2][1]!=150 and pitch_list_x[2][0]!=-50 and pitch_list_x[2][1]!=150:#wumpus리스트의 좌표와 , 웅덩이리스트에 존재하는  좌표를 현재 위치 좌표와 비교한다.
                    if gold==2:
                        gold_list_x[gold][0]=x_value
                        gold_list_x[gold][1]=y_value
                if x_value==150 and y_value==150 and wumpus_list_x[3][0]!=150 and wumpus_list_x[3][1]!=150 and pitch_list_x[3][0]!=150 and pitch_list_x[3][1]!=150:#wumpus리스트의 좌표와 , 웅덩이리스트에 존재하는  좌표를 현재 위치 좌표와 비교한다.
                    if gold==3:
                        gold_list_x[gold][0]=x_value
                        gold_list_x[gold][1]=y_value
                                
                #######################          
                if x_value==-150 and y_value==50 and wumpus_list_x[4][0]!=-150 and wumpus_list_x[4][1]!=50 and pitch_list_x[4][0]!=-150 and pitch_list_x[4][1]!=50:#wumpus리스트의 좌표와 , 웅덩이리스트에 존재하는  좌표를 현재 위치 좌표와 비교한다.
                    if gold==4:
                        gold_list_x[gold][0]=x_value
                        gold_list_x[gold][1]=y_value
                                
                if x_value==-50 and y_value==50 and wumpus_list_x[5][0]!=-50 and wumpus_list_x[5][1]!=50 and pitch_list_x[5][0]!=-50 and pitch_list_x[5][1]!=50:#wumpus리스트의 좌표와 , 웅덩이리스트에 존재하는  좌표를 현재 위치 좌표와 비교한다.
                    if gold==5:
                        gold_list_x[gold][0]=x_value
                        gold_list_x[gold][1]=y_value
                                
                if x_value==50 and y_value==50 and wumpus_list_x[6][0]!=50 and wumpus_list_x[6][1]!=50 and pitch_list_x[6][0]!=50 and pitch_list_x[6][1]!=50: #wumpus리스트의 좌표와 , 웅덩이리스트에 존재하는  좌표를 현재 위치 좌표와 비교한다.
                    if gold==6:
                        gold_list_x[gold][0]=x_value
                        gold_list_x[gold][1]=y_value
                                
                if x_value==150 and y_value==50 and wumpus_list_x[7][0]!=150 and wumpus_list_x[7][1]!=50 and pitch_list_x[4][0]!=150 and pitch_list_x[7][1]!=50: #wumpus리스트의 좌표와 , 웅덩이리스트에 존재하는  좌표를 현재 위치 좌표와 비교한다.
                    if gold==7:
                        gold_list_x[gold][0]=x_value
                        gold_list_x[gold][1]=y_value
                ####################### 
                if x_value==-150 and y_value==-50 and wumpus_list_x[8][0]!=-150 and wumpus_list_x[8][1]!=-50 and pitch_list_x[8][0]!=-150 and pitch_list_x[8][1]!=-50: #wumpus리스트의 좌표와 , 웅덩이리스트에 존재하는  좌표를 현재 위치 좌표와 비교한다.
                    if gold==8:
                        gold_list_x[gold][0]=x_value
                        gold_list_x[gold][1]=y_value
                        
                if x_value==-50 and y_value==-50 and wumpus_list_x[9][0]!=-50 and wumpus_list_x[9][1]!=-50 and pitch_list_x[9][0]!=-50 and pitch_list_x[9][1]!=-50: #wumpus리스트의 좌표와 , 웅덩이리스트에 존재하는  좌표를 현재 위치 좌표와 비교한다.:
                    if gold==9: 
                        gold_list_x[gold][0]=x_value
                        gold_list_x[gold][1]=y_value
                        
                if x_value==50 and y_value==-50 and wumpus_list_x[10][0]!=50 and wumpus_list_x[10][1]!=-50 and pitch_list_x[10][0]!=50 and pitch_list_x[10][1]!=-50: #wumpus리스트의 좌표와 , 웅덩이리스트에 존재하는  좌표를 현재 위치 좌표와 비교한다.
                    if gold==10:
                        gold_list_x[gold][0]=x_value
                        gold_list_x[gold][1]=y_value
                        
                if x_value==150 and y_value==-50 and wumpus_list_x[11][0]!=150 and wumpus_list_x[11][1]!=-50 and pitch_list_x[11][0]!=150 and pitch_list_x[11][1]!=-50: #wumpus리스트의 좌표와 , 웅덩이리스트에 존재하는  좌표를 현재 위치 좌표와 비교한다.
                    if gold==11:
                        gold_list_x[gold][0]=x_value
                        gold_list_x[gold][1]=y_value
                #######################
                #################################################### 
                # x2=-150, y2=-150(12자리) -> [1,1]이므로 제외한다.#
                ####################################################

                if x_value==-50 and y_value==-150 and wumpus_list_x[13][0]!=-50 and wumpus_list_x[13][1]!=-150 and pitch_list_x[13][0]!=-50 and pitch_list_x[13][1]!=-150: #wumpus리스트의 좌표와 , 웅덩이리스트에 존재하는  좌표를 현재 위치 좌표와 비교한다.
                    if gold==12: # ==13칸
                        gold_1=gold+1 #12자리를 제외하였으므로 13자리에 데이터를 저장하기위해+1을 해준다
                        gold_list_x[gold_1][0]=x_value
                        gold_list_x[gold_1][1]=y_value
                                
                if x_value==50 and y_value==-150 and wumpus_list_x[14][0]!=50 and wumpus_list_x[14][1]!=-150 and pitch_list_x[14][0]!=50 and pitch_list_x[14][1]!=-150: #wumpus리스트의 좌표와 , 웅덩이리스트에 존재하는  좌표를 현재 위치 좌표와 비교한다.
                    if gold==13: # ==14칸
                        gold_2=gold+1 #12자리를 제외하였으므로 14자리에 데이터를 저장하기위해 +1을 해준다
                        gold_list_x[gold_2][0]=x_value
                        gold_list_x[gold_2][1]=y_value
                                
                if x_value==150 and y_value==-150 and wumpus_list_x[15][0]!=150 and wumpus_list_x[15][1]!=-150 and pitch_list_x[15][0]!=150 and pitch_list_x[15][1]!=-150: #wumpus리스트의 좌표와 , 웅덩이리스트에 존재하는  좌표를 현재 위치 좌표와 비교한다.
                     if gold==14: # ==15칸
                         gold_3=gold+1 #12자리를 제외하였으므로 15자리에 데이터를 저장하기위해 +1을 해준다.
                         gold_list_x[gold_3][0]=x_value
                         gold_list_x[gold_3][1]=y_value
                
                x_value+=100
        y_value-=100             
    print("골드 위치 데이더")##############################################
    print("==")
    print(gold_list_x)
    print("")


#4. 벽의 위치
bump_list_x=[] #bump좌표리스트 생성
for i in range(16):
    bump_list_y=[]
    for j in range(2):
        bump_list_y.append(0)
    bump_list_x.append(bump_list_y)


def save_bump_xy(x, y, num):
    if x + 100 > 200:
        t.penup()
        t.goto(x + 100, y)
        t.write("bump")

    if x - 100 < -200:
        t.penup()
        t.goto(x - 100, y)
        t.write("bump")

    if y + 100 > 200:
        t.penup()
        t.goto(x, y + 100)
        t.write("bump")

    if y - 100 < -200:
        t.penup()
        t.goto(x, y - 100)
        t.write("bump")


y_value = 150
for j in range(0, 13, 4):
    x_value = -150
    for i in range(j, j + 4, 1):
        if (x_value == -50 and y_value == 50) or (x_value == 50 and y_value == 50) or (
                x_value == -50 and y_value == -50) or (x_value == 50 and y_value == -50):
            x_value += 100
            continue
        bump_list_x[i][0] = x_value
        bump_list_x[i][1] = y_value
        x_value += 100
    y_value -= 100

if bump_list_x[0][0] == -150 and bump_list_x[0][1] == 150:
    save_bump_xy(bump_list_x[0][0], bump_list_x[0][1], 0)
if bump_list_x[1][0] == -50 and bump_list_x[1][1] == 150:
    save_bump_xy(bump_list_x[1][0], bump_list_x[1][1], 1)
if bump_list_x[2][0] == 50 and bump_list_x[2][1] == 150:
    save_bump_xy(bump_list_x[2][0], bump_list_x[2][1], 2)

if bump_list_x[3][0] == 150 and bump_list_x[3][1] == 150:
    save_bump_xy(bump_list_x[3][0], bump_list_x[3][1], 3)

##
if bump_list_x[4][0] == -150 and bump_list_x[4][1] == 50:
    save_bump_xy(bump_list_x[4][0], bump_list_x[4][1], 4)
if bump_list_x[7][0] == 150 and bump_list_x[7][1] == 50:
    save_bump_xy(bump_list_x[7][0], bump_list_x[7][1], 7)

if bump_list_x[8][0] == -150 and bump_list_x[8][1] == -50:
    save_bump_xy(bump_list_x[8][0], bump_list_x[8][1], 8)
if bump_list_x[11][0] == 150 and bump_list_x[11][1] == -50:
    save_bump_xy(bump_list_x[11][0], bump_list_x[11][1], 11)
##

if bump_list_x[12][0] == -150 and bump_list_x[12][1] == -150:
    save_bump_xy(bump_list_x[12][0], bump_list_x[12][1], 12)

if bump_list_x[13][0] == -50 and bump_list_x[13][1] == -150:
    save_bump_xy(bump_list_x[13][0], bump_list_x[13][1], 13)
if bump_list_x[14][0] == 50 and bump_list_x[14][1] == -150:
    save_bump_xy(bump_list_x[14][0], bump_list_x[14][1], 14)

if bump_list_x[15][0] == 150 and bump_list_x[15][1] == -150:
    save_bump_xy(bump_list_x[15][0], bump_list_x[15][1], 15)

print("벽이 있는 칸 위치 데이더")##############################################
print("==")
print(bump_list_x)
print("")

#5. 골드(반짝임),Wumpus,구덩이,냄새,바람위치를 출력한다.
y_value=150
for j in range(0,16,4):
    x_value=-150
    for i in range(j,j+4,1):   
        #골드와 냄새,바람위치 중복 출력(골드, Wumpus, 구덩이는 사전에 중복되지 않게 설계함)
        if gold_list_x[i][0]==stench_list_x[i][0]== breeze_list_x[i][0]==x_value and gold_list_x[i][1]==stench_list_x[i][1]== breeze_list_x[i][1]==y_value:
            t.penup()
            t.goto(x_value,y_value)
            t.pendown()
            t.write("[G(Glitter)],\n S,B")
            
        
        #골드위치와 냄새위치 중복 출력 (골드, Wumpus, 구덩이는 사전에 중복되지 않게 설계함) 
        elif gold_list_x[i][0]==stench_list_x[i][0]==x_value and gold_list_x[i][1]==stench_list_x[i][1]==y_value:
            t.penup()
            t.goto(x_value,y_value)
            t.pendown()
            t.write("[G(Glitter)],\n S")
        #골드와 냄새위치 중 출력 (골드, Wumpus, 구덩이는 사전에 중복되지 않게 설계함)
        elif gold_list_x[i][0]== breeze_list_x[i][0]==x_value and gold_list_x[i][1]== breeze_list_x[i][1]==y_value:
            t.penup()
            t.goto(x_value,y_value)
            t.pendown()
            t.write("[G(Glitter)],\n B")

        #구덩이와 냄새위치 중복 출력 (구덩이는 바람과 사전에 중복되지 않게 설계함)
        elif stench_list_x[i][0]==pitch_list_x[i][0]==x_value and stench_list_x[i][1]==pitch_list_x[i][1]==y_value:
            t.penup()
            t.goto(x_value,y_value)
            t.pendown()
            t.write("[P],S")
        #Wumpus와 바람위치 중복 출력 (Wumpus은 냄새와 사전에 중복되지 않게 설계함)
        elif breeze_list_x[i][0]==wumpus_list_x[i][0]==x_value and  breeze_list_x[i][1]==wumpus_list_x[i][1]==y_value:
            t.penup()
            t.goto(x_value,y_value)
            t.pendown()
            t.write("[W],B")

        # 냄새와 바람위치 중복 출력 (Wumpus은 냄새와 , 구덩이는 바람과 사전에 중복되지 않게 설계함)
        elif stench_list_x[i][0] == breeze_list_x[i][0] == x_value and stench_list_x[i][1] == breeze_list_x[i][1] == y_value:
            t.penup()
            t.goto(x_value, y_value)
            t.pendown()
            t.write("S,B")

        #금위치 출력
        elif gold_list_x[i][0]==x_value and gold_list_x[i][1]==y_value:
            t.penup()
            t.goto(x_value,y_value)
            t.pendown()
            t.write("[G(Glitter)]")
        #Wumpus 위치 출력
        elif wumpus_list_x[i][0]==x_value and wumpus_list_x[i][1]==y_value:
            t.penup()
            t.goto(x_value,y_value)
            t.pendown()
            t.write("[W]")
        #구덩이 위치 출력
        elif pitch_list_x[i][0]==x_value and pitch_list_x[i][1]==y_value:
            t.penup()
            t.goto(x_value,y_value)
            t.pendown()
            t.write("[P]")

            
        #바람위치 출력
        elif breeze_list_x[i][0]==x_value and  breeze_list_x[i][1]==y_value:
            t.penup()
            t.goto(x_value,y_value)
            t.pendown()
            t.write("B")
        #냄새위치 출력
        elif stench_list_x[i][0]==x_value and stench_list_x[i][1]==y_value:
            t.penup()
            t.goto(x_value,y_value)
            t.pendown()
            t.write("S")
        
        
        
        x_value+=100
    y_value-=100





































        























            







