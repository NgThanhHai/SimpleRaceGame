import pygame,sys,random
from pygame.locals import*
pygame.init()
#information player
gameplayed=0
gamewin=0
#signin-entercoin
name=""
coin=0
mychar=0
statistic = False
rank1=0
rank2=0
rank3=0
rank4=0
rank5=0
#setup window
disp_width=1040
disp_height=585
disp=pygame.display.set_mode((disp_width,disp_height),pygame.RESIZABLE)
pygame.display.set_caption("THE RACE-BET GAME")
#load backgrounds
king=pygame.image.load("king.png")
showranking=pygame.image.load("ShowRanking.png")
guide1=pygame.image.load("Guide1.png")
ItemShop = pygame.image.load("ItemShop.png")
guide2=pygame.image.load("Guide2.png")
in4=pygame.image.load("In4.png")
sign=pygame.image.load("sign.png")
bg=pygame.image.load("map.png")
menu=pygame.image.load("menu.png")
entercoin=pygame.image.load("EnterCoin.png")
menuBD=pygame.image.load("menuBD.png")
showcoin=pygame.image.load("coin.png")
selectset=pygame.image.load("selectset.png")
selectcat=pygame.image.load("selectcat.png")
selectdino=pygame.image.load("selectdino.png")
selectrocket=pygame.image.load("selectrocket.png")
selectsnake=pygame.image.load("selectsnake.png")
selectteam=pygame.image.load("selectteam.png")
bgm=pygame.image.load("minigame.png")
bgm1=pygame.image.load("minigame1.png")
bgm2=pygame.image.load("minigame2.png")
bgm3=pygame.image.load("minigame3.jpg")
bgm4=pygame.image.load("minigame4.png")
bet=pygame.image.load("bet.png")
#load image "right"
runcat1=[pygame.image.load("C_B1.png"),pygame.image.load("C_B2.png"),pygame.image.load("C_B3.png"),#1~blue
         pygame.image.load("C_B4.png"),pygame.image.load("C_B5.png"),pygame.image.load("C_B6.png"),
         pygame.image.load("C_B7.png"),pygame.image.load("C_B8.png")]
runcat2=[pygame.image.load("C_G1.png"),pygame.image.load("C_G2.png"),pygame.image.load("C_G3.png"),#2~green
         pygame.image.load("C_G4.png"),pygame.image.load("C_G5.png"),pygame.image.load("C_G6.png"),
         pygame.image.load("C_G7.png"),pygame.image.load("C_G8.png")]
runcat3=[pygame.image.load("C_P1.png"),pygame.image.load("C_P2.png"),pygame.image.load("C_P3.png"),#3~purple
         pygame.image.load("C_P4.png"),pygame.image.load("C_P5.png"),pygame.image.load("C_P6.png"),
         pygame.image.load("C_P7.png"),pygame.image.load("C_P8.png")]
runcat4=[pygame.image.load("C_PK1.png"),pygame.image.load("C_PK2.png"),pygame.image.load("C_PK3.png"),#4~pink
         pygame.image.load("C_PK4.png"),pygame.image.load("C_PK5.png"),pygame.image.load("C_PK6.png"),
         pygame.image.load("C_PK7.png"),pygame.image.load("C_PK8.png")]
runcat5=[pygame.image.load("C_R1.png"),pygame.image.load("C_R2.png"),pygame.image.load("C_R3.png"),#5~red
         pygame.image.load("C_R4.png"),pygame.image.load("C_R5.png"),pygame.image.load("C_R6.png"),
         pygame.image.load("C_R7.png"),pygame.image.load("C_R8.png")]
#
rundino1=[pygame.image.load("RunB_1.png"),pygame.image.load("RunB_2.png"),pygame.image.load("RunB_3.png"),
          pygame.image.load("RunB_4.png"),pygame.image.load("RunB_5.png"),pygame.image.load("RunB_6.png"),
          pygame.image.load("RunB_7.png"),pygame.image.load("RunB_8.png")]
rundino2=[pygame.image.load("RunG_1.png"),pygame.image.load("RunG_2.png"),pygame.image.load("RunG_3.png"),
          pygame.image.load("RunG_4.png"),pygame.image.load("RunG_5.png"),pygame.image.load("RunG_6.png"),
          pygame.image.load("RunG_7.png"),pygame.image.load("RunG_8.png")]
rundino3=[pygame.image.load("RunP_1.png"),pygame.image.load("RunP_2.png"),pygame.image.load("RunP_3.png"),
          pygame.image.load("RunP_4.png"),pygame.image.load("RunP_5.png"),pygame.image.load("RunP_6.png"),
          pygame.image.load("RunP_7.png"),pygame.image.load("RunP_8.png")]
rundino4=[pygame.image.load("RunPK_1.png"),pygame.image.load("RunPK_2.png"),pygame.image.load("RunPK_3.png"),
          pygame.image.load("RunPK_4.png"),pygame.image.load("RunPK_5.png"),pygame.image.load("RunPK_6.png"),
          pygame.image.load("RunPK_7.png"),pygame.image.load("RunPK_8.png")]
rundino5=[pygame.image.load("RunR_1.png"),pygame.image.load("RunR_2.png"),pygame.image.load("RunR_3.png"),
          pygame.image.load("RunR_4.png"),pygame.image.load("RunR_5.png"),pygame.image.load("RunR_6.png"),
          pygame.image.load("RunR_7.png"),pygame.image.load("RunB_8.png")]
#
runrocket1=[pygame.image.load("R_B1.png"),pygame.image.load("R_B2.png"),pygame.image.load("R_B3.png"),
            pygame.image.load("R_B4.png"),pygame.image.load("R_B5.png"),pygame.image.load("R_B6.png"),
            pygame.image.load("R_B7.png"),pygame.image.load("R_B8.png")]
runrocket2=[pygame.image.load("R_G1.png"),pygame.image.load("R_G2.png"),pygame.image.load("R_G3.png"),
            pygame.image.load("R_G4.png"),pygame.image.load("R_G5.png"),pygame.image.load("R_G6.png"),
            pygame.image.load("R_G7.png"),pygame.image.load("R_G8.png")]
runrocket3=[pygame.image.load("R_P1.png"),pygame.image.load("R_P2.png"),pygame.image.load("R_P3.png"),
            pygame.image.load("R_P4.png"),pygame.image.load("R_P5.png"),pygame.image.load("R_P6.png"),
            pygame.image.load("R_P7.png"),pygame.image.load("R_P8.png")]
runrocket4=[pygame.image.load("R_PK1.png"),pygame.image.load("R_PK2.png"),pygame.image.load("R_PK3.png"),
            pygame.image.load("R_PK4.png"),pygame.image.load("R_PK5.png"),pygame.image.load("R_PK6.png"),
            pygame.image.load("R_PK7.png"),pygame.image.load("R_PK8.png")]
runrocket5=[pygame.image.load("R_R1.png"),pygame.image.load("R_R2.png"),pygame.image.load("R_R3.png"),
            pygame.image.load("R_R4.png"),pygame.image.load("R_R5.png"),pygame.image.load("R_R6.png"),
            pygame.image.load("R_R7.png"),pygame.image.load("R_R8.png")]
#
runsnake1=[pygame.image.load("S_B1.png"),pygame.image.load("S_B2.png"),pygame.image.load("S_B3.png"),
           pygame.image.load("S_B4.png"),pygame.image.load("S_B5.png"),pygame.image.load("S_B6.png"),
           pygame.image.load("S_B7.png"),pygame.image.load("S_B8.png")]
runsnake2=[pygame.image.load("S_G1.png"),pygame.image.load("S_G2.png"),pygame.image.load("S_G3.png"),
           pygame.image.load("S_G4.png"),pygame.image.load("S_G5.png"),pygame.image.load("S_G6.png"),
           pygame.image.load("S_G7.png"),pygame.image.load("S_G8.png")]
runsnake3=[pygame.image.load("S_P1.png"),pygame.image.load("S_P2.png"),pygame.image.load("S_P3.png"),
           pygame.image.load("S_P4.png"),pygame.image.load("S_P5.png"),pygame.image.load("S_P6.png"),
           pygame.image.load("S_P7.png"),pygame.image.load("S_P8.png")]
runsnake4=[pygame.image.load("S_PK1.png"),pygame.image.load("S_PK2.png"),pygame.image.load("S_PK3.png"),
           pygame.image.load("S_PK4.png"),pygame.image.load("S_PK5.png"),pygame.image.load("S_PK6.png"),
           pygame.image.load("S_PK7.png"),pygame.image.load("S_PK8.png")]
runsnake5=[pygame.image.load("S_R1.png"),pygame.image.load("S_R2.png"),pygame.image.load("S_R3.png"),
           pygame.image.load("S_R4.png"),pygame.image.load("S_R5.png"),pygame.image.load("S_R6.png"),
           pygame.image.load("S_R7.png"),pygame.image.load("S_R8.png")]
#team17
runteam1=[pygame.image.load("HAI1.png"),pygame.image.load("HAI2.png"),pygame.image.load("HAI3.png"),
          pygame.image.load("HAI4.png"),pygame.image.load("HAI5.png"),pygame.image.load("HAI6.png"),
          pygame.image.load("HAI7.png"),pygame.image.load("HAI8.png")]
runteam2=[pygame.image.load("DUYV1.png"),pygame.image.load("DUYV2.png"),pygame.image.load("DUYV3.png"),
          pygame.image.load("DUYV4.png"),pygame.image.load("DUYV5.png"),pygame.image.load("DUYV6.png"),
          pygame.image.load("DUYV7.png"),pygame.image.load("DUYV8.png")]
runteam3=[pygame.image.load("DUONG1.png"),pygame.image.load("DUONG2.png"),pygame.image.load("DUONG3.png"),
          pygame.image.load("DUONG4.png"),pygame.image.load("DUONG5.png"),pygame.image.load("DUONG6.png"),
          pygame.image.load("DUONG7.png"),pygame.image.load("DUONG8.png")]
runteam4=[pygame.image.load("DUYT1.png"),pygame.image.load("DUYT2.png"),pygame.image.load("DUYT3.png"),
          pygame.image.load("DUYT4.png"),pygame.image.load("DUYT5.png"),pygame.image.load("DUYT6.png"),
          pygame.image.load("DUYT7.png"),pygame.image.load("DUYT8.png")]
runteam5=[pygame.image.load("DUC1.png"),pygame.image.load("DUC2.png"),pygame.image.load("DUC3.png"),
          pygame.image.load("DUC4.png"),pygame.image.load("DUC5.png"),pygame.image.load("DUC6.png"),
          pygame.image.load("DUC7.png"),pygame.image.load("DUC8.png")]
#load image "left"
runlcat1=[pygame.image.load("L_C_B1.png"),pygame.image.load("L_C_B2.png"),pygame.image.load("L_C_B3.png"),#1~blue
          pygame.image.load("L_C_B4.png"),pygame.image.load("L_C_B5.png"),pygame.image.load("L_C_B6.png"),
          pygame.image.load("L_C_B7.png"),pygame.image.load("L_C_B8.png")]
runlcat2=[pygame.image.load("L_C_G1.png"),pygame.image.load("L_C_G2.png"),pygame.image.load("L_C_G3.png"),#2~green
          pygame.image.load("L_C_G4.png"),pygame.image.load("L_C_G5.png"),pygame.image.load("L_C_G6.png"),
          pygame.image.load("L_C_G7.png"),pygame.image.load("L_C_G8.png")]
runlcat3=[pygame.image.load("L_C_P1.png"),pygame.image.load("L_C_P2.png"),pygame.image.load("L_C_P3.png"),#3~purple
          pygame.image.load("L_C_P4.png"),pygame.image.load("L_C_P5.png"),pygame.image.load("L_C_P6.png"),
          pygame.image.load("L_C_P7.png"),pygame.image.load("L_C_P8.png")]
runlcat4=[pygame.image.load("L_C_PK1.png"),pygame.image.load("L_C_PK2.png"),pygame.image.load("L_C_PK3.png"),#4~pink
          pygame.image.load("L_C_PK4.png"),pygame.image.load("L_C_PK5.png"),pygame.image.load("L_C_PK6.png"),
          pygame.image.load("L_C_PK7.png"),pygame.image.load("L_C_PK8.png")]
runlcat5=[pygame.image.load("L_C_R1.png"),pygame.image.load("L_C_R2.png"),pygame.image.load("L_C_R3.png"),#5~red
          pygame.image.load("L_C_R4.png"),pygame.image.load("L_C_R5.png"),pygame.image.load("L_C_R6.png"),
          pygame.image.load("L_C_R7.png"),pygame.image.load("L_C_R8.png")]
#dino
runldino1=[pygame.image.load("L_RunB_1.png"),pygame.image.load("L_RunB_2.png"),pygame.image.load("L_RunB_3.png"),
           pygame.image.load("L_RunB_4.png"),pygame.image.load("L_RunB_5.png"),pygame.image.load("L_RunB_6.png"),
           pygame.image.load("L_RunB_7.png"),pygame.image.load("L_RunB_8.png")]
runldino2=[pygame.image.load("L_RunG_1.png"),pygame.image.load("L_RunG_2.png"),pygame.image.load("L_RunG_3.png"),
           pygame.image.load("L_RunG_4.png"),pygame.image.load("L_RunG_5.png"),pygame.image.load("L_RunG_6.png"),
           pygame.image.load("L_RunG_7.png"),pygame.image.load("L_RunG_8.png")]
runldino3=[pygame.image.load("L_RunP_1.png"),pygame.image.load("L_RunP_2.png"),pygame.image.load("L_RunP_3.png"),
           pygame.image.load("L_RunP_4.png"),pygame.image.load("L_RunP_5.png"),pygame.image.load("L_RunP_6.png"),
           pygame.image.load("L_RunP_7.png"),pygame.image.load("L_RunP_8.png")]
runldino4=[pygame.image.load("L_RunPK_1.png"),pygame.image.load("L_RunPK_2.png"),pygame.image.load("L_RunPK_3.png"),
           pygame.image.load("L_RunPK_4.png"),pygame.image.load("L_RunPK_5.png"),pygame.image.load("L_RunPK_6.png"),
           pygame.image.load("L_RunPK_7.png"),pygame.image.load("L_RunPK_8.png")]
runldino5=[pygame.image.load("L_RunR_1.png"),pygame.image.load("L_RunR_2.png"),pygame.image.load("L_RunR_3.png"),
           pygame.image.load("L_RunR_4.png"),pygame.image.load("L_RunR_5.png"),pygame.image.load("L_RunR_6.png"),
           pygame.image.load("L_RunR_7.png"),pygame.image.load("L_RunB_8.png")]
stand=pygame.image.load("stand.png")
#rocket
runlrocket1=[pygame.image.load("L_R_B1.png"),pygame.image.load("L_R_B2.png"),pygame.image.load("L_R_B3.png"),
             pygame.image.load("L_R_B4.png"),pygame.image.load("L_R_B5.png"),pygame.image.load("L_R_B6.png"),
             pygame.image.load("L_R_B7.png"),pygame.image.load("L_R_B8.png")]
runlrocket2=[pygame.image.load("L_R_G1.png"),pygame.image.load("L_R_G2.png"),pygame.image.load("L_R_G3.png"),
             pygame.image.load("L_R_G4.png"),pygame.image.load("L_R_G5.png"),pygame.image.load("L_R_G6.png"),
             pygame.image.load("L_R_G7.png"),pygame.image.load("L_R_G8.png")]
runlrocket3=[pygame.image.load("L_R_P1.png"),pygame.image.load("L_R_P2.png"),pygame.image.load("L_R_P3.png"),
             pygame.image.load("L_R_P4.png"),pygame.image.load("L_R_P5.png"),pygame.image.load("L_R_P6.png"),
             pygame.image.load("L_R_P7.png"),pygame.image.load("L_R_P8.png")]
runlrocket4=[pygame.image.load("L_R_PK1.png"),pygame.image.load("L_R_PK2.png"),pygame.image.load("L_R_PK3.png"),
             pygame.image.load("L_R_PK4.png"),pygame.image.load("L_R_PK5.png"),pygame.image.load("L_R_PK6.png"),
             pygame.image.load("L_R_PK7.png"),pygame.image.load("L_R_PK8.png")]
runlrocket5=[pygame.image.load("L_R_R1.png"),pygame.image.load("L_R_R2.png"),pygame.image.load("L_R_R3.png"),
             pygame.image.load("L_R_R4.png"),pygame.image.load("L_R_R5.png"),pygame.image.load("L_R_R6.png"),
             pygame.image.load("L_R_R7.png"),pygame.image.load("L_R_R8.png")]
#snake
runlsnake1=[pygame.image.load("L_S_B1.png"),pygame.image.load("L_S_B2.png"),pygame.image.load("L_S_B3.png"),
            pygame.image.load("L_S_B4.png"),pygame.image.load("L_S_B5.png"),pygame.image.load("L_S_B6.png"),
            pygame.image.load("L_S_B7.png"),pygame.image.load("L_S_B8.png")]
runlsnake2=[pygame.image.load("L_S_G1.png"),pygame.image.load("L_S_G2.png"),pygame.image.load("L_S_G3.png"),
            pygame.image.load("L_S_G4.png"),pygame.image.load("L_S_G5.png"),pygame.image.load("L_S_G6.png"),
            pygame.image.load("L_S_G7.png"),pygame.image.load("L_S_G8.png")]
runlsnake3=[pygame.image.load("L_S_P1.png"),pygame.image.load("L_S_P2.png"),pygame.image.load("L_S_P3.png"),
            pygame.image.load("L_S_P4.png"),pygame.image.load("L_S_P5.png"),pygame.image.load("L_S_P6.png"),
            pygame.image.load("L_S_P7.png"),pygame.image.load("L_S_P8.png")]
runlsnake4=[pygame.image.load("L_S_PK1.png"),pygame.image.load("L_S_PK2.png"),pygame.image.load("L_S_PK3.png"),
            pygame.image.load("L_S_PK4.png"),pygame.image.load("L_S_PK5.png"),pygame.image.load("L_S_PK6.png"),
            pygame.image.load("L_S_PK7.png"),pygame.image.load("L_S_PK8.png")]
runlsnake5=[pygame.image.load("L_S_R1.png"),pygame.image.load("L_S_R2.png"),pygame.image.load("L_S_R3.png"),
            pygame.image.load("L_S_R4.png"),pygame.image.load("L_S_R5.png"),pygame.image.load("L_S_R6.png"),
            pygame.image.load("L_S_R7.png"),pygame.image.load("L_S_R8.png")]
#team17
runlteam1=[pygame.image.load("L_HAI1.png"),pygame.image.load("L_HAI2.png"),pygame.image.load("L_HAI3.png"),
           pygame.image.load("L_HAI4.png"),pygame.image.load("L_HAI5.png"),pygame.image.load("L_HAI6.png"),
           pygame.image.load("L_HAI7.png"),pygame.image.load("L_HAI8.png")]
runlteam2=[pygame.image.load("L_DUYV1.png"),pygame.image.load("L_DUYV2.png"),pygame.image.load("L_DUYV3.png"),
           pygame.image.load("L_DUYV4.png"),pygame.image.load("L_DUYV5.png"),pygame.image.load("L_DUYV6.png"),
           pygame.image.load("L_DUYV7.png"),pygame.image.load("L_DUYV8.png")]
runlteam3=[pygame.image.load("L_DUONG1.png"),pygame.image.load("L_DUONG2.png"),pygame.image.load("L_DUONG3.png"),
           pygame.image.load("L_DUONG4.png"),pygame.image.load("L_DUONG5.png"),pygame.image.load("L_DUONG6.png"),
           pygame.image.load("L_DUONG7.png"),pygame.image.load("L_DUONG8.png")]
runlteam4=[pygame.image.load("L_DUYT1.png"),pygame.image.load("L_DUYT2.png"),pygame.image.load("L_DUYT3.png"),
           pygame.image.load("L_DUYT4.png"),pygame.image.load("L_DUYT5.png"),pygame.image.load("L_DUYT6.png"),
           pygame.image.load("L_DUYT7.png"),pygame.image.load("L_DUYT8.png")]
runlteam5=[pygame.image.load("L_DUC1.png"),pygame.image.load("L_DUC2.png"),pygame.image.load("L_DUC3.png"),
           pygame.image.load("L_DUC4.png"),pygame.image.load("L_DUC5.png"),pygame.image.load("L_DUC6.png"),
           pygame.image.load("L_DUC7.png"),pygame.image.load("L_DUC8.png")]
thingImg1=pygame.image.load("thing.png")#minigame
delta=5 #step player in minigame
walk_right=[pygame.image.load("R1E.png"),pygame.image.load("R2E.png"),pygame.image.load("R3E.png"),pygame.image.load("R4E.png"),
            pygame.image.load("R5E.png"),pygame.image.load("R6E.png"),pygame.image.load("R7E.png"),pygame.image.load("R8E.png"),
            pygame.image.load("R9E.png")]
walk_left=[pygame.image.load("L1E.png"),pygame.image.load("L2E.png"),pygame.image.load("L3E.png"),pygame.image.load("L4E.png"),
           pygame.image.load("L5E.png"),pygame.image.load("L6E.png"),pygame.image.load("L7E.png"),pygame.image.load("L8E.png"),
           pygame.image.load("L9E.png")]
icon=pygame.image.load("icon.jpg")
gameoversound=pygame.mixer.Sound("gameover.wav")
startsound=pygame.mixer.Sound("start.wav")
pygame.display.set_icon(icon)
deltaspeed1=disp.get_height()/230000
deltaspeed2=disp.get_height()/380000
fps=pygame.time.Clock()
#incantation
FASTER=pygame.image.load("FASTER.png")
SLOWER=pygame.image.load("SLOWER.png")
RETURN=pygame.image.load("RETURN.png")
START=pygame.image.load("START.png")
FINISH=pygame.image.load("FINISH.png")
STOP=pygame.image.load("STOP.png")
FASTERSHOP=pygame.image.load("FASTERSHOP.png")
SLOWERSHOP=pygame.image.load("SLOWERSHOP.png")
RETURNSHOP=pygame.image.load("RETURNSHOP.png")
STARTSHOP=pygame.image.load("STARTSHOP.png")
FINISHSHOP=pygame.image.load("FINISHSHOP.png")
STOPSHOP=pygame.image.load("STOPSHOP.png")
#            R        G       B
BLACK=      (0  ,     0,     0 )
VIOLET=     (82	,     9,    108)
WHITE=      (255,   255,    255)
BLUE=       (0  ,     0,    255)
GREEN=      (0  ,   255,     0 )
BGREEN=     (0  ,   190,     0 )
RED=        (255,     0,     0 )
BRED=       (190,     0,     0 )
YELLOW=     (255,   255,     0 )
#MiniGame
class player(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=24
        self.height=53
        self.jump=False
        self.right=False
        self.left=False
        self.jumpcount=10
        self.walk=0
    def draw(self,disp): #animation minigame
        if (self.walk>20):
            self.walk=0
        if self.right:
            disp.blit(walk_right[self.walk//3],(self.x,self.y))
            self.walk+=1
        elif self.left:
            disp.blit(walk_left[self.walk//3],(self.x,self.y))
            self.walk+=1
        else:
            disp.blit(stand,(self.x,self.y))
class things(object):
    def __init__(self,thingx,thingy,thingImg):
        self.thingx=thingx
        self.thingy=thingy
        self.thingw=43
        self.thingh=145
        self.speedx=6
        self.speedy=6
        self.thingImg=thingImg
    def drawthing(self,disp):
        disp.blit(self.thingImg,(self.thingx,self.thingy))
def draw_disp():#draw display minigame
    evil.draw(disp)
    thing1.drawthing(disp)
    thing2.drawthing(disp)
    thing3.drawthing(disp)
    thing4.drawthing(disp)
    thing5.drawthing(disp)
    thing6.drawthing(disp)
    thing7.drawthing(disp)
#initialize the variable in minigame
start1=random.randrange(0,1040-157)
start2=random.randrange(0,1040-157)
start3=random.randrange(0,1040-157)
start4=random.randrange(0,1040-157)
start5=random.randrange(0,1040-157)
start6=random.randrange(0,1040-157)
start7=random.randrange(0,1040-157)
evil=player(disp.get_width()/2,disp.get_height()*0.9)
thing1=things(start1,-200,thingImg1)
thing2=things(start2,-200,thingImg1)
thing3=things(start3,-200,thingImg1)
thing4=things(start4,-200,thingImg1)
thing5=things(start5,-200,thingImg1)
thing6=things(start6,-200,thingImg1)
thing7=things(start7,-200,thingImg1)
def resizeMain(w,h):
    global disp,bg,run1,run2,run3,run4,run5,y1,y2,y3,y4,y5,guide1,guide2,in4
    old_disp_saved_main = disp
    disp = pygame.display.set_mode((w,h),pygame.RESIZABLE)
    disp.blit(old_disp_saved_main, (0,0))
    bg=pygame.transform.scale(bg,(w,h))
    guide1=pygame.transform.scale(guide1,(w,h))
    guide2=pygame.transform.scale(guide2,(w,h))
    in4=pygame.transform.scale(in4,(w,h))
    y1=int(disp.get_height()/29.25)
    y2=int(disp.get_height()/3.75)
    y3=int(disp.get_height()/2.2)
    y4=int(disp.get_height()/1.5)
    y5=int(disp.get_height()/1.15)
    del old_disp_saved_main
def resizeshop(w,h):
    global disp,ItemShop
    old_disp_saved_main = disp
    disp = pygame.display.set_mode((w,h),pygame.RESIZABLE)
    disp.blit(old_disp_saved_main, (0,0))
    ItemShop=pygame.transform.scale(ItemShop,(w,h))
    del old_disp_saved_main
def resizeranking(w,h):
    global disp,showranking
    old_disp_saved_main = disp
    disp = pygame.display.set_mode((w,h),pygame.RESIZABLE)
    disp.blit(old_disp_saved_main, (0,0))
    showranking=pygame.transform.scale(showranking,(w,h))
    del old_disp_saved_main
def resizestart(w,h):
    global disp,menu,menuBD,bet
    old_disp_saved_main = disp
    disp = pygame.display.set_mode((w,h),pygame.RESIZABLE)
    disp.blit(old_disp_saved_main, (0,0))
    menu=pygame.transform.scale(menu,(w,h))
    menuBD=pygame.transform.scale(menuBD,(w,h))
    bet=pygame.transform.scale(bet,(w,h))
    del old_disp_saved_main
def resizeSelectSet(w,h):
    global disp,selectset
    old_disp_saved_main = disp
    disp = pygame.display.set_mode((w,h),pygame.RESIZABLE)
    disp.blit(old_disp_saved_main, (0,0))
    selectset=pygame.transform.scale(selectset,(w,h))
    del old_disp_saved_main
def resizeSelectCharacter(w,h):
    global disp,selectcat,selectdino,selectrocket,selectsnake,selectteam
    old_disp_saved_main = disp
    disp = pygame.display.set_mode((w,h),pygame.RESIZABLE)
    disp.blit(old_disp_saved_main, (0,0))
    selectcat=pygame.transform.scale(selectcat,(w,h))
    selectdino=pygame.transform.scale(selectdino,(w,h))
    selectrocket=pygame.transform.scale(selectrocket,(w,h))
    selectsnake=pygame.transform.scale(selectsnake,(w,h))
    selectteam=pygame.transform.scale(selectteam,(w,h))
    del old_disp_saved_main
def resizeSign(w,h):
    global disp,sign,menuBD
    old_disp_saved_main = disp
    disp = pygame.display.set_mode((w,h),pygame.RESIZABLE)
    disp.blit(old_disp_saved_main, (0,0))
    sign=pygame.transform.scale(sign,(w,h))
    del old_disp_saved_main
def resizecoin(w,h):
    global disp,entercoin
    old_disp_saved_main = disp
    disp = pygame.display.set_mode((w,h),pygame.RESIZABLE)
    disp.blit(old_disp_saved_main, (0,0))
    entercoin=pygame.transform.scale(entercoin,(w,h))
    del old_disp_saved_main
def resize(w,h):
    global disp,bgm,bgm1,bgm2,bgm3,bgm4,walk_right,walk_left,thingImg1
    old_disp_saved = disp
    disp = pygame.display.set_mode((w,h),pygame.RESIZABLE)
    disp.blit(old_disp_saved, (0,0))
    randomStart(w,h)
    evil.y=int(h*0.9)-evil.height-5
    delta=int(w/208)
    bgm=pygame.transform.scale(bgm,(w,h))
    bgm1=pygame.transform.scale(bgm1,(w,h))
    bgm2=pygame.transform.scale(bgm2,(w,h))
    bgm3=pygame.transform.scale(bgm3,(w,h))
    bgm4=pygame.transform.scale(bgm4,(w,h))
    deltaspeed1=int(h/234000)
    deltaspeed2=int(h/390000)
    thing1.speedy=int(h/140)
    thing2.speedy=int(h/135)
    thing3.speedy=int(h/130)
    thing4.speedy=int(h/125)
    thing5.speedy=int(h/120)
    thing6.speedy=int(h/115)
    thing7.speedy=int(h/110)
    del old_disp_saved
def randomStart(w,h):
    start1=random.randrange(0,w-157)
    start2=random.randrange(0,w-157)
    start3=random.randrange(0,w-157)
    start4=random.randrange(0,w-157)
    start5=random.randrange(0,w-157)
    start6=random.randrange(0,w-157)
    start7=random.randrange(0,w-157)
    thing1=things(start1,-200,thingImg1)
    thing2=things(start2,-200,thingImg1)
    thing3=things(start3,-200,thingImg1)
    thing4=things(start4,-200,thingImg1)
    thing5=things(start5,-200,thingImg1)
    thing6=things(start6,-200,thingImg1)
    thing7=things(start7,-200,thingImg1)
def terminate():
    pygame.quit()
    sys.exit()
def text_objiect(text,font):
    textsurf=font.render(text,True,BLACK)
    return textsurf,textsurf.get_rect()
def drawscore(score):
    textfont=pygame.font.Font("freesansbold.ttf",20)
    text,textrect=text_objiect("SCORE: "+str(score),textfont)
    textrect.center=(700,50)
    disp.blit(text,textrect)
def stopMain(x1,x2,x3,x4,x5,disp_width): #gameoverMain
    if x1>=(97*disp.get_width())/104 and x2>=(97*disp.get_width())/104 and x3>=(97*disp.get_width())/104 and x4>=(97*disp.get_width())/104 and x5>=(97*disp.get_width())/104:
        return True
    return False
def stop(x1,y1,w1,h1,x2,y2,w2,h2): #gameover
    if (abs(x1+w1/2-x2-w2/2)<=(w1/2+w2/2) and abs(y1+h1/2-y2-h2/2)<=(h1/2+h2/2)):
        return True
    return False
def GameloopMain(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5, item):
    global gamewin
    pygame.mixer.music.load("ingame.mp3")
    pygame.mixer.music.play(-1)
    pos1=-1
    pos2=-1
    pos3=-1
    pos4=-1
    pos5=-1
    walk1=0
    walk2=0
    walk3=0
    walk4=0
    walk5=0
    walk=0
    counttemp=1
    tempwin=1
    lane1=0
    lane2=0
    lane3=0
    lane4=0
    lane5=0
    temp1=0
    temp2=0
    temp3=0
    temp4=0
    temp5=0
    localx=[]
    localy=[]
    isItem=False
    jumpcount=10
    xtemp=0
    type_incantation=[]
    state=[]
    state_item=False
    list_type=["FASTER","SLOWER","RETURN","STOP","START","FINISH"]
    dic={"FASTER":FASTER,"SLOWER":SLOWER,"RETURN":RETURN,"STOP":STOP,"START":START,"FINISH":FINISH}
    dicshop={"FASTERSHOP":FASTERSHOP,"SLOWERSHOP":SLOWERSHOP,"RETURNSHOP":RETURNSHOP,"STOPSHOP":STOPSHOP,"STARTSHOP":STARTSHOP,"FINISHSHOP":FINISHSHOP}
    list_y=[int(disp.get_height()/29.25),int(disp.get_height()/3.75),int(disp.get_height()/2.2),int(disp.get_height()/1.5),int(disp.get_height()/1.15)]
    count_incantation=random.randrange(1,6)
    for i in range(0,count_incantation):
        localx.append(random.randrange(int(disp.get_width()*0.2),int(disp.get_width()*0.7)))
        localy.append(random.choice(list_y))
        type_incantation.append(random.choice(list_type))
        state.append(True)
    count_faster1=40
    count_slower1=100
    count_stop1=80
    count_return1=40
    isReturn1=False
    #
    count_faster2=40
    count_slower2=100
    count_stop2=80
    count_return2=40
    isReturn2=False
    #
    count_faster3=40
    count_slower3=100
    count_stop3=80
    count_return3=40
    isReturn3=False
    #
    count_faster4=40
    count_slower4=100
    count_stop4=80
    count_return4=40
    isReturn4=False
    
    #
    count_faster5=40
    count_slower5=100
    count_stop5=80
    count_return5=40
    isReturn5=False
    #
    count_faster_shop=40
    global x1,x2,x3,x4,x5,y1,y2,y3,y4,y5,rank1,rank2,rank3,rank4,rank5,statistic,state_star
    statistic = False
    state_star=False
    x1=0
    y1=int(disp.get_height()/29.25)
    x2=0
    y2=int(disp.get_height()/3.75)
    x3=0
    y3=int(disp.get_height()/2.2)
    x4=0
    y4=int(disp.get_height()/1.5)
    x5=0
    y5=int(disp.get_height()/1.15)
    speed=[0.1,0.4,0.8,1.4,1.6,2,3,3.2]
    if mychar == 1:
        list_y2=[y2, y3, y4, y5]
    elif mychar == 2:
        list_y2=[y1, y3, y4, y5]
    elif mychar == 3:
        list_y2=[y1, y2, y4, y5]
    elif mychar == 4:
        list_y2=[y1, y2, y3, y5]
    elif mychar == 5:
        list_y2=[y1, y2, y3, y4]
    list_type2=["SLOWERSHOP","RETURNSHOP","STOPSHOP","STARTSHOP"]
    if item == 2:
        state_item=True
        localx2=random.randrange(int(disp.get_width()*0.2),int(disp.get_width()*0.8))
        localy2=random.choice(list_y2)
        type_incantation2=random.choice(list_type2)
    if item == 1:
        state_item=True
        itemx = random.randrange(int(disp.get_width()*0.2),int(disp.get_width()*0.8))
        if mychar == 1:
            itemy = y1
        elif mychar == 2:
            itemy = y2
        elif mychar == 3:
            itemy = y3
        elif mychar == 4:
            itemy = y4
        elif mychar == 5:
            itemy = y5
    while True:
        fps.tick(60)
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            if event.type==VIDEORESIZE:
                resizeMain(event.w,event.h)
                resizestart(event.w,event.h)
                resizecoin(event.w,event.h)
                resize(event.w,event.h)
                resizeranking(event.w,event.h)
                resizeshop(event.w,event.h)
                resizeSelectSet(event.w,event.h)
                resizeSelectCharacter(event.w,event.h)
                y1=event.h/29.25
                y2=event.h/3.75
                y3=event.h/2.1
                y4=event.h/1.5
                y5=event.h/1.15
        pygame.display.update()
        disp.blit(bg,(0,0))
        delta1=random.choice(speed)
        delta2=random.choice(speed)
        delta3=random.choice(speed)
        delta4=random.choice(speed)
        delta5=random.choice(speed)
        if (item == 1):
            if state_item:
                disp.blit(FASTERSHOP,(itemx, itemy))
                if mychar == 1:
                    if x1>=itemx:
                        if count_faster_shop>0:
                            delta1=max(speed)
                            count_faster_shop-=1
                        if count_faster_shop==0:
                            count_faster_shop=40
                            state_item = False
                elif mychar == 2:
                    if x2>=itemx:
                        if count_faster_shop>0:
                            delta2=max(speed)
                            count_faster_shop-=1
                        if count_faster_shop==0:
                            count_faster_shop=40
                            state_item = False
                elif mychar == 3:
                    if x3>=itemx:
                        if count_faster_shop>0:
                            delta3=max(speed)
                            count_faster_shop-=1
                        if count_faster_shop==0:
                            count_faster_shop=40
                            state_item = False
                elif mychar == 4:
                    if x4>=itemx:
                        if count_faster_shop>0:
                            delta4=max(speed)
                            count_faster_shop-=1
                        if count_faster_shop==0:
                            count_faster_shop=40
                            state_item = False
                elif mychar == 5:
                    if x5>=itemx:
                        if count_faster_shop>0:
                            delta5=max(speed)
                            count_faster_shop-=1
                        if count_faster_shop==0:
                            count_faster_shop=40
                            state_item = False
        if (item == 2):
            if state_item:
                disp.blit(dicshop[type_incantation2],(localx2, localy2))
                if localy2 == y1 and x1 >= localx2:
                        if type_incantation2=="SLOWERSHOP":
                            if count_slower1>0:
                                delta1=min(speed)*5
                                count_slower1-=1
                            if count_slower1==0:
                                state_item = False
                                count_slower1=100
                        elif type_incantation2=="STOPSHOP":
                            if count_stop1>0:
                                delta1=0
                                walk1=0
                                count_stop1-=1
                            if count_stop1==0:
                                state_item = False
                                count_stop1=80
                        elif type_incantation2=="STARTSHOP":
                            x1=0
                            disp.blit(run1[int(walk1)//4],(x1,y1))
                            pygame.display.update()
                            state_item = False
                        else:
                            isReturn1 = True
                            isItemp=True
                if localy2 == y2 and x2 >= localx2:
                        if type_incantation2=="SLOWERSHOP":
                            if count_slower2>0:
                                delta2=min(speed)*5
                                count_slower2-=1
                            if count_slower2==0:
                                state_item = False
                                count_slower2=100
                        elif type_incantation2=="STOPSHOP":
                            if count_stop2>0:
                                delta2=0
                                walk2=0
                                count_stop2-=1
                            if count_stop2==0:
                                state_item = False
                                count_stop2=80
                        elif type_incantation2=="STARTSHOP":
                            x2=0
                            disp.blit(run2[int(walk2)//4],(x2,y2))
                            pygame.display.update()
                            state_item = False
                        else:
                            isReturn2 = True
                            isItem = True
                if localy2 == y3 and x3 >= localx2:
                        if type_incantation2=="SLOWERSHOP":
                            if count_slower2>0:
                                delta3=min(speed)*5
                                count_slower3-=1
                            if count_slower3==0:
                                state_item = False
                                count_slower3=100
                        elif type_incantation2=="STOPSHOP":
                            if count_stop3>0:
                                delta3=0
                                walk3=0
                                count_stop3-=1
                            if count_stop3==0:
                                state_item = False
                                count_stop3=80
                        elif type_incantation2=="STARTSHOP":
                            x3=0
                            disp.blit(run3[int(walk3)//4],(x3,y3))
                            pygame.display.update()
                            state_item = False
                        else:
                            isReturn3 = True
                            isItem=True
                if localy2 == y4 and x4 >= localx2:
                        if type_incantation2=="SLOWERSHOP":
                            if count_slower4>0:
                                delta4=min(speed)*5
                                count_slower4-=1
                            if count_slower4==0:
                                state_item = False
                                count_slower4=100
                        elif type_incantation2=="STOPSHOP":
                            if count_stop4>0:
                                delta4=0
                                walk4=0
                                count_stop4-=1
                            if count_stop4==0:
                                state_item = False
                                count_stop4=80
                        elif type_incantation2=="STARTSHOP":
                            x4=0
                            disp.blit(run4[int(walk4)//4],(x4,y4))
                            pygame.display.update()
                            state_item = False
                        else:
                            isReturn4 = True
                            isItem = True
                if localy2 == y5 and x5 >= localx2:
                        if type_incantation2=="SLOWERSHOP":
                            if count_slower5>0:
                                delta5=min(speed)*5
                                count_slower5-=1
                            if count_slower5==0:
                                state_item = False
                                count_slower5=100
                        elif type_incantation2=="STOPSHOP":
                            if count_stop5>0:
                                delta5=0
                                walk5=0
                                count_stop5-=1
                            if count_stop5==0:
                                state_item = False
                                count_stop5=80
                        elif type_incantation2=="STARTSHOP":
                            x5=0
                            disp.blit(run5[int(walk5)//4],(x5,y5))
                            pygame.display.update()
                            state_item = False
                        else:
                            isReturn5 = True
                            isItem = True
        if item==3:
            state_star=True
        for i in range(0,count_incantation):
            if state[i]:
                disp.blit(dic[type_incantation[i]],(localx[i],localy[i]))
                if x1>=localx[i] and y1==localy[i]:
                    if type_incantation[i]=="FASTER":
                        if count_faster1>0:
                            delta1=max(speed)
                            count_faster1-=1
                        if count_faster1==0:
                            state[i]=False
                            count_faster1=20
                    elif type_incantation[i]=="SLOWER":
                        if count_slower1>0:
                            delta1=min(speed)*5
                            count_slower1-=1
                        if count_slower1==0:
                            state[i]=False
                            count_slower1=100
                    elif type_incantation[i]=="STOP":
                        if count_stop1>0:
                            walk1=0
                            delta1=0
                            count_stop1-=1
                        if count_stop1==0:
                            state[i]=False
                            count_stop1=80
                    elif type_incantation[i]=="START":
                        x1=0
                        disp.blit(run1[int(walk1)//4],(x1,y1))
                        pygame.display.update()
                        state[i]=False
                    elif type_incantation[i]=="FINISH":
                        x1=(97*disp.get_width())/104
                        disp.blit(run1[int(walk1)//4],(x1,y1))
                        pygame.display.update()
                        state[i]=False
                    else:
                        isReturn1=True
                        pos1=i
                if x2>=localx[i] and y2==localy[i]:
                    if type_incantation[i]=="FASTER":
                        if count_faster2>0:
                            delta2=max(speed)
                            count_faster2-=1
                        if count_faster2==0:
                            state[i]=False
                            count_faster2=20
                    elif type_incantation[i]=="SLOWER":
                        if count_slower2>0:
                            delta2=min(speed)*5
                            count_slower2-=1
                        if count_slower2==0:
                            state[i]=False
                            count_slower2=100
                    elif type_incantation[i]=="STOP":
                        if count_stop2>0:
                            walk2=0
                            delta2=0
                            count_stop2-=1
                        if count_stop2==0:
                            state[i]=False
                            count_stop2=80
                    elif type_incantation[i]=="START":
                        x2=0
                        disp.blit(run2[int(walk2)//4],(x2,y2))
                        pygame.display.update()
                        state[i]=False
                    elif type_incantation[i]=="FINISH":
                        x2=(97*disp.get_width())/104
                        disp.blit(run2[int(walk2)//4],(x2,y2))
                        pygame.display.update()
                        state[i]=False
                    else:
                        isReturn2=True
                        pos2=i
                if x3>=localx[i] and y3==localy[i]:
                    if type_incantation[i]=="FASTER":
                        if count_faster3>0:
                            delta3=max(speed)
                            count_faster3-=1
                        if count_faster3==0:
                            state[i]=False
                            count_faster3=20
                    elif type_incantation[i]=="SLOWER":
                        if count_slower2>0:
                            delta3=min(speed)*5
                            count_slower3-=1
                        if count_slower3==0:
                            state[i]=False
                            count_slower3=100
                    elif type_incantation[i]=="STOP":
                        if count_stop3>0:
                            walk3=0
                            delta3=0
                            count_stop3-=1
                        if count_stop3==0:
                            state[i]=False
                            count_stop3=80
                    elif type_incantation[i]=="START":
                        x3=0
                        disp.blit(run3[int(walk3)//4],(x3,y3))
                        pygame.display.update()
                        state[i]=False
                    elif type_incantation[i]=="FINISH":
                        x3=(97*disp.get_width())/104
                        disp.blit(run2[int(walk3)//4],(x3,y3))
                        pygame.display.update()
                        state[i]=False
                    else:
                        isReturn3=True
                        pos3=i
                if x4>=localx[i] and y4==localy[i]:
                    if type_incantation[i]=="FASTER":
                        if count_faster4>0:
                            delta4=max(speed)
                            count_faster4-=1
                        if count_faster4==0:
                            state[i]=False
                            count_faster4=20
                    elif type_incantation[i]=="SLOWER":
                        if count_slower4>0:
                            delta4=min(speed)*5
                            count_slower4-=1
                        if count_slower4==0:
                            state[i]=False
                            count_slower4=100
                    elif type_incantation[i]=="STOP":
                        if count_stop4>0:
                            walk4=0
                            delta4=0
                            count_stop4-=1
                        if count_stop4==0:
                            state[i]=False
                            count_stop4=80
                    elif type_incantation[i]=="START":
                        x4=0
                        disp.blit(run4[int(walk4)//4],(x4,y4))
                        pygame.display.update()
                        state[i]=False
                    elif type_incantation[i]=="FINISH":
                        x4=(97*disp.get_width())/104
                        disp.blit(run4[int(walk4)//4],(x4,y4))
                        pygame.display.update()
                        state[i]=False
                    else:
                        isReturn4=True
                        pos4=i
                if x5>=localx[i] and y5==localy[i]:
                    if type_incantation[i]=="FASTER":
                        if count_faster5>0:
                            delta5=max(speed)
                            count_faster5-=1
                        if count_faster5==0:
                            state[i]=False
                            count_faster5=20
                    elif type_incantation[i]=="SLOWER":
                        if count_slower5>0:
                            delta5=min(speed)*5
                            count_slower5-=1
                        if count_slower5==0:
                            state[i]=False
                            count_slower5=100
                    elif type_incantation[i]=="STOP":
                        if count_stop5>0:
                            walk5=0
                            delta5=0
                            count_stop5-=1
                        if count_stop5==0:
                            state[i]=False
                            count_stop5=80
                    elif type_incantation[i]=="START":
                        x5=0
                        disp.blit(run5[int(walk5)//4],(x5,y5))
                        pygame.display.update()
                        state[i]=False
                    elif type_incantation[i]=="FINISH":
                        x5=(97*disp.get_width())/104
                        disp.blit(run5[int(walk5)//4],(x5,y5))
                        pygame.display.update()
                        state[i]=False
                    else:
                        isReturn5=True
                        pos5=i
        if not isReturn1:
            if lane1!=1:
                disp.blit(run1[int(walk1)//4],(x1,y1))
        else:
            if count_return1>0:
                delta1=-max(speed)
                disp.blit(runl1[int(walk1)//4],(x1,y1))
                count_return1-=1
            if count_return1==0:
                if not isItem:
                    isReturn1=False
                    state[pos1]=False
                    count_return1=30
                else:
                    isReturn1=False
                    state_item=False
                    isItem=False
                    count_return1=30
        if not isReturn2:
            if lane2!=1:
                disp.blit(run2[int(walk2)//4],(x2,y2))
        else:
            if count_return2>0:
                delta2=-max(speed)
                disp.blit(runl2[int(walk2)//4],(x2,y2))
                count_return2-=1
            if count_return2==0:
                if not isItem:
                    isReturn2=False
                    state[pos2]=False
                    count_return2=30
                else:
                    isReturn2=False
                    state_item=False
                    isItem=False
                    count_return2=30
        if not isReturn3:
            if lane3!=1:
                disp.blit(run3[int(walk3)//4],(x3,y3))
        else:
            if count_return3>0:
                delta3=-max(speed)
                disp.blit(runl3[int(walk3)//4],(x3,y3))
                count_return3-=1
            if count_return3==0:
                if not isItem:
                    isReturn3=False
                    state[pos3]=False
                    count_return3=30
                else:
                    isReturn3=False
                    state_item=False
                    isItem=False
                    count_return3=30
        if not isReturn4:
            if lane4!=1:
                disp.blit(run4[int(walk4)//4],(x4,y4))
        else:
            if count_return4>0:
                delta4=-max(speed)
                disp.blit(runl4[int(walk4)//4],(x4,y4))
                count_return4-=1
            if count_return4==0:
                if not isItem:
                    isReturn4=False
                    state[pos4]=False
                    count_return4=30
                else:
                    isReturn4=False
                    state_item=False
                    isItem=False
                    count_return4=30
        if not isReturn5:
            if lane5!=1:
                disp.blit(run5[int(walk5)//4],(x5,y5))
        else:
            if count_return5>0:
                delta5=-max(speed)
                disp.blit(runl5[int(walk5)//4],(x5,y5))
                count_return5-=1
            if count_return5==0:
                if not isItem:
                    isReturn5=False
                    state[pos5]=False
                    count_return2=30
                else:
                    isReturn5=False
                    state_item=False
                    isItem=False
                    count_return2=30
        if walk1>23:
            walk1=0
        if walk2>23:
            walk2=0
        if walk3>23:
            walk3=0
        if walk4>23:
            walk4=0
        if walk5>23:
            walk5=0
#ranking
        if (Finish(x1)==True):
            walk1=0
            delta1=0
            if (temp1==0):
                lane1=counttemp
                counttemp+=1
                temp1+=1
        if (Finish(x2)==True):
            walk2=0
            delta2=0
            if (temp2==0):
                lane2=counttemp
                counttemp+=1
                temp2+=1
        if (Finish(x3)==True):
            walk3=0
            delta3=0
            if (temp3==0):
                lane3=counttemp
                counttemp+=1
                temp3+=1
        if (Finish(x4)==True):
            walk4=0
            delta4=0
            if (temp4==0):
                lane4=counttemp
                counttemp+=1
                temp4+=1
        if (Finish(x5)==True):
            walk5=0
            delta5=0
            if (temp5==0):
                lane5=counttemp
                counttemp+=1
                temp5+=1
        if lane1==1:
            xtemp=int(disp.get_width()/2)
            if jumpcount>=-10:
                y1-=(jumpcount*abs(jumpcount)*0.3)
                jumpcount-=1
            else:
                y1=int(disp.get_height()/29.25)
                jumpcount=10
            if 0<walk%20<10:
                disp.blit(runl1[int(walk1)//4],(xtemp,y1))
            else:
                disp.blit(run1[int(walk1)//4],(xtemp,y1))
            disp.blit(king,(xtemp+10,y1-20))
            pygame.display.update()
        if lane1==1:
            rank1=1
        if lane1==2:
            rank2=1
        if lane1==3:
            rank3=1
        if lane1==4:
            rank4=1
        if lane1==5:
            rank5=1
        if lane2==1:
            xtemp=int(disp.get_width()/2)
            if jumpcount>=-10:
                y2-=(jumpcount*abs(jumpcount)*0.3)
                jumpcount-=1
            else:
                y2=int(disp.get_height()/3.75)
                jumpcount=10
            if 0<walk%20<10:
                disp.blit(runl2[int(walk2)//4],(xtemp,y2))
            else:
                disp.blit(run2[int(walk2)//4],(xtemp,y2))
            disp.blit(king,(xtemp+10,y2-20))
            pygame.display.update()
        if lane2==1:
            rank1=2
        if (lane2==2):
            rank2=2
        if (lane2==3):
            rank3=2
        if (lane2==4):
            rank4=2
        if (lane2==5):
            rank5=2
        if (lane3==1):
            xtemp=int(disp.get_width()/2)
            if jumpcount>=-10:
                y3-=(jumpcount*abs(jumpcount)*0.3)
                jumpcount-=1
            else:
                y3=int(disp.get_height()/2.2)
                jumpcount=10
            if 0<walk%20<10:
                disp.blit(runl3[int(walk3)//4],(xtemp,y3))
            else:
                disp.blit(run3[int(walk3)//4],(xtemp,y3))
            disp.blit(king,(xtemp+10,y3-20))
            pygame.display.update()
        if lane3==1:
            rank1=3
        if (lane3==2):
            rank2=3
        if (lane3==3):
            rank3=3
        if (lane3==4):
            rank4=3
        if (lane3==5):
            rank5=3
        if (lane4==1):
            xtemp=int(disp.get_width()/2)
            if jumpcount>=-10:
                y4-=(jumpcount*abs(jumpcount)*0.3)
                jumpcount-=1
            else:
                y4=int(disp.get_height()/1.5)
                jumpcount=10
            if 0<walk%20<10:
                disp.blit(runl4[int(walk4)//4],(xtemp,y4))
            else:
                disp.blit(run4[int(walk4)//4],(xtemp,y4))
            disp.blit(king,(xtemp+10,y4-20))
            pygame.display.update()
        if lane4==1:
            rank1=4
        if (lane4==2):
            rank2=4
        if (lane4==3):
            rank3=4
        if (lane4==4):
            rank4=4
        if (lane4==5):
            rank5=4
        if (lane5==1):
            xtemp=int(disp.get_width()/2)
            if jumpcount>=-10:
                y5-=(jumpcount*abs(jumpcount)*0.3)
                jumpcount-=1
            else:
                y5=int(disp.get_height()/1.15)
                jumpcount=10
            if 0<walk%20<10:
                disp.blit(runl5[int(walk5)//4],(xtemp,y5))
            else:
                disp.blit(run5[int(walk5)//4],(xtemp,y5))
            disp.blit(king,(xtemp+10,y5-20))
            pygame.display.update()
        if lane5==1:
            rank1=5
        if (lane5==2):
            rank2=5
        if (lane5==3):
            rank3=5
        if (lane5==4):
            rank4=5
        if (lane5==5):
            rank5=5
        if (mychar == rank1):
            statistic = True
            if (tempwin==1):
                gamewin+=1
                tempwin+=1
        if stopMain(x1,x2,x3,x4,x5,disp_width):
            GameoverMain(rank1,rank2,rank3,rank4,rank5,statistic,state_star,ranking1,ranking2,ranking3,ranking4,ranking5)
        x1+=delta1
        x2+=delta2
        x3+=delta3
        x4+=delta4
        x5+=delta5
        walk1+=1
        walk2+=1
        walk3+=1
        walk4+=1
        walk5+=1
        walk+=1
        pygame.display.update()
def Finish(n):
    if ((97*disp.get_width())/104-n<=0) and ((97*disp.get_width())/104-n>=-22) :
        return True
    return False
def Gameloop(): #gameloop minigame
    temp=0
    pygame.mixer.music.load("back.mp3")
    pygame.mixer.music.play(-1)
    score=0
    evil.x=disp.get_width()/2
    evil.y=disp.get_height()*0.9-evil.height-5
    thing1.thingx=random.randrange(0,disp.get_width()-157)
    thing2.thingx=random.randrange(0,disp.get_width()-157)
    thing3.thingx=random.randrange(0,disp.get_width()-157)
    thing4.thingx=random.randrange(0,disp.get_width()-157)
    thing5.thingx=random.randrange(0,disp.get_width()-157)
    thing6.thingx=random.randrange(0,disp.get_width()-157)
    thing7.thingx=random.randrange(0,disp.get_width()-157)
    thing1.thingy=-200
    thing2.thingy=-200
    thing3.thingy=-200
    thing4.thingy=-200
    thing5.thingy=-200
    thing6.thingy=-200
    thing7.thingy=-200
    thing1.speedy=4
    thing2.speedy=4.2
    thing3.speedy=4.4
    thing4.speedy=4.6
    thing5.speedy=4.8
    thing6.speedy=4.9
    thing7.speedy=4.95
    global fps
    while True:
        for event in pygame.event.get(): 
            if event.type==QUIT:
                terminate()
            if event.type==VIDEORESIZE:
                resizeMain(event.w,event.h)
                resizestart(event.w,event.h)
                resizecoin(event.w,event.h)
                resize(event.w,event.h)
                resizeranking(event.w,event.h)
                resizeshop(event.w,event.h)
                resizeSelectSet(event.w,event.h)
                resizeSelectCharacter(event.w,event.h)
        keys=pygame.key.get_pressed()
        fps.tick(60)
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and evil.x>=delta:
            evil.x-=delta
            evil.left=True
            evil.right=False
        elif keys[pygame.K_RIGHT] and evil.x<=(disp.get_width()-evil.width):
            evil.x+=delta
            evil.left=False
            evil.right=True
        else:
            evil.right=False
            evil.left=False
            evil.walk=0
        if not evil.jump:
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                evil.jump=True
                evil.right=False
                evil.left=False
                evil.walk=0
        else:
            if evil.jumpcount>=-10:
                evil.y-=(evil.jumpcount*abs(evil.jumpcount)*0.3)
                evil.jumpcount-=1
            else:
                evil.y=disp.get_height()*0.9-evil.height
                evil.jumpcount=10
                evil.jump=False
        if evil.y>disp.get_height()*0.9-evil.height-5:
            evil.y=disp.get_height()*0.9-evil.height-5
        thing1.thingy+=thing1.speedy
        if (thing1.thingy>=disp.get_height()):
            score+=1
            thing1.thingx=random.randrange(0,disp.get_width()-20)
            thing1.thingy=-200
            drawscore(score)
        thing2.thingy+=thing2.speedy
        if (thing2.thingy>=disp.get_height()):
            score+=1
            thing2.thingx=random.randrange(0,disp.get_width()-20)
            thing2.thingy=-200
            drawscore(score)
        thing3.thingy+=thing3.speedy
        if (thing3.thingy>=disp.get_height()):
            score+=1
            thing3.thingx=random.randrange(0,disp.get_width()-20)
            thing3.thingy=-200
            drawscore(score)
        thing4.thingy+=thing4.speedy
        if (thing4.thingy>=disp.get_height()):
            score+=1
            thing4.thingx=random.randrange(0,disp.get_width()-20)
            thing4.thingy=-200
            drawscore(score)
        thing5.thingy+=thing5.speedy
        if (thing5.thingy>=disp.get_height()):
            score+=1
            thing5.thingx=random.randrange(0,disp.get_width()-20)
            thing5.thingy=-200
            drawscore(score)
        thing6.thingy+=thing6.speedy
        if (thing6.thingy>=disp.get_height()):
            score+=1
            thing6.thingx=random.randrange(0,disp.get_width()-20)
            thing6.thingy=-200
            drawscore(score)
        thing7.thingy+=thing7.speedy
        if (thing7.thingy>=disp.get_height()):
            score+=1
            thing7.thingx=random.randrange(0,disp.get_width()-20)
            thing7.thingy=-200
            drawscore(score)
        if stop(evil.x,evil.y,evil.width,evil.height,thing1.thingx,thing1.thingy,thing1.thingw,thing1.thingh):
            Gameover(score)
        if stop(evil.x,evil.y,evil.width,evil.height,thing2.thingx,thing2.thingy,thing2.thingw,thing2.thingh):
            Gameover(score)
        if stop(evil.x,evil.y,evil.width,evil.height,thing3.thingx,thing3.thingy,thing3.thingw,thing3.thingh):
            Gameover(score)
        if stop(evil.x,evil.y,evil.width,evil.height,thing4.thingx,thing4.thingy,thing4.thingw,thing4.thingh):
            Gameover(score)
        if stop(evil.x,evil.y,evil.width,evil.height,thing5.thingx,thing5.thingy,thing5.thingw,thing5.thingh):
            Gameover(score)
        if stop(evil.x,evil.y,evil.width,evil.height,thing6.thingx,thing6.thingy,thing6.thingw,thing6.thingh):
            Gameover(score)
        if stop(evil.x,evil.y,evil.width,evil.height,thing7.thingx,thing7.thingy,thing7.thingw,thing7.thingh):
            Gameover(score)
        if 120>score>=0:
            thing1.speedy+=deltaspeed1
            thing2.speedy+=deltaspeed1
            thing3.speedy+=deltaspeed1
            thing5.speedy+=deltaspeed1
            thing6.speedy+=deltaspeed1
            thing7.speedy+=deltaspeed1
        else:
            thing1.speedy+=deltaspeed2
            thing2.speedy+=deltaspeed2
            thing3.speedy+=deltaspeed2
            thing4.speedy+=deltaspeed2
            thing5.speedy+=deltaspeed2
            thing6.speedy+=deltaspeed2
            thing7.speedy+=deltaspeed2
        if temp==0 and 200<score<400:
            temp=1
        if temp==1 and 400<score<600:
            temp=2
        if temp==2 and 600<score<800:
            temp=3
        if temp==3 and 800<score:
            temp==4
        if temp==0:
            disp.blit(bgm,(0,0))
        elif temp==1:
            disp.blit(bgm1,(0,0))
        elif temp==2:
            disp.blit(bgm2,(0,0))
        elif temp==3:
            disp.blit(bgm3,(0,0))
        else:
            disp.blit(bgm4,(0,0))
        draw_disp()
        drawscore(score)
        button("BACK",disp.get_width()-150,disp.get_height()*0.05,100,50,RED,BRED,Start)
        pygame.display.update()
        
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(disp,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            action()
    else:
        pygame.draw.rect(disp,ic,(x,y,w,h))
    text_font=pygame.font.Font("freesansbold.ttf",20)
    text,textrect=text_objiect(msg,text_font)
    textrect.center=((x+w/2),(y+h/2))
    disp.blit(text,textrect)
def EnterCoin(name):
    global coin
    count=0
    disp.blit(menuBD,(0,0))
    disp.blit(entercoin,(0,0))
    pygame.display.update()
    while (True):
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()        
            if event.type==KEYDOWN:
                keys=pygame.key.get_pressed()
                if keys[K_0] or keys[K_1] or keys[K_2] or keys[K_3] or keys[K_4] or keys[K_5] or keys[K_6] or keys[K_7] or keys[K_8] or keys[K_9]:
                    key=str(pygame.key.name(event.key))
                    if (count==0):
                        text1=key
                        count+=1
                        text1_font=pygame.font.Font("freesansbold.ttf",25)
                        pcoin=text1_font.render(text1,True,YELLOW)
                        disp.blit(pcoin,(int(disp.get_width()/2.1),int(disp.get_height()/2-32)))
                        pygame.display.update()
                        coin = str(coin)+str(key)
                    else:
                        text1=str(text1)+str(key)
                        count+=1
                        text1_font=pygame.font.Font("freesansbold.ttf",25)
                        pcoin=text1_font.render(text1,True,YELLOW)
                        disp.blit(pcoin,(int(disp.get_width()/2.1),int(disp.get_height()/2-32)))
                        pygame.display.update()
                        coin=str(coin)+str(key)
                if keys[K_BACKSPACE]:
                    text1=text1[:-1]
                    count-=1
                    disp.blit(entercoin,(0,0))
                    text1_font=pygame.font.Font("freesansbold.ttf",25)
                    pcoin=text1_font.render(text1,True,YELLOW)
                    disp.blit(pcoin,(int(disp.get_width()/2.1),int(disp.get_height()/2-32)))
                    pygame.display.update()
                    coin=coin[:-1]
                if keys[K_RETURN] or keys[K_KP_ENTER]:
                    coin=int(coin)
                    Start()
            if event.type==VIDEORESIZE:
                    resizeMain(event.w,event.h)
                    resizestart(event.w,event.h)
                    resizecoin(event.w,event.h)
                    resize(event.w,event.h)
                    resizeranking(event.w,event.h)
                    resizeshop(event.w,event.h)
                    resizeSelectSet(event.w,event.h)
                    resizeSelectCharacter(event.w,event.h)
                    disp.blit(entercoin,(0,0))
                    pygame.display.update()
                    if count!=0:
                        disp.blit(entercoin,(0,0))
                        text1_font=pygame.font.Font("freesansbold.ttf",25)
                        pcoin=text1_font.render(text1,True,YELLOW
                                                )
                        disp.blit(pcoin,(int(disp.get_width()/2.1),int(disp.get_height()/2-32)))
                        pygame.display.update()
def SignIn():
    global name
    count=0
    disp.blit(sign,(0,0))
    pygame.display.update()
    while (True):
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()        
            if event.type==KEYDOWN:
                keys=pygame.key.get_pressed()
                if keys[K_a] or keys[K_z] or keys[K_q] or keys[K_w] or keys[K_s] or keys[K_x] or keys[K_c] or keys[K_d] or keys[K_e] or keys[K_r] or keys[K_f] or keys[K_v] or keys[K_b] or keys[K_g] or keys[K_t] or keys[K_y] or keys[K_h] or keys[K_n] or keys[K_m] or keys[K_j] or keys[K_u] or keys[K_i] or keys[K_k] or keys[K_l] or keys[K_o] or keys[K_p] or keys[K_0] or keys[K_1] or keys[K_2] or keys[K_3] or keys[K_4] or keys[K_5] or keys[K_6] or keys[K_7] or keys[K_8] or keys[K_9]:
                    key=str(pygame.key.name(event.key))
                    if (count==0):
                        text=key
                        count+=1
                        text_font=pygame.font.Font("freesansbold.ttf",25)
                        pname=text_font.render(text,True,BLACK)
                        disp.blit(pname,(int(disp.get_width()/2.1),int(disp.get_height()/2-27)))
                        pygame.display.update()
                        name = str(name)+str(key)
                    else:
                        text=str(text)+str(key)
                        count+=1
                        text_font=pygame.font.Font("freesansbold.ttf",25)
                        pname=text_font.render(text,True,BLACK)
                        disp.blit(pname,(int(disp.get_width()/2.1),int(disp.get_height()/2-27)))
                        pygame.display.update()
                        name=str(name)+str(key)
                if keys[K_BACKSPACE]:
                    text=text[:-1]
                    count-=1
                    disp.blit(sign,(0,0))
                    text_font=pygame.font.Font("freesansbold.ttf",25)
                    pname=text_font.render(text,True,BLACK)
                    disp.blit(pname,(int(disp.get_width()/2.1),int(disp.get_height()/2-27)))
                    pygame.display.update()
                    name=name[:-1]
                if keys[K_RETURN] or keys[K_KP_ENTER]:
                    EnterCoin(name)
            if event.type==VIDEORESIZE:
                    resizeSign(event.w,event.h)
                    resizeMain(event.w,event.h)
                    resizestart(event.w,event.h)
                    resizecoin(event.w,event.h)
                    resize(event.w,event.h)
                    resizeranking(event.w,event.h)
                    resizeshop(event.w,event.h)
                    resizeSelectSet(event.w,event.h)
                    resizeSelectCharacter(event.w,event.h)
                    disp.blit(sign,(0,0))
                    pygame.display.update()
                    if count!=0:
                        disp.blit(sign,(0,0))
                        text_font=pygame.font.Font("freesansbold.ttf",25)
                        pname=text_font.render(text,True,BLACK)
                        disp.blit(pname,(int(disp.get_width()/2.1),int(disp.get_height()/2-27)))
                        pygame.display.update()
def GameoverMain(rank1,rank2,rank3,rank4,rank5,statistic,state_star,ranking1,ranking2,ranking3,ranking4,ranking5):
    global name,coin,betcoin,gameplayed,gamewin
    wd=disp.get_width()
    hd=disp.get_height()
    gameplayed +=1
    tmp=0
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            if event.type==VIDEORESIZE:
                resizeMain(event.w,event.h)
                resizestart(event.w,event.h)
                resizecoin(event.w,event.h)
                resize(event.w,event.h)
                resizeranking(event.w,event.h)
                resizeshop(event.w,event.h)
                resizeSelectSet(event.w,event.h)
                resizeSelectCharacter(event.w,event.h)
                resizeranking(event.w,event.h)
                wd=disp.get_width()
                hd=disp.get_height()
        disp.blit(showranking,(0,0))
        text_font=pygame.font.Font("freesansbold.ttf",15)
        text1_font=pygame.font.Font("freesansbold.ttf",30)
        text1=text1_font.render("rank 1:             ",True,BLACK)
        disp.blit(text1,(int(wd/2-100),int(hd/2-100)))
        if (rank1==1):
            disp.blit(ranking1,(int(wd/2+60),int(hd/2-120)))
        if (rank1==2):
            disp.blit(ranking2,(int(wd/2+60),int(hd/2-120)))
        if (rank1==3):
            disp.blit(ranking3,(int(wd/2+60),int(hd/2-120)))
        if (rank1==4):
            disp.blit(ranking4,(int(wd/2+60),int(hd/2-120)))
        if (rank1==5):
            disp.blit(ranking5,(int(wd/2+60),int(hd/2-120)))
        text2=text1_font.render("rank 2:             ",True,BLACK)
        disp.blit(text2,(wd/2-100,hd/2-40))
        if (rank2==1):
            disp.blit(ranking1,(int(wd/2+60),int(hd/2-60)))
        if (rank2==2):
            disp.blit(ranking2,(int(wd/2+60),int(hd/2-60)))
        if (rank2==3):
            disp.blit(ranking3,(int(wd/2+60),int(hd/2-60)))
        if (rank2==4):
            disp.blit(ranking4,(int(wd/2+60),int(hd/2-60)))
        if (rank2==5):
            disp.blit(ranking5,(int(wd/2+60),int(hd/2-60)))
        text3=text1_font.render("rank 3:             ",True,BLACK)
        disp.blit(text3,(wd/2-100,hd/2+20))
        if (rank3==1):
            disp.blit(ranking1,(int(wd/2+60),int(hd/2)))
        if (rank3==2):
            disp.blit(ranking2,(int(wd/2+60),int(hd/2)))
        if (rank3==3):
            disp.blit(ranking3,(int(wd/2+60),int(hd/2)))
        if (rank3==4):
            disp.blit(ranking4,(int(wd/2+60),int(hd/2)))
        if (rank3==5):
            disp.blit(ranking5,(int(wd/2+60),int(hd/2)))
        text4=text1_font.render("rank 4:             ",True,BLACK)
        disp.blit(text4,(wd/2-100,hd/2+80))
        if (rank4==1):
            disp.blit(ranking1,(int(wd/2+60),int(hd/2+60)))
        if (rank4==2):
            disp.blit(ranking2,(int(wd/2+60),int(hd/2+60)))
        if (rank4==3):
            disp.blit(ranking3,(int(wd/2+60),int(hd/2+60)))
        if (rank4==4):
            disp.blit(ranking4,(int(wd/2+60),int(hd/2+60)))
        if (rank4==5):
            disp.blit(ranking5,(int(wd/2+60),int(hd/2+60)))
        text5=text1_font.render("rank 5:             ",True,BLACK)
        disp.blit(text5,(wd/2-100,hd/2+140))
        if (rank5==1):
            disp.blit(ranking1,(int(wd/2+60),int(hd/2+120)))
        if (rank5==2):
            disp.blit(ranking2,(int(wd/2+60),int(hd/2+120)))
        if (rank5==3):
            disp.blit(ranking3,(int(wd/2+60),int(hd/2+120)))
        if (rank5==4):
            disp.blit(ranking4,(int(wd/2+60),int(hd/2+120)))
        if (rank5==5):
            disp.blit(ranking5,(int(wd/2+60),int(hd/2+120)))
        if (statistic == True):
            if state_star==False:
                if tmp==0:
                    coin += (4*int(betcoin))
                    tmp+=1
                text=text1_font.render("YAHHH " +str(name) + " win " ,True,VIOLET)
                disp.blit(text, (wd/2-100,hd/2-170))
                text_coin=text_font.render("ADD COIN:"+str(4*int(betcoin)),True,YELLOW)
                disp.blit(text_coin,((97*wd)/208,(32*hd)/117))
            else:
                if tmp==0:
                    coin+=(8*int(betcoin))
                    tmp+=1
                text=text1_font.render("YAHHH " +str(name) + " win " ,True,VIOLET)
                disp.blit(text, (wd/2-100,hd/2-170))
                text_coin=text_font.render("ADD COIN(STAR):"+str(8*int(betcoin)),True,YELLOW)
                disp.blit(text_coin,((97*wd)/208,(32*hd)/117))
        else:
            text=text1_font.render("NOOO " +str(name) + " lose " ,True,VIOLET)
            disp.blit(text, (wd/2-70,hd/2-170))
            text_coin=text_font.render("ADD COIN: 0",True,YELLOW)
            disp.blit(text_coin,((97*wd)/208,(32*hd)/117))
        button("PLAY-AGAIN",disp.get_width()/5,disp.get_height()*0.8,200,50,GREEN,BGREEN,selectSet)
        button("BACK",disp.get_width()*0.8-150,disp.get_height()*0.8,100,50,RED,BRED,Start)
        pygame.display.update()
        fps.tick(15)
def buttonimg(x,y,w,h,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y and click[0]==1 and action!=None:
        action()
def Gameover(score):
    global coin
    pygame.mixer.Sound.play(gameoversound)
    pygame.mixer.music.stop()
    coin+=score
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            if event.type==VIDEORESIZE:
                resizeMain(event.w,event.h)
                resizestart(event.w,event.h)
                resizecoin(event.w,event.h)
                resize(event.w,event.h)
                resizeranking(event.w,event.h)
                resizeshop(event.w,event.h)
                resizeSelectSet(event.w,event.h)
                resizeSelectCharacter(event.w,event.h)
        disp.blit(menuBD,(0,0))   
        text_font=pygame.font.Font("freesansbold.ttf",100)
        text_font2=pygame.font.Font("freesansbold.ttf",30)
        text=text_font.render("GAME OVER",True,BLUE)
        text2=text_font2.render("ADD COIN: "+str(score),True,BLACK)
        textrect=text.get_rect()
        text2rect=text2.get_rect()
        textrect.center=(disp.get_width()/2,disp.get_height()/4)
        text2rect.center=(disp.get_width()/2,disp.get_height()/2.5)
        disp.blit(text,textrect)
        disp.blit(text2,text2rect)       
        button("PLAY-AGAIN",disp.get_width()/5,disp.get_height()*0.8,200,50,GREEN,BGREEN,Gameloop)
        button("BACK",disp.get_width()*0.8-150,disp.get_height()*0.8,100,50,RED,BRED,Start)
        pygame.display.update()
        fps.tick(15)
select=None
def selectSet():
    global run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,select,mychar
    def setcat():
        global selectcat
        run1=runcat1
        run2=runcat2
        run3=runcat3
        run4=runcat4
        run5=runcat5
        runl1=runlcat1
        runl2=runlcat2
        runl3=runlcat3
        runl4=runlcat4
        runl5=runlcat5
        ranking1=pygame.image.load("C_B1.png")
        ranking2=pygame.image.load("C_G1.png")
        ranking3=pygame.image.load("C_P1.png")
        ranking4=pygame.image.load("C_PK1.png")
        ranking5=pygame.image.load("C_R1.png")
        def catblue():
            select=runcat1
            mychar=1
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def catgreen():
            select=runcat2
            mychar=2
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def catpurple():
            select=runcat3
            mychar=3
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def catpink():
            select=runcat4
            mychar=4
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def catred():
            select=runcat5
            mychar=5
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        while True:
            disp.blit(selectcat,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==QUIT:
                    terminate()
                if event.type==VIDEORESIZE:
                    resizeMain(event.w,event.h)
                    resizestart(event.w,event.h)
                    resizecoin(event.w,event.h)
                    resize(event.w,event.h)
                    resizeranking(event.w,event.h)
                    resizeshop(event.w,event.h)
                    resizeSelectSet(event.w,event.h)
                    resizeSelectCharacter(event.w,event.h)
            wd=disp.get_width()
            hd=disp.get_height()
            buttonimg(29*wd/104,47*hd/117,15*wd/208,2*hd/39,catblue)#blue
            buttonimg(101*wd/208,47*hd/117,15*wd/208,2*hd/39,catgreen)#green
            buttonimg(145*wd/208,47*hd/117,15*wd/208,2*hd/39,catpurple)#purple
            buttonimg(9*wd/26,2*hd/3,15*wd/208,2*hd/39,catpink)#pink
            buttonimg(61*wd/104,2*hd/3,15*wd/208,2*hd/39,catred)#red     
    def setdino():
        global selectdino
        run1=rundino1
        run2=rundino2
        run3=rundino3
        run4=rundino4
        run5=rundino5
        runl1=runldino1
        runl2=runldino2
        runl3=runldino3
        runl4=runldino4
        runl5=runldino5
        ranking1=pygame.image.load("RunB_1.png")
        ranking2=pygame.image.load("RunG_1.png")
        ranking3=pygame.image.load("RunP_1.png")
        ranking4=pygame.image.load("RunPK_1.png")
        ranking5=pygame.image.load("RunR_1.png")
        def dinoblue():
            select=rundino1
            mychar=1
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def dinogreen():
            select=rundino2
            mychar=2
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def dinopurple():
            select=rundino3
            mychar=3
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def dinopink():
            select=rundino4
            mychar=4
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def dinored():
            select=rundino5
            mychar=5
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        while True:
            disp.blit(selectdino,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==QUIT:
                    terminate()
                if event.type==VIDEORESIZE:
                    resizeMain(event.w,event.h)
                    resizestart(event.w,event.h)
                    resizecoin(event.w,event.h)
                    resize(event.w,event.h)
                    resizeranking(event.w,event.h)
                    resizeshop(event.w,event.h)
                    resizeSelectSet(event.w,event.h)
                    resizeSelectCharacter(event.w,event.h)
            wd=disp.get_width()
            hd=disp.get_height()
            buttonimg(29*wd/104,47*hd/117,15*wd/208,2*hd/39,dinoblue)#blue
            buttonimg(101*wd/208,47*hd/117,15*wd/208,2*hd/39,dinogreen)#green
            buttonimg(145*wd/208,47*hd/117,15*wd/208,2*hd/39,dinopurple)#purple
            buttonimg(9*wd/26,2*hd/3,15*wd/208,2*hd/39,dinopink)#pink
            buttonimg(61*wd/104,2*hd/3,15*wd/208,2*hd/39,dinored)#red     
    def setrocket():
        global selectrocket
        run1=runrocket1
        run2=runrocket2
        run3=runrocket3
        run4=runrocket4
        run5=runrocket5
        runl1=runlrocket1
        runl2=runlrocket2
        runl3=runlrocket3
        runl4=runlrocket4
        runl5=runlrocket5
        ranking1=pygame.image.load("R_B1.png")
        ranking2=pygame.image.load("R_G1.png")
        ranking3=pygame.image.load("R_P1.png")
        ranking4=pygame.image.load("R_PK1.png")
        ranking5=pygame.image.load("R_R1.png")
        def rocketblue():
            select=runrocket1
            mychar=1
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def rocketgreen():
            select=runrocket2
            mychar=2
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def rocketpurple():
            select=runrocket3
            mychar=3
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def rocketpink():
            select=runrocket4
            mychar=4
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def rocketred():
            select=runrocket5
            mychar=5
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        while True:
            disp.blit(selectrocket,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==QUIT:
                    terminate()
                if event.type==VIDEORESIZE:
                    resizeMain(event.w,event.h)
                    resizestart(event.w,event.h)
                    resizecoin(event.w,event.h)
                    resize(event.w,event.h)
                    resizeranking(event.w,event.h)
                    resizeshop(event.w,event.h)
                    resizeSelectSet(event.w,event.h)
                    resizeSelectCharacter(event.w,event.h)
            wd=disp.get_width()
            hd=disp.get_height()
            buttonimg(29*wd/104,47*hd/117,15*wd/208,2*hd/39,rocketblue)#blue
            buttonimg(101*wd/208,47*hd/117,15*wd/208,2*hd/39,rocketgreen)#green
            buttonimg(145*wd/208,47*hd/117,15*wd/208,2*hd/39,rocketpurple)#purple
            buttonimg(9*wd/26,2*hd/3,15*wd/208,2*hd/39,rocketpink)#pink
            buttonimg(61*wd/104,2*hd/3,15*wd/208,2*hd/39,rocketred)#red     
    def setsnake():
        global selectsnake
        run1=runsnake1
        run2=runsnake2
        run3=runsnake3
        run4=runsnake4
        run5=runsnake5
        runl1=runlsnake1
        runl2=runlsnake2
        runl3=runlsnake3
        runl4=runlsnake4
        runl5=runlsnake5
        ranking1=pygame.image.load("S_B1.png")
        ranking2=pygame.image.load("S_G1.png")
        ranking3=pygame.image.load("S_P1.png")
        ranking4=pygame.image.load("S_PK1.png")
        ranking5=pygame.image.load("S_R1.png")
        def snakeblue():
            select=runsnake1
            mychar=1
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def snakegreen():
            select=runsnake2
            mychar=2
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def snakepurple():
            select=runsnake3
            mychar=3
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def snakepink():
            select=runsnake4
            mychar=4
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def snakered():
            select=runsnake5
            mychar=5
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        while True:
            disp.blit(selectsnake,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==QUIT:
                    terminate()
                if event.type==VIDEORESIZE:
                    resizeMain(event.w,event.h)
                    resizestart(event.w,event.h)
                    resizecoin(event.w,event.h)
                    resize(event.w,event.h)
                    resizeranking(event.w,event.h)
                    resizeshop(event.w,event.h)
                    resizeSelectSet(event.w,event.h)
                    resizeSelectCharacter(event.w,event.h)
            wd=disp.get_width()
            hd=disp.get_height()
            buttonimg(29*wd/104,47*hd/117,15*wd/208,2*hd/39,snakeblue)#blue
            buttonimg(101*wd/208,47*hd/117,15*wd/208,2*hd/39,snakegreen)#green
            buttonimg(145*wd/208,47*hd/117,15*wd/208,2*hd/39,snakepurple)#purple
            buttonimg(9*wd/26,2*hd/3,15*wd/208,2*hd/39,snakepink)#pink
            buttonimg(61*wd/104,2*hd/3,15*wd/208,2*hd/39,snakered)#red     
    def setteam():
        global selectteam
        run1=runteam1
        run2=runteam2
        run3=runteam3
        run4=runteam4
        run5=runteam5
        runl1=runlteam1
        runl2=runlteam2
        runl3=runlteam3
        runl4=runlteam4
        runl5=runlteam5
        ranking1=pygame.image.load("HAI1.png")
        ranking2=pygame.image.load("DUYV1.png")
        ranking3=pygame.image.load("DUONG1.png")
        ranking4=pygame.image.load("DUYT1.png")
        ranking5=pygame.image.load("DUC1.png")
        def teamblue():
            select=runteam1
            mychar=1
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def teamgreen():
            select=runteam2
            mychar=2
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def teampurple():
            select=runteam3
            mychar=3
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def teampink():
            select=runteam4
            mychar=4
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        def teamred():
            select=runteam5
            mychar=5
            bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
        while True:
            disp.blit(selectteam,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==QUIT:
                    terminate()
                if event.type==VIDEORESIZE:
                    resizeMain(event.w,event.h)
                    resizestart(event.w,event.h)
                    resizecoin(event.w,event.h)
                    resize(event.w,event.h)
                    resizeranking(event.w,event.h)
                    resizeshop(event.w,event.h)
                    resizeSelectSet(event.w,event.h)
                    resizeSelectCharacter(event.w,event.h)
            wd=disp.get_width()
            hd=disp.get_height()
            buttonimg(29*wd/104,47*hd/117,15*wd/208,2*hd/39,teamblue)#hai
            buttonimg(101*wd/208,47*hd/117,15*wd/208,2*hd/39,teamgreen)#vanduy
            buttonimg(145*wd/208,47*hd/117,15*wd/208,2*hd/39,teampurple)#duong
            buttonimg(9*wd/26,2*hd/3,15*wd/208,2*hd/39,teampink)#duytruong
            buttonimg(61*wd/104,2*hd/3,15*wd/208,2*hd/39,teamred)#duc    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            if event.type==VIDEORESIZE:
                resizestart(event.w,event.h)
                resizeMain(event.w,event.h)
                resizecoin(event.w,event.h)
                resize(event.w,event.h)
                resizeranking(event.w,event.h)
                resizeshop(event.w,event.h)
                resizeSelectSet(event.w,event.h)
                resizeSelectCharacter(event.w,event.h)
        disp.blit(selectset,(0,0,))
        wd=disp.get_width()
        hd=disp.get_height()
        buttonimg(69*wd/208,46*hd/117,15*wd/208,2*hd/39,setcat)#cat
        buttonimg(133*wd/208,49*hd/117,15*wd/208,2*hd/39,setdino)#dino
        buttonimg(69*wd/208,68*hd/117,15*wd/208,2*hd/39,setrocket)#rocket
        buttonimg(69*wd/208,86*hd/117,15*wd/208,2*hd/39,setsnake)#snake
        buttonimg(133*wd/208,86*hd/117,15*wd/208,2*hd/39,setteam)
        pygame.display.update()
def bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5):
    global coin,betcoin
    count=0
    betcoin=0
    disp.blit(bet,(0,0))
    pygame.display.update()
    while (True):
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()        
            if event.type==KEYDOWN:
                keys=pygame.key.get_pressed()
                if keys[K_0] or keys[K_1] or keys[K_2] or keys[K_3] or keys[K_4] or keys[K_5] or keys[K_6] or keys[K_7] or keys[K_8] or keys[K_9]:
                    key=str(pygame.key.name(event.key))
                    if (count==0):
                        text1=key
                        count+=1
                        text1_font=pygame.font.Font("freesansbold.ttf",25)
                        pbetcoin=text1_font.render(text1,True,YELLOW)
                        disp.blit(pbetcoin,(int(47*disp.get_width()/104),int(62*disp.get_height()/117)))
                        pygame.display.update()
                        betcoin = str(betcoin)+str(key)
                    else:
                        text1=str(text1)+str(key)
                        count+=1
                        text1_font=pygame.font.Font("freesansbold.ttf",25)
                        pbetcoin=text1_font.render(text1,True,YELLOW)
                        disp.blit(pbetcoin,(int(47*disp.get_width()/104),int(62*disp.get_height()/117)))
                        pygame.display.update()
                        betcoin=str(betcoin)+str(key)
                if keys[K_BACKSPACE]:
                    text1=text1[:-1]
                    count-=1
                    disp.blit(bet,(0,0))
                    text1_font=pygame.font.Font("freesansbold.ttf",25)
                    pbetcoin=text1_font.render(text1,True,YELLOW)
                    disp.blit(pbetcoin,(int(47*disp.get_width()/104),int(62*disp.get_height()/117)))
                    pygame.display.update()
                    betcoin=betcoin[:-1]
                if keys[K_RETURN] or keys[K_KP_ENTER]:
                    if 0<int(betcoin)<=coin:
                        coin-=int(betcoin)
                        BuyItem(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
                    else:
                        wd=disp.get_width()
                        hd=disp.get_height()
                        text_font1=pygame.font.Font("freesansbold.ttf",30)
                        text=text_font1.render("Please check your coins!!",True,RED)
                        disp.blit(text,(0,hd-40))
                        pygame.display.update()
                        pygame.time.delay(1000) 
                        bet_coin(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
            if event.type==VIDEORESIZE:
                resizeMain(event.w,event.h)
                resizestart(event.w,event.h)
                resizecoin(event.w,event.h)
                resize(event.w,event.h)
                resizeranking(event.w,event.h)
                resizeshop(event.w,event.h)
                resizeSelectSet(event.w,event.h)
                resizeSelectCharacter(event.w,event.h)
                disp.blit(bet,(0,0))
                pygame.display.update()
                if count!=0:
                    disp.blit(bet,(0,0))
                    text1_font=pygame.font.Font("freesansbold.ttf",25)
                    pbetcoin=text1_font.render(text1,True,YELLOW)
                    disp.blit(pbetcoin,(int(47*disp.get_width()/104),int(62*disp.get_height()/117)))
                    pygame.display.update()
def BuyItem(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5):
    global coin, item
    item = 0
    price_item1 = 1000
    price_item2 = 1000
    price_item3 = 1000
    wd=disp.get_width()
    hd=disp.get_height()
    disp.blit(ItemShop,(0,0))
    pygame.display.update()
    def Item0():
        global item
        item = 0
        GameloopMain(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5, item)
    def Item1():
        global coin, item
        if (coin>=1000):
            item = 1
            coin -= price_item1
            GameloopMain(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5,item)
        else :
            wd=disp.get_width()
            hd=disp.get_height()
            text_font1=pygame.font.Font("freesansbold.ttf",30)
            text=text_font1.render("Please check your coins!!",True,RED)
            disp.blit(text,(0,hd-40))
            pygame.display.update()
            pygame.time.delay(1000) 
            BuyItem(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
    def Item2():
        global coin, item
        if (coin>=1000):
            item = 2
            coin -= price_item2
            GameloopMain(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5,item)
        else :
            wd=disp.get_width()
            hd=disp.get_height()
            text_font1=pygame.font.Font("freesansbold.ttf",30)
            text=text_font1.render("Please check your coins!!",True,RED)
            disp.blit(text,(0,hd-40))
            pygame.display.update()
            pygame.time.delay(1000) 
            BuyItem(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
    def Item3():
        global coin, item
        if (coin>=5000):
            item = 3
            coin -= price_item3
            GameloopMain(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5,item)
        else :
            wd=disp.get_width()
            hd=disp.get_height()
            text_font1=pygame.font.Font("freesansbold.ttf",30)
            text=text_font1.render("Please check your coins!!",True,RED)
            disp.blit(text,(0,hd-40))
            pygame.display.update()
            pygame.time.delay(1000) 
            BuyItem(run1,run2,run3,run4,run5,runl1,runl2,runl3,runl4,runl5,mychar,ranking1,ranking2,ranking3,ranking4,ranking5)
    while (True):
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            if event.type==VIDEORESIZE:
                    resizeMain(event.w,event.h)
                    resizestart(event.w,event.h)
                    resizecoin(event.w,event.h)
                    resize(event.w,event.h)
                    resizeranking(event.w,event.h)
                    resizeshop(event.w,event.h)
                    wd=disp.get_width()
                    hd=disp.get_height()
                    resizeSelectSet(event.w,event.h)
                    resizeSelectCharacter(event.w,event.h)
                    disp.blit(ItemShop,(0,0))
                    pygame.display.update()
            buttonimg(482*wd/1040, 410*hd/585, 100*wd/1040, 40*hd/585, Item0)
            buttonimg(328*wd/1040, 310*hd/585, 80*wd/1040, 40*hd/585, Item1)
            buttonimg(482*wd/1040, 310*hd/585, 80*wd/1040, 40*hd/585, Item2)
            buttonimg(633*wd/1040, 310*hd/585, 80*wd/1040, 40*hd/585, Item3)
def Guide1():
    disp.blit(guide1, (0,0))
    pygame.display.update()
    wd=disp.get_width()
    hd=disp.get_height()
    while (True):
        for event in pygame.event.get():
            if event.type==VIDEORESIZE:
                resizeMain(event.w,event.h)
                resizestart(event.w,event.h)
                resizecoin(event.w,event.h)
                resize(event.w,event.h)
                resizeranking(event.w,event.h)
                resizeshop(event.w,event.h)
                resizeSelectSet(event.w,event.h)
                resizeSelectCharacter(event.w,event.h)
                disp.blit(guide1,(0,0))
                pygame.display.update()
        buttonimg(47*wd/104,100*hd/117,wd/13,16*hd/117,Start)
        buttonimg(437*wd/520,242*hd/585,wd/13,16*hd/117,Guide2) 
def Guide2():
    disp.blit(guide2, (0,0))
    pygame.display.update()
    wd=disp.get_width()
    hd=disp.get_height()
    while (True):
        for event in pygame.event.get():
            if event.type==VIDEORESIZE:
                resizeMain(event.w,event.h)
                resizestart(event.w,event.h)
                resizecoin(event.w,event.h)
                resize(event.w,event.h)
                resizeranking(event.w,event.h)
                resizeshop(event.w,event.h)
                resizeSelectSet(event.w,event.h)
                resizeSelectCharacter(event.w,event.h)
                disp.blit(guide2,(0,0))
                pygame.display.update()
        buttonimg(47*wd/104,100*hd/117,wd/13,55*hd/117,Start)
        buttonimg(9*wd/104,242*hd/585,wd/13,16*hd/117,Guide1)
def Informations():
    global name,gameplayed,winrate,gamewin
    sz=14
    disp.blit(in4, (0,0))
    pygame.display.update()
    wd=disp.get_width()
    hd=disp.get_height()
    text_font=pygame.font.Font("freesansbold.ttf",sz)
    text=text_font.render(str(name),True,WHITE)
    disp.blit(text, (123*wd/260,6*hd/13))
    text1=text_font.render(str(gameplayed),True,WHITE)
    disp.blit(text1, (123*wd/260,20*hd/39))
    text2=text_font.render(str(gamewin),True,WHITE)
    disp.blit(text2, (123*wd/260,22*hd/39))
    buttonimg(311*wd/520,40*hd/117,wd/26,8*hd/117,Start)
    pygame.display.update()
    while (True):
        for event in pygame.event.get():
            if event.type==VIDEORESIZE:
                resizeMain(event.w,event.h)
                resizestart(event.w,event.h)
                resizecoin(event.w,event.h)
                resize(event.w,event.h)
                resizeranking(event.w,event.h)
                resizeshop(event.w,event.h)
                resizeSelectSet(event.w,event.h)
                resizeSelectCharacter(event.w,event.h)
                disp.blit(in4,(0,0))
                w=disp.get_width()
                h=disp.get_height()
                sz=int(14*h/hd)
                text_font=pygame.font.Font("freesansbold.ttf",sz)
                text=text_font.render(str(name),True,WHITE)
                text1=text_font.render(str(gameplayed),True,WHITE)
                disp.blit(text1, (123*w/260,20*h/39))
                text2=text_font.render(str(gamewin),True,WHITE)
                disp.blit(text2, (123*w/260,22*h/39))
                disp.blit(text, (123*w/260,6*h/13))
                buttonimg(311*w/520,40*h/117,w/26,8*h/117,Start)
                pygame.display.update()
        buttonimg(311*wd/520,40*hd/117,wd/26,8*hd/117,Start)
def Start():
    global name,coin
    pygame.mixer.Sound.play(startsound)
    pygame.mixer.music.stop()
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            if event.type==VIDEORESIZE:
                resizestart(event.w,event.h)
                resizeMain(event.w,event.h)
                resizecoin(event.w,event.h)
                resizeSign(event.w,event.h)
                resize(event.w,event.h)
                resizeranking(event.w,event.h)
                resizeshop(event.w,event.h)
                resizeSelectSet(event.w,event.h)
                resizeSelectCharacter(event.w,event.h)
        disp.blit(menu,(0,0))
        disp.blit(showcoin,(0,0))
        text_font1=pygame.font.Font("freesansbold.ttf",30)
        text3=text_font1.render(str(coin),True,YELLOW)
        textrect2=text3.get_rect()
        textrect2.center=(120,40)
        disp.blit(text3,textrect2)
        wd=disp.get_width()
        hd=disp.get_height()
        buttonimg(99*wd/104,242*hd/585,wd/26,8*hd/117,Guide1)
        buttonimg(99*wd/104,178*hd/585,wd/26,8*hd/117,Informations)
        buttonimg(wd/13,9*hd/13,19*wd/104,hd/9,Gameloop)
        buttonimg(43*wd/104,9*hd/13,19*wd/104,hd/9,selectSet)
        buttonimg(77*wd/104,9*hd/13,19*wd/104,hd/9,terminate)
        pygame.display.update()
        fps.tick(20)
SignIn()
pygame.quit()
quit()
