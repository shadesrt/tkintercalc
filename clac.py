import tkinter as tk

expr=''

def printNumber(num):
    global label2
    global expr
    global var1,var2,opr,res

    if(num=='1' or num=='2' or num=='3' or num=='4' or num=='5' or num=='6' or num=='7' or num=='8' or num=='9' or num=='0'):
        expr=(expr+num)
        #label2.set(label2.get()+expr)                  -> chala nhi
        label2.config(text=expr)
    elif( num=='+' or num=='-' or num=='*' or num=='/' ):
        try:
            opr=num
            var1=int(expr)
            label2.config(text=opr)
            expr=''
        except (ValueError,ZeroDivisionError):
            label2.config(text='3RR0R')
    #equals to
    else:
        try:
            var2=int(expr)
            if(opr=='+'):
                res=var1+var2
            elif(opr=='*'):
                res =var1*var2
            elif (opr == '-'):
                res =var1-var2
            else: #divide
                res =var1/var2
            label2.config(text=res)
            expr=res
        except (ValueError,ZeroDivisionError):
            label2.config(text='3RR0R')

def clearOut():
    label2.config(text='')
    global expr
    expr=''


mainWindow= tk.Tk()

label1= tk.Label(mainWindow, text='Calculator')
label1.config(bg='White',fg='blue',font=('BEYNO',20))
label1.grid(row=1,columnspan=4)

label2= tk.Label(mainWindow, height=2, width=15)
label2.config(bg='White',fg='green',font=('Calibari',20))
label2.grid(row=2,columnspan=4,padx=5,pady=5,ipadx=3,ipady=3)

button1= tk.Button(mainWindow, text='1', command=lambda:printNumber('1'))
button1.grid(row=3,columnspan=1,padx=15,pady=5,ipadx=3,ipady=3)

button2= tk.Button(mainWindow, text='2', command=lambda:printNumber('2'))
button2.grid(row=3,columnspan=2,padx=15,pady=5,ipadx=3,ipady=3)

button3= tk.Button(mainWindow, text='3', command=lambda:printNumber('3'))
button3.grid(row=3,columnspan=3,padx=15,pady=5,ipadx=3,ipady=3)

button4= tk.Button(mainWindow, text='4', command=lambda:printNumber('4'))
button4.grid(row=4,columnspan=1,padx=5,pady=5,ipadx=3,ipady=3)

button5= tk.Button(mainWindow, text='5', command=lambda:printNumber('5'))
button5.grid(row=4,columnspan=2,padx=5,pady=5,ipadx=3,ipady=3)

button6= tk.Button(mainWindow, text='6', command=lambda:printNumber('6'))
button6.grid(row=4,columnspan=3,padx=5,pady=5,ipadx=3,ipady=3)

button7= tk.Button(mainWindow, text='7', command=lambda:printNumber('7'))
button7.grid(row=5,columnspan=1,padx=5,pady=5,ipadx=3,ipady=3)

button8= tk.Button(mainWindow, text='8', command=lambda:printNumber('8'))
button8.grid(row=5,columnspan=2,padx=5,pady=5,ipadx=3,ipady=3)

button9= tk.Button(mainWindow, text='9', command=lambda:printNumber('9'))
button9.grid(row=5,columnspan=3,padx=5,pady=5,ipadx=3,ipady=3)

button0=tk.Button(mainWindow, text='0', command=lambda:printNumber('0'))
button0.grid(row=6,columnspan=2,padx=5,pady=5,ipadx=3,ipady=3)

buttona=tk.Button(mainWindow, text='+', command=lambda:printNumber('+'))
buttona.grid(row=3,columnspan=4,padx=5,pady=5,ipadx=3,ipady=3)

buttonm=tk.Button(mainWindow, text='*', command=lambda:printNumber('*'))
buttonm.grid(row=4,columnspan=4,padx=5,pady=5,ipadx=3,ipady=3)

buttond=tk.Button(mainWindow, text='/', command=lambda:printNumber('/'))
buttond.grid(row=5,columnspan=4,padx=5,pady=5,ipadx=3,ipady=3)

buttone=tk.Button(mainWindow, text='=', command=lambda:printNumber('='))
buttone.grid(row=6,columnspan=4,padx=5,pady=5,ipadx=3,ipady=3)

buttons=tk.Button(mainWindow, text='-', command=lambda:printNumber('-'))
buttons.grid(row=6,columnspan=3,padx=5,pady=5,ipadx=3,ipady=3)

buttonc=tk.Button(mainWindow, text='C', command=lambda:clearOut())
buttonc.grid(row=6,columnspan=1,padx=5,pady=5,ipadx=3,ipady=3)

mainWindow.mainloop()