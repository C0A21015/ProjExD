import tkinter as tk
import tkinter.messagebox as tkm

def button_click():
    tkm.showwarning("警告","１万円支払いました")

def button_click2(event):
    btn=event.widget
    txt=btn["text"]
    tkm.showinfo(txt,f"[{txt}]から１万円支払いました")    

root = tk.Tk() #モジュールのインポート.インスタンスの生成
root.title("あくたん") #ウィンドウのタイトル
root.geometry("500x200") #ウィンドウのサイズ（幅「横」x高さ「縦」）
root.resizable(True , True) #ウィンドウのサイズの変更可能（幅「横」x高さ「縦」）
                            #True（可） か　False（不可） で設定

label = tk.Label(root,                      #文字列描画   
                text="#あくあ色パレット",    #ラベルの文字列
                font=(",20")                #（フォントタイプ,フォントサイズ）
                )
label.pack()

#button = tk.Button(root,text="スパチャ",command=button_click) #ボタン描画
button = tk.Button(root,text="スパチャ") 
button.bind("<3>",button_click2)
button.pack()     

entry = tk.Entry(width=30)
entry.insert(tk.END,"aqukinmaster")
entry.pack()

root.mainloop() #ウィンドウを表示
