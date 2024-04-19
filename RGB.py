from tkinter import *
import pyperclip
import pyautogui as pg
import keyboard as kb
from tkinter import colorchooser

app=Tk()
app.minsize(600,500)
app.title("RGB - HEX  ranglar")
app.config(bg="lightcyan")
app.resizable(0,0)
app.attributes("-topmost",True)

def RGB(red,green,blue):
    return f'#{red:02x}{green:02x}{blue:02x}'

r_s_var=0
g_s_var=0
b_s_var=0

def Red(red):
    global r_s_var
    r_s_var=int(red)
    rang_f.config(bg=RGB(r_s_var,g_s_var,b_s_var))
    r.config(troughcolor=RGB(r_s_var,g_s_var,b_s_var))
    g.config(troughcolor=RGB(r_s_var,g_s_var,b_s_var))
    b.config(troughcolor=RGB(r_s_var,g_s_var,b_s_var))
    copy.config(bg=RGB(r_s_var,g_s_var,b_s_var))
    copy2.config(bg=RGB(r_s_var,g_s_var,b_s_var))
    r_s.delete(0,END)
    code.delete(0,END)
    code2.delete(0,END)
    r_s.insert(END,red)
    code.insert(END,f"RGB({r_s_var},{g_s_var},{b_s_var})")
    code2.insert(END,RGB(r_s_var,g_s_var,b_s_var))
    if r_s_var+g_s_var+b_s_var<180:
        copy.config(fg="white")
        copy2.config(fg="white")
    else:
        copy.config(fg="black")
        copy2.config(fg="black")
    


def Green(green):
    global g_s_var
    g_s_var=int(green)
    rang_f.config(bg=RGB(r_s_var,g_s_var,b_s_var))
    r.config(troughcolor=RGB(r_s_var,g_s_var,b_s_var))
    g.config(troughcolor=RGB(r_s_var,g_s_var,b_s_var))
    b.config(troughcolor=RGB(r_s_var,g_s_var,b_s_var))
    copy.config(bg=RGB(r_s_var,g_s_var,b_s_var))
    copy2.config(bg=RGB(r_s_var,g_s_var,b_s_var))
    g_s.delete(0,END)
    code.delete(0,END)
    code2.delete(0,END)
    g_s.insert(END,green)
    code.insert(END,f"RGB({r_s_var},{g_s_var},{b_s_var})")
    code2.insert(END,RGB(r_s_var,g_s_var,b_s_var))
    if r_s_var+g_s_var+b_s_var<180:
        copy.config(fg="white")
        copy2.config(fg="white")
    else:
        copy.config(fg="black")
        copy2.config(fg="black")

def Blue(blue):
    global b_s_var
    b_s_var=int(blue)
    rang_f.config(bg=RGB(r_s_var,g_s_var,b_s_var))
    r.config(troughcolor=RGB(r_s_var,g_s_var,b_s_var))
    g.config(troughcolor=RGB(r_s_var,g_s_var,b_s_var))
    b.config(troughcolor=RGB(r_s_var,g_s_var,b_s_var))
    copy.config(bg=RGB(r_s_var,g_s_var,b_s_var))
    copy2.config(bg=RGB(r_s_var,g_s_var,b_s_var))
    b_s.delete(0,END)
    code.delete(0,END)
    b_s.insert(END,blue)
    code2.delete(0,END)
    code.insert(END,f"RGB({r_s_var},{g_s_var},{b_s_var})")
    code2.insert(END,RGB(r_s_var,g_s_var,b_s_var))
    if r_s_var+g_s_var+b_s_var<190:
        copy.config(fg="white")
        copy2.config(fg="white")
    else:
        copy.config(fg="black")
        copy2.config(fg="black")

def sinbox_r(e):
    ozgaruvchi=r_s.get()
    if ozgaruvchi!="":
        if ozgaruvchi.isdigit():
            if int(ozgaruvchi)>255:
                r_s.delete(0,END)
                r_s.insert(0,255)
            try:
                r.set(ozgaruvchi)
            except:
                r_s.delete(0,END)
                r_s.insert(END,ozgaruvchi[-1])
                r.set(ozgaruvchi[-1])
        else:
            r_s.delete(0,END)
    else:
        r.set(0)
        r_s.insert(0,0)
    

def sinbox_g(e):
    ozgaruvchi=g_s.get()
    if ozgaruvchi!="":
        if ozgaruvchi.isdigit():
            if int(ozgaruvchi)>255:
                g_s.delete(0,END)
                g_s.insert(0,255)
            try:
                g.set(ozgaruvchi)
            except:
                g_s.delete(0,END)
                g_s.insert(END,ozgaruvchi[-1])
                g.set(ozgaruvchi[-1])
        else:
            g_s.delete(0,END)
    else:
        g.set(0)
        g_s.insert(0,0)

def sinbox_b(e):
    ozgaruvchi=b_s.get()
    if ozgaruvchi!="":
        if ozgaruvchi.isdigit():
            if int(ozgaruvchi)>255:
                b_s.delete(0,END)
                b_s.insert(0,255)
            try:
                b.set(ozgaruvchi)
            except:
                b_s.delete(0,END)
                b_s.insert(END,ozgaruvchi[-1])
                b.set(ozgaruvchi[-1])
        else:
            b_s.delete(0,END)
    else:
        b.set(0)
        b_s.insert(0,0)

fonts=("times",16,"bold")

menu=Menu(app,tearoff=False,
    font=("times",12,"bold"),
    activeborderwidth=8,
    activebackground="yellow",
    activeforeground="red",bg="blue",
    fg="white")

copy_ma=""

def Copy():
    pyperclip.copy(code.get())
    mishka.config(state="normal")
    try:
        app.after_cancel(copy_ma)
    except:
        pass


def Copy2():
    pyperclip.copy(code2.get())
    mishka.config(state="normal")
    try:
        app.after_cancel(copy_ma)
    except:
        pass
menu.add_command(label="RGB - copy",command=Copy)
menu.add_separator()
menu.add_command(label="HEX - copy",command=Copy2)

def popup_menu(e):
    menu.tk_popup(x=e.x_root,y=e.y_root)

#----------------------(mouse)-------------------------------------------
def mouse_rgb():
    global copy_ma
    mishka.config(state="disabled")
    x,y=pg.position()
    p=pg.screenshot().getpixel((x,y))
    code.delete(0,END)
    code.insert(0,f"RGB({p[0]},{p[1]},{p[2]})")
    r.set(p[0])
    g.set(p[1])
    b.set(p[2])
    copy_ma=app.after(func=mouse_rgb,ms=10)

kb.add_hotkey("ctrl+c",Copy)
kb.add_hotkey("ctrl+d",Copy2)

def ranglar():
    rang=colorchooser.askcolor(title="Ranglar",color="yellow")
    try:
        r.set(rang[0][0])
        g.set(rang[0][1])
        b.set(rang[0][2])
        code.delete(0,END)
        code.insert(0,f"RGB({rang[0][0]},{rang[0][1]},{rang[0][2]})")
    except:
        pass

rang_f=Frame(width=200,height=200,bg="yellow")
rang_f.pack(expand=1,fill=BOTH)
rang_f.bind("<Button-3>",popup_menu)

r_f=Frame(width=1,height=1,bg="white")
g_f=Frame(width=1,height=1,bg="white")
b_f=Frame(width=1,height=1,bg="white")
r_f.pack(fill=X,pady=5)
g_f.pack(fill=X,pady=5)
b_f.pack(fill=X,pady=5)

r_l=Label(r_f,text="R",font=fonts,padx=5,fg="red")
g_l=Label(g_f,text="G",font=fonts,padx=5,fg="green")
b_l=Label(b_f,text="B",font=fonts,padx=5,fg="blue")
r_l.pack(side=LEFT)
g_l.pack(side=LEFT)
b_l.pack(side=LEFT)

r_s=Entry(r_f,font=fonts,width=5,bd=3,justify="center",fg="red")
r_s.insert(0,0)
g_s=Entry(g_f,font=fonts,width=5,bd=3,justify="center",fg="green")
g_s.insert(0,0)
b_s=Entry(b_f,font=fonts,width=5,bd=3,justify="center",fg="blue") 
b_s.insert(0,0)

r_s.bind("<KeyRelease>",sinbox_r) 
g_s.bind("<KeyRelease>",sinbox_g)
b_s.bind("<KeyRelease>",sinbox_b)

r_s.pack(side=LEFT,padx=3)
g_s.pack(side=LEFT,padx=3)
b_s.pack(side=LEFT,padx=3)

r=Scale(r_f,bg="red",bd=0,from_=0,to=255,
    font=fonts,
    fg="white",
    cursor="hand2",
    orient="horizontal",
    highlightbackground="black",
    sliderrelief="solid",
    sliderlength=30,
    troughcolor="yellow",
    width=15,
    command=Red)

g=Scale(g_f,bg="green",bd=0,from_=0,to=255,
    font=fonts,
    fg="white",
    cursor="hand2",
    orient="horizontal",
    highlightbackground="black",
    sliderrelief="solid",
    sliderlength=30,
    troughcolor="yellow",
    width=15,
    command=Green)

b=Scale(b_f,bg="blue",bd=0,from_=0,to=255,
    font=fonts,
    fg="white",
    cursor="hand2",
    orient="horizontal",
    highlightbackground="black",
    sliderrelief="solid",
    sliderlength=30,
    troughcolor="yellow",
    width=15,
    command=Blue)

r.pack(fill=X,side="left",expand=1)
g.pack(fill=X,side="left",expand=1)
b.pack(fill=X,side="left",expand=1)

codbar=Frame(width=1,height=1,bg="lightgreen")
codbar.pack()

RGB_label=Label(codbar,text="Ctrl + c",font=("times",18),padx=5,relief=SOLID)
RGB_label.pack(side=LEFT)

code=Entry(codbar,font=("times",17,"bold"),justify=CENTER,bd=3,relief=SOLID,width=18)
code.pack(side=LEFT,padx=2)
code.insert(0,"RGB(0,0,0)")

copy=Button(codbar,text="Copy",font=("times",12,"bold"),command=Copy,relief=SOLID,cursor="hand2",activebackground="yellow")
copy.pack(side=LEFT)



codbar2=Frame(width=1,height=1,bg="lightgreen")
codbar2.pack(pady=5)

RGB_label2=Label(codbar2,text="Ctrl + d",font=("times",18),padx=5,relief=SOLID)
RGB_label2.pack(side=LEFT)

code2=Entry(codbar2,font=("times",17,"bold"),justify=CENTER,bd=3,relief=SOLID,width=18)
code2.pack(side=LEFT,padx=2)
code2.insert(0,"#000000")

copy2=Button(codbar2,text="Copy",font=("times",12,"bold"),command=Copy2,relief=SOLID,cursor="hand2",activebackground="yellow")
copy2.pack(side=LEFT)

mish=Frame(width=100,height=50,bg="lightcyan",padx=115)
mish.pack(fill=X,expand=1)

mishka=Button(mish,text="Mouse",command=mouse_rgb,width=17,font=("times",13,"bold"),relief=SOLID,cursor="hand2",activebackground="yellow")
mishka.pack(side=LEFT,expand=1)

rang=Button(mish,text="Ranglar",command=ranglar,width=17,font=("times",13,"bold"),relief=SOLID,cursor="hand2",activebackground="yellow")
rang.pack(side=LEFT,expand=1)


app.mainloop()
