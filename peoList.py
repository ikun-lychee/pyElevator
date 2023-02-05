"""
欢迎使用！

为了不使大家迷路，我准备了这个文档，专解释它如何工作：

    module peolist
    |-- (v) eleNum 电梯里的所有乘客
    |-- (v) thisEle 电梯所在楼层
    |-- (f) add() 添加人
    |-- (f) remove() 删除人
    |-- (f) nextSection() 推荐最佳前往楼层
    |-- (f) board() 载入乘客
    |__ (f) leave() 载出乘客
"""
import easygui
from tkinter.messagebox import showerror, showinfo, showwarning, askyesno

# 常量：电梯承载人数
MAX_NUM = 10

num = {0: [], 1: [], 2: [], 3: [], 4: []}
eleNum = []
thisEle = 0
upDown = "UP"



def add():  # 添加某人
    try:
        fe = int(easygui.choicebox("请选择起点楼层：", "PyElevator", [1, 2, 3, 4, 5]))
        oe = [1, 2, 3, 4, 5]
        for i in oe:
            if i == fe:
                oe.remove(i)
        te = int(easygui.choicebox("请选择终点楼层：", "PyElevator", oe))
        if fe == te:
            showwarning("PyElevator", "您不能输入两个相同的数。")
            return "ASK_END_SAME_NUM"
        yn = askyesno("PyElevator", "确认要添加吗？")
        if yn:
            num[int(fe - 1)].append(int(te - 1))
            showinfo("PyElevator", "已成功添加。")
    except TypeError:
        showinfo("pyElevator", "询问已中断。")


def remove():  # 删除某人
    try:
        fe = int(easygui.choicebox("请选择要删除的起点楼层：", "PyElevator", [1, 2, 3, 4, 5]))
        if not fe:
            return "ASK_END_NO_START"
        oe = [1, 2, 3, 4, 5]
        for i in oe:
            if i == fe:
                oe.remove(i)
        te = int(easygui.choicebox("请选择要删除的终点楼层：", "PyElevator", oe))
        if not te:
            return "ASK_END_NO_END"
        if fe == te:
            showwarning("PyElevator", "您不能输入两个相同的数。")
            return "ASK_END_SAME_NUM"
        yn = askyesno("PyElevator", "确认要删除吗？")
        if yn:
            try:
                num[int(fe - 1)].remove(int(te - 1))
                showinfo("PyElevator", "已成功删除。")
            except ValueError:
                showerror("PyElevator", "没有该人。")
    except TypeError:
        showinfo("pyElevator", "询问已中断。")
    except:
        showerror("pyElevator", "程序内部发生错误。")
        raise Exception


def nextSection():
    global upDown
    if upDown == "UP":
        flush: set = {i for i in eleNum if i >= thisEle}
    else:
        flush: set = {i for i in eleNum if i <= thisEle}

    def up():
        for i in range(thisEle, 5):
            if num[i]:
                flush.add(i)
                return "ADD_END"
        return "NOBODY"

    def down():
        for i in range(thisEle, -1, -1):
            if num[i]:
                flush.add(i)
                return "ADD_END"
        return "NOBODY"

    if upDown == "UP":
        up()
        if flush is None:
            response = down()
            if response == "NOBODY":
                return "ok"
        minn = 4
        for i in flush:
            if i < minn:
                minn = i
        return "ok", minn
    if upDown == "DOWN":
        down()
        if flush is None:
            response = up()
            if response == "NOBODY":
                return "ok", None
        minn = 0
        for i in flush:
            if i > minn:
                minn = i
        return "ok", minn


def board():
    flush = num[thisEle]
    for i in flush:
        if len(eleNum) < 10:
            eleNum.append(i)
            num[thisEle].pop(0)


def leave():
    for i in eleNum:
        if i == thisEle:
            eleNum.remove(i)


#------------------------------------------------------
add()
thisEle = nextSection()[1] if nextSection()[1] is not None else thisEle
print(thisEle)
board()
print(nextSection())
