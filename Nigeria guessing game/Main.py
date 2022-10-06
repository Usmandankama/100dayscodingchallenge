from turtle import *
import pandas as pd

screen = Screen()
screen.addshape('C:\\Users\\SALISU\\Desktop\\Mini Desktop\\Nigeria guessing game\\nigeria_map.gif')
object_ = Turtle()
object_.shape('C:\\Users\\SALISU\\Desktop\\Mini Desktop\\Nigeria guessing game\\nigeria_map.gif')
while True:
    object1 = Turtle()
    df = pd.read_csv('Modules.csv')
    a = screen.textinput("Here", 'here').title()
    if a == 'Exit':
        break
    df = df[df.state.str.contains(a)]
    object1.penup()
    object1.goto(int(df.x), int(df.y))
    object1.turtlesize(.3,.3)
    object1.shape('circle')



screen.mainloop()




# print(df)

