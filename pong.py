import pygame,sys,random

pygame.init()

screen=pygame.display.set_mode((700,500))
clock=pygame.time.Clock()
mylist=[-2.1,-2,2,2.1]
ball_x=random.choice(mylist)
ball_y=random.choice(mylist)
red_y=0
blue_y=0
run=True
bluescore=0
redscore=0
ballhitleft=False
ballhitright=False


def change_score():
	
	blue_score=game_font.render(str(bluescore),True,(255,255,255))
	blue_rect=blue_score.get_rect(center=(175,50))
	red_score=game_font.render(str(redscore),True,(255,255,255))
	red_rect=red_score.get_rect(center=(525,50))
	screen.blit(blue_score,blue_rect)
	screen.blit(red_score,red_rect)

def update_score():
	global ballhitleft,ballhitright,redscore,bluescore
	if ballhitleft==True:
		if ball.y>150 and ball.y<350:
			redscore+=2
			ballhitleft=False
		else:
			redscore+=1
			ballhitleft=False
	if ballhitright==True:
		if ball.y>150 and ball.y<350:
			bluescore+=2
			ballhitright=False
		else:
			bluescore+=1
			ballhitright=False

def check_score():
	
	if redscore>=7 or bluescore>=7:
		return False
		
	return True	



			

blue=pygame.Rect(10,200,10,100)
red=pygame.Rect(680,200,10,100)
ball=pygame.Rect(343,243,14,14)
circle=pygame.Rect(300,200,100,100)

game_font=pygame.font.Font('04B_19.ttf',40)

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_UP and run==True:
				red_y=0
				red_y-=2
			if event.key==pygame.K_DOWN and run==True:
				red_y=0
				red_y+=2
			if event.key==pygame.K_w and run==True:
				blue_y=0
				blue_y-=2
			if event.key==pygame.K_s and run==True:
				blue_y=0
				blue_y+=2
				
	



			
	red.y+=red_y
	blue.y+=blue_y	
	ball.x+=ball_x	
	ball.y+=ball_y

	if ball.top<=10 :
		ball_y=-ball_y
	if ball.bottom>=490:
		ball_y=-ball_y
		
	if ball.left<=10:
		ball_x=-ball_x
		ballhitleft=True
	if ball.right>=690:
		ball_x=-ball_x
		ballhitright=True

	if ball.colliderect(red):
		ball_x=-ball_x
	if ball.colliderect(blue):
		ball_x=-ball_x
		



		

	screen.fill((0,0,0))
	#pygame.draw.ellipse(screen,(255,225,225),circle)
	if run:
		pygame.draw.rect(screen,(0,0,255),blue)
		pygame.draw.rect(screen,(255,0,0),red)
		pygame.draw.aaline(screen,(255,225,225),(350,10),(350,490))
		pygame.draw.aaline(screen,(255,225,225),(7,10),(693,10))
		pygame.draw.aaline(screen,(255,225,225),(7,490),(693,490))
		pygame.draw.aaline(screen,(255,225,225),(7,10),(7,490))
		pygame.draw.aaline(screen,(255,225,225),(693,10),(693,490))
		pygame.draw.aaline(screen,(255,225,225),(7,150),(120,150))
		pygame.draw.aaline(screen,(255,225,225),(120,150),(120,350))
		pygame.draw.aaline(screen,(255,225,225),(7,350),(120,350))
		pygame.draw.aaline(screen,(255,225,225),(580,150),(693,150))
		pygame.draw.aaline(screen,(255,225,225),(580,150),(580,350))
		pygame.draw.aaline(screen,(255,225,225),(580,350),(693,350))
		change_score()
		update_score()
		run=check_score()


		pygame.draw.ellipse(screen,(255,165,0),ball)
	else:
		pygame.draw.rect(screen,(0,0,255),blue)
		pygame.draw.rect(screen,(255,0,0),red)
		pygame.draw.aaline(screen,(255,225,225),(350,10),(350,490))
		pygame.draw.aaline(screen,(255,225,225),(7,10),(693,10))
		pygame.draw.aaline(screen,(255,225,225),(7,490),(693,490))
		pygame.draw.aaline(screen,(255,225,225),(7,10),(7,490))
		pygame.draw.aaline(screen,(255,225,225),(693,10),(693,490))
		pygame.draw.aaline(screen,(255,225,225),(7,150),(120,150))
		pygame.draw.aaline(screen,(255,225,225),(120,150),(120,350))
		pygame.draw.aaline(screen,(255,225,225),(7,350),(120,350))
		pygame.draw.aaline(screen,(255,225,225),(580,150),(693,150))
		pygame.draw.aaline(screen,(255,225,225),(580,150),(580,350))
		pygame.draw.aaline(screen,(255,225,225),(580,350),(693,350))
		pygame.draw.ellipse(screen,(255,165,0),ball)
		change_score()
		
		ball_x=0
		ball_y=0
		red_y=0
		blue_y=0	



		
	
	
	
	
	
	
	
	

	


	if red.top<=10:
		red_y=0
	if red.bottom>=490:
		red_y=0
	if blue.top<=10:
		blue_y=0
	if blue.bottom>=490:
		blue_y=0

		

	


	pygame.display.update()	
	clock.tick(200)	