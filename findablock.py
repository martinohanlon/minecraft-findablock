from mcpi.minecraft import Minecraft
from mcpi import block
from random import randint
from gpiozero import LED, Buzzer
from time import sleep
from math import sqrt

#create connection to Minecraft
mc = Minecraft.create()

mc.postToChat("Go find the block")

#get players position
p = mc.player.getTilePos()

#hide a gold block near the player
#create a random position
x = p.x + randint(-20, 20)
y = p.y + randint(-5, 5)
z = p.z + randint(-20, 20)

#create the gold block
mc.setBlock(x, y, z, block.GOLD_BLOCK.id)

#create LED
led = LED(4)

#create the buzzer
buzz = Buzzer(17)

#flash all the LED and buzz on
led.on()
buzz.on()

sleep(1)

led.off()
buzz.off()

dist = 0

gameover = False

while gameover == False:
    
    #get the players position now
    p = mc.player.getTilePos()
    
    #work out the distance between the player and the gold block
    xd = p.x - x
    yd = p.y - y
    zd = p.z - z
    dist_now = sqrt((xd*xd) + (yd*yd) + (zd*zd))

    #if dist is going up turn the buzz on, otherwise turn it off
    if dist_now > dist:
        buzz.on()
    else:
        buzz.off()

    dist = dist_now
        
    #if dist is less than 5 turn the led on
    if dist_now < 5:
        led.on()
    else:
        led.off()

    if dist_now < 1.5:
        gameover = True
        mc.postToChat("You got GOLD")
        led.off()
        buzz.off()
