from tkinter import*

window = Tk()
window.geometry("800x600")
'''
#2. 이미지 위젯 표시
filename1 = PhotoImage(file = "../gif/puz1.gif")
imagelabel1 = Label(window, image = filename1)
imagelabel1.pack(side=LEFT)

filename2 = PhotoImage(file = "../gif/puz2.gif")
imagelabel2 = Label(window, image = filename2)
imagelabel2.pack(side=LEFT)

filename3 = PhotoImage(file = "../gif/puz3.gif")
imagelabel3 = Label(window, image = filename3)
imagelabel3.pack(side=LEFT)

'''
#반복문과 리스트를 결합하여 이미지 웨짓을 순서대로 표시하
#빈 리스트 선언
#filename = [] #append로 반복적으로 추가해서 사용
filename = [None]*10
imagelabel = [None]*10 #미리 리스트 길이를 지정
for i in range(1,10,1):    
    filename[i] = PhotoImage(file = "../gif/puz"+str(i)+".gif")
    imagelabel[i] = Label(window, image = filename[i])
    imagelabel[i].pack(side=LEFT)
