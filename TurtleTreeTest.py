import turtle

def tree(branchLen, t):
    if branchLen > 5:
        #画树干
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-15, t)
        t.right(20)
        t.backward(branchLen)

def main():
    #生成海龟
    t = turtle.Turtle()
    myWin = turtle.Screen()
    #海龟位置默认屏幕中央，调整到下面
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    #画树，树干长度75
    tree(75,t)
    myWin.exitonclick()

main()