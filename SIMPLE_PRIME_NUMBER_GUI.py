
from tkinter import *


win=Tk()
win.title('simple prime number')
main=Frame(win)

win.geometry("700x350")




def cal_sum():
       global n_Prime
       
       t1=int(a.get())
       myButton['state'] = DISABLED       

       if t1 > 1:
           for i in range(2, int(t1/2)+1):
               if t1 % i == 0:
                   n_Prime=Label(win, text="not a prime number")
                   n_Prime.pack()
                   break
           else:
                n_Prime=Label(win, text="is a Prime Number")
                n_Prime.pack()    


def myDel(): 
    n_Prime.pack_forget()
    myButton['state'] = NORMAL      
           
   



# Create an Entry widget
Label(win, text="Enter Number", font=('Calibri 10')).pack()
a=Entry(win, width=35)
a.pack()



myButton = Button(win, text="calculate", command=cal_sum , bg="red", fg="white")
myButton.pack(ipadx=50, pady=8)

myDel2 = Button(win, text="Clear Prime", command=myDel)
myDel2.pack(ipadx=5)




win.mainloop()
