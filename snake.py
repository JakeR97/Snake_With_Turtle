import turtle
import random

#Set up window
gameWindow = turtle.Screen()
gameWindow.title("Jake's Snake")
gameWindow.screensize(900, 600, "black")
gameWindow.setup(width=.9, height=.9, startx=None, starty=None)
gameWindow.listen()
gameWindow.mode(mode="logo")

#Misc variables
fruit = turtle.Turtle()
global done
global speed
global score
global printedParts
global playerBody
speed = 0.75
done = False
score = 0
printedParts = 0
playerBody = []
draw = turtle.Turtle()

#Define class for recording location of body parts
class BodyPart():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def xcor(self):
    return self.x

  def ycor(self):
    return self.y
  
#Draw border
border = turtle.Turtle()
border.color("white")
border.pensize(4)
border.pu()
border.ht()
border.setpos(-400, -300)
border.pd()
border.st()
for x in range(2):
  border.fd(600)
  border.rt(90)
  border.fd(950)
  border.rt(90)
border.ht()

#Draw score
drawScore = turtle.Turtle()
drawScore.ht()
drawScore.color("white")
drawScore.speed(0)
drawScore.pu()
drawScore.setpos(-550, 200)
drawScore.pd()
drawScore._write("Score: " + str(score), align="left", font=(20))

#Create "player"
player = turtle.Turtle()
player.shape("triangle")
player.speed(0.75)
player.resizemode("user")
player.turtlesize(0.5, 0.5, 1)
player.color("white")
player.pu()
player.ht()
player.setpos(0, -270)
player.st()

#Create "fruit"
fruit = turtle.Turtle()
fruit.pu()
fruit.speed(0)
fruit.color("white")
fruit.shape("circle")
fruit.resizemode("user")
fruit.shapesize(.4, .4, 1)
    
#Define function
def right():
  if (player.heading() != 270):
    global speed
    player.speed(0)
    player.seth(90)
    player.speed(speed)
  
def left():
  if (player.heading() != 90):
    global speed
    player.speed(0)
    player.seth(270)
    player.speed(speed)
  
def up():
  if (player.heading() != 180):
    global speed
    player.speed(0)
    player.seth(0)
    player.speed(speed)
  
def down():
  if (player.heading() != 0):
    global speed
    player.speed(0)
    player.seth(180)
    player.speed(speed)
  
def isCollidedWith(a, b):
  return (abs(a.xcor()-b.xcor()) < 5 and abs(a.ycor()-b.ycor()) < 5)
  
def checkBounds():
  x = player.xcor()
  y = player.ycor()
  global speed
  global done
  if x < -390 or x > 540:
    speed = 0
    done = True
  if y < -290 or y > 290:
    speed = 0
    done = True
    
  if done == True:
    gameOver()
    
def addFruit():
  fruit.ht()
  rand = random.Random()
  x = random.Random.randint(rand, -39, 54) * 10
  y = random.Random.randint(rand, -29, 29) * 10
  fruit.setpos(x, y)
  fruit.st()
  
def eatFruit():
  global score
  drawScore.clear()
  drawScore._write("Score: " + str(score), align="left", font=(20))
  
def movePlayer():
  global printedParts
  global score
  global playerBody
  player.stamp()
  playerBody.append(BodyPart(player.xcor(), player.ycor()))
  if printedParts >= score:
    player.clearstamps(1)
    playerBody.pop(0)
  else:
    printedParts += 1
  player.forward(10)  
    
def checkFruit():
  global score
  if isCollidedWith(player, fruit):
    #Move fruit, add to player, add to score
    score += 1
    eatFruit()
    addFruit()
    
def checkCollision():
  for part in playerBody:
    if (isCollidedWith(player, part)):
      gameOver()
    
  
def gameOver():
  #Set up writing turtle
  global done
  done = True
  draw.pu()
  draw.color("white")
  draw.speed(0)
  draw.pensize(10)
  draw.setpos(100, 0)
  draw.pd()
  draw._write("Loser", align="center", font=("Arial", 72, "normal"))
  draw.pu()
  draw.setpos(100, -50)
  draw.write("Final Score: " + str(score), align="center", font=("Arial", 32, "normal"))
  draw.pu()
  draw.setpos(100, -100)
  draw.write("Press Enter to Restart", align="Center", font=("Arial", 24, "normal"))
  draw.ht()
  
def restart():
  global done
  global speed
  global score
  global playerBody
  global printedParts
  printedParts = 0
  score = 0
  playerBody = []
  draw.clear()
  player.pu()
  player.ht()
  player.speed(0)
  player.setpos(0, -270)
  player.setheading(0)
  player.st()
  speed = 0.75
  player.speed(speed)
  drawScore.clear()
  player.clearstamps(n=None)
  drawScore._write("Score: " + str(score), align="left", font=(20))
  done = False
  run()
  
def run():
  global done
  global score
  global speed
  while done == False:
    movePlayer()
    checkFruit()
    checkBounds()
    checkCollision()  

#Create key-binds
gameWindow.listen()
gameWindow.onkey(left, "Left")
gameWindow.onkey(right, "Right")
gameWindow.onkey(up, "Up")
gameWindow.onkey(down, "Down")
gameWindow.onkey(restart, "Return")

run()

turtle.mainloop()