import sys 
import pygame
from pygame.locals import *
import random
pygame.init()
# Resolution is ignored on Android
surface = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
#gameapp controls variables
game_start=True
menu_start=False
theame_start=False
#snake movement variables
right=False
left=False
up=False
down=False
srun=False
dmb_x=500
dmb_y=500
file1=open("theamed.txt","r+")
Ttf=file1.read()
file1.close()
if Ttf=="1":
	Theame1=True
	Theame2=False
if Ttf=="2":
	Theame1=False
	Theame2=True	
#1st Theame colours
pink=(255,0,255)
red=(255,0,0)
blue=(0,0,255)
white=(255,255,255)
#2nd Theame colours
yollow=(250,5,255)
green=(0,255,0)
red2=(255,0,0)
head_colour=(255,0,0)

#1st Teame apply
if Theame1==True:
	tb_text_col=red
	db_text_col=red
	lb_text_col=pink
	rb_text_col=pink
	pt_text_col=pink
	pv_text_col=red
	ht_text_col=red
	hv_text_col=pink
	bf_line_col=blue
	mb_body_col=red
	but_change_col=blue
#2nd Teame apply
if Theame2==True:
	tb_text_col=green
	db_text_col=green
	lb_text_col=yollow
	rb_text_col=yollow
	pt_text_col=green
	pv_text_col=yollow
	ht_text_col=red
	hv_text_col=pink
	bf_line_col=blue
	mb_body_col=blue
	but_change_col=blue
#button values variables
b_col1=(255,255,255)
b_col2=(255,255,255)
b_col3=(255,255,255)
b_col4=(255,255,255)
b_x1=750
b_y1=1500
b_x2=150
b_y2=1500
b_x3=450
b_y3=1300
b_x4=450
b_y4=1700
b_x5=750
b_y5=50
b_col5=(255,255,255)
# menu button variable
mb_x1=250
mb_y1=900
mb_x2=650
mb_y2=900
#snakefoods variable
sf_x=random.randint(200,900)
sf_y=random.randint(250,900)
#match Points variable
add_value=False
point_value=0
h_point_value=0
file=open("hpointr.txt","r+")
hfile=file.read()
h_point_value=int(hfile)
file.close()
#its for some test
run_value="None"
#snake body positioning list
main_box_list=[[dmb_x,dmb_y],[520,500],[540,500],[560,500]]
main_box_list2=[[500,500],[520,500],[540,500],[560,500]]
#snake body part add variable
add_bodypart=False
#menu text list 
mbut_text_list=[["Theame",mb_x1,mb_y1],["Play",mb_x2,mb_y2]]
#button text list 
but_text_list=[["Right",rb_text_col,b_x1+30,b_y1+15],["Left",lb_text_col,b_x2+40,b_y2+15],["Top",tb_text_col,b_x3+40,b_y3+15],["Down",db_text_col,b_x4+20,b_y4+15],["POINTS - ",pt_text_col,50,30],[str(point_value),pv_text_col,350,30],["HIGHEST - ",ht_text_col,50,120],[str(h_point_value),hv_text_col,400,120]]
#buttin definaton
def buttons(b_x,b_y,b_col):
	pygame.draw.rect(surface,b_col,[b_x,b_y,200,100],5)
#button_text defination
def but_text(text_value,text_col,text_x,text_y):
	myfont = pygame.font.SysFont("Arial",60)
	label = myfont.render(text_value, 1,text_col)
	surface.blit(label,(text_x,text_y))
#fullbody of snake defination
def main_box(mb_x,mb_y,mb_body_col):
	pygame.draw.rect(surface,mb_body_col,[mb_x,mb_y,20,20])
#bigframe defination
def bigframe(bf_line_col):
	pygame.draw.rect(surface,bf_line_col,[50,250,950,950],5)
#snake foods defination
def snakefood(sf_x,sf_y):
	pygame.draw.rect(surface,(250,0,255),[sf_x,sf_y,50,50])
#exit button defination
def exit_button(e_text,e_but_x,e_but_y):
	myfont = pygame.font.SysFont("Arial",60)
	label = myfont.render(str(e_text), 1,(255,255,0))
	surface.blit(label,(e_but_x+30,e_but_y+10))
while True:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
        elif ev.type==MOUSEBUTTONDOWN:
        	x,y=pygame.mouse.get_pos()
        	if theame_start==True:
        		menu_start=True
        		game_start=False
        		theame_start=False
        	if menu_start==True:
        		if mb_x2<x<mb_x2+260 and mb_y2<y<mb_y2+100:
        			menu_start=False
        			game_start=True
        			theame_start=False
        	if game_start==True:
#button fuction logics
        		if b_x1<x<b_x1+200 and b_y1<y<b_y1+100:
        			b_col1=but_change_col
        			b_col2=white
        			b_col3=white
        			b_col4=(255,255,255)
        			right=True
        			left=False
        			up=False
        			down=False
        			srun=True
        		elif b_x2<x<b_x2+200 and b_y2<y<b_y2+100:
        			b_col2=but_change_col
        			b_col1=(255,255,255)
        			b_col3=(255,255,255)
        			b_col4=(255,255,255)
        			right=False
        			left=True
        			up=False
        			down=False
        			srun=True
        		elif b_x3<x<b_x3+200 and b_y3<y<b_y3+100:
        			b_col3=but_change_col
        			b_col1=(255,255,255)
        			b_col2=(255,255,255)
        			b_col4=(255,255,255)
        			right=False
        			left=False
        			up=True
        			down=False
        			srun=True
        		elif b_x4<x<b_x4+200 and b_y4<y<b_y4+100:
        			b_col4=but_change_col
        			b_col1=(255,255,255)
        			b_col2=(255,255,255)
        			b_col3=(255,255,255)
        			right=False
        			left=False
        			up=False
        			down=True
        			srun=True
        		elif b_x5<x<b_x5+200 and b_y5<y<b_y5+100:
        			sf_x=random.randint(200,900)
        			sf_y=random.randint(250,900)
        			dmb_x=500
        			dmb_y=500
        			main_box_list=[[dmb_x,dmb_y],[520,500],[540,500],[560,500]]
        			main_box_list2=[[500,500],[520,500],[540,500],[560,500]]
        			point_value=0
        			but_text_list[5][2]="0"
        			b_col5=but_change_col
        			b_col4=(255,255,255)
        			b_col1=(255,255,255)
        			b_col2=(255,255,255)
        			b_col3=(255,255,255)
        			right=False
        			left=False
        			up=False
        			down=False
        			srun=False
        			menu_start=True
        			game_start=False
    if game_start==True:       			
# if snake goes outside it can manage 		
    	if dmb_x>950:
    		dmb_x=51
    		main_box_list[0][0]=dmb_x
    	if dmb_x<50:
    		dmb_x=949
    		main_box_list[0][0]=dmb_x
    	if dmb_y>1150:
    		dmb_y=251
    		main_box_list[0][1]=dmb_y
    	if dmb_y<250:
    		dmb_y=1149
    		main_box_list[0][1]=dmb_y
    	if right==True:
    		dmb_x+=20
    		main_box_list[0][0]+=20
    	if left==True:
    		dmb_x-=20
    		main_box_list[0][0]-=20
    	if up==True:
    		dmb_y-=20
    		main_box_list[0][1]-=20
    	if down==True:
    		dmb_y+=20
    		main_box_list[0][1]+=20
#snake full body movement by logic 
    	if srun==True:
    		for i in range(len(main_box_list)-1):
    			main_box_list[i+1][0]=main_box_list2[i][0]
    			main_box_list[i+1][1]=main_box_list2[i][1]
    		for i in range(len(main_box_list)):
    			main_box_list2[i][0]=main_box_list[i][0]
    			main_box_list2[i][1]=main_box_list[i][1]
#snake eating logic and food placement
    	if (sf_x<dmb_x<sf_x+50 and sf_y<dmb_y<sf_y+50) or (sf_x<dmb_x+20<sf_x+50 and sf_y<dmb_y<sf_y+50) :
    		sf_x=random.randint(200,900)
    		sf_y=random.randint(250,900)
    		add_bodypart=True
    		add_value=True
#snake body part adding logics
    	if add_bodypart==True:
    		main_box_list.append([(main_box_list[len(main_box_list)-1][0]+20),(main_box_list[len(main_box_list)-1][1]+20)])
    		main_box_list2.append([(main_box_list2[len(main_box_list2)-1][0]+20),(main_box_list2[len(main_box_list2)-1][1]+20)])
    		add_bodypart=False
#adding value logic
    	if add_value==True:
    		point_value+=10
    		but_text_list[5][0]=str(point_value)
    		add_value=False
#updating heighest value and hpointr.txt file
    	if point_value>h_point_value:
    		h_point_value=point_value
    		but_text_list[7][2]=str(h_point_value)
    		file=open("hpointr.txt","w+")
    		file.write(str(h_point_value))
    		file.close()
    if game_start==True:
    	surface.fill((0, 0, 0))
#button images   	
    	buttons(b_x1,b_y1,b_col1)
    	buttons(b_x2,b_y2,b_col2)
    	buttons(b_x3,b_y3,b_col3)
    	buttons(b_x4,b_y4,b_col4)
    	buttons(b_x5,b_y5,b_col5)
    	exit_button("Back",b_x5,b_y5)
#button texts

    
    	for i in range(8):
    		but_text(but_text_list[i][0],but_text_list[i][1],but_text_list[i][2],but_text_list[i][3])
#snakefoods
    	snakefood(sf_x,sf_y)
    	
#main snake    
    	for i in range(len(main_box_list)):
    		if i==0:
    			mb_body_col=(255,0,0)
    		else:
    			mb_body_col=(255,100,100)
    		main_box(main_box_list[i][0],main_box_list[i][1],mb_body_col)
#field of snake
    	bigframe(bf_line_col)
    if menu_start==True:
    	surface.fill((0, 0, 0))
    	b_col5=(255,255,255)
    	pygame.draw.rect(surface,(255,255,255),[mb_x1,mb_y1,260,100],5)
    	pygame.draw.rect(surface,(255,255,255),[mb_x2,mb_y2,200,100],5)
    	for i in range(2):
    		exit_button(mbut_text_list[i][0],mbut_text_list[i][1],mbut_text_list[i][2])
    if theame_start==True:
    	pygame.draw.rect(surface,(255,255,255),[500,500,260,100],5)
    	
    
    pygame.display.flip()
