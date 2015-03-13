import turtle

#recursive tree function pulled from
#http://interactivepython.org/runestone/static/pythonds/Recursion/graphical.html

def draw_branch(aTurtle, branchLength):
    if(branchLength>5):
        aTurtle.forward(branchLength)
        aTurtle.right(20)
        draw_branch(aTurtle, branchLength-10)
        aTurtle.left(40)
        draw_branch(aTurtle, branchLength-10)
        aTurtle.right(20)
        aTurtle.backward(branchLength)

def main():
    window = turtle.Screen()
    a = turtle.Turtle()
    a.speed(500)
    for x in range(0, 12):
        draw_branch(a, 75)
        a.right(30)
    a.right(90)
    
    window.exitonclick()

main()
