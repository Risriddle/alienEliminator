import pygame
import math
import random
from pygame import mixer

# Function to check if the mouse is over a button
def is_over_button(button_rect):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return button_rect.collidepoint(mouse_x, mouse_y)

# Function to display the game menu with buttons
def game_menu():
    menu_font = pygame.font.Font("freesansbold.ttf", 64)
    menu_text = menu_font.render("Space Invaders", True, (255, 255, 255))
    screen.blit(menu_text, (200, 200))

    # Play button
    play_button = pygame.Rect(300, 300, 200, 50)
    pygame.draw.rect(screen, (0, 128, 255), play_button)
    play_text = font.render("Play", True, (255, 255, 255))
    screen.blit(play_text, (350, 310))

    # Quit button
    quit_button = pygame.Rect(300, 370, 200, 50)
    pygame.draw.rect(screen, (255, 0, 0), quit_button)
    quit_text = font.render("Quit", True, (255, 255, 255))
    screen.blit(quit_text, (350, 380))

    pygame.display.update()

    # Check for button clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            l1.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if is_over_button(play_button):
                l1.started = True
            elif is_over_button(quit_button):
                l1.running = False


# Function to display the game over menu with high score
def game_over_menu(high_score):
    menu_font = pygame.font.Font("freesansbold.ttf", 64)
    over_text = menu_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 200))

    # Display high score
    high_score_text = font.render("High Score: " + str(high_score), True, (255, 255, 255))
    screen.blit(high_score_text, (300, 300))

    # Replay button
    replay_button = pygame.Rect(300, 370, 200, 50)
    pygame.draw.rect(screen, (0, 128, 255), replay_button)
    replay_text = font.render("Replay", True, (255, 255, 255))
    screen.blit(replay_text, (350, 380))

    # Quit button
    quit_button = pygame.Rect(300, 440, 200, 50)
    pygame.draw.rect(screen, (255, 0, 0), quit_button)
    quit_text = font.render("Quit", True, (255, 255, 255))
    screen.blit(quit_text, (350, 450))

    pygame.display.update()

    # Check for button clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            l1.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if is_over_button(replay_button):
                l1.score_value=0
                l1.started = True
            elif is_over_button(quit_button):
                l1.running = False




class Player:
    def __init__(self):
        self.playerImg = pygame.image.load("static/spaceship.png")
        self.playerX = 370
        self.playerY = 480
        self.playerX_change = 0

    def drawPlayer(self):
        screen.blit(self.playerImg, (self.playerX, self.playerY))

class Enemy:
    def __init__(self,x,y):
        self.enemyImg=[]
        self.enemyX=[]
        self.enemyY=[]
        self.enemyX_change=[]
        self.enemyY_change=[]
        self.num_of_enemies=5
        for i in range(self.num_of_enemies):
           self.enemyImg.append(pygame.image.load("static/alien.png"))
           self.enemyX.append(random.randint(0,736))
           self.enemyY.append(random.randint(50,250))
           self.enemyX_change.append(3)
           self.enemyY_change.append(15)

    def drawEnemy(self,x,y,i):
        screen.blit(self.enemyImg[i], (x,y))
       
    
    
   
class Bullet:
    def __init__(self):
        self.bulletImg=pygame.image.load("static/bullet.png")
        self.bulletX=0
        self.bulletY=480
        self.bulletX_change=0
        self.bulletY_change=1
        
    def drawBullet(self):
            global bullet_state
            bullet_state = "fire"
            screen.blit(self.bulletImg, (self.bulletX+16, self.bulletY+10))


class Asteroid:
    def __init__(self):
        self.asteroidImg = []
        self.asteroidX = []
        self.asteroidY = []
        self.asteroidY_change = []
        self.num_of_asteroids = 4
        self.asteroid_speed=0.4
        for i in range(self.num_of_asteroids):
            self.asteroidImg.append(pygame.image.load("static/asteroid.png"))
            self.asteroidX.append(random.randint(0, 736))
            self.asteroidY.append(random.randint(50,550))  # Start each asteroid above the screen
            self.asteroidY_change.append(self.asteroid_speed)  
        self.explosionImg = pygame.image.load("static/explosion.png")
        self.explosionX = 0
        self.explosionY = 0
        self.explosion_state = "ready"

    def explosion(self,x, y):
       screen.blit(self.explosionImg, (x, y))

 
    # asteroids function, to draw image of asteroids we use blit function
    def asteroids(self,x, y, i):
      screen.blit(self.asteroidImg[i], (x, y))


class EnemyLaser:
    def __init__(self):
        self.laserImg = []
        self.laserX = []
        self.laserY = []
        self.laserY_change = []
        self.num_of_lasers = 4
        self.laser_speed=0.4
        for i in range(self.num_of_lasers):
            self.laserImg.append(pygame.image.load("static/flash.png"))
            self.laserX.append(random.randint(0, 736))
            self.laserY.append(random.randint(50,550))  # Start each asteroid above the screen
            self.laserY_change.append(self.laser_speed)  
        self.explosionImg = pygame.image.load("static/explosion.png")
        self.explosionX = 0
        self.explosionY = 0
        self.explosion_state = "ready"

    def explosion(self,x, y):
       screen.blit(self.explosionImg, (x, y))
    
    def lasers(self,x, y, i):
      screen.blit(self.laserImg[i], (x, y))

    

# Enemy class with lasers
class EnemyL:
    def __init__(self):
        self.enemyImg=[]
        self.enemyX=[]
        self.enemyY=[]
        self.enemyX_change=[]
        self.enemyY_change=[]
        self.num_of_enemies=6
    
        for i in range(self.num_of_enemies):
           self.enemyImg.append(pygame.image.load("static/ufo.png"))
           self.enemyX.append(random.randint(0,736))
           self.enemyY.append(random.randint(50,250))
           self.enemyX_change.append(5)
           self.enemyY_change.append(15)
        self.enemyLasers = []
        self.laser_cooldown = random.randint(500, 2000)  # Initial cooldown
        
        
    def draw_Enemy(self,x,y,i):
        screen.blit(self.enemyImg[i], (x,y))
        



class GameLevel:
    def __init__(self):
        self.level = "1"
        self.score_value=0
        self.running=True
        self.started=False
        self.high_score=0
        
    def game_over_text(self):
        #over_font = pygame.font.Font("freesansbold.ttf", 70)
        over_text = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (210, 250))
        
    def display_level_transition(self, message):
        level_text = font.render(message, True, (255, 255, 255))
        screen.blit(level_text, (210, 250))
        pygame.display.update()
        pygame.time.delay(2000) 

    def show_score(self,x,y):
        #s = pygame.font.Font("freesansbold.ttf", 70)
        score = font.render("Score:" + str(self.score_value), True, (255, 255, 255))
        screen.blit(score, (x,y))
        
    def isCollision(self, x1, x2, y1, y2):
        distance = math.sqrt((math.pow(x1 - y1, 2)) + (math.pow(x2 - y2, 2)))
        if distance < 37:
            return True
        else:
            return False
    
    def level1(self):
        global bullet_state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.playerX_change = -0.2
                if event.key == pygame.K_RIGHT:
                    player.playerX_change = 0.2
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound("static/laser.wav")
                        bullet_sound.play()
                        bullet.bulletX = player.playerX
                        bullet.drawBullet()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.playerX_change = 0

        player.playerX += player.playerX_change
        #to keep player in boundary
        if player.playerX<=0:
         player.playerX=0
        elif player.playerX>=(800-64):
         player.playerX=736
         
         
        if self.score_value >= 10 and not l2.started:  # Check if the score is 5 and level 2 is not started
            self.display_level_transition("LEVEL 2")  # Display level transition message
            l2.started = True  # Set the flag to indicate that level 2 has started
        
        if self.score_value >20 and not l3.started:  # Check if the score is 5 and level 2 is not started
            self.display_level_transition("LEVEL 3")  # Display level transition message
            l3.started = True  # Set the flag to indicate that level 2 has started

        
        if self.score_value>=10 and  self.score_value<=20 and not l3.started:
            l2.level2()
        
        if self.score_value>20 or l3.started:
            l3.level3()
            
        for i in range(enemy.num_of_enemies):
            enemy.enemyX[i] += enemy.enemyX_change[i]

            if enemy.enemyX[i]<=0:
                enemy.enemyX_change[i]=0.1
                enemy.enemyY[i]+=enemy.enemyY_change[i]
            elif enemy.enemyX[i]>=(800-64):
                enemy.enemyX_change[i]=-0.1
                enemy.enemyY[i]+=enemy.enemyY_change[i]

            if enemy.enemyY[i] >= 400:
                for j in range(enemy.num_of_enemies):
                    enemy.enemyY[j] = 2000
                if l1.score_value >= self.high_score:
                    self.high_score = l1.score_value  # Update high score
                    game_over_menu(self.high_score)
                    pygame.display.update()
                    pygame.time.delay(5000)
                #self.game_over_text()

            collision = self.isCollision(enemy.enemyX[i], enemy.enemyY[i], bullet.bulletX, bullet.bulletY)
            if collision:
                explosion_sound = mixer.Sound("static/explosion.wav")
                explosion_sound.play()
                bullet.bulletY = 480
                bullet_state = "ready"
                self.score_value += 1
                print(self.score_value)
                enemy.enemyX[i] = random.randint(0, 735)
                enemy.enemyY[i] = random.randint(50, 150)

            enemy.drawEnemy(enemy.enemyX[i],enemy.enemyY[i],i)

        if bullet_state == "fire":
            bullet.drawBullet()
            bullet.bulletY -= bullet.bulletY_change
        if bullet.bulletY <= 0:
            bullet.bulletY = 480
            bullet_state = "ready"

        player.drawPlayer()
        self.show_score(textX, textY)
        pygame.display.update()
        screen.blit(background, (0, 0))
    
    def level2(self):
        for i in range(aster.num_of_asteroids):
          aster.asteroidY[i] += aster.asteroidY_change[i]

        # reset asteroid position if it goes beyond the screen
          if aster.asteroidY[i] > 600:
            aster.asteroidY[i] = random.randint(50, 150)  # Reset the Y-coordinate above the screen
            aster.asteroidX[i] = random.randint(0, 736)  # Reset the X-coordinate

        # Check for collision with the player
          if self.isCollision(aster.asteroidX[i], aster.asteroidY[i],player.playerX,player.playerY):
            aster.explosionX = player.playerX-150
            aster.explosionY = player.playerY-150
            aster.explosion_state = "explode"
            if aster.explosion_state == "explode":
                aster.explosion(aster.explosionX, aster.explosionY)
                l2_sound=mixer.Sound("static/l2over.mp3")
                mixer.music.pause()
                l2_sound.play()
                pygame.time.delay(500)
                if l1.score_value >= self.high_score:
                    self.high_score = l1.score_value  # Update high score
                    game_over_menu(self.high_score)
                    pygame.display.update()
                    pygame.time.delay(5000)  # Add a delay to show the high score menu
                l1.running = False  # End the game when there's a collision


          aster.asteroids(aster.asteroidX[i],aster.asteroidY[i], i)
        
    
    def level3(self):
     global bullet_state
     for i in range(laser.num_of_lasers):
          laser.laserY[i] += laser.laserY_change[i]

        # reset asteroid position if it goes beyond the screen
          if laser.laserY[i] > 600:
            laser.laserY[i] = random.randint(50, 150)  # Reset the Y-coordinate above the screen
            laser.laserX[i] = random.randint(0, 736)  # Reset the X-coordinate

        # Check for collision with the player
          if self.isCollision(laser.laserX[i], laser.laserY[i],player.playerX,player.playerY):
            laser.explosionX = player.playerX-150
            laser.explosionY = player.playerY-150
            laser.explosion_state = "explode"
            if laser.explosion_state == "explode":
                laser.explosion(laser.explosionX, laser.explosionY)
                l2_sound=mixer.Sound("static/l2over.mp3")
                mixer.music.pause()
                l2_sound.play()
                pygame.time.delay(500)
                if l1.score_value >= self.high_score:
                    self.high_score = l1.score_value  # Update high score
                    game_over_menu(self.high_score)
                    pygame.display.update()
                    pygame.time.delay(15000)
                l1.running = False  # End the game when there's a collision


          laser.lasers(laser.laserX[i],laser.laserY[i], i)
        
    
     for i in range(enemyL.num_of_enemies):
            enemyL.enemyX[i] += enemyL.enemyX_change[i]
            
            if enemyL.enemyX[i]<=0:
                enemyL.enemyX_change[i]=0.1
                enemyL.enemyY[i]+=enemyL.enemyY_change[i]
            elif enemyL.enemyX[i]>=(800-64):
                enemyL.enemyX_change[i]=-0.1
                enemyL.enemyY[i]+=enemyL.enemyY_change[i]

            if enemyL.enemyY[i] >= 400:
                for j in range(enemy.num_of_enemies):
                    enemyL.enemyY[j] = 2000
                
                self.game_over_text()

            collision = self.isCollision(enemyL.enemyX[i], enemyL.enemyY[i], bullet.bulletX, bullet.bulletY)
            if collision:
                explosion_sound = mixer.Sound("static/explosion.wav")
                explosion_sound.play()
                bullet.bulletY = 480
                bullet_state = "ready"
                self.score_value += 1
                print(self.score_value)
                enemyL.enemyX[i] = random.randint(0, 735)
                enemyL.enemyY[i] = random.randint(50, 150)

            enemyL.draw_Enemy(enemyL.enemyX[i],enemyL.enemyY[i],i)
            
    
     if bullet_state == "fire":
            bullet.drawBullet()
            bullet.bulletY -= bullet.bulletY_change
     if bullet.bulletY <= 0:
            bullet.bulletY = 480
            bullet_state = "ready"
    

# Initializing pygame
pygame.init()

# Setting up the screen
screen = pygame.display.set_mode((800, 600))

# Background image
background = pygame.image.load("static/back.png")

# Background music
mixer.music.load("static/background_music.mp3")
mixer.music.play(-1)

# Changing title, adding icon logo
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("static/ufo.png")
pygame.display.set_icon(icon)

# Creating instances of classes
player = Player()
bullet = Bullet()
enemy = Enemy(0, 0)  # You may want to adjust the starting position of the first enemy
aster=Asteroid()
laser=EnemyLaser()
enemyL=EnemyL()
bullet_state="ready"
# Other game-related variables


font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10
l1=GameLevel()
l2=GameLevel()
l3=GameLevel()
# Main game loop

while l1.running:
    if not l1.started:
        game_menu()
    else:
        l1.level1()
        
    