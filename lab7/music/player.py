import pygame



pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))


WHITE = (255, 255, 255)


musics = ["track1.mp3","track2.mp3", 'track3.mp3']
ct = 0


v = 0.4
def play_music(track):
    pygame.mixer.music.load(track)
    pygame.mixer.music.play()

pygame.mixer.music.set_volume(v)


running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
           
            elif event.key == pygame.K_RIGHT:
                ct = (ct + 1) % len(musics)
                play_music(musics[ct])
          
            elif event.key == pygame.K_LEFT:
                ct = (ct - 1) % len(musics)
                play_music(musics[ct])
        
            elif event.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()

            if event.key == pygame.K_UP:
                v += 0.2
                pygame.mixer.music.set_volume(v)
            if event.key == pygame.K_DOWN:
                v -= 0.2
                pygame.mixer.music.set_volume(v)

    
    screen.fill(WHITE)
    
    pygame.display.flip()


pygame.quit()
