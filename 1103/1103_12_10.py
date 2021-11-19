from tkinter import*
window = Tk()
window.geometry("210x210")
'''
button1 = Button(window, text = "버튼1")
button2 = Button(window, text = "버튼2")
button3 = Button(window, text = "버튼3")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)


window.mainloop()


button = [""]*12
n=0
for i in range(3):
    for j in range (0,4):

        button[j] = Button(window, text = "버튼"+str(n))

        button[j].place(x=j*50-40,y=i*30)
        n+=1
window.mainloop()
'''
button = [""]*10
xPos, yPos = 0,0
photolist = [""]*10

i=1

for y in range(0,3):
    for x in range (0,3):
        photolist[i] = PhotoImage(file = "../gif/puz"+str(i)+".gif")

        button[i] = Button(window, image = photolist[i])

        button[i].place(x=xPos,y=yPos)
        xPos += 70
        i+=1
    xPos = 0
    yPos += 70

window.mainloop()


