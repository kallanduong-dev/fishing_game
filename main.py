import pygame
import os
import random

pygame.font.init()
pygame.mixer.init()

#set window 
WIDTH, HEIGHT = 1120,704
WIN = pygame.display.set_mode((Constants.WIDTH,Constants.HEIGHT))
pygame.display.set_caption("Fishing Freak")


TITLEFONT = pygame.font.SysFont("comicsans",50   )
TEXTFONT = pygame.font.SysFont("comicsans",20   )
MIDFONT = pygame.font.SysFont("comicsans",30   )

TILEMAP = [
'...............................pp..',
'....wwwwwwwwwwwwwwwwwwwwwwwwww.pp..',
'....wwwwwwwwwwwwwwwwwwwwwwwwww.pp..',
'....wwwwwwwwwwwwwwwwwwwwwwwwww.pp..',
'....wwwwwwwwwwwwwwwwwwwwwwwwww.pp..',
'....wwwwwwwwwwwwwwwwwwwwwwwwww.pp..',
'...............................pp..',
'...............................pp..',
'ppppppppppppppppppppppppppppppppppp',
'ppppppppppppppppppppppppppppppppppp',
'..pp...............................',
'..pp...............................',
'..pp...............................',
'..pp...............................',
'..pp...............................',
'sssssssssssssssssssssssssssssssssss',
'sssssssssssssssssssssssssssssssssss',
'sssssssssssssssssssssssssssssssssss',
'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
]

OFFSET = 40
FISHZONE = 5

WHITE = (255,255,255)
GREEN = (0, 154, 23)
BLUE = (0,94,184)
BLACK = (0,0,0)

ZONE1 = pygame.Rect(125,100,150,500)
ZONE2 = pygame.Rect(475,100,150,500)
ZONE3 = pygame.Rect(825,100,150,500)

FPS = 60
VEL = 2
OBJECTVEL = 15
FISHVEL = 18
BARVEL = 15

FISHERMANWIDTH = 35
FISHERMANHEIGHT = 25
TILESIZE = 32

FISHERMANIMAGE = pygame.image.load(os.path.join('Assets','fisherman.png'))
FISHERMANL = pygame.transform.scale(FISHERMANIMAGE,(FISHERMANWIDTH,FISHERMANHEIGHT))
FISHERMANR = pygame.transform.flip(FISHERMANL, True, False)

CHESTIMAGE = pygame.image.load(os.path.join('Assets','chest.png'))
CHESTWIDTH = 45
CHESTHEIGHT = 40
CHEST = pygame.transform.scale(CHESTIMAGE,(CHESTWIDTH,CHESTHEIGHT))
CHESTX, CHESTY = 10, 210

WATERIMAGE = pygame.image.load(os.path.join('Assets','water.png'))
WATER = pygame.transform.scale(WATERIMAGE,(TILESIZE,TILESIZE))

GRASSIMAGE = pygame.image.load(os.path.join('Assets','grass.png'))
GRASS = pygame.transform.scale(GRASSIMAGE,(TILESIZE,TILESIZE))

SANDIMAGE = pygame.image.load(os.path.join('Assets','sand.png'))
SAND = pygame.transform.scale(SANDIMAGE,(TILESIZE,TILESIZE))

PATHIMAGE = pygame.image.load(os.path.join('Assets','path.png'))
PATH = pygame.transform.scale(PATHIMAGE,(TILESIZE,TILESIZE))

HOOKIMAGE = pygame.image.load(os.path.join('Assets','hook.png'))
HOOKWIDTH = 80
HOOKHEIGHT = 120
HOOK = pygame.transform.rotate(pygame.transform.scale(HOOKIMAGE,(HOOKWIDTH,HOOKHEIGHT)),90)

SEAWEEDIMAGE = pygame.image.load(os.path.join('Assets','seaweed.png'))
SEAWEEDWIDTH = 350
SEAWEEDHEIGHT = 600
SEAWEEDBOT = pygame.transform.scale(SEAWEEDIMAGE,(SEAWEEDWIDTH,SEAWEEDHEIGHT))
SEAWEEDTOP = pygame.transform.flip(SEAWEEDBOT, False, True)

FISHIMAGE = pygame.image.load(os.path.join('Assets','fish.png'))
FISHWIDTH = 300
FISHHEIGHT = 150
FISHR = pygame.transform.scale(FISHIMAGE,(FISHWIDTH,FISHHEIGHT))
FISHL = pygame.transform.flip(FISHR, True, False)

STARHEIGHT = 30
STARWIDTH = 35
STARIMAGE = pygame.image.load(os.path.join('Assets','star.png'))
STAR = pygame.transform.scale(STARIMAGE,(STARWIDTH,STARHEIGHT))

LAKEXMIN = 3.5*32
LAKEXMAX = 29.5*32
LAKEYMIN = 11
LAKEYMAX = 6*32-16
BEACHTOP = 17.3*32

FISHING_MUSIC = pygame.mixer.Sound(os.path.join('Assets','accumula.mp3'))
CATCHING_CLICK = pygame.mixer.Sound(os.path.join('Assets','click.wav'))
CAUGHT_SF = pygame.mixer.Sound(os.path.join('Assets','caught.wav'))
CAUGHT_SCREEN = pygame.mixer.Sound(os.path.join('Assets','caughtscreen.wav'))
SW_COLLISION = pygame.mixer.Sound(os.path.join('Assets','swcollision.wav'))
SW_COLLISION.set_volume(0.3)
FISH_GONE = pygame.mixer.Sound(os.path.join('Assets','fishgone.wav'))
SW_COLLISION.set_volume(0.3)
CHEST_OPEN = pygame.mixer.Sound(os.path.join('Assets','chestopen.mp3'))
CHEST_CLOSE = pygame.mixer.Sound(os.path.join('Assets','chestclose.mp3'))

resize = ["Octopus","Anglerfish"]

FISHAREA2 = ["Herring","Flounder","Halibut","Cod","Snapper","Stingray","Tuna","Sunfish","Mahi Mahi","Coelecanth"]
FISHAREA4 = ["Anchovy","Sardine","Pufferfish","Shrimp","Crab","Lobster","Octopus","Blue Marlin","Shark","Giant Squid"]
FISHAREA3 = ["Carp","Catfish","Largemouth Bass","Smallmouth Bass","Salmon","Pike","Tilapia","Sturgeon","Gar","Loch Ness"]
FISHAREA1 = ["Yellow Perch","Bullhead","Chub","Rainbow Trout","Crayfish","Bream","Walleye","Anglerfish","Tiger Trout","Arapaima"]

ALL_FISH = ["Herring","Flounder","Halibut","Cod","Anchovy","Sardine","Pufferfish","Shrimp","Carp","Catfish","Largemouth Bass","Smallmouth Bass","Yellow Perch","Bullhead","Chub","Rainbow Trout","Snapper","Stingray","Tuna","Crab","Lobster","Octopus","Salmon","Pike","Tilapia","Crayfish","Bream","Walleye","Sunfish","Mahi Mahi","Blue Marlin","Shark","Sturgeon","Gar","Anglerfish","Tiger Trout","Coelecanth","Giant Squid","Loch Ness","Arapaima"]

FISH_AREA_ORDERED = ["Yellow Perch","Bullhead","Chub","Rainbow Trout","Crayfish","Bream","Walleye","Anglerfish","Tiger Trout","Arapaima","Herring","Flounder","Halibut","Cod","Snapper","Stingray","Tuna","Sunfish","Mahi Mahi","Coelecanth","Carp","Catfish","Largemouth Bass","Smallmouth Bass","Salmon","Pike","Tilapia","Sturgeon","Gar","Loch Ness","Anchovy","Sardine","Pufferfish","Shrimp","Crab","Lobster","Octopus","Blue Marlin","Shark","Giant Squid"]

FISHIMAGELIST = []
FISHYWIDTH = 500
FISHYHEIGHT = 200
SMALLFISHYWIDTH = 75
SMALLFISHYHEIGHT = 30

SMALLFISHIMAGELIST = []

for fish in FISH_AREA_ORDERED:
    FISHYIMAGE = pygame.image.load(os.path.join('Assets',f'{fish}.png'))
    if fish == "Sunfish":
        SMALLFISHY = pygame.transform.scale(FISHYIMAGE,(50,40))
    elif fish == "Pufferfish":
        SMALLFISHY = pygame.transform.scale(FISHYIMAGE,(60,40))
    elif fish in resize:
        SMALLFISHY = pygame.transform.scale(FISHYIMAGE,(70,40))
    else:
        SMALLFISHY = pygame.transform.scale(FISHYIMAGE,(SMALLFISHYWIDTH,SMALLFISHYHEIGHT))
    SMALLFISHIMAGELIST.append(SMALLFISHY)

for fish in FISH_AREA_ORDERED:
    FISHYIMAGE = pygame.image.load(os.path.join('Assets',f'{fish}.png'))
    if fish == "Sunfish":
        FISHY = pygame.transform.scale(FISHYIMAGE,(440,380))
    elif fish == "Pufferfish":
        FISHY = pygame.transform.scale(FISHYIMAGE,(470,380))
    elif fish in resize:
        FISHY = pygame.transform.scale(FISHYIMAGE,(500,380))
    else:
        FISHY = pygame.transform.scale(FISHYIMAGE,(FISHYWIDTH,FISHYHEIGHT))
    FISHIMAGELIST.append(FISHY)


class game_state():
    def __init__(self):
        self.state = 'main_game'

    def walkabout(self,startx,starty):
        player = pygame.Rect(startx,starty,FISHERMANWIDTH,FISHERMANHEIGHT)
        clock = pygame.time.Clock()
        direction = 1
        run = True

        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f and ((player.x > CHESTX-FISHZONE and player.x < CHESTX+CHESTWIDTH) and (player.y > CHESTY-FISHZONE and player.y < CHESTY+CHESTHEIGHT)) :
                        CHEST_OPEN.play()
                        return 5, player.x, player.y
                    if event.key == pygame.K_f and ((player.x > LAKEXMIN-FISHZONE and player.x < LAKEXMAX+FISHZONE and player.y > LAKEYMIN-FISHZONE and player.y < LAKEYMAX + FISHZONE) or player.y > BEACHTOP-FISHZONE):
                        return 2, player.x, player.y
           
            #movement
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_a] and player.x - VEL > 0 and (player.x < LAKEXMIN or player.x - VEL > LAKEXMAX or player.y < LAKEYMIN or player.y > LAKEYMAX): #left 
                player.x -= VEL
                direction = 2
            if keys_pressed[pygame.K_d] and player.x + VEL < WIDTH-OFFSET and (player.x + VEL < LAKEXMIN or player.x > LAKEXMAX or player.y < LAKEYMIN or player.y > LAKEYMAX): #right 
                player.x += VEL
                direction = 1
            if keys_pressed[pygame.K_w] and player.y - VEL > 0 and (player.x < LAKEXMIN or player.x > LAKEXMAX or player.y < LAKEYMIN or player.y - VEL > LAKEYMAX): #up
                player.y -= VEL
            if keys_pressed[pygame.K_s] and player.y + VEL < HEIGHT-OFFSET and (player.x < LAKEXMIN or player.x > LAKEXMAX or player.y + VEL < LAKEYMIN or player.y > LAKEYMAX) and player.y + VEL < BEACHTOP: #down
                player.y += VEL
            
            draw_walkabout(player,direction)
        return None,1,1


    def fishing(self):
        player = pygame.Rect(2,300,HOOKWIDTH,HOOKHEIGHT)
        clock = pygame.time.Clock()
        run = True
        count = 0
        seaweeds = []
        fish = None

        randdifficulty = random.random()
        if randdifficulty < 0.45:
            difficulty = 0
            frequency = 60
        elif randdifficulty >= 0.45 and randdifficulty < 0.8:
            difficulty = 10
            frequency = 50
        elif randdifficulty >= 0.8 and randdifficulty < 0.95:
            difficulty = 15
            frequency = 40
        else:
            difficulty = 20
            frequency = 30
        while run:
            clock.tick(FPS)
            count += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            #movement 
            x,y = pygame.mouse.get_pos()
            player.x = x
            player.y = y

            #check if player collides with seaweed
            for i in range(len(seaweeds)):
                if x > seaweeds[i][0].x + 100 and x < seaweeds[i][0].x + 200 and y > 300 and seaweeds[i][1] == 1:
                    SW_COLLISION.play()
                    return 1,1
                if x > seaweeds[i][0].x + 100 and x < seaweeds[i][0].x + 200 and y < 350 and seaweeds[i][1] == 2:
                    SW_COLLISION.play()
                    return 1,1 
                i += 1

            #generate random fish
            fishchance = random.random()
            if fishchance < 0.25 and count % 90 == 0 and fish == None:
                height = random.randint(100,900)
                fish = pygame.Rect(1000,height,FISHWIDTH,FISHHEIGHT)

            #check fish collision or fish off the map 
            if fish:
                if x > fish.x and x < fish.x + 200 and y >= height and y < height + 100:
                    CAUGHT_SF.play()
                    return 3, difficulty
                if fish.x < -50:
                    FISH_GONE.play()
                    return 1,1
                fish.x -= FISHVEL

            #generate obstacle on top or bottom
            if count % frequency == 0:
                rand = random.random()
                if rand >= 0.5:
                    seaweed = pygame.Rect(1000,-100,SEAWEEDWIDTH,SEAWEEDHEIGHT)
                    seaweeds.append([seaweed,2])
                else:
                    seaweed = pygame.Rect(1000,200,SEAWEEDWIDTH,SEAWEEDHEIGHT)
                    seaweeds.append([seaweed,1])
            
            #draw screen
            draw_fishing(player,seaweeds,fish)

            #decrement seaweed position
            for s in seaweeds:
                s[0].x -= (OBJECTVEL + difficulty)

            
        return None,1
        

    def catching(self,difficulty):
        clock = pygame.time.Clock()
        step = 1
        run = True
        height = 200
        direction = 2
        xpos = 125
        targ1y = random.randint(110,480)
        targ2y = random.randint(110,480)
        targ3y = random.randint(110,480)
        targheight = 90-2*difficulty
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if step == 1 and height <= targ1y + targheight and height >= targ1y:
                            xpos = 475
                            step = 2
                    elif step == 2 and height <= targ2y + targheight and height >= targ2y:
                            xpos = 825
                            step = 3
                    elif step == 3 and height <= targ3y + targheight and height >= targ3y:
                            CATCHING_CLICK.play()
                            return 4
                    else:
                        return 1
                    CATCHING_CLICK.play()

            if height > 600:
                direction = 1
            if height < 100:
                direction = 2
            if direction == 1: 
                height -= BARVEL
            if direction == 2:
                height += BARVEL
                
            bar = pygame.Rect(xpos,height,150,10)
            draw_catching(step,bar,targ1y,targ2y,targ3y,targheight)
        return None


    def caught(self,difficulty,x,y):
        CAUGHT_SCREEN.play()
        clock = pygame.time.Clock()

        run = True
        if difficulty == 20:
            index = 9
            rarity = "Legendary"
        elif difficulty == 15:
            index = random.randint(7,8)
            rarity = "Rare"
        elif difficulty == 10:
            index = random.randint(4,6)
            rarity = "Uncommon"
        else:
            index = random.randint(0,4)
            rarity = "Common"

        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    return 1,fish,(area-1)*10+index

            if x < WIDTH / 2 and y < HEIGHT / 2:
                fish = FISHAREA1[index]
                area = 1
            elif x < WIDTH / 2 and y > HEIGHT / 2:
                fish = FISHAREA2[index]
                area = 2
            elif x > WIDTH / 2 and y < HEIGHT / 2:
                fish = FISHAREA3[index]
                area = 3
            elif x > WIDTH / 2 and y > HEIGHT / 2:
                fish = FISHAREA4[index]
                area = 4

            draw_caught(fish,rarity,index,area)

        return None,None,1

    def collection(self,catchstate,lencaught):
        clock = pygame.time.Clock()
        run = True

        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    CHEST_CLOSE.play()
                    return 1

            draw_collection(catchstate,lencaught)

        return None

def draw_collection(catchstate,lencaught):
    WIN.fill((BLUE))
    location = 120
    col = 50
    title = TITLEFONT.render(f"Fish Collection ({lencaught}/40 fish)",1,WHITE)
    WIN.blit(title,(200,20))
    for i in range(40):
        if i == 10:
            col = 310
            location = 120
        if i == 20:
            col = 580
            location = 120
        if i == 30:
            col = 850
            location = 120
        if catchstate[i] == True:
            textTBD = TEXTFONT.render(f"{FISH_AREA_ORDERED[i]}",1,WHITE)
            WIN.blit(textTBD,(col,location))
            WIN.blit(STAR,(col-10,location+20))
            if i >= 16:
                WIN.blit(STAR,(col+15,location+20))
            if i >= 28:
                WIN.blit(STAR,(col+40,location+20))
            if i >= 36:
                WIN.blit(STAR,(col+65,location+20))
            WIN.blit(SMALLFISHIMAGELIST[i],(col+150,location+11))
        else:
            textTBD = TEXTFONT.render(f"?????????",1,WHITE)
            WIN.blit(textTBD,(col,location))
        location += 50
    pygame.display.update()


def draw_caught(fish,rarity,index,area):
    WIN.fill((BLUE))
    textTBD = MIDFONT.render(f"Congratulations You Caught a {fish} ({rarity})",1,WHITE)
    WIN.blit(textTBD,(200,100))
    WIN.blit(FISHIMAGELIST[(area-1)*10+index],(300,300))
    pygame.display.update()
            
def draw_catching(step,bar,targ1y,targ2y,targ3y,targheight):
    WIN.fill((BLUE))
    TARGET1 = pygame.Rect(125,targ1y,150,targheight)
    TARGET2 = pygame.Rect(475,targ2y,150,targheight)
    TARGET3 = pygame.Rect(825,targ3y,150,targheight)
    pygame.draw.rect(WIN,WHITE,ZONE1)
    pygame.draw.rect(WIN,WHITE,ZONE2)
    pygame.draw.rect(WIN,WHITE,ZONE3)
    pygame.draw.rect(WIN,GREEN,TARGET1)
    pygame.draw.rect(WIN,GREEN,TARGET2)
    pygame.draw.rect(WIN,GREEN,TARGET3)

    if step == 1:
        pygame.draw.rect(WIN,BLACK,bar)
    if step == 2:
        pygame.draw.rect(WIN,BLACK,bar)
    if step == 3:
        pygame.draw.rect(WIN,BLACK,bar)
    pygame.display.update()

def draw_fishing(player,seaweeds,fish):
    WIN.fill((BLUE))
    line = pygame.Rect(0,player.y,player.x,5)
    WIN.blit(HOOK,(player.x-15,player.y-38))
    pygame.draw.rect(WIN,(0,0,0),line)
    for seaweed in seaweeds:
        if seaweed[0].x > -50:
            if seaweed[1] == 1:
                WIN.blit(SEAWEEDBOT,(seaweed[0].x,seaweed[0].y))
            else:
                WIN.blit(SEAWEEDTOP,(seaweed[0].x,seaweed[0].y))
    if fish:
        WIN.blit(FISHL,(fish.x,fish.y))
    pygame.display.update()


def draw_walkabout(player,direction):
    WIN.fill((GREEN))

    for i in range(len(TILEMAP)):
        for j in range(len(TILEMAP[i])):
            x = (j) * TILESIZE
            y = (i) * TILESIZE
            if TILEMAP[i][j] == 'w':
                WIN.blit((WATER),(x,y))
            elif TILEMAP[i][j] == 's':
                WIN.blit((SAND),(x,y))
            elif TILEMAP[i][j] == 'p':
                WIN.blit((PATH),(x,y))
            else:
                WIN.blit((GRASS),(x,y))
    WIN.blit((CHEST),(CHESTX,CHESTY))              
    if direction == 1:
        WIN.blit(FISHERMANR,(player.x,player.y))
    else:
        WIN.blit(FISHERMANL,(player.x,player.y))

    pygame.display.update()

def main():
    GameState = game_state()
    gstate = 1
    x = 100
    y = 300
    caught = []
    FISHING_MUSIC.play(-1)
    FISHING_MUSIC.set_volume(0.065)
    with open('savedata.txt') as sf:
        lines = sf.readlines()
        for line in lines:
            if line != '\n':
                caught.append(line[:len(line)-1])

    catchstate = [False] * 40
    

    for i in range(len(FISH_AREA_ORDERED)):
        if FISH_AREA_ORDERED[i] in caught:
            catchstate[i] = True
            print(i)

        
    while gstate:
        if gstate == 1:  
            gstate, x, y = GameState.walkabout(x,y)
        if gstate == 2:
            gstate, difficulty = GameState.fishing()
        if gstate == 3:
            gstate = GameState.catching(difficulty)
        if gstate == 4:
            gstate,fish,index = GameState.caught(difficulty,x,y)
            if fish:
                if fish not in caught:
                    caught.append(fish)
                    catchstate[index] = True
        if gstate == 5:
            gstate = GameState.collection(catchstate,len(caught))

    with open(r'/Users/kallan/Documents/Project/FishingGame/savedata.txt', 'w') as sf:
        for item in caught:
            sf.write("%s\n" % item)

    pygame.quit()

if __name__ == "__main__":
    main()


