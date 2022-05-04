import pygame
import random




pygame.init()
screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("ShootingGame")

clock=pygame.time.Clock()
game_font=pygame.font.Font(None,40)
game_result="game over!"
            
background=pygame.image.load(r"\night.png")
chargrond=pygame.image.load(r"\jet.png")
enemygrond=pygame.image.load(r"\nom.png")
missile=pygame.image.load(r"\missile.png")

chargrond_size=chargrond.get_rect().size
chargrond_width=chargrond_size[0]
chargrond_height=chargrond_size[1]
chargrond_x_pos=screen_width/2-chargrond_width/2
chargrond_y_pos=screen_height-chargrond_height

enemygrond_size=enemygrond.get_rect().size
enemygrond_width=enemygrond_size[0]
enemygrond_height=enemygrond_size[1]
enemygrond_x_pos=screen_width/2-enemygrond_width/2
enemygrond_y_pos=0-enemygrond_height

missile_size=missile.get_rect().size
missile_width=missile_size[0]
missile_height=missile_size[1]
missile_x_pos=chargrond_x_pos+chargrond_width/2-missile_width/2
missile_y_pos=chargrond_y_pos

total_time=10
start_tick=pygame.time.get_ticks()




to_x=0
to_y=0
char_speed=1
enemy_speed=10
missile_speed=10   
missile_to_y=0
running=True
while running:
    dt=clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                to_x-=char_speed
            elif event.key==pygame.K_RIGHT:
                to_x+=char_speed
            elif event.key==pygame.K_DOWN:
                to_y+=char_speed
            elif event.key==pygame.K_UP:
                to_y-=char_speed
            elif event.key==pygame.K_SPACE:
                missile_x_pos=chargrond_x_pos+chargrond_width/2-missile_width/2
                missile_y_pos=chargrond_y_pos
                missile_to_y-=missile_speed



        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                to_x=0
            elif event.key==pygame.K_DOWN or event.key==pygame.K_UP:
                to_y=0

    chargrond_x_pos+=to_x*dt
    chargrond_y_pos+=to_y*dt
    missile_y_pos+=missile_to_y

    if chargrond_x_pos<0:
        chargrond_x_pos=0
    elif chargrond_x_pos>screen_width-chargrond_width:
        chargrond_x_pos=screen_width-chargrond_width
    
    enemygrond_y_pos+=enemy_speed
    if enemygrond_y_pos>screen_height:
        enemygrond_y_pos=0
        enemygrond_x_pos=random.randrange(0,screen_width-chargrond_width)
        enemy_speed+=3

    if chargrond_y_pos<0:
        chargrond_y_pos=0
    elif chargrond_y_pos>screen_height-chargrond_height:
        chargrond_y_pos=screen_height-chargrond_height

    chargrond_rect=chargrond.get_rect()
    chargrond_rect.left=chargrond_x_pos
    chargrond_rect.top=chargrond_y_pos

    enemygrond_rect=enemygrond.get_rect()
    enemygrond_rect.left=enemygrond_x_pos
    enemygrond_rect.top=enemygrond_y_pos

    if chargrond_rect.colliderect(enemygrond_rect):
        game_result="Crask! Game Over"
        running=False

    
    screen.blit(background,(0,0))
    screen.blit(missile,(missile_x_pos,missile_y_pos))
    screen.blit(chargrond,(chargrond_x_pos,chargrond_y_pos))
    screen.blit(enemygrond,(enemygrond_x_pos,enemygrond_y_pos))



    elapser_time=(pygame.time.get_ticks()-start_tick)/1000
    remaining_time=int(total_time-elapser_time)
    timer=game_font.render("Time:"+str(remaining_time),True,(255,255,255))
    screen.blit(timer,(10,10))
    #print(remaining_time)
    if remaining_time<=0:
        game_result="Time Over!"
        running=False
    pygame.display.update()

msg=game_font.render(game_result,True,(255,255,255))
msg_rect=msg.get_rect(center=(int(screen_width/2),int(screen_height/2)))
screen.blit(msg,(msg_rect))
pygame.display.update()
pygame.time.delay(2000)

pygame.quit()