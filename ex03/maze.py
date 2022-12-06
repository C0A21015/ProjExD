import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
import random

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key=""

def main_proc():
    global cx , cy , mx , my
    if key == "Up":
        my -=1
    elif key == "Down": 
        my += 1
    elif key == "Left":
        mx -= 1
    elif key == "Right":
        mx += 1
    if maze_list[mx][my] == 1: #移動先が壁なら
        if key == "Up":
            my +=1
        elif key == "Down":
            my -= 1
        elif key == "Left":
            mx += 1
        elif key == "Right":
            mx -= 1

    cx , cy = mx*100+50 , my*100+50     
    canvas.coords("kokaton" , cx , cy) 
    root.after(100 , main_proc)          

def option(): #追加機能
    global cx , cy, mx , my , key
    if key == "r": #ｒキーでリセット
        mx , my = 1  , 0
    if mx == 13 and my ==8:  #ゴールしたことを知らせる
        tkm.showinfo("ゴール","ゴールしました")
    cx , cy = mx*100+50 , my*100+50
    canvas.coords("kokaton" , cx , cy)  
    root.after(100 , option)   



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root , width=1500 , height=900 , bg="black")
    canvas.pack()
    maze_list = mm.make_maze(15,9)
    mm.show_maze(canvas , maze_list)
    num = random.randint(0,9) #ランダムのこうかとん画像を決める
    images = tk.PhotoImage(file=f"fig/{num}.png")
    mx , my = 1 , 0
    cx , cy = mx*150 , my*150 #初期位置
    canvas.create_image(cx , cy , image=images , tag="kokaton")
    key=""
    root.bind("<KeyPress>" , key_down)
    root.bind("<KeyRelease>" , key_up)
    main_proc()
    option()
    root.mainloop()
