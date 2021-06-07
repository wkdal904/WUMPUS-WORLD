# 4X4 만들기
import turtle
t=turtle.Turtle()
t.hideturtle()
t.speed(0)

def go_x_y(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def draw_4x4():
    for i in range(2):
        t.forward(400)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(400)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.forward(400)
    t.right(90)

go_x_y(-200,-200)
draw_4x4()

go_x_y(-200,200)
draw_4x4()

# 기호와 뜻
go_x_y(300, 200)
t.write("[G(Glitter)] = 반짝임, 금",font=("",10))

go_x_y(300, 180)
t.write("[P] = 구덩이",font=("",10))


go_x_y(300, 160)
t.write("[W] = 웜푸스",font=("",10))

go_x_y(300, 140)
t.write("S = 악취",font=("",10))

go_x_y(300, 120)
t.write("B = 미풍",font=("",10))

go_x_y(300, 100)
t.write("bump = 벽",font=("",10))



import WorldRandom

