import random
import tkinter as tk
import tkinter.messagebox as tkm

def clear():
    tkm.showinfo(title="History", message= "Freed File")
        
    with open("Save.txt", 'w') as clear:
        clear.write("")
    clear.close()

conv = {
    1:'⚀',
    2:'⚁',
    3:'⚂',
    4:'⚃',
    5:'⚄',
    6:'⚅',
}

def fetch():
    with open('Save.txt','r') as saved:
        strr = saved.readlines()
        msg=strr[-1:-6:-1]

        l = 20
        for i in msg:
            tk.Label(text= str(conv[int(i[0])]), font= 'arial 65', fg='#149776', bg='#ADDDB5').place(x=l,y=270)
            l += 70

def dice():
    possibilities = [1,2,3,4,5,6]
    if chBias.get() == 1:
        for i in range(4):
            possibilities.append(got.get())
        a = random.choice(possibilities)
        possibilities = [1,2,3,4,5,6]
        
    else:
        a = random.choice(possibilities)
  
    tk.Label(text=f"{conv[a]}", font= 'arial 65', fg='#149776', bg='#ADDDB5').place(x=150,y=120)

    with open("Save.txt",'a') as saver:
        saver.write(str(a)+'\n')
    saver.close()

root = tk.Tk()

chBias = tk.IntVar()

bais = tk.Checkbutton(text="Biased Dice",variable= chBias,bg= '#ADDDB5',font='15').place(x=130,y=5)
got = tk.IntVar()

tk.Label(text="Choose Biased Value: ",bg= '#ADDDB5',font='15').place(x=100,y=40)

tk.Radiobutton(root, text='1',variable=got, value=1,fg='#149776',bg='#ADDDB5',font='10').place(x=45,y=70)
tk.Radiobutton(root, text='2',variable=got, value=2,fg='#149776',bg='#ADDDB5',font='10').place(x=95,y=70)
tk.Radiobutton(root, text='3',variable=got, value=3,fg='#149776',bg='#ADDDB5',font='10').place(x=145,y=70)
tk.Radiobutton(root, text='4',variable=got, value=4,fg='#149776',bg='#ADDDB5',font='10').place(x=195,y=70)
tk.Radiobutton(root, text='5',variable=got, value=5,fg='#149776',bg='#ADDDB5',font='10').place(x=245,y=70)
tk.Radiobutton(root, text='6',variable=got, value=6,fg='#149776',bg='#ADDDB5',font='10').place(x=295,y=70)

mainMenu = tk.Menu(root,tearoff=0, bg='#149776', fg='#ADDDB5')
check = tk.Menu(mainMenu,tearoff=0,bg='#ADDDB5', fg='#107359')
check.add_command(label="Previous Datas",command=fetch)
check.add_command(label="Free Data", command= clear)
check.add_command(label="Exit", command= quit)
mainMenu.add_cascade(label="Menu",menu= check)

root.config(menu=mainMenu)

tk.Button(text="Generate Result", fg='white',bg='#149776', font='10',command=dice).place(x=110,y=225)

sbar = tk.Label(root, text="You Have 50% Chance to get biased choice", relief='sunken', anchor="w",bg="#149776",fg='white')
sbar.pack(side='bottom', fill='x')

root.configure(bg="#ADDDB5")
root.title("Besharam Dice")
root.geometry("400x400")
# root.wm_iconbitmap("i.ico")
root.minsize(400,400)
root.maxsize(400,400)
root.mainloop()