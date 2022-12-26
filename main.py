import turtle as t
import time
import random

delay = 0.1 #время задержки
color_wnd = 'Light gray'
color_head = 'red'
color_food = 'yellow'
color_tmp = 'red'

def create_screen(width, height, color):
    wn = t.Screen()
    wn.title('Test game')
    wn.bgcolor(color)
    wn.setup(width=width, height=height)
    wn.tracer(0)
    return wn

def create_turtle(x, y, shape, color):
    print(x, y)
    tmp = t.Turtle()
    tmp.shape(shape)
    tmp.penup()
    tmp.color(color)
    tmp.setx(x)
    tmp.sety(y)
    return tmp

def move_turtle(obj):
    obj.setpos(random.randrange(-280, 280, 20), random.randrange(-280,280,20))

def goleft():
    head.setheading(180)

def goright():
    head.setheading(0)

def goup():
    head.setheading(90)

def godown():
    head.setheading(270)

######################
wn = create_screen(600,600,color_wnd)
wn.listen()
wn.onkeypress(goleft,"Left")
wn.onkeypress(goright,"Right")
wn.onkeypress(goup,"Up")
wn.onkeypress(godown,"Down")

head = create_turtle(0,0,'turtle',color_head)
food = create_turtle(0,0,'circle',color_food)
move_turtle(food)
snake = [create_turtle(-20*(i+1),0,'turtle', color_tmp) for i in range(4)]

score = 0
while True:
    wn.update()

    (pos, hd) = (head.pos(), head.heading())
    for s in snake:
        (tmp_pos, tmp_hd) = (s.pos(), s.heading())
        s.setheading(hd)
        s.setpos(pos)
        (hd, pos) = (tmp_hd, tmp_pos)

    head.forward(20)

    if head.distance(food) < 20:
        [x,y] = snake[-1].pos()
        snake.append(create_turtle(x,y,'turtle', color_tmp))
        move_turtle(food)
        score += 1

    wn.title('Snake score = {} !!!!!' .format(score))
    time.sleep(delay)
######################
#диапазон поля, врезаясь в стенку, она выходит из противоположной (так как разные знаки)
t.update()
t.mainloop()

