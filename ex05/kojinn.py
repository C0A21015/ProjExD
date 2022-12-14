import pygame as pg
import os
import random
import sys


main_dir = os.path.split(os.path.abspath(__file__))[0]


class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]  
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)                    


class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def load_sound(file):
    """because pygame can be be compiled without mixer."""
    if not pg.mixer:
        return None
    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print("Warning, unable to load, %s" % file)
    return None


class Guard_item: #安全地帯生成アイテム
    def __init__(self,image,ratio,xy):
        self.sfc = pg.image.load(image)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
        
    def update(self, scr:Screen):
        self.blit(scr)   


class Guard: #安全地帯の生成
    def __init__(self, color, rad, x, y, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = x
        self.rct.centery = y

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.blit(scr)


def main():
    if pg.get_sdl_version()[0] == 2:
        pg.mixer.pre_init(44100, 32, 2, 1024)
    pg.init()
    if pg.mixer and not pg.mixer.get_init():
        print("Warning, no sound")
        pg.mixer = None

    boom_sound = load_sound("boom.wav")
    shoot_sound = load_sound("car_door.wav")
    if pg.mixer:
        music = os.path.join(main_dir, "data", "house_lo.wav")
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)

    clock =pg.time.Clock()

    # 練習１
    scr = Screen("逃げろ！こうかとん", (1600,900), "fig/pg_bg.jpg")

    # 練習３
    kkt = Bird("fig/6.png", 2.0, (900,400))
    kkt.update(scr)

    # 練習５
    bkd_lst = []
    color_lst = ["red", "green", "blue", "yellow", "magenta"]
    for i in range(5):
        bkd = Bomb(color_lst[i%5], 10, (random.choice(range(-2, 3)), random.choice(range(-2, 3))), scr)
        bkd_lst.append(bkd)
    # bkd.update(scr)

    #安置生成アイテムの初期設定
    gd_x = random.randint(300,1500)
    gd_y = random.randint(300,700)
    gd_item = Guard_item("fig/7.png",0.5,(gd_x, gd_y))
    gd_item.update(scr)

    #安置の初期設定
    gd_rad = 100
    gd = Guard("pink", gd_rad, -100, -100, scr) 

    # 練習２
    while True:        
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        gd.update(scr)

        if kkt.rct.colliderect(gd_item.rct): #安置生成アイテム取得時
            gd_rad = 100 #半径を100に再設定
            gd = Guard("pink", gd_rad, gd_x, gd_y, scr) #アイテムの場所に安置を生成
            old_gd_x = gd_x #現在の安置座標を格納
            old_gd_y = gd_y
            gd_x = random.randint(300,1500) #安置生成アイテムの座標更新
            gd_y = random.randint(300,700)
            gd_item = Guard_item("fig/7.png",0.5,(gd_x,gd_y))
            gd_item.update(scr)
            gd.update(scr)

        if kkt.rct.colliderect(gd.rct): #安全地帯にいる場合
            for bomb in bkd_lst:
                if gd.rct.colliderect(bomb.rct): #安全地帯に爆弾が触れた際
                    gd_rad -= 0.15 #安全地帯の大きさが減少
                    gd = Guard("red", gd_rad, old_gd_x, old_gd_y, scr)
                    gd.update(scr)
                bomb.update(scr)    
        else:
            for bomb in bkd_lst:
                if gd.rct.colliderect(bomb.rct): #安全地帯に爆弾が触れた際
                    gd =  Guard("pink", 100, -100, -100, scr) #画面から安全地帯が消失
                    gd.update(scr)  
                bomb.update(scr)    
                if kkt.rct.colliderect(bomb.rct):
                    return

        if gd_rad <=65:  #安全地帯の半径が65以下になったら
            gd =  Guard("pink", 100, -100, -100, scr) #画面から安全地帯の消失
            gd.update(scr) 

        gd_item.update(scr)
        kkt.update(scr)        

        pg.display.update()
    
        clock.tick(1000)
    

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

