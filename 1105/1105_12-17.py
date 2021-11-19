from tkinter import*
from time import*


fnameList=[None]*9
photoList=[None]*9
num=0 #리스트의 인덱스 값

for i in range(0,9):
    fnameList[i] = "jeju"+str(i+1)+".gif"

def clickNext():
    global num
    num+=1
    if num>8 :
        num=0
    photo = PhotoImage(file="../gif/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    photoname.configure(text = fnameList[num])

def clickPrev():
    global num
    num-=1
    if num<0 :
        num=8
    photo = PhotoImage(file="../gif/"+fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    photoname.configure(text = fnameList[num])
                        
def pageUp(event) :
    clickNext()

def pageDown(event) :
    clickPrev()

def clickImageR(event):
    clickNext()
def clickImageL(event):
    clickPrev()


window = Tk()
window.geometry("1069x780")
window.title("사진 앨범 보기")

#bg = PhotoImage(file = "../gif/bg.gif")
bgimg = Label(window, bg = "gray")
bgimg.place(x = -1, y = -1)


window.bind("<Prior>",pageUp)
window.bind("<Next>",pageDown)

arrowL = PhotoImage(file = "../gif/arrow_L.png")
arrowR = PhotoImage(file = "../gif/arrow_R.png")

imgprev = Label(window, image = arrowL)
imgnext = Label(window, image = arrowR)
#btnPrev = Button(window, image = arrowL , command = clickPrev)
#btnNext = Button(window, image = arrowR, command = clickNext)
imgprev.bind("<Button-1>",clickImageL)
imgnext.bind("<Button-1>",clickImageR)

photoname = Label(window,text = fnameList[num])
photo = PhotoImage(file = "../gif/"+fnameList[0])
pLabel = Label(window, image = photo)

imgprev.place(x = 0, y =0)
#btnPrev.place(x = 250, y = 10)
photoname.place(x = 825,y = 620)
imgnext.place(x = 1034, y =0)
#btnNext.place(x = 400, y = 10)
pLabel.place(x = 220, y = 170)

window.mainloop()
