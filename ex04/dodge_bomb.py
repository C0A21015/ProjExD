import pygame as pg
import sys
import random

def check_bound(obj_rct, scr_rct):
    # 第1引数：こうかとんrectまたは爆弾rect
    # 第2引数：スクリーンrect
    # 範囲内：+1／範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def main():
    clock =pg.time.Clock()
    # 練習1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    # 練習3
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct)

    # 練習5
    bomb_sfc = pg.image.load("fig/bomb.png")
    bomb_sfc = pg.transform.rotozoom(bomb_sfc,0,0.05) 
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct) 
    vx,vy,vx1,vy1 = 1,1,1,1
    
    #for文を使用
    bomb2_sfc = pg.image.load("fig/bomb.png")
    bomb2_sfc = pg.transform.rotozoom(bomb2_sfc,0,0.1) 
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = random.randint(0, scrn_rct.width)
    bomb2_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb2_sfc, bomb2_rct) 

    # 練習2
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        # 練習4
        key_dct = pg.key.get_pressed() # 辞書型
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみ出ていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1            
        scrn_sfc.blit(tori_sfc, tori_rct) 

        # 練習６
        bomb_rct.move_ip(vx, vy)
        bomb2_rct.move_ip(vx1, vy1)
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        scrn_sfc.blit(bomb2_sfc, bomb2_rct) 
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        yoko, tate = check_bound(bomb2_rct, scrn_rct)
        vx1 *= yoko
        vy1 *= tate

        # 練習8
        if tori_rct.colliderect(bomb_rct) or tori_rct.colliderect(bomb2_rct):
            fonto = pg.font.Font(None,200)
            txt = fonto.render("GAME OVER",True,(0,0,0))
            vx, vy, vx1, vy1 =0, 0, 0, 0
            tori2_sfc = pg.image.load("fig/8.png")
            tori2_sfc = pg.transform.rotozoom(tori2_sfc, 0, 2.0)
            tori2_rct = tori2_sfc.get_rect()
            tori2_rct.center = tori_rct.centerx,tori_rct.centery
            scrn_sfc.blit(tori2_sfc, tori2_rct)
            scrn_sfc.blit(txt,(400,350))
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()