import tesseract
import ctypes
import os
import pygame, sys
import pygame.camera
from pygame.locals import *

from PIL import Image

api = tesseract.TessBaseAPI()
api.SetOutputName("outputName");
api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetPageSegMode(tesseract.PSM_AUTO)
#mImgFile = "2.jpg"
#result = tesseract.ProcessPagesWrapper(mImgFile,api)
#print result
#print type(result)
'''
pygame.init()
pygame.camera.init()
screen = pygame.display.set_mode((640,480),0)
surface = pygame.surface.Surface((640,480),0,screen)
cam=pygame.camera.Camera(0,(640,480))
cam.start()
i=1
while 1:
    im = cam.get_image(surface)
    pygame.display.update()
    screen.blit(im,(0,0))
    #if i==400:
    #    pygame.image.save(im, "a.jpg")
    #    img="a.jpg"
    #    result = tesseract.ProcessPagesWrapper(img,api)
    #    print result
    #    print "ok"
    for event in pygame.event.get():
        # Shutdown with X button
        if event.type==pygame.QUIT:
            sys.exit()
        # Shutdown with ESC
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
    i=i+1
'''
im=Image.open("5.jpg")
#im=im.rotate(1)
im.save("e.jpg")
im2=im.convert("L")
im2.save("b.jpg")
threshold = 100
im = im2.point(lambda p: p > threshold and 255)
im.save("d.jpg")
img="d.jpg"
result = tesseract.ProcessPagesWrapper(img,api)
print result
print "ok"