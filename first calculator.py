from tkinter import*
from os import system

def fCalc(src, side):
    appObj = Frame(src, borderwidth=4, bd=2,bg = "#1c1c1c")
    appObj.pack(side=side, expand=YES, fill=BOTH)
    return appObj
def unity(unity_screen):
  system("cls&color 0f")
  print("\n  Screen Cleared "+"\n\n by amirali \n \n  ---- > https://github.com/AmiraliZandirad1")
  unity_screen.set("")
def unity_action(unity_screen,button):
    if unity_screen.get()=="ERROR":
        unity_screen.set('')
    unity_screen.set(unity_screen.get() + button)
    system("cls&color 0f")
    print("\n  Button Press : "+str(button)+"\n\n make by amirali \n \n  ---- >  https://github.com/AmiraliZandirad1")
def button(src, side, text, command=None):
    appObj = Button(src, text=text,width=0, fg="#1253cc", bg="#1c1c1c" ,font=("tahoma",20),command=command)
    appObj.pack(side=side, expand=YES, fill=BOTH)
    return appObj
def unity_bcreator(src, side, text, command_unity=None):
    unity_obj = Button(src, text=text,width=0, fg="#ff0000", bg="#1c1c1c" ,font=("tahoma",20),command=command_unity)
    unity_obj.pack(side=side, expand=YES, fill=BOTH)
    return unity_obj
class app(Frame):
    
    def __init__(self, root = Tk(), width=364, height=525):
        Frame.__init__(self)
        self.option_add("*Font", 'tahoma 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title("first calculator")
        

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        display = StringVar()
        Entry(self, relief= RIDGE,      
                    textvariable=display, justify='left',fg="#1253cc", bg="#1c1c1c").pack(side=TOP, expand=YES,
                            fill=BOTH)
        unity_bcreator(self, TOP, "Exit", lambda appObj=display , i="Exit":exit())
        unity_bcreator(self, TOP, "Clear", lambda appObj=display , i="Clear":unity(appObj))
        lbl_title = Label(root, text="\n\n make by amirali \n \n", width=600, fg="#009040", bg="#1c1c1c" ,font=("tahoma", 20))
        lbl_title.pack()

        for btnNum in ("789/", "456*", "123-", "0.+"):

            FunctionNum = fCalc(self, TOP)
            for fEquals in btnNum:
                button(FunctionNum, LEFT, fEquals,
                        lambda appObj=display,fg="#1253cc", bg="#1c1c1c" ,font=("tahoma", 20), i=fEquals:unity_action(appObj,i))
                EqualsButton = fCalc(self, TOP)

        for fEquals in "=":
            if fEquals == "=":
                btnEquals = button(EqualsButton, LEFT, "=",)
                btnEquals.bind('<ButtonRelease-1>',
                                lambda e, s=self, appObj=display: s.result(appObj), "+")
            else:
                btnEquals = button(EqualsButton, LEFT, fEquals,
                        lambda appObj=display, s=" %s "%fEquals: appObj.set(appObj.get()+s),fg="#1253cc", bg="#1c1c1c" ,font=("tahoma", 20))
       
    def result(self, display):
        try:
            system('cls&color 02')
            print("\n  "+str(display.get())+"="+str(eval(display.get()))+"\n\n make by amirali \n \n  ---- >  https://github.com/AmiraliZandirad1")
            display.set(eval(display.get()))
        except Exception as err:
            system('cls&color 04')
            print("\n  "+str(display.get())+"="+"ERROR\n\n  DATA Err : "+str(err)+"\n\n make by amirali \n \n  ---- >  https://github.com/AmiraliZandirad1")
            display.set("ERROR")

try:
    system("cls&color 02")
    print("\n  Advanced Calculator"+"\n\n  make by amirali \n \n  ---- >  https://github.com/AmiraliZandirad1")
    app().mainloop()
except Exception as err:
        system("cls&color 04")
        print("\n  Error to Launche Calculator Code ! \n\n  Err DATA : \n  "+str(err)+"\n\n make by amirali \n \n  ---- >  https://github.com/AmiraliZandirad1")

