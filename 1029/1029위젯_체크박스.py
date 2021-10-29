from tkinter import*
from tkinter import messagebox
window =Tk()
'''
#함수 정의 부분
def myFunc() :
    if chk.get()==0 :
        messagebox.showinfo("", " 체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("", " 체크버튼이 켜졌어요.")

#메인 코드 부분
#IntVar()는 정수형 형식의 변수를 생성하는 함수
chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)

cb1.pack()

window.mainloop()


#위젯명.configure(옵션 = 값) 은 해당 위젯의 옵션 값을 변경해주는 함수
#var 값을 
def myFunc():
    if var.get() == 1:
        label1.configure(text="파이썬을 선택하셨습니다.")
    elif var.get() ==2:
        label1.configure(text="C++을 선택하셨습니다.")
    else:
        label1.configure(text="Java을 선택하셨습니다.")


#메인 코드 부분    
#variable은 변수명을 정하기 위한것

var = IntVar()
rb1 = Radiobutton(window, text="파이썬", variable = var, value = 1, command = myFunc)
rb2 = Radiobutton(window, text="C++", variable = var, value = 2, command = myFunc)
rb3 = Radiobutton(window, text="Java", variable = var, value = 3, command = myFunc)

label1 = Label(window, text = "선택한 언어 : ",fg = "red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()


#동물 투표 프로그램 완성
window.geometry("400x400")
window.title("애완동물 선택 하기")

def myFunc():
    if var.get() == 1:
        labelImage.configure(image = photo1)
    elif var.get() ==2:
        labelImage.configure(image = photo2)
    else:
        labelImage.configure(image = photo3)

#메인 코드 부분
labelText = Label(window, text= "좋아하는 동물 투표 ",fg="blue" ,font = ("궁서체",20))
var = IntVar()
rb1 = Radiobutton(window, text = "강아지", variable = var, value =1)
rb2 = Radiobutton(window, text = "고양이", variable = var, value =2)
rb3 = Radiobutton(window, text = "토끼", variable = var, value =3)
button0k = Button(window, text = "사진보기", command = myFunc)

photo1 = PhotoImage(file = "../gif/dog4.gif")
photo2 = PhotoImage(file = "../gif/cat.gif")
photo3 = PhotoImage(file = "../gif/rabbit.gif")

labelImage = Label(window, width = 200, height = 200, bg = "yellow", image = None)

labelText.pack(padx = 5, pady = 5)
rb1.pack(padx = 5, pady = 5)
rb2.pack(padx = 5, pady = 5)
rb3.pack(padx = 5, pady = 5)
button0k.pack(padx = 5, pady = 5)
labelImage.pack(padx = 5, pady = 5)


window.mainloop()

'''

#동물 투표 프로그램 완성 var.1
window.geometry("400x400")
window.title("애완동물 선택 하기")

def myFunc():
    if var.get() == 1:
        labelImage.configure(image = photo1)
        labelimageText1.configure(text ="아~ 강아지 좋아하시는구나!" )
    elif var.get() ==2:
        labelImage.configure(image = photo2)
        labelimageText1.configure(text ="아~ 고양이 좋아하시는구나!" )
    else:
        labelImage.configure(image = photo3)
        labelimageText1.configure(text ="아~ 토끼 좋아하시는구나!" )

#메인 코드 부분
bgi = PhotoImage(file = "../gif/jeju14.gif")
imagelabelbgi = Label(window, image = bgi)
imagelabelbgi.place(x=-2,y=-2)
        
labelText = Label(window, text= "좋아하는 동물 투표 ",fg="blue" ,font = ("나눔고딕",20))
var = IntVar()
rb1 = Radiobutton(window, text = "강아지", variable = var, value =1,command = myFunc)
rb2 = Radiobutton(window, text = "고양이", variable = var, value =2,command = myFunc)
rb3 = Radiobutton(window, text = "토끼", variable = var, value =3,command = myFunc)


photo1 = PhotoImage(file = "../gif/dog4.png")
photo2 = PhotoImage(file = "../gif/cat.png")
photo3 = PhotoImage(file = "../gif/rabbit.png")


labelImage = Label(window, width = 200, height = 200, bg = None, image = photo1)
labelimageText1 = Label(window, text=None, fg="red" ,font = ("나눔고딕",15))


labelText.pack(padx = 5, pady = 5)
rb1.pack(padx = 5, pady = 5)
rb2.pack(padx = 5, pady = 5)
rb3.pack(padx = 5, pady = 5)

labelImage.pack(padx = 5, pady = 5)
labelimageText1.pack()

window.mainloop()
