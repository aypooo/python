# 20211006 윈도우 프로그래밍, 그림판 만들기,홍륜건 #

#윈도우 프로그래밍을 하기 위해 tkinter 모듈 가져오기
from tkinter import*

#변수 선언#

window = None #창의 정보를 저장 할 수 있는 변수 생성
canvas = None #캔버스의 정보를 저장 할 수 있는 변수 생성
x1, y1, x2, y2 = None, None, None, None #선의 시작점좌 끝점의 정보(x,y 좌표값)를 저장할 수 있는 변수 생성

#함수 선언#

def MouseClick(event): #마우스를 클릭했을 때 실행 할 사용자 정의 한수 선언
    global x1,y1,x2,y2 #전역변수 선언#
    x1 = event.x
    y1 = event.y

    
def MouseDrop(event): #마우스를 떼었을 때 실행 할 사용자 정의 한수 선언
    global x1,y1,x2,y2
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1,y1,x2,y2,width=5,fill="red")



#메인 코드#

window = Tk() #창 생성 
window.title("그림판 비슷한 프로그램") #생성된 창의 이름 설정
canvas = Canvas(window, height = 600, width =600) #생성된 창 (window)에 그림을 그릴 수 있는 캔버스 생성
canvas.bind("<Button-1>",MouseClick) #bind() 함수로 이벤트와 함수를 연결
canvas.bind("<ButtonRelease-1>",MouseDrop)    
canvas.pack() #화면에 캔버스 디스플레이
window.mainloop() #창에 이벤트가 발생 여부를 확인하는 함수
