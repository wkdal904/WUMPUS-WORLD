#에이전트 모양

import turtle
import WorldRandom

t=turtle.Turtle()
s=turtle.Screen()

t.penup()
t.goto(-150,-150)
t.pendown()

########################
WorldRandom.wumpus_list_x
WorldRandom.pitch_list_x
WorldRandom.gold_list_x
WorldRandom.breeze_list_x
WorldRandom.stench_list_x
WorldRandom.bump_list_x
########################

visit_list_x=[] #방문한 곳 리스트
for i in range(16):
    visit_list_y=[]
    for j in range(2):
        visit_list_y.append(0)
    visit_list_x.append(visit_list_y)

visit_sequence=[]# 방문한 위치를 순서대로 리스트에 저장한다.

init_x_value=-150 #초기 x좌표값
init_y_value=-150 #초기 y좌표값
init_num=12 # 초기 칸값
init_arrow=3 # 초기 화살 갯수
init_point=0 #포인트 값을 0으로 초기화

visit_list_x[init_num][0]=init_x_value
visit_list_x[init_num][1]=init_y_value
visit_sequence.append([init_x_value,init_y_value])

x_value=init_x_value # 초기 x좌표값을 x값에 넣는다.
y_value=init_y_value # 초기 y좌표값을 y값에 넣는다.
num=init_num # 초기 칸값을 num값에 넣는다.
arrow=init_arrow # 초기 화살 갯수를 arrow를 넣는다.
point=init_point #포인트 값을 point를 넣는다.

print()
print("=====다 시 확 인=====")

print()
print("wumpus 리스트")
print(WorldRandom.wumpus_list_x) #wumpus 리스트를 다시한번 확인한다.


print()
print("구덩이 리스트")
print(WorldRandom.pitch_list_x) #pitch 리스트를 다시한번 확인한다.

print("===================")

while True:
    #초기에 모든 길이 구덩이에 막혀있을 때
    if (WorldRandom.pitch_list_x[8][0]==-150 and WorldRandom.pitch_list_x[8][1]==-50) and (WorldRandom.pitch_list_x[13][0]==-50 and WorldRandom.pitch_list_x[13][1]==-150):
        t.write("모든 길이 구덩이로 막혀있음")
        break

    # 1. 현재 위치에 금이 있을 때/ 금은 현재 위치에서만 percept가 가능하기 때문에 현재 위치에서만 발견이 가능하다.
    elif  WorldRandom.gold_list_x[num][0]==x_value and WorldRandom.gold_list_x[num][1]==y_value: #현재 위치와 황금의 위치와 같으면 멈춘다.

        t.write("=====\n")
        t.write("=====")
        point+=10000
        print("현재 포인트 : %d\n"%point)
        print()

        while visit_sequence!=[]:
            x_value=visit_sequence[len(visit_sequence)-1][0]
            y_value=visit_sequence[len(visit_sequence)-1][1]

            print("금을 찾고 한 칸 돌아가기 전")
            print(visit_sequence)
            print()
            if x_value==-150 and y_value==-150:
                visit_sequence.pop()
            elif x_value + 100 == visit_sequence[(len(visit_sequence) - 1) - 1][0] and \
                    y_value == visit_sequence[(len(visit_sequence) - 1) - 1][1]:
                t.seth(0)
                t.goto(visit_sequence[(len(visit_sequence) - 1) - 1][0],visit_sequence[(len(visit_sequence) - 1) - 1][1])
                visit_sequence.pop()  # 마지막으로 이동했던 위치를 리스트에서 삭제한다.

            elif x_value - 100 == visit_sequence[(len(visit_sequence) - 1) - 1][0] and \
                    y_value == visit_sequence[(len(visit_sequence) - 1) - 1][1]:
                t.seth(180)
                t.goto(visit_sequence[(len(visit_sequence) - 1) - 1][0],
                       visit_sequence[(len(visit_sequence) - 1) - 1][1])
                visit_sequence.pop()

            elif x_value == visit_sequence[(len(visit_sequence) - 1) - 1][0] and \
                    y_value+ 100 == visit_sequence[(len(visit_sequence) - 1) - 1][1] :
                t.seth(90)
                t.goto(visit_sequence[(len(visit_sequence) - 1) - 1][0],
                       visit_sequence[(len(visit_sequence) - 1) - 1][1])
                visit_sequence.pop()

            elif x_value == visit_sequence[(len(visit_sequence) - 1) - 1][0] and \
                    y_value- 100 == visit_sequence[(len(visit_sequence) - 1) - 1][1] :
                t.seth(270)
                t.goto(visit_sequence[(len(visit_sequence) - 1) - 1][0],
                       visit_sequence[(len(visit_sequence) - 1) - 1][1])
                visit_sequence.pop()

            print("금을 찾고 한 칸 돌아간 후")
            print(visit_sequence)
            print()

        t.seth(270)
        t.goto(-150, -300)
        t.write("Climb\n")
        print("\n")

        t.stamp()

        t.hideturtle()
        t.penup()
        t.goto(0,-300)
        t.write("최종 포인트 : %d"%point,font=(10))
        print("최종 포인트 : %d\n" % point)

        break

    # 2. wumpus, 구덩이 피하기

    elif x_value + 100 < 200 and num + 1 <= 15 and visit_list_x[num + 1][0] != x_value + 100 and visit_list_x[num + 1][1] != y_value and WorldRandom.wumpus_list_x[num + 1][0] != x_value + 100 and WorldRandom.wumpus_list_x[num + 1][1] != y_value and WorldRandom.pitch_list_x[num + 1][0] != x_value + 100 and WorldRandom.pitch_list_x[num + 1][1] != y_value:
            # x,y값의 범위와 리스트의 범위를 넘어가지 않게 한다. / 이전에 방문했던적이 있는지 확인한다.
            # wumpus가 존재하지않고 구덩이가 존재하지 않으면 움직인다. 오른쪽으로 한 칸 움직임
        t.seth(0)
        t.goto(x_value + 100, y_value)  # 움직임을 출력한다.
        point -= 100
        print("현재 포인트 : %d\n" % point)
        print()

        visit_list_x[num + 1][0] = x_value + 100  # 나중에 방문했던적 있는 위치의 중복을 피하기 위해 이동한 위치를 방문리스트에 저장한다.(x 좌표값)
        visit_list_x[num + 1][1] = y_value  # 나중에 방문했던적 있는 위치의 중복을 피하기 위해 이동한 위치를 방문리스트에 저장한다.(y 좌표값)
        visit_sequence.append([x_value + 100, y_value])

        x_value = x_value + 100  # 움직인 좌표값을 반영한다.(x_value+100)
        num = num + 1  # 움직인 좌표값을 반영하다.(num+1)

        print()
        print("에이전트의 방문기록=")
        print(visit_list_x)
        print()

    elif x_value - 100 > -200 and num - 1 >= 0 and visit_list_x[num - 1][0] != x_value - 100 and visit_list_x[num - 1][1] != y_value and WorldRandom.wumpus_list_x[num - 1][0] != x_value - 100 and WorldRandom.wumpus_list_x[num - 1][1] != y_value and WorldRandom.pitch_list_x[num - 1][0] != x_value - 100 and WorldRandom.pitch_list_x[num - 1][1] != y_value:
        # wumpus가 존재하지않고 구덩이가 존재하지 않으면 움직인다. 왼쪽으로 한 칸 움직임
        t.seth(180)
        t.goto(x_value - 100, y_value)
        point-=100
        print("현재 포인트 : %d\n" % point)
        print()

        visit_list_x[num - 1][0] = x_value - 100
        visit_list_x[num - 1][1] = y_value
        visit_sequence.append([x_value - 100, y_value])

        x_value = x_value - 100  # 움직인 좌표값을 반영한다.(x_value-100)
        num = num - 1  # 움직인 좌표값을 반영하다.(num-1)

        print()
        print("에이전트의 방문기록=")
        print(visit_list_x)
        print()

    elif y_value + 100 < 200 and num - 4 >= 0 and visit_list_x[num - 4][0] != x_value and visit_list_x[num - 4][1] != y_value + 100 and WorldRandom.wumpus_list_x[num - 4][0] != x_value and WorldRandom.wumpus_list_x[num - 4][1] != y_value + 100 and WorldRandom.pitch_list_x[num - 4][0] != x_value and WorldRandom.pitch_list_x[num - 4][1] != y_value + 100:
        # wumpus가 존재하지않고 구덩이가 존재하지 않으면 움직인다. 위로 한 칸 움직임
        t.seth(90)
        t.goto(x_value, y_value + 100)
        point -= 100
        print("현재 포인트 : %d\n" % point)
        print()

        visit_list_x[num - 4][0] = x_value
        visit_list_x[num - 4][1] = y_value + 100
        visit_sequence.append([x_value, y_value + 100])

        y_value = y_value + 100  # 움직인 좌표값을 반영한다.(y_value+100)
        num = num - 4  # 움직인 좌표값을 반영하다.(num-4)

        print()
        print("에이전트의 방문기록=")
        print(visit_list_x)
        print()

    elif y_value - 100 > -200 and num + 4 <= 15 and visit_list_x[num + 4][0] != x_value and visit_list_x[num + 4][1] != y_value - 100 and WorldRandom.wumpus_list_x[num + 4][0] != x_value and WorldRandom.wumpus_list_x[num + 4][1] != y_value - 100 and WorldRandom.pitch_list_x[num + 4][0] != x_value and WorldRandom.pitch_list_x[num + 4][1] != y_value - 100:
        # wumpus가 존재하지않고 구덩이가 존재하지 않으면 움직인다. 아래로 한 칸 움직임
        t.seth(270)
        t.goto(x_value, y_value - 100)
        point -= 100
        print("현재 포인트 : %d\n" % point)
        print()

        visit_list_x[num + 4][0] = x_value
        visit_list_x[num + 4][1] = y_value - 100
        visit_sequence.append([x_value, y_value - 100])

        y_value = y_value - 100  # 움직인 좌표값을 반영한다.(y_value-100)
        num = num + 4  # 움직인 좌표값을 반영하다.(num+4)

        print()
        print("에이전트의 방문기록=")
        print(visit_list_x)
        print()

    # 3. wumpus를 만났을 때  죽이기(화살이 있을 때)
    elif arrow!=0 and (x_value+100<200 and num+1<=150) and (visit_list_x[num+1][0]!=x_value+100 and visit_list_x[num+1][1]!=y_value) and (WorldRandom.wumpus_list_x[num+1][0]==x_value+100  and WorldRandom.wumpus_list_x[num+1][1]==y_value) and (WorldRandom.pitch_list_x[num+1][0]!=x_value+100 and WorldRandom.pitch_list_x[num+1][1]!=y_value):

            print()
            print("wumpus를 제거하기 전 wumpus리스트==")
            print(WorldRandom.wumpus_list_x)

            t.seth(0)

            t.penup()
            t.hideturtle()
            t.goto(x_value+100, y_value)
            x_value=x_value+100
            t.write("=====\n")
            t.write("=====")
            point -= 500
            print("현재 포인트 : %d\n" % point)
            print()

            t.goto(x_value-100, y_value)
            x_value=x_value-100
            t.showturtle()
            t.pendown()

            WorldRandom.wumpus_list_x[num+1][0]=0
            WorldRandom.wumpus_list_x[num+1][1]=0

            print()
            print()
            print("wumpus를 제거 후 wumpus리스트==")
            print(WorldRandom.wumpus_list_x)

            t.goto(x_value + 100, y_value)
            visit_list_x[num + 1][0] = x_value + 100
            visit_list_x[num + 1][1] = y_value
            visit_sequence.append([x_value + 100, y_value])

            x_value=x_value+100
            num=num+1
            arrow-=1
            
            print("남은 화살 갯수 : %d"%arrow)

    elif arrow!=0 and (x_value-100>-200 and num-1>=0) and (visit_list_x[num-1][0]!=x_value-100 and visit_list_x[num-1][1]!=y_value) and (WorldRandom.wumpus_list_x[num-1][0]==x_value-100  and WorldRandom.wumpus_list_x[num-1][1]==y_value) and (WorldRandom.pitch_list_x[num-1][0]!=x_value-100 and WorldRandom.pitch_list_x[num-1][1]!=y_value):

            print()
            print("wumpus를 제거하기 전 wumpus리스트==")
            print(WorldRandom.wumpus_list_x)

            t.seth(180)

            t.penup()
            t.hideturtle()
            t.goto(x_value-100, y_value)
            x_value=x_value-100
            t.write("=====\n")
            t.write("=====")
            point -= 500
            print("현재 포인트 : %d\n" % point)
            print()

            t.goto(x_value+100, y_value)
            x_value=x_value+100
            t.showturtle()
            t.pendown()

            WorldRandom.wumpus_list_x[num-1][0]=0
            WorldRandom.wumpus_list_x[num-1][1]=0

            print()
            print("wumpus를 제거 후 wumpus리스트==")
            print(WorldRandom.wumpus_list_x)

            t.goto(x_value - 100, y_value)
            visit_list_x[num - 1][0] = x_value - 100
            visit_list_x[num - 1][1] = y_value
            visit_sequence.append([x_value - 100, y_value])

            x_value=x_value-100
            num=num-1
            arrow-=1
                        
            print("남은 화살 갯수 : %d"%arrow)
            
    elif  arrow!=0 and (y_value+100<200 and num-4>=0) and (visit_list_x[num-4][0]!=x_value and visit_list_x[num-4][1]!=y_value+100) and (WorldRandom.wumpus_list_x[num-4][0]==x_value and WorldRandom.wumpus_list_x[num-4][1]==y_value+100) and (WorldRandom.pitch_list_x[num-4][0]!=x_value and WorldRandom.pitch_list_x[num-4][1]!=y_value+100):

            print()
            print("wumpus를 제거하기 전 wumpus리스트==")
            print(WorldRandom.wumpus_list_x)

            t.seth(90)

            t.penup()
            t.hideturtle()
            t.goto(x_value, y_value + 100)
            y_value=y_value+100
            t.write("=====\n")
            t.write("=====")
            point -= 500
            print("현재 포인트 : %d\n" % point)
            print()

            t.goto(x_value, y_value - 100)
            y_value=y_value-100
            t.showturtle()
            t.pendown()

            WorldRandom.wumpus_list_x[num-4][0]=0
            WorldRandom.wumpus_list_x[num-4][1]=0

            print()
            print("wumpus를 제거 후 wumpus리스트==")
            print(WorldRandom.wumpus_list_x)

            t.goto(x_value, y_value + 100)
            visit_list_x[num - 4][0] = x_value
            visit_list_x[num - 4][1] = y_value + 100
            visit_sequence.append([x_value, y_value + 100])

            y_value=y_value+100
            num=num-4
            arrow-=1
                        
            print("남은 화살 갯수 : %d"%arrow)

    elif  arrow!=0 and (y_value-100>-200 and num+4<=15) and (visit_list_x[num+4][0]!=x_value and visit_list_x[num+4][1]!=y_value-100) and (WorldRandom.wumpus_list_x[num+4][0]==x_value  and WorldRandom.wumpus_list_x[num+4][1]==y_value-100) and (WorldRandom.pitch_list_x[num+4][0]!=x_value and WorldRandom.pitch_list_x[num+4][1]!=y_value-100):

            print()
            print("wumpus를 제거하기 전 wumpus리스트==")
            print(WorldRandom.wumpus_list_x)

            t.seth(270)

            t.penup()
            t.hideturtle()
            t.goto(x_value,y_value-100)
            y_value-100
            t.write("=====\n")
            t.write("=====")
            point -= 500
            print("현재 포인트 : %d\n" % point)
            print()

            t.goto(x_value,y_value+100)
            y_value+100
            t.showturtle()
            t.pendown()

            WorldRandom.wumpus_list_x[num+4][0]=0
            WorldRandom.wumpus_list_x[num+4][1]=0

            print()
            print("wumpus를 제거 후 wumpus리스트==")
            print(WorldRandom.wumpus_list_x)

            t.goto(x_value, y_value - 100)
            visit_list_x[num + 4][0] = x_value
            visit_list_x[num + 4][1] = y_value - 100
            visit_sequence.append([x_value, y_value - 100])

            y_value=y_value-100
            num=num+4
            arrow-=1
                        
            print("남은 화살 갯수 : %d"%arrow)


    # 4.길이 막혔을 때
    elif (visit_sequence[len(visit_sequence)-1][0]==x_value and visit_sequence[len(visit_sequence)-1][1]==y_value):#  현재 위치가 순차 리스트에 존재 하는 확인한다. /주변에 wumpus와 구덩이가 없는지 확인한다/주변에 벽이 있는지 확인한다.
                print("장애물로 인한 왔던 길로 한 칸 돌아기기 전 에이전트 방문기록=")
                print(visit_sequence)
                print()

                t.goto(visit_sequence[(len(visit_sequence) - 1) - 1][0],
                       visit_sequence[(len(visit_sequence) - 1) - 1][1])
                point -= 100
                print("현재 포인트 : %d\n" % point)
                print()

                if visit_sequence[len(visit_sequence) - 1][0] + 100 == visit_sequence[(len(visit_sequence) - 1) - 1][0] and \
                        visit_sequence[len(visit_sequence) - 1][1] == visit_sequence[(len(visit_sequence) - 1) - 1][1]:
                    t.seth(0)
                    num = num + 1  # 되돌아간 칸값을 반영하다.(num+1)

                elif visit_sequence[len(visit_sequence) - 1][0] - 100 == visit_sequence[(len(visit_sequence) - 1) - 1][0] and \
                        visit_sequence[len(visit_sequence) - 1][1] == visit_sequence[(len(visit_sequence) - 1) - 1][1]:
                    t.seth(90)
                    num = num - 1  # 되돌아간 칸값을 반영하다.(num-1)

                elif visit_sequence[len(visit_sequence) - 1][0] == visit_sequence[(len(visit_sequence) - 1) - 1][0] and \
                        visit_sequence[len(visit_sequence) - 1][1] + 100 == visit_sequence[(len(visit_sequence) - 1) - 1][1]:
                    t.seth(180)
                    num = num - 4  # 되돌아간 칸값을 반영하다.(num-4)

                elif visit_sequence[len(visit_sequence) - 1][0] == visit_sequence[(len(visit_sequence) - 1) - 1][0] and \
                        visit_sequence[len(visit_sequence) - 1][1]- 100 == visit_sequence[(len(visit_sequence) - 1) - 1][1] :
                    t.seth(270)
                    num = num + 4  # 되돌아간 칸값을 반영하다.(num+4)

                x_value = visit_sequence[(len(visit_sequence) - 1) - 1][0]  # 되돌아간 x좌표 위치를 반영한다.
                y_value = visit_sequence[(len(visit_sequence) - 1) - 1][1]  # 되돌아간 y좌표 위치를 반영한다.

                visit_sequence.pop()

                print(" 장애물로 인한 왔던 길로 한 칸 돌아간 후 에이전트 방문 기록=")
                print(visit_sequence)
                print()












