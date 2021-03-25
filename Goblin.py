import pygame

pygame.init()#you need initalize the pygame

win = pygame.display.set_mode((500,480))#window size

pygame.display.set_caption("Fight with Goblin")

#load aniamation images. In this case can change other computers. if this doesnt work for you try  pygame.image.load('R1.png')
walkRight = [pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R1.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R2.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R3.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R4.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R5.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R6.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R7.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R8.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R9.png')]
walkLeft = [pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L1.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L2.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L3.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L4.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L5.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L6.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L7.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L8.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L9.png')]
bg = pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\bg.jpg')
char = pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\standing.png')

music = pygame.mixer.music.load(r'C:\Users\Furkan\Documents\Python\Game\Game\music.mp3')
pygame.mixer.music.play(-1)

class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)#characters has a hitbox, if bullet hit the hitbox than we understand bullet or enemy hit the characters

        
    def draw(self,win):
        if self.walkCount +1 >=27:#FPS is 27, if walk more than 27 than stop.
            self.walkCount = 0

        #animation of standing type
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x,self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))        
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)#create a hitbox
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.x = 60 
        self.y = 410 
        self.walkCount = 0
        font = pygame.font.SysFont('comicsans', 75)
        text = font.render("You are dying", 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        
        x = 0
        while x < 300:
            pygame.time.delay(10)
            x += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    x = 301
                    pygame.quit()
        

#create bullets 
class Projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class Enemy(object):
    walkRight = [pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R1E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R2E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R3E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R4E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R5E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R6E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R7E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R8E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R9E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R10E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\R11E.png')]
    walkLeft = [pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L1E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L2E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L3E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L4E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L5E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L6E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L7E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L8E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L9E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L10E.png'), pygame.image.load(r'C:\Users\Furkan\Documents\Python\Game\Game\L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True


    #enemy walking constantly


    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            #create damage bar. 
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False  
            font2 = pygame.font.SysFont('comicsans', 50)  
            text = font2.render('GOBLIN IS DEAD', 1, (255,0,0))
            win.blit(text, (250 - (text.get_width()/2),200))
            pygame.display.update()
        print('hit')
 


def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    win.blit(text, (390, 10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()



#mainloop
clock = pygame.time.Clock()#for FPS
score = 0
font = pygame.font.SysFont('comicsans', 30, True)
man = Player(200, 410, 64,64)
goblin = Enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)#FPS

    if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
            man.hit()
            score -= 5

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    #necessary to avoid getting an error when the window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    #Buttons settings
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(Projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()