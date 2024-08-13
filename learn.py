import pygame
from moviepy.editor import VideoFileClip
from utils import draw_text, draw_button

def play_video_in_popup(file, screen):
    clip = VideoFileClip(file)
    video_size = (400, 300)
    video_surface = pygame.Surface(video_size)
    screen_width, screen_height = screen.get_size()
    popup_position = ((screen_width - video_size[0]) // 2, (screen_height - video_size[1]) // 2)
    
    clock = pygame.time.Clock()
    
    for frame in clip.iter_frames(fps=24, with_times=False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                clip.close()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Exit video on ESC key press
                    clip.close()
                    return

        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        frame_surface = pygame.transform.scale(frame_surface, video_size)
        video_surface.blit(frame_surface, (0, 0))
        screen.blit(video_surface, popup_position)
        pygame.display.flip()
        clock.tick(24)  # Maintain the frame rate
        
    clip.close()

def run_learn_section(screen, font):
    videos = {
        "Addition": "assets/videos/addition.mp4",
        "Subtraction": "assets/videos/addition.mp4",
        "Multiplication": "assets/videos/multiplication.mp4",
        "Division": "assets/videos/division.mp4"
    }
    background_image = pygame.image.load("assets/images/background.jpg")
    background_image = pygame.transform.scale(background_image, screen.get_size())

    def display_learn():
        screen.blit(background_image, (0, 0))
        draw_text(screen, "Select a topic to learn:", (50, 50), font, color=(0, 0, 128))

        button_addition = pygame.Rect(275, 150, 250, 75)
        button_subtraction = pygame.Rect(275, 250, 250, 75)
        button_tables = pygame.Rect(275, 350, 250, 75)
        button_division = pygame.Rect(275, 450, 250, 75)
        button_back = pygame.Rect(725, 10, 75, 30)

        draw_button(screen, "Addition", button_addition, font, color=(25, 25, 112))
        draw_button(screen, "Subtraction", button_subtraction, font, color=(25, 25, 112))
        draw_button(screen, "Multiplication", button_tables, font, color=(25, 25, 112))
        draw_button(screen, "Division", button_division, font, color=(25, 25, 112))
        draw_button(screen, "Back", button_back, font, color=(255, 0, 0))

        pygame.display.flip()
        return [button_addition, button_subtraction, button_tables, button_division, button_back]

    buttons = display_learn()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = event.pos
                    if buttons[0].collidepoint(mouse_pos):
                        play_video_in_popup(videos["Addition"], screen)
                    elif buttons[1].collidepoint(mouse_pos):
                        play_video_in_popup(videos["Subtraction"], screen)
                    elif buttons[2].collidepoint(mouse_pos):
                        play_video_in_popup(videos["Multiplication"], screen)
                    elif buttons[3].collidepoint(mouse_pos):
                        play_video_in_popup(videos["Division"], screen)
                    elif buttons[4].collidepoint(mouse_pos):
                        return

        display_learn()

