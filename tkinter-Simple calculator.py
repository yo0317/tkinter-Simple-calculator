__author__ = "YOU XUAN-CHANG"
# 協助者： pk
# SJW.M
import tkinter as tk
from PIL import ImageTk, Image
win = tk.Tk()
pastRes = 0             # 設立pastRes變數 用來儲存上一次輸入、計算過的值
lastOp = ""             # 設立lastOp變數 用來儲存上一次按的計算按鈕（加、減、乘、除、等於、空值）（空值可能為第一次計算或已按過AC)
# 數字按鈕所對應的function
# 按下數字按鈕時 將上次從showNumber中得到的值乘以十 再加上按鈕對應的數字
# 例如輸入1 因為showNumber預設值為0 故變成 0 * 10 + 1
# 第二次輸入2 因為showNumber 已變成1 所以變成 1 * 10 + 1 以此類推
def zero():
    temp = showNumber.get() * 10
    showNumber.set(temp)
def one():
    temp = showNumber.get() * 10 + 1
    showNumber.set(temp)
def two():
    temp = showNumber.get() * 10 + 2
    showNumber.set(temp)
def three():
    temp = showNumber.get() * 10 + 3
    showNumber.set(temp)
def four():
    temp = showNumber.get() * 10 + 4
    showNumber.set(temp)
def five():
    temp = showNumber.get() * 10 + 5
    showNumber.set(temp)
def six():
    temp = showNumber.get() * 10 + 6
    showNumber.set(temp)
def seven():
    temp = showNumber.get() * 10 + 7
    showNumber.set(temp)
def eight():
    temp = showNumber.get() * 10 + 8
    showNumber.set(temp)
def nine():
    temp = showNumber.get() * 10 + 9
    showNumber.set(temp)
# AC按鈕所對應的function
# 當按下AC時 將showNumber及pastRes設為0 將lastOp設為空值""
def AC():
    global pastRes
    global lastOp
    showNumber.set(0)
    lastOp = ""
    pastRes = 0
# 當按下加減乘除時 呼叫以下對應的function
# 進入function後 呼叫計算的function math()
# 計算完畢後 將lastOp設為當次按下按鈕對應的名稱 並將showNumber歸零
def add():                              # 加法
    global lastOp
    global pastRes
    math()
    lastOp = "add"
    showNumber.set(0)

def sub():                              # 減法
    global lastOp
    global pastRes
    math()
    lastOp = "sub"
    showNumber.set(0)

def mul():                              # 乘法
    global lastOp
    global pastRes
    math()
    lastOp = "mul"
    showNumber.set(0)

def div():                              # 除法
    global lastOp
    global pastRes
    math()
    lastOp = "div"
    showNumber.set(0)

# 按下等於按鈕對應的function
# 進入function後 呼叫計算的function math()
# 計算完畢後 將最終pastRes的值轉為整數 放置在showNumber的位置上
# 將lastOp修改為"equal"
def equal():
    global pastRes
    global lastOp
    math()
    showNumber.set(int(pastRes))
    lastOp = "equal"

# 綜合計算的function
def math():
    global pastRes
    # 判斷上次的lastOp 也就是上次按下的計算符號按鈕是哪一個 進入對應的條件式
    if lastOp == "add":
        pastRes = pastRes + showNumber.get()
    elif lastOp == "sub":
        pastRes = pastRes - showNumber.get()
    elif lastOp == "mul":
        pastRes = pastRes * showNumber.get()
    elif lastOp == "div":
        pastRes = pastRes / showNumber.get()
    # 當上次按下的按鈕是「等於」時 不動作
    elif lastOp == "equal":
        pastRes = pastRes + 0
    # 當上次按下的按鈕是「AC」或尚未有上次按的按鈕時 直接將showNumber的值存入變數pastRes
    elif lastOp == "":
        pastRes = showNumber.get()
# ================================================================================
win.wm_title("計算機")                          # 視窗標題
win.resizable(width=False, height=False)      # 視窗設為不可拉動大小
win.minsize(width=480, height=480)             # 視窗最小範圍
win.maxsize(width=480, height=480)             # 視窗最大範圍
x = Image.open("#c1c0b9.png")                   # 讀取背景圖片
img = ImageTk.PhotoImage(x)                     # 轉換成PhotoImage
labelBackground = tk.Label(win, image=img)      # 建立Label物件 顯示圖片
labelBackground.pack()                          # 置入圖片
# 裝飾文字放置 顯示本計算機可計算的位數為12
labelDigits = tk.Label(win, text="12 Digits", fg="#537791", bg="#c1c0b9", bd=0, font=("Helvetica", 30))
labelDigits.place(x=60, y=100)
# 計算機顯示框
showNumber = tk.IntVar()
showNumber.set(0)
labelShow = tk.Label(win, text="", textvariable=showNumber, fg="#c1c0b9", bg="#537791", bd=0, font=("Helvetica", 50), width=13)
labelShow.place(x=60, y=20)
# 數字按鈕 按下數字後會呼叫對應的function
btnZero = tk.Button(win, text="0", command=zero, fg="#c1c0b9", bg="#537791", bd=0, font=("Helvetica", 50), width=4)
btnZero.place(x=60, y=400)
btnOne = tk.Button(win, text="1", command=one, fg="#c1c0b9", bg="#537791", bd=0, font=("Helvetica", 50))
btnOne.place(x=60, y=320)
btnTwo = tk.Button(win, text="2", command=two, fg="#c1c0b9", bg="#537791", bd=0, font=("Helvetica", 50))
btnTwo.place(x=150, y=320)
btnThree = tk.Button(win, text="3", command=three, fg="#c1c0b9", bg="#537791", bd=0, font=("Helvetica", 50))
btnThree.place(x=240, y=320)
btnFour = tk.Button(win, text="4", command=four, fg="#c1c0b9", bg="#537791", bd=0, font=("Helvetica", 50))
btnFour.place(x=60, y=240)
btnFive = tk.Button(win, text="5", command=five, fg="#c1c0b9", bg="#537791", bd=0, font=("Helvetica", 50))
btnFive.place(x=150, y=240)
btnSix = tk.Button(win, text="6", command=six, fg="#c1c0b9", bg="#537791", bd=0, font=("Helvetica", 50))
btnSix.place(x=240, y=240)
btnSeven = tk.Button(win, text="7", command=seven, fg="#c1c0b9", bg="#537791", bd=0, font=("Helvetica", 50))
btnSeven.place(x=60, y=160)
btnEight = tk.Button(win, text="8", command=eight, fg="#c1c0b9", bg="#537791", bd=0, font=("Helvetica", 50))
btnEight.place(x=150, y=160)
btnNine = tk.Button(win, text="9", command=nine, fg="#c1c0b9", bg="#537791", bd=0, font=("Helvetica", 50))
btnNine.place(x=240, y=160)
# 等於按鈕 按下後會呼叫對應的equal function
btnEqual = tk.Button(win, text="=", command=equal, fg="#537791", bg="#537791", bd=0, font=("Helvetica", 50))
btnEqual.place(x=240, y=400)
# 加號按鈕 按下後會呼叫對應的add function
btnAdd = tk.Button(win, text="+", command=add, fg="#537791", bg="#537791", bd=0, font=("Helvetica", 50), width=2)
btnAdd.place(x=330, y=160)
# 減號按鈕  按下後會呼叫對應的sub function
btnSub = tk.Button(win, text="–", command=sub, fg="#537791", bg="#537791", bd=0, font=("Helvetica", 50), width=2)
btnSub.place(x=330, y=240)
# 乘號按鈕  按下後會呼叫對應的mul function
btnMul = tk.Button(win, text="✕", command=mul, fg="#537791", bg="#537791", bd=0, font=("Helvetica", 50), width=2)
btnMul.place(x=330, y=320)
# 除號按鈕  按下後會呼叫對應的div function
btnDiv = tk.Button(win, text="/", command=div, fg="#537791", bg="#537791", bd=0, font=("Helvetica", 50), width=2)
btnDiv.place(x=330, y=400)
# AC按鈕  按下後會呼叫對應的AC function
btnClick = tk.Button(win, text="AC", command=AC, fg="#537791", bg="#537791", bd=0, font=("Helvetica", 40))
btnClick.place(x=329, y=100)

win.mainloop()