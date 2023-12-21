from tkinter import *
from tkinter import messagebox
main = Tk()
main.title('Tic Tac Toe Game')

xo=True
flag=0

def CheckButton(button):
    global xo,flag
    if button['text']=='' and xo==True:
        button['bg']='#90EE90'
        button['text']='X'
        checkgame()
        xo=False
        flag=flag+1
        
    elif button['text']==''and xo==False:
        button['bg']='#FFA756'
        button['text']='O'
        checkgame()
        xo=True
        flag=flag+1
        
    else:
        messagebox.showinfo('Tic Tac Toe','Player has already entered!')
def checkgame():

    if button1['text']==button2['text']==button3['text']=='X' or button4['text']==button5['text']==button6['text']=='X' or button7['text']==button8['text']==button9['text']=='X' or button1['text']==button4['text']==button7['text']=='X' or button2['text']==button5['text']==button8['text']=='X' or button3['text']==button6['text']==button9['text']=='X' or button1['text']==button5['text']==button9['text']=='X' or button7['text']==button5['text']==button3['text']=='X':
        messagebox.showinfo('Tic Tac Toe','Player X Won')

    elif button1['text']==button2['text']==button3['text']=='O' or button4['text']==button5['text']==button6['text']=='O' or button7['text']==button8['text']==button9['text']=='O' or button1['text']==button4['text']==button7['text']=='O' or button2['text']==button5['text']==button8['text']=='O' or button3['text']==button6['text']==button9['text']=='O' or button1['text']==button5['text']==button9['text']=='O' or button7['text']==button5['text']==button3['text']=='O':
        messagebox.showinfo('Tic Tac Toe','Player O Won')
    elif flag==8:
        messagebox.showinfo('Tic Tac Toe','Draw')



button1=Button(main,text='',font=('times new roman',55,'bold'),bg='#87CEEB',fg='white',width=3,command=lambda:CheckButton(button1))
button1.grid(row=0,column=0)
button2=Button(main,text='',font=('times new roman',55,'bold'),bg='#87CEEB',fg='white',width=3,command=lambda:CheckButton(button2))
button2.grid(row=0,column=1)
button3=Button(main,text='',font=('times new roman',55,'bold'),bg='#87CEEB',fg='white',width=3,command=lambda:CheckButton(button3))
button3.grid(row=0,column=2)
button4=Button(main,text='',font=('times new roman',55,'bold'),bg='#87CEEB',fg='white',width=3,command=lambda:CheckButton(button4))
button4.grid(row=1,column=0)
button5=Button(main,text='',font=('times new roman',55,'bold'),bg='#87CEEB',fg='white',width=3,command=lambda:CheckButton(button5))
button5.grid(row=1,column=1)
button6=Button(main,text='',font=('times new roman',55,'bold'),bg='#87CEEB',fg='white',width=3,command=lambda:CheckButton(button6))
button6.grid(row=1,column=2)
button7=Button(main,text='',font=('times new roman',55,'bold'),bg='#87CEEB',fg='white',width=3,command=lambda:CheckButton(button7))
button7.grid(row=2,column=0)
button8=Button(main,text='',font=('times new roman',55,'bold'),bg='#87CEEB',fg='white',width=3,command=lambda:CheckButton(button8))
button8.grid(row=2,column=1)
button9=Button(main,text='',font=('times new roman',55,'bold'),bg='#87CEEB',fg='white',width=3,command=lambda:CheckButton(button9))
button9.grid(row=2,column=2)

main.mainloop()

