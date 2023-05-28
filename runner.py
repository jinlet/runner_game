import pygame
from sys import exit
from random import randint

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surface = text.render(f'Score:{current_time/1000:.0f}', False, (64,64,64))
    score_rectangle = score_surface.get_rect(center = (400,40))
    screen.blit(score_surface, score_rectangle)
    return current_time

def enemy_movement(enemy_list):
    if enemy_list:
        for enemy_rect in enemy_list:
            enemy_rect.x -= 5

            if enemy_rect.bottom == 300:
                screen.blit(dog_surf, enemy_rect)
            elif enemy_rect.bottom == 210:
                screen.blit(bird_surf, enemy_rect)
            else:
                screen.blit(hound_surf, enemy_rect)
        
        enemy_list = [enemy for enemy in enemy_list if enemy.x > -100] 
        return enemy_list
    else:
        return []

def collisions(player, enemy):
    if enemy:
        for enemy_rect in enemy:
            if player.colliderect(enemy_rect):
                return False
    return True

def player_animation():
    # Play walking animation if player is on ground
    # Play jump animation when player is not on ground
    global player_surface, player_walk_idx, player_jump_idx, player_stand_idx

    if game_active:
        if player_rectangle.bottom < 300:
            # Jump
            player_jump_idx += 0.1
            if player_jump_idx >= len(player_jump):player_jump_idx = 0
            player_surface = player_jump[int(player_jump_idx)]

        else:
            # Walk
            player_walk_idx += 0.1
            if player_walk_idx >= len(player_walk): player_walk_idx = 0
            player_surface = player_walk[int(player_walk_idx)]

pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
text = pygame.font.Font('fonts/joystix.monospace-regular.otf', 30) #To display score
game_active = False
start_time = 0
score = 0

""" We use rectangles for positioning and collisions"""
sky_surface = pygame.image.load('graphics/sky.png').convert() # Convert before they are blitted too many times/ convert makes code run faster
ground_surface = pygame.image.load('graphics/ground.png').convert()


#Enemy
dog_frame1 = pygame.image.load('graphics/enemy/dog1.png').convert_alpha()
dog_frame1 = pygame.transform.scale(dog_frame1, (64,54))
dog_frame2 = pygame.image.load('graphics/enemy/dog2.png').convert_alpha()
dog_frame2 = pygame.transform.scale(dog_frame2, (64,54))
dog_frame3 = pygame.image.load('graphics/enemy/dog3.png').convert_alpha()
dog_frame3 = pygame.transform.scale(dog_frame3, (64,54))
dog_frames = [dog_frame1, dog_frame2, dog_frame3]
dog_frames_idx = 0
dog_surf = dog_frames[dog_frames_idx]

bird_frame1 = pygame.image.load('graphics/enemy/bird1.png').convert_alpha()
bird_frame1 = pygame.transform.scale(bird_frame1, (74,64))
bird_frame2 = pygame.image.load('graphics/enemy/bird2.png').convert_alpha()
bird_frame2 = pygame.transform.scale(bird_frame2, (74,64))
bird_frames = [bird_frame1, bird_frame2]
bird_frames_idx = 0
bird_surf = bird_frames[bird_frames_idx]

hound_frame1 = pygame.image.load('graphics/enemy/hound1.png').convert_alpha()
hound_frame1 = pygame.transform.scale(hound_frame1, (64,54))
hound_frame2 = pygame.image.load('graphics/enemy/hound2.png').convert_alpha()
hound_frame2 = pygame.transform.scale(hound_frame2, (64,54))
hound_frame3 = pygame.image.load('graphics/enemy/hound3.png').convert_alpha()
hound_frame3 = pygame.transform.scale(hound_frame3, (64,54))
hound_frames = [hound_frame1, hound_frame2, hound_frame3]
hound_frames_idx = 0
hound_surf = hound_frames[hound_frames_idx]


enemy_rect_list = []


#Player
player_walk1 = pygame.image.load('graphics/player/walk1.png').convert_alpha()
player_walk1 = pygame.transform.scale(player_walk1, (84, 84))

player_walk2 = pygame.image.load('graphics/player/walk2.png').convert_alpha()
player_walk2 = pygame.transform.scale(player_walk2, (84, 84))
player_walk3 = pygame.image.load('graphics/player/walk3.png').convert_alpha()
player_walk3 = pygame.transform.scale(player_walk3, (84, 84))
player_walk4 = pygame.image.load('graphics/player/walk4.png').convert_alpha()
player_walk4 = pygame.transform.scale(player_walk4, (84, 84))
player_walk5 = pygame.image.load('graphics/player/walk5.png').convert_alpha()
player_walk5 = pygame.transform.scale(player_walk5, (84, 84))
player_walk6 = pygame.image.load('graphics/player/walk6.png').convert_alpha()
player_walk6 = pygame.transform.scale(player_walk6, (84, 84))
player_walk = [player_walk1, player_walk2, player_walk3, player_walk4, player_walk5,player_walk6] # Walking animation
player_walk_idx = 0

player_jump1 = pygame.image.load('graphics/player/jump1.png').convert_alpha()
player_jump1 = pygame.transform.scale(player_jump1, (84, 84))
player_jump2 = pygame.image.load('graphics/player/jump2.png').convert_alpha()
player_jump2 = pygame.transform.scale(player_jump2, (84, 84))
player_jump3 = pygame.image.load('graphics/player/jump3.png').convert_alpha()
player_jump3 = pygame.transform.scale(player_jump3, (84, 84))
player_jump4 = pygame.image.load('graphics/player/jump4.png').convert_alpha()
player_jump4 = pygame.transform.scale(player_jump4, (84, 84))
player_jump5 = pygame.image.load('graphics/player/jump5.png').convert_alpha()
player_jump5 = pygame.transform.scale(player_jump5, (84, 84))
player_jump6 = pygame.image.load('graphics/player/jump6.png').convert_alpha()
player_jump6 = pygame.transform.scale(player_jump6, (84, 84))
player_jump = [player_jump1,player_jump2,player_jump3,player_jump4,player_jump5,player_jump6]
player_jump_idx = 0

player_surface = player_walk[player_walk_idx]
player_rectangle = player_surface.get_rect(bottomleft = (80,300)) # Creates rectangle for easier placement control
player_gravity = 0 # To imitate gravity when falling



#Start screen
player_stand1 = pygame.image.load('graphics/player/idle1.png').convert_alpha()
player_stand1 = pygame.transform.scale(player_stand1, (192, 192)) #Scaling
player_stand2 = pygame.image.load('graphics/player/idle2.png').convert_alpha()
player_stand2 = pygame.transform.scale(player_stand2, (192, 192)) #Scaling
player_stand3 = pygame.image.load('graphics/player/idle3.png').convert_alpha()
player_stand3 = pygame.transform.scale(player_stand3, (192, 192)) #Scaling
player_stand4 = pygame.image.load('graphics/player/idle4.png').convert_alpha()
player_stand4 = pygame.transform.scale(player_stand4, (192, 192)) #Scaling

player_stand = [player_stand1, player_stand2, player_stand3, player_stand4]
player_stand_idx = 0

player_stand_rectangle = player_stand1.get_rect(center = (400,200))



game_name = text.render('Start screen', False, (111,196,169))
game_name_rectangle = game_name.get_rect(center = (400,80))

game_message = text.render('Press enter to run', False, (111,196,169))
game_message_rectangle = game_message.get_rect(center=(400,310))

game_over = text.render('Game Over', False, (111,196,169))
game_over_rectangle = game_over.get_rect(center = (400,80))

#Spawn timer
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1900)

dog_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(dog_animation_timer,200)

bird_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(bird_animation_timer,200)

hound_animation_timer = pygame.USEREVENT + 4
pygame.time.set_timer(hound_animation_timer,200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom == 300:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_active = True
                start_time = pygame.time.get_ticks()
        
        if game_active:
            if event.type == enemy_timer:
                enemy_type = randint(0,2) # Either spawn enemy 1, 2 or 3
                if enemy_type == 0:
                    enemy_rect_list.append(dog_surf.get_rect(bottomleft = (randint(900,1300),300))) #Spawn enemy at random x-coord
                elif enemy_type == 1:
                    enemy_rect_list.append(bird_surf.get_rect(bottomleft = (randint(900,1300),210)))
                else:
                    enemy_rect_list.append(hound_surf.get_rect(bottomleft=(randint(900, 1300), 301)))

            if event.type == dog_animation_timer:
                if dog_frames_idx == 0: dog_frames_idx = 1
                elif dog_frames_idx == 1: dog_frames_idx = 2
                else: dog_frames_idx = 0
                dog_surf = dog_frames[dog_frames_idx]

            if event.type == bird_animation_timer:
                if bird_frames_idx == 0: bird_frames_idx = 1
                else: bird_frames_idx = 0
                bird_surf = bird_frames[bird_frames_idx]

            if event.type == hound_animation_timer:
                if hound_frames_idx == 0: hound_frames_idx = 1
                elif hound_frames_idx == 1: hound_frames_idx = 2
                else: hound_frames_idx = 0
                hound_surf = hound_frames[hound_frames_idx]
  
    if game_active:
        # Block image transfers of all objects
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rectangle, 20)
        # pygame.draw.rect(screen, '#c0e8ec', score_rectangle)
        # screen.blit(score_surface, score_rectangle)
        score = display_score()

        #Enemy
        # enemy_rectangle.x -= 4
        # if enemy_rectangle.right < 0:
        #     enemy_rectangle.x = 800
        # screen.blit(enemy_surface,enemy_rectangle)

        #Player
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300
        player_animation()
        screen.blit(player_surface,player_rectangle)

        #Enemy movements
        enemy_rect_list = enemy_movement(enemy_rect_list)

        #Collisions
        game_active = collisions(player_rectangle, enemy_rect_list)


    else:
        #Intro screen
        screen.fill((94,129,162))
        player_stand_idx += 0.1
        if player_stand_idx >= len(player_stand):player_stand_idx = 0
        player_surface = player_stand[int(player_stand_idx)]
        screen.blit(player_surface, player_stand_rectangle)
        score_message = text.render(f'Score: {score/1000:.0f}', False, (111,196,169))
        score_message_rectangle = score_message.get_rect(center = (400,310))

        enemy_rect_list.clear()
        player_rectangle.midbottom = (80,300) #To start at the beginning 
        player_gravity = 0
        
        #Text for intro screen
        if score == 0:
            screen.blit(game_name, game_name_rectangle)
            screen.blit(game_message,game_message_rectangle)
        else:
            screen.blit(score_message,score_message_rectangle)
            screen.blit(game_over, game_over_rectangle)
    

    pygame.display.update()
    clock.tick(60) #To not run faster than x60/s