import pygame

def calc_acc():
    global x_acc, y_acc
    y_acc = 0.09
    x_acc = 0.09
    absdiff_posx = abs(mousepos[0] - mainrect.x)
    absdiff_posy = abs(mousepos[1] - mainrect.y)
    absdiff_pos = (absdiff_posx, absdiff_posy)
    if absdiff_pos[0] > absdiff_pos[1] and absdiff_pos[1] !=0:
        x_acc = (absdiff_pos[0]/absdiff_pos[1])*0.09
    if absdiff_pos[0] < absdiff_pos[1] and absdiff_pos[0] !=0:
        y_acc = (absdiff_pos[1]/absdiff_pos[0])*0.09
        

pygame.init()
WIDTH, HEIGHT = 800, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#Basic Variables
x_pos , y_pos = 50 , 50
y_vel = 3
x_vel = 2
acceleration = 0.1
mainrect = pygame.Rect((x_pos, y_pos),(25 , 25))
plat = pygame.Rect((0, 300),(WIDTH, 1))
clock = pygame.time.Clock()
#Using bools instead of functions cuz lazy
draw_line = False
gravity = True
move = True
get_mousepos = True
arrived = False #nik oomok , checks if mainrect arrived at destination
running = True
while running:
    clock.tick(60)
    WIN.fill((0,0,0))
    keys = pygame.key.get_pressed()
    #This makes the line not follow the mouse after clicking
    if get_mousepos == True:
        mousepos = pygame.mouse.get_pos()
    #Applying Gravity
    if gravity == True:
        y_vel += acceleration
        mainrect.y += y_vel
    #Handling movement
    if move == True:
        if keys[pygame.K_RIGHT]:
            x_vel += acceleration
            mainrect.x += x_vel
        if keys[pygame.K_LEFT]:
            x_vel += acceleration
            mainrect.x -= x_vel
        if x_vel >10:
            x_vel = 10
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            x_vel = 2   
    #Collision Detection between the rectangle and the platform
    if pygame.Rect.colliderect(mainrect, plat):
        on_platform = True
        mainrect.y = 300 - mainrect.height
        y_vel = 0
        move = True
        arrived = False
    #Checking for mouse click and for line drawing
    if draw_line == True:
        print(x_acc ,y_acc)
        get_mousepos = False
        gravity = False
        move = False
        if mousepos[1] < 300: #==> Checking if mouse click is higher than platform
            if x_vel > 10:
                x_vel = 10
            pygame.draw.line(WIN, (0 , 255 , 100), (mainrect.x, mainrect.y),mousepos, 1)
            if mainrect.x  != mousepos[0]:
                x_vel += x_acc
                if mainrect.x < mousepos[0]:
                    mainrect.x += x_vel
                if mainrect.x > mousepos[0]:
                    mainrect.x -= x_vel
            if mainrect.y != mousepos[1]:
                y_vel += y_acc
                if mainrect.y > mousepos[1]:
                    mainrect.y -= y_vel
                if mainrect.y < mousepos[1]:
                    mainrect.y += y_vel
            if pygame.Rect.collidepoint(mainrect, mousepos[0], mousepos[1]):#==> check for collision between rectangle and the mouse point
                arrived = True
                if x_vel > 10:
                    x_vel = 10
                draw_line = False
                get_mousepos = True
                if diff_posy > 0:
                    gravity = True
                    y_vel = -y_vel/2
                if diff_posy < 0:
                    gravity = True
        else: #==> if mouse click is under the platform
            get_mousepos = True
            gravity = True
            draw_line = False
            move = True


    if arrived == True:
        if diff_posx < 0:
            x_vel -= acceleration
            mainrect.x += x_vel
            if x_vel < 0:
                x_vel = 0
                arrived = False
                gravity = True
        if diff_posx > 0:
            x_vel -= acceleration
            mainrect.x -= x_vel
            if x_vel < 0:
                x_vel = 0
                arrived = False
                gravity = True

   
    #print(x_vel, arrived)
    #drawing principal objects
    pygame.draw.rect(WIN,(255, 255 ,255),mainrect)
    pygame.draw.rect(WIN, (255 , 255 , 255) , plat)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #check for mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            calc_acc()
            y_vel = 0
            diff_posx = (mainrect.x - mousepos[0])
            diff_posy = (mainrect.y - mousepos[1])
            absdiff_posx = abs(mousepos[0] - mainrect.x)
            absdiff_posy = abs(mousepos[1] - mainrect.y)
            absdiff_pos = (absdiff_posx, absdiff_posy)
            draw_line = True
