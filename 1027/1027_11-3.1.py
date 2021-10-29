#클래스 정의 부분
class Car :
    #필드부분
    #color=""  #필드 선언 및 초기값 대입
    #speed = 0
#메소드 부분
    #매개변수를 입력받아 생성자 실행
    def __init__(self,value1,value2) : #생성자,인스턴스를 생성하면 무조건 호출되는 메소드
        self.color = value1
        self.speed= value2
    
    def upSpeed(self,value) :
        self.speed +=value

    def downSpeed(self, value) :
        self.speed-=value

#메인코드 부분

#생성자로 초기값 지정하면 아래의 메소드 실행부는 안적어도 됨
maCar1 = Car("빨강",0)   #myCar1 인스턴스 생성
maCar2 = Car("빨강",0)
maCar3 = Car("빨강",0)


#메소드 실행 
myCar1.upSpeed(30)
pring("자동차1의 색상은 %s이며, 현재속도는 %d km 입니다." %(myCar1.color,myCar1.speed))

myCar2.upSpeed(60)
pring("자동차3의 색상은 %s이며, 현재속도는 %d km 입니다." %(myCar2.color,myCar2.speed))

myCar3.upSpeed(0)
pring("자동차3의 색상은 %s이며, 현재속도는 %d km 입니다." %(myCar3.color,myCar3.speed))
