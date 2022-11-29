import tkinter as tk
import tkinter.messagebox as tkm
import math

def button_click(event):
    btn = event.widget
    num = btn["text"]
    siki = entry.get() # 数式の文字列
    
    if num == "=":
        if siki=="":
            pass
        else:
            if siki[-1]=="+" or siki[-1]=="-" or siki[-1]=="*" or siki[-1]=="/"or siki[-1]==".":
                pass
            else:        
                res = eval(siki) # 数式文字列の評価
                entry.delete(0, tk.END) # 表示文字列の削除
                entry.insert(tk.END, res) # 結果の挿入
    elif num=="+" :
        if siki == "":
            pass
        else:
            if siki[-1]=="+" or siki[-1]=="*" or siki[-1]=="/" or siki[-1]=="." :
                pass
            else:
                entry.insert(tk.END,num)

    elif num=="-" :
        if siki == "":
            entry.insert(tk.END,num)
        else:
            if siki[-1]=="." :
                pass
            else:
                entry.insert(tk.END,num)            

    elif num==".":
        if siki == "":
            pass
        else:
            if siki[-1]=="+" or siki[-1]=="-" or siki[-1]=="*" or siki[-1]=="/" or siki[-1]=="." :
                pass
            else:
                entry.insert(tk.END,num)            
    elif num == "×":
        if siki=="":
            pass
        else:
            if siki[-1]=="+" or siki[-1]=="-"or siki[-1]=="*" or siki[-1]=="/"or siki[-1]==".":
                pass
            else:
                entry.insert(tk.END,"*")
    elif num == "÷":
        if siki == "":
            pass
        else:
            if siki[-1]=="+" or siki[-1]=="-" or siki[-1]=="*" or siki[-1]=="/"or siki[-1]=="." :
                pass
            else:
                entry.insert(tk.END,"/")

    elif num == "C":
        entry.delete(0,tk.END)   

    elif num == "π":
        entry.insert(tk.END,f"{math.pi}")

    elif num == "e":
        entry.insert(tk.END,f"{math.e}") 
    elif num == "√":
        if siki =="":
            pass
        else:
            res=eval(siki)
            if int(res) < 0:
                    pass
            else: 
                entry.delete(0, tk.END) # 表示文字列の削除
                entry.insert(tk.END,f"{math.sqrt(int(res))}")     

    else: # 「=」以外のボタン字
        #tkm.showinfo("", f"{num}ボタンがクリックされました")
            entry.insert(tk.END, num)

root = tk.Tk()
root.geometry("450x600")

entry = tk.Entry(root, justify="right", width=15, font=("",40))
entry.grid(row=0, column=0, columnspan=4)

r, c = 1, 0
operators = ["√","e","π","+","7","8","9","-","4","5","6","×","1","2","3","÷","C","0",".", "="]
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%4 == 0:
        r += 1
        c = 0

root.mainloop() 
