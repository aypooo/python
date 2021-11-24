from tkinter import*
from table import*

import random

class Ball:
    def __init__(self,table,width,height,color,x_speed,y_speed,x_posn,y_posn):
        self.width = width #공의 가로 사이즈
        self.height = height #공의 세로 사이즈
        self.color = color #공의 색상        
        self.x_posn = x_posn #공의 x 좌표값
        self.y_posn = y_posn #공의 y 좌표값

        self.x_start = x_posn
        self.y_start = y_posn
        self.x_speed = x_speed 
        self.y_speed = y_speed

        self.table = table
        self.circle = self.table.draw_oval(self)
    #함수부
    #공이 움직이는 부분
    def move_next(self):
        self.x_posn = self.x_posn +self.x_speed#현재 공의 위치에 이동할 거리 x를 추가
        self.y_posn = self.y_posn +self.y_speed#현재 공의 위치에 이동할 거리 y를 추가
    #공이 위쪽 벽에 충돌했을 때:
        if(self.y_posn <=0):
            self.y_posn = 0
            self.y_speed = -self.y_speed
    #공이 아래쪽 벽에 충돌했을 때:
        if(self.y_posn>=(self.table.height - self.height)):
            self.y_posn = (self.table.height - self.height)
            self.y_speed = -self.y_speed


    #공의 변경된 위치 지정 및 이동
        x1 = self.x_posn
        x2 = self.x_posn + self.width
        y1 = self.y_posn
        y2 = self.y_posn + self.height
        self.table.move_item(self.circle, x1,y1,x2,y2)

    #공의 초기 위치값 지정
    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start
    #전역변수 x_speed의 값을 불러와서 공의 속도에 대입, 랜덤하게 생성된 값에 의해 + 또는 -스피드 값이 적용
    def start_ball(self,x_speed,y_speed):
        self.x_speed = -x_speed if random.randint(0,1)else x_speed #randint(0,1)이 참이냐 거짓이냐에 따라 x_speed가 +,-가 결정
        self.y_speed = -y_speed if random.randint(0,1)else y_speed
        self.start_position()

    #공을 멈춤, x_speed의 값을 불러와서 공의 속도에 대입, 랜덤하게 생성된 값에 의해 +또는 -스피드 값이 적용
    def stop_ball(self):
        self.x_speed = 0
        self.y_speed = 0
