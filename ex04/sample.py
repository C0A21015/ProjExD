import pygame as pg
import sys

def main():
    #ここに実行プログラムを書く
    clock = pg.time.Clock() #時間計測オブジェクト

    pg.display.set_caption("初めてのpygame") #タイトルバーの名前
    scrn_sfc = pg.display.set_mode((800,600)) #800X600の画面surfaceを生成
    
    tori_sfc = pg.image.load("fig/6.png") #Surface
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect() #Rect
    tori_rct.center = 400,300
    #scrn_sfcにtori_rct従って，tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc,tori_rct) #blit
    
    pg.display.update() #blitしてもスクリーン更新しないと表示されない
    clock.tick(1) #1fpの時を刻む
    

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()