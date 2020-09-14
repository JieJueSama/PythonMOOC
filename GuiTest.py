import easygui as g
import sys

while 1:
    g.msgbox('嗨，欢迎进入第一个gui制作的小游戏')
    msg = '你希望学习到什么知识'
    title = '互动小游戏'
    choices = ['琴棋书画','四书五经','程序编写','逆向分析']
    chocie = g.choicebox(msg, title, choices)
    g.msgbox('你的选择是：' + str(chocie), '结果')
    msg = '你希望重新开始小游戏吗？'
    title = '请选择'
    if g.ccbox(msg, title):
        pass
    else:
        sys.exit(0)
