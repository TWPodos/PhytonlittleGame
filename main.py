import turtle
import random

sc = turtle.Screen()
sc.bgcolor("light blue")
sc.title("TURTLE GAME")
scoret = turtle.Turtle()
score = 0
countdown_turtle = turtle.Turtle()
gameover = False
x_coordinates = [-300, -200, -100, 0, 100, 200, 300]
y_coordinates = [-300, -200, -100, 0, 100, 200, 300]

turtle_list = []
def setup_score():
 scoret.color("dark blue")
 scoret.penup()
 scoret.sety(350)
 scoret.write(arg="Score : 0 ",move=False,align="center",font=("Arial", 18, "normal"))
 scoret.hideturtle()

def mturtle(x,y):
 t = turtle.Turtle()
 def click(x,y):
  global score
  score += 1
  scoret.clear()
  scoret.write(arg=f"Score :{score} ", move=False, align="center", font=("Arial", 14, "normal"))

  print(x,y)
 t.onclick(click)
 t.penup()
 t.shape("turtle")
 t.shapesize(2,2)
 t.color("black")
 t.goto(x,y)
 turtle_list.append(t)
def entturtle():
 for x in x_coordinates:
  for y in y_coordinates:
   mturtle(x,y)
def hideturt():
 for t in turtle_list:
  t.hideturtle()

def showrandom():
 if not gameover:
  hideturt()
  random.choice(turtle_list).showturtle()
  sc.ontimer(showrandom,100)

def countdown(time):
 global gameover
 countdown_turtle.color("red")
 countdown_turtle.penup()
 countdown_turtle.sety(300)
 countdown_turtle.hideturtle()
 countdown_turtle.clear()
 if time > 0 :
  countdown_turtle.clear()
  countdown_turtle.write(arg=f"Time : {time} ", move=False, align="center", font=("Arial", 14, "normal"))
  sc.ontimer(lambda: countdown(time - 1), 1000)
 else:
  gameover=True
  countdown_turtle.clear()
  hideturt()
  countdown_turtle.write(arg="GAME OVER!!", move=False, align="center", font=("Arial", 14, "normal"))


def start_game():
 turtle.tracer(0)
 setup_score()
 entturtle()
 hideturt()
 showrandom()
 countdown(30)
 turtle.tracer(1)


start_game()
sc.mainloop()

