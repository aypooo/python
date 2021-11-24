from tkinter import*
score_left = 0 #왼쪽 득점판
score_right = 0 #오른쪽 득점판

class Table:
    #생성자
    def __init__(self, window, width, height, bg_color, net_color, scoreboard):
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.net_color = net_color
        self.scoreboard = scoreboard
        
        
        #Table 클래스 내에서 캔버스 생성
        self.canvas=Canvas(window, width=self.width, height=self.height)
        self.back_img = PhotoImage(file = "./dog.png")
        
        self.canvas.create_image((width/2, height/2), image=self.back_img)
        self.canvas.pack()
        #Table 클래스 내에서 네트 선 생성
        self.canvas.create_line(self.width/2,0,width/2,400,width=3,fill=net_color, dash=(15,23))
        
        #Table 클래스 내에서 득점판 생성
        font = ("monaco",60)
        self.scoreboard = self.canvas.create_text(self.width/2,65,font=font,fill=scoreboard,text=str(score_left)+" "+str(score_right))

    #함수부
    #Canvas(Table)에 타원(공)을 추가하는 함수
    def draw_oval(self, oval):
        x1 = oval.x_posn
        x2 = oval.x_posn + oval.width
        y1 = oval.y_posn
        y2 = oval.y_posn + oval.height
        c = oval.color
        return self.canvas.create_oval(x1,y1,x2,y2,fill=c)
    #Canvas(Table)에 직사각형(배트)을 추가하는 함수
    def draw_rectangle(self, rectangle):       
        x1 = rectangle.x_posn
        x2 = rectangle.x_posn + rectangle.width
        y1 = rectangle.y_posn
        y2 = rectangle.y_posn + rectangle.height
        c = rectangle.color
        return self.canvas.create_rectangle(x1,y1,x2,y2,fill=c)
    #Canvas(Table)에 아이템(공과 배트)을 조작할 수 있는 함수 coords()이
    #coords()는 입력받은 값으로 속성값 업데이트하는 함수
    #변경된 위치값으로 공과 배트의 위치 변경
    def move_item(self,item,x1,y1,x2,y2):
        self.canvas.coords(item,x1,y1,x2,y2)

    #Canvas(Table)에 득점판을 갱신하는 함수
    def draw_score(self,left,right,scoreboard):
        scores = str(left) +" "+ str(right)
        self.canvas.itemconfigure(self.scoreboard, text=scores, fill=scoreboard)
    
