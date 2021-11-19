
#주의 사항1. 이미지 파일명이나 저장된 경로에 한글이 들어가면 안됨
#주의 사항2. 이미지 크기는 가로와 세로가 동일 해야 함
#주의 사항3. 처리하는 속도가 다소 오래 걸림

from tkinter import* #라이브러리 또는 모듈 임포트
from tkinter.filedialog import* #파일 입출력을 위한 모듈
from tkinter.simpledialog import* #숫자나 문자를 입력 받기 위한 모듈
from wand.image import *
#이미지 처리 기능을 제공하는 imagemaick 라이브러리
#GIF 뿐 아니라 JPG. PNG 같은 이미지를 모두 처리하기 위해 외부 라이브러리 imagemagick 사용

#변수 선언 부분
menu = ["파일 저장","되돌리기","확대","축소","상하 반전","좌우 반전","회전"]
menu1 =["명암","밝게","어둡게","선명하게","탁하게","채도","흑백"]
window,window2, canvas, paper = None, None, None, None
photo, photo2 = None, None #photo는 처음 불러들인 원본 이미지, photo2는 처리 결과를 저장 할 사본 이미지
oriX, oriY =0,0 #원본 이미지의 폭과 높이를 저장하는 함수



#함수정의

def displayImage(img, width, height): #이미지를 화면에 출력하는 함수
    global window,window2 , canvas, paper, photo, photo2, oriX, oriY
    #이전 캔버스가 존재한다면 새 캔버스와 그 위에 새 종이를 생성하여 깨끗하게 처리한 후 처리된 이미지 출력
    #이전 캔버스가 존재한다면 이전 캔버스를 삭제하여 기존에 이미지가 출력된 캔버스를 깨끗하게 처리
    if canvas != None:
        canvas.destroy()
    if window2 != None:
        window2.destroy()
      
    window2 =Toplevel()
    window2.wm_attributes("-topmost", 1)
    window2.title("이미지")
    window2.geometry(str(width)+"x"+str(height)+"+500+500")

    #새 캔버스 생성, 처리된 이미지의 가로 세로 사이즈대로 생성
    canvas = Canvas(window2, width = width , height=height, bg ='#626262', bd= 0, highlightthickness = 0)
    #새 캔버스에 붙일 종이(paper)생성, 처리된 이미지의 가로 세로 사이즈 대로 생성
    
    paper = PhotoImage(width = width, height = height)
    #새 캔버스에 종이를 붙인 (차후 그 종이 위에 처리된 이미지를 출력)
    #생성 될 페이퍼의 위치는 캔버스의 가로 세로 사이즈의 중간 위치
    blob = img.make_blob(format = 'png')#png로 변경해서 출력한다. 처리속도 빠름
    paper.put(blob)
    canvas.create_image((width/2, height/2), image=paper, state ="normal")
    #새 캔버스와 새 종이 위에 처리된 이미지를 출력
    #make_blob(format =None) 는 이미지를 바이너리 코드로 변환해주는 함수, 배열의 형태로 저장
    #흰 종이에 사진을 출력하기 위해 이미지 파일의 모든 점 (픽셀)에 접근                   
    '''blob = img.make_blob(format="RGB")

    for i in range(0, width):
        for k in range(0, height):
            r = blob[(i*3*width)+(k*3) +0] #blob[0],blob[3],blob[6],blob[9]...의 값을 r에 저장
            g = blob[(i*3*width)+(k*3) +1] #blob[1],blob[4],blob[7],blob[10]...의 값을 g에 저장
            b = blob[(i*3*width)+(k*3) +2] #blob[2],blob[5],blob[8],blob[11]...의 값을 b에 저장
            #paper에 칼라로 점을 찍어줌, 세로로 높이 만큼 찍고 가로를 너비 만큼 반복
            paper.put("#%02x%02x%02x" %(r,g,b),(k,i)) #rgb위치 변경하면 색 밸런스 변경 가능'''

    canvas.pack()
   
                        
def func_open():
    global window, canvas, paper, photo, photo2, oriX, oriY , menu
    readFp = askopenfilename(parent = window, filetype =(("모든 그림 파일","*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"),("모든 파일", "*.*")))
    photo = Image(filename = readFp) #photo는 처음 불러들인 원본 이미지
    oriX = photo.width #원본 이미지의 가로 사이즈를 oriX 에 저장
    oriY = photo.height #원본 이미지의 세로  사이즈를 oriY 에 저장
    #photo2는 처리; 결과를 저장 할 변수
    photo2 = photo.clone() #원본 이미지의 photo를 복사하여 photo2에 저장
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY) #화면에 이미지를 출력하는 displayImage()함수 호출
    fileMenu.entryconfig(1, state = "normal")
    for i in range(len(menu)):
        if i != 1:
           imageMenu1.entryconfig(i, state = "normal")
    for i in range(len(menu1)):
        if i != 1 and i != 4:
           imageMenu2.entryconfig(i, state = "normal")
        
def func_save():
    global window, canvas, paper, photo, photo2, oriX, oriY
    #photo2는 func_open() 함수를 실행하면 생성됨
    #파일을 열지 않았다면 저장하기를 눌렀을 때 함수를 빠져나감
    if photo2 ==None :
        return
    saveFp = asksaveasfile(parent = window, mode = "w",defaultextenstion = "jpg", filetypes =(("JPG 파일", ".jpg", ".jpeg"), ("모든 파일","*,*")))
    savePhoto = photo2.convert("jpg") #결과 이미지인 photo2를 jpg로 변환
    savePhoto.save(filename = saveFp.name) #파일 저장 대화창에서 입력받은 파일 이름으로 저장
                                                                                                                        

def func_exit():
    widow.quit()
    window.destroy()

#
def func_rollback():
    global window, canvas, paper, photo, photo2, oriX, oriY

    if photo2 ==None:
        return
    
    photo2 = photo.clone()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_zoomin():
    global window, canvas, paper, photo, photo2, oriX, oriY

    if photo2 ==None:
        return
    #askinteger() 함수를 실행해 대화 상자로 확대 할 배수 입력받음
    scale = askinteger("확대배수", " 확대할 배수를 입력하세요(2~4)",minvalue =2,maxvalue= 4)
    photo2.resize(int(oriX*scale),(int(oriY*scale)))#원본 이미지의 가로 세로 사이즈에 배수를 곱하여 크기 변경
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY) #화면에 이미지를 출력하는 displayImage() 함수 호
def func_zoomout():
    global window, canvas, paper, photo, photo2, oriX, oriY

    if photo2 ==None:
        return
    scale = askinteger("확대배수", " 확대할 배수를 입력하세요(2~4)",minvalue =2,maxvalue= 4)
    photo2.resize(int(oriX/scale),(int(oriY/scale)))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_horizontal():
    global window, canvas, paper, photo, photo2, oriX, oriY
    if photo2 ==None:
        return
    photo2.flip()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_vertical():
    global window, canvas, paper, photo, photo2, oriX, oriY
    if photo2 == None:
        return
    photo2.flop()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_rotate():
    global window, canvas, paper, photo, photo2, oriX, oriY

    if photo2 == None:
        return
    value = askinteger("회전", " 회전 할 각도를 입력하세요(0~100)",minvalue =0,maxvalue= 100)
    photo2.rotate(value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

#Wand 라이브러리에서 제공하는 modulate(명도값, 채도값, 색상값)함수를 사용
#명초는 modulate (명도값, 100,100) 함수를 사용
#원본의 명도값이 100이므로 100이상은 '밝게' 100이하는 '어둡게' 처리
#밝게, modulate(밝기값, 100, 100) 함수에 100~200 값 입력
def func_bright():
    global window, canvas, paper, photo, photo2, oriX, oriY

    if photo2 == None:
        return
    value = askinteger("밝게","값을 입력하세요(100~200)",minvalue = 100, maxvalue= 200)
    photo2.modulate(value, 100, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_dark():
    global window, canvas, paper, photo, photo2, oriX, oriY

    if photo2 == None:
        return
    value = askinteger("어둡게","값을 입력하세요(0~100)",minvalue = 0, maxvalue= 100)
    photo2.modulate(value, 100, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_clear():
    global window, canvas, paper, photo, photo2, oriX, oriY

    if photo2 == None:
        return
    value = askinteger("선명하게","값을 입력하세요(100~200)",minvalue = 100, maxvalue= 200)
    photo2.modulate(100, value, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_cloudy():
    global window, canvas, paper, photo, photo2, oriX, oriY

    if photo2 == None:
        return
    value = askinteger("탁하게","값을 입력하세요(0~100)",minvalue = 0, maxvalue= 100)
    photo2.modulate(100, value, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_saturation():
    global window, canvas, paper, photo, photo2, oriX, oriY

    if photo2 == None:
        return
    value = askinteger("채도","값을 입력하세요(0~200)",minvalue = 0, maxvalue= 200)
    photo2.modulate(100, 100, value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

#이미지처리2 >흑백이미지
#이미지의 type 값을 "grayscale"로 설정
def func_bw():
    global window, canvas, paper, photo, photo2, oriX, oriY

    if photo2 == None:
        return
    photo2.type="grayscale"
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

#메인코드
window = Tk()
window.geometry("900x600")
window.title("미니 포토샵(Ver 0.1)")

#메인 메뉴 생성
mainMenu = Menu(window) 
window.config(menu = mainMenu, bg ="gray") #메뉴자체 생성 및 화면에 디스플레이

#상위 메뉴 생성
fileMenu = Menu(mainMenu, tearoff =0)                           
mainMenu.add_cascade(label = "파일", menu = fileMenu)                                    
#메인 메뉴이름에 add_cascade(label="상위 메뉴 텍스트", menu = 상위메뉴이름)
#add_cadcade() 메소드는 메뉴자체와 상위 메뉴를 연결


#하위 메뉴 생성
fileMenu.add_command(label="파일 열기", command = func_open)             
fileMenu.add_command(label="파일 저장", command = func_save, state = "disable")
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command = func_exit)
#상위 메뉴 이름에 add_command(label="하위 메뉴 이름", command = 함수명)
#add_command() 메소드는 하위 메뉴 항목 생성

imageMenu1 = Menu(mainMenu, tearoff =0)
mainMenu.add_cascade(label="편집", menu =imageMenu1)
imageMenu1.add_command(label="되돌리기", command = func_rollback, state = "disable")
imageMenu1.add_separator()
imageMenu1.add_command(label="확대", command = func_zoomin, state = "disable")
imageMenu1.add_command(label="축소", command = func_zoomout, state = "disable")
imageMenu1.add_command(label="상하 반전", command = func_horizontal, state = "disable")
imageMenu1.add_command(label="좌우 반전", command = func_vertical, state = "disable")
imageMenu1.add_command(label="회전", command = func_rotate, state = "disable")


imageMenu2 = Menu(mainMenu, tearoff =0)
mainMenu.add_cascade(label ="이미지", menu =imageMenu2)

imageMenu2_1 = Menu(mainMenu, tearoff =0)
imageMenu2.add_cascade(label ="명암", menu =imageMenu2_1, state = "disable")
imageMenu2_1.add_command(label="밝게", command = func_bright, state = "normal")
imageMenu2_1.add_command(label="어둡게", command = func_dark, state = "normal")
imageMenu2.add_separator()
imageMenu2.add_command(label="선명하게", command = func_clear, state = "disable")
imageMenu2.add_command(label="탁하게", command = func_cloudy, state = "disable")
imageMenu2.add_separator()
imageMenu2.add_command(label="채도", command = func_saturation, state = "disable")
imageMenu2.add_command(label="흑백", command = func_bw, state = "disable")


window.mainloop()


#원본으로 돌릴 수 있도록 메뉴추가하고 함수도 추가
#채도와 색상도 조정가능하도록 응용
#나머지 UI및 기능을 이미지 편집 프로그램 답게 커스터마이징
#이미지를 불러들였을 때 파일명도 표시
#하위메뉴에 하위메뉴
#이미지 열기전에 특정 메뉴 클릭 안되게
