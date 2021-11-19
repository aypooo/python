
from tkinter import*
from tkinter import messagebox
'''
def clickLeft(event):
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼이 클릭됨")
def clickRigth(event):
    messagebox.showinfo("마우스", "마우스 오른쪽 버튼이 클릭됨")    

window = Tk()
window.bind("<Button-1>", clickLeft)
window.bind("<Button-3>", clickRigth)

window.mainloop()
'''
def clickImage(event):
    messagebox.showinfo("마우스", "토끼에서 마우스 클릭됨")

window = Tk()
window.geometry("400x400")
photo = PhotoImage(file = "../gif/rabbit.gif")
label1 = Label(window, image = photo)
label1.bind("<Enter>",clickImage)
label1.pack(expand=1,anchor=CENTER)

window.mainloop()
