from tkinter import*
from table import*
from ball import*
from bat import*
#randint 함수를 불러오기 위한 모듈 임포트
import random
#전역 변수 초기화
x_speed = 15 #공 x속도
y_speed = 0 #공 y속도

score_left = 0 #왼쪽 득점판
score_right = 0 #오른쪽 득점판
first_serve =True #첫번째 서브 여
scoreboard = "magenta2"

window = Tk()
window.title("MyPingPong")

#game flow()함수부
def game_flow():

    global score_left, score_right, scoreboard 
    #공이 일정 시간마다 움직임
    my_ball.move_next()
    window.after(30,game_flow) #30밀리초마다 game_flow 함수 실행, ex 5초는 500
    #공이 배트에 닿았는지 충돌 확인, 두 배트에 대해 detect_collision()함수 실행
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)
    #공이 좌우 벽에 충돌했을 때 처리
    #공의 x좌표값이 0보다 작을 경우 왼쪽 벽에 충돌한 상황
    if(my_ball.x_posn <= 0):
        my_ball.stop_ball() # 공을 멈춤, x_speed, y_speed를 0으로 설정
        my_ball.start_position() #공의 위치 초기화
        bat_L.start_position()
        bat_R.start_position()
        my_table.move_item(bat_L.rectangle,20,150,35,250)#bat_L배트를 초기위치로 이동
        my_table.move_item(bat_R.rectangle,565,150,580,250)#bat_R배트를 초기위치로 이동
        #득점판 득점 표시
        score_right = score_right + 1
        if score_right >= 3:
            score_right = "W"
            score_left = "L"
            scoreboard = "RoyalBlue1"
        my_table.draw_score(score_left,score_right,scoreboard)

    #공이 오른쪽 벽에 충돌했는지 감지하여 처리 
    if(my_ball.x_posn + my_ball.width >= my_table.width):
        my_ball.stop_ball() # 공을 멈춤, x_speed, y_speed를 0으로 설정
        my_ball.start_position() #공의 위치 초기화
        bat_L.start_position()
        bat_R.start_position()
        my_table.move_item(bat_L.rectangle,20,150,35,250)#bat_L배트를 초기위치로 이동
        my_table.move_item(bat_R.rectangle,565,150,580,250)#bat_R배트를 초기위치로 이동

        #득점판 득점 표시
        score_left = score_left +1
        if score_left >= 3:
           score_right = "L"
           score_left = "W"
           scoreboard = "RoyalBlue1"  
        my_table.draw_score(score_left,score_right,scoreboard)

        
#restart_game(master):
#게임을 재시작하는 함수
def restart_game(master):
    global score_left, score_right, scoreborad
    my_ball.start_ball(x_speed=x_speed,y_speed=y_speed)
    bat_L.start_position
    bat_R.start_position
    my_table.move_item(bat_L.rectangle,20,150,35,250)
    my_table.move_item(bat_R.rectangle,565,150,580,250)
    scoreboard = "magenta2"
    if score_right == ("L" or " W"):
        score_right = 0
        score_left = 0
        
    my_table.draw_score(score_left,score_right,scoreboard)
                
        
    
#테이블 생성    
my_table = Table(window, 600, 400, "black","skyblue",scoreboard)
#공생성 self,table,width,height,color,x_speed,y_speed,x_posn,y_posn):
my_ball = Ball(table=my_table,width=24,height=24,color="magenta2",x_speed=0,y_speed=0,x_posn=288,y_posn=188)
my_ball.move_next()

#배트생성
bat_L = Bat(table = my_table,width=15,height=100,color="cyan2",x_posn=20,y_posn=150)
bat_R = Bat(table = my_table,width=15,height=100,color="green yellow",x_posn=565,y_posn=150)

#함수의 실행부
game_flow()
window.bind("<space>",restart_game)
#배트를 제어하기 위함 키이벤트 및 연결 될 함수 지정
#window.bind("<키명>",함수명)
window.bind("<Up>",bat_R.move_up)
window.bind("<Down>",bat_R.move_down)
window.bind("<w>",bat_L.move_up)
window.bind("<s>",bat_L.move_down)



window.mainloop()
