import pygame

def play_background_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

def pause_background_music():
    pygame.mixer.music.pause()

def resume_background_music():
    pygame.mixer.music.unpause()
