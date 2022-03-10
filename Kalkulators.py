from ast import operator
from tkinter import*
from math import*
from unittest import result
mansLogs=Tk()
mansLogs.title("Kalkulators")

def btnClick(number):
    current=e.get()
    e.delete(0,END)
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)
    return 0

def btnCommand(command):
    global num1
    global mathOp
    mathOp=command #+,-,*,/
    num1=float(e.get())
    e.delete(0,END)
    return 0

def Equals():
    global num2
    num2=float(e.get())
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    elif mathOp=="x²":
        result=num1**2
    elif mathOp=="π":
        result=3.14    
    else:    
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

def Clear():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0        

def Sqrt():
    global operator
    global num1
    global mathOp
    #mathOp=command
    num1=float(e.get())
    num1=sqrt(num1)
    e.delete(0,END)
    e.insert(0,num1)

#def Kvdr():
 #   global operator
  #  global num1
   # global mathOp
    #num1=float(e.get()**2)
    #e.delete(0,END)
    #e.insert(0,num1)
    #result

def Punkt():
    if e.get()==".":
        pass
    else:
        e.insert(END,".")
        
#def Pi():
 #   global operator
  #  global num1
   # global mathOp
    #mathOp=command
    #num1=float(e.get())
    #num1=pi(num1)
    #e.delete(0,END)
    #e.insert(0,num1)  

btn0=Button(mansLogs, text="0", padx="40", bd=20, pady="20", font=("Arial Black",20), command = lambda:btnClick(0))
btn1=Button(mansLogs, text="1", padx="40", bd=20, pady="20", font=("Arial Black",20), command = lambda:btnClick(1))
btn2=Button(mansLogs, text="2", padx="40", bd=20, pady="20", font=("Arial Black",20),command = lambda:btnClick(2))
btn3=Button(mansLogs, text="3", padx="40", bd=20, pady="20", font=("Arial Black",20),command = lambda:btnClick(3))
btn4=Button(mansLogs, text="4", padx="40", bd=20, pady="20", font=("Arial Black",20),command = lambda:btnClick(4))
btn5=Button(mansLogs, text="5", padx="40", bd=20, pady="20", font=("Arial Black",20),command = lambda:btnClick(5))
btn6=Button(mansLogs, text="6", padx="40", bd=20, pady="20", font=("Arial Black",20),command = lambda:btnClick(6))
btn7=Button(mansLogs, text="7", padx="40", bd=20, pady="20", font=("Arial Black",20),command = lambda:btnClick(7))
btn8=Button(mansLogs, text="8", padx="40", bd=20, pady="20", font=("Arial Black",20),command = lambda:btnClick(8))
btn9=Button(mansLogs, text="9", padx="40", bd=20, pady="20", font=("Arial Black",20),command = lambda:btnClick(9))
btnAdd=Button(mansLogs, text="+", padx="40", bd=20, pady="20", font=("Arial Black",20),command = lambda:btnCommand("+"))
btnSub=Button(mansLogs, text="-", padx="40", bd=20, pady="20", font=("Arial Black",20),command = lambda:btnCommand("-"))
btnEquals=Button(mansLogs, text="=", padx="40", bd=20, pady="20", font=("Arial Black",20),command = Equals)
btnDiv=Button(mansLogs, text="/", padx="40", bd=20, pady="20", font=("Arial Black",20),command = lambda:btnCommand("/"))
btnReiz=Button(mansLogs, text="*", padx="40", bd=20, pady="20", font=("Arial Black",20),command = lambda:btnCommand("*"))
btnClear=Button(mansLogs, text="C", padx="40", bd=20, pady="20", font=("Arial Black",20),command = Clear)
btnSqrt=Button(mansLogs, text="√", padx="40", bd=20, pady="20", font=("Arial Black",20),command = Sqrt)
btnKvdr=Button(mansLogs, text="x²", padx="40", bd=20, pady="20", font=("Arial Black",20),command = lambda:btnCommand("x²"))
btnPunkt=Button(mansLogs, text=".", padx="40", bd=20, pady="20", font=("Arial Black",20),command = Punkt)
btnPi=Button(mansLogs, text="π", padx="40", bd=20, pady="20", font=("Arial Black",20),command = lambda:btnCommand("π"))

btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
btn0.grid(row=4,column=0)
btnAdd.grid(row=2,column=3)
btnSub.grid(row=3,column=3)
btnEquals.grid(row=1,column=3)
btnReiz.grid(row=4,column=1)
btnDiv.grid(row=4,column=2)
btnClear.grid(row=4,column=3)
btnSqrt.grid(row=5, column=0)
btnKvdr.grid(row=5, column=1)
btnPunkt.grid(row=5, column=2)
btnPi.grid(row=5, column=3)
e=Entry(mansLogs,width=15, bd=20,font=("Arial Black",20))
e.grid(row=0,column=0,columnspan=4)
mansLogs.mainloop()