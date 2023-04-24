# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:49:47 2023

@author: WIN10 PRO 22H2
"""

import pygame
from Blob import Blob
BLUE_BLOBS=10
RED_BLOBS=5
WIDTH=800
HEIGHT=600
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)

game_display=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blob Game")
clock= pygame.time.Clock()

def draw_Environment(blob_list):
    game_display.fill(WHITE)
    for blob_dict in blob_list:
        
        for blob_id in blob_dict:
            blob=blob_dict[blob_id]
            pygame.draw.circle(game_display,blob.color,[blob.x,blob.y],blob.size)
            #pygame.draw.line(game_display,blob.color,start_pos=(blob.i,blob.j), end_pos=(blob.K,blob.L))

            blob.move()
            blob.move_boundary()
            
    
    pygame.display.update()
    
def main():
    blue_blobs = dict(enumerate([Blob(BLUE,WIDTH,HEIGHT) for i in range(BLUE_BLOBS)]))
    red_blobs=dict(enumerate([Blob(RED,WIDTH,HEIGHT) for i in range(RED_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                
        
        draw_Environment([blue_blobs,red_blobs])
        #draw_Environment(red_blobs)
        clock.tick(50)
        #print(red_blob.x,red_blob.y)
    
    
if __name__ == '__main__':
    main()