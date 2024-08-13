import pygame
import sys
from learn import run_learn_section
from play import run_play_section
from test import run_test_section
from utils import draw_text, load_image, draw_button, play_background_music, stop_background_music

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Educational Math Game")
font = pygame.font.SysFont(None, 55)
menu_background = load_image("assets/images/background.jpg", 800, 600)

# Play background music when the game starts
play_background_music("assets/sounds/background_music.mp3")

def main_menu():
    screen.blit(menu_background, (0, 0))
    
    # Define buttons
    button_1 = pygame.Rect(275, 150, 250, 75)
    button_2 = pygame.Rect(275, 250, 250, 75)
    button_3 = pygame.Rect(275, 350, 250, 75)
    
    draw_button(screen, "Learn", button_1, font, color=(25, 25, 112))
    draw_button(screen, "Play", button_2, font, color=(25, 25, 112))
    draw_button(screen, "Test", button_3, font, color=(25, 25, 112))
    
    # Draw Exit button
    exit_button = pygame.Rect(680, 10, 100, 50)
    draw_button(screen, "Exit", exit_button, font, color=(255, 0, 0))
    
    pygame.display.flip()
    return [button_1, button_2, button_3, exit_button]

def main_game_loop():
    buttons = main_menu()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_background_music()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = event.pos
                    if buttons[0].collidepoint(mouse_pos):
                        run_learn_section(screen, font)
                        buttons = main_menu()
                    elif buttons[1].collidepoint(mouse_pos):
                        result = run_play_section(screen, font)
                        if result == "back_to_menu":
                            buttons = main_menu()
                            play_background_music("assets/sounds/background_music.mp3")
                    elif buttons[2].collidepoint(mouse_pos):
                        result = run_test_section(screen, font)
                        if result == "back_to_menu":
                            buttons = main_menu()
                            play_background_music("assets/sounds/background_music.mp3")
                    elif buttons[3].collidepoint(mouse_pos):  # Exit button
                        stop_background_music()
                        running = False

    pygame.quit()
    sys.exit()

main_game_loop()
