#tkinter 는 파이썬에서 GUI 관련 모듈을 제공해주는 표준 윈도우 라이브러리
#위젯(Widget) - 윈도우 창에 나올 수 있는 문자, 버튼 체크박스, 라디오 버튼 등을 말함.
from tkinter import *
from tkinter import messagebox
#Tk( )는 기본이 되는 윈도우를 반환, 루트 윈도우(Root Window) 또는 베이스 윈도우(Base Window)라고 함
window = Tk()
window.title("윈도우 창 연습")
window.geometry("650x440")
window.resizable(width = 0, height = 0)
#1. 라벨은 문자 또는이미지를 표현 할 수 있는 위젯
#step1.라벨 위젯 생성
label1 = Label(window, text = "SWEDU~~Python을")
label2 = Label(window, text = "열심히", font=("궁서체", 30), fg="blue")
label3 = Label(window, text = "공부 중입니다.", bg= "magenta",width=24, height=5, anchor=N, font=("궁서체"), fg="white")

#step2.라벨 위젯을 화면에 표시
#pack()함수를 호출하여 화면에 디스플레이 됨
label1.pack()
label2.pack()
label3.pack()

#2.이미지 위젯 표시
#step1.이미지 불러옴
filename = PhotoImage(file = "../gif/dog.gif")
filename2 = PhotoImage(file = "../gif/dog4.gif")
filename3 = PhotoImage(file = "../gif/jeju2.gif")
#step2.라벨 위젯을 생
imagelabel3 = Label(window, image= filename3)
imagelabel = Label(window, image= filename)
imagelabel2 = Label(window, image= filename2)

#step3. 라벨 위젯을 화면에 표시
imagelabel3.place(x=-2,y=-2)
imagelabel.pack(side=LEFT)
imagelabel2.pack(side=RIGHT)

#버튼을 눌렀을 때 사용자 정의 함수가 실행되도록 하기
#사용자 정의 함수 만들기
def myFunc():
    messagebox.showinfo("강아지 버튼","강아지 이쁘죠?^^")



    
#3.버튼 위젯 표시
button1 = Button(window, text= "파이썬 종료",bg = "skyblue",fg = "red",command = quit)#버튼에 텍스트 표시
button2 = Button(window, image= filename ,command = myFunc)#버튼에 이미지 표시

button2.pack(side=LEFT)
button1.place(x=290,y=400)


#마지막으로 생성되면 가장 앞으로 나온다.
#라벨은 문자를 표현 할 수 있는 위젯
#위젯은 생성하고 디스플레이하는 2스텝으로 진행

#이 부분에서 화면을 구성하고 처리
#윈도우 창에 키보드 누르기, 마우스 클릭 등 다양한 이벤트 처
window.mainloop()
