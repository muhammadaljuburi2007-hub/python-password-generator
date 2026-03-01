import tkinter as tk 
import random 
root = tk.Tk()
root.title("Password Generator ")
root.geometry("270x300")


chk06v = tk.BooleanVar()
chk08v = tk.BooleanVar()
chk10v = tk.BooleanVar()
chk12v = tk.BooleanVar() 


letrs=("a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","v","V","u","U","w","W","x","X","y","Y","z","Z","1","2","3","4","5","6","7","8","9","0",".","#","@","_","%")

lbl = ""

#---------DEFS------#
def kbuttons() :
	global letrs
	global chk06v
	global chk06v
	global chk08v
	global chk10v
	global chk12v
	global lbl 
	lbl=""
	if chk06v.get() == True :
		x = 6
		
	elif chk08v.get() == True :
		x = 8		
	elif chk10v.get() == True :
		x = 10
	elif chk12v.get() == True :
		x = 12
	else :
		x = 8
		
	for i in range(x) :
		xx = random.randrange(0,66)
		lbl = lbl + letrs[xx]
	lbls = str (lbl)
	klabel.config(text=lbls)
		
def copys():
	global lbl
	root.clipboard_clear()
	root.clipboard_append(lbl)

style={"selectcolor" : "#00aa00"}
#-----buttons---labels----#
klabel = tk.Label(root,text="")
kbutton = tk.Button(root,text="Generate",command=kbuttons)
cbutton = tk.Button(root,text="Copy",command=copys)
chk06=tk.Checkbutton(root,text="6",variable=chk06v,**style)
chk08=tk.Checkbutton(root,text="8",variable=chk08v,**style)
chk10 = tk.Checkbutton(root,text="10",variable=chk10v,**style)
chk12 = tk.Checkbutton(root,text="12",variable=chk12v,**style)

kbutton.grid(row=1,column=0)
cbutton.grid(row=1,column=1)
klabel.grid(row=2,column=0,columnspan=4,pady=30)
chk06.grid(row=3,column=0)
chk08.grid(row=3,column=1)
chk10.grid(row=3,column=2)
chk12.grid(row=3,column=3)

root.mainloop()
