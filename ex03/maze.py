import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key=""

def main_proc():
    global cx , cy
    if key == "Up":
        cy -=100
    elif key == "Down":
        cy += 100
    elif key == "Left":
        cx -= 100
    elif key == "Right":
        cx += 100
    canvas.coords("kokaton" , cx , cy) 
    root.after(150 , main_proc)          

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root , width=1500 , height=900 , bg="black")
    canvas.pack()

    maze_list = mm.make_maze(15,9)
    mm.show_maze(canvas , maze_list)

    images = tk.PhotoImage(file="fig/0.png")
    cx , cy = 150 , 150 #初期位置
    canvas.create_image(cx , cy , image=images , tag="kokaton")
    key=""
    root.bind("<KeyPress>" , key_down)
    root.bind("<KeyRelease>" , key_up)
    main_proc()
    root.mainloop()
