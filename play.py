import pygame
import random
#from music_utils import play_background_music
from utils import draw_text, play_sound, stop_sound, draw_button, play_background_music
from moviepy.editor import VideoFileClip

def play_video_in_popup(file, start_time, end_time, screen):
    clip = VideoFileClip(file).subclip(start_time, end_time)
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

def generate_problem():
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)
    if operation == '+':
        a, b = random.randint(1, 10), random.randint(1, 10)
        answer = a + b
    elif operation == '-':
        a, b = random.randint(1, 10), random.randint(1, 10)
        if a < b:
            a, b = b, a
        answer = a - b
    elif operation == '*':
        a, b = random.randint(1, 10), random.randint(1, 10)
        answer = a * b
    elif operation == '/':
        b = random.randint(1, 10)
        a = b * random.randint(1, 10)
        answer = a // b
    return a, b, operation, answer

def run_play_section(screen, font):
    problems = [generate_problem() for _ in range(5)]
    random.shuffle(problems)

    story = [
        ("What do you think, who will cross the bridge first? Solve this question to find out.", "assets/sounds/1.wav"),
        ("Oh no! Now how will these cuties cross the bridge. Keep answering...", "assets/sounds/2.wav"),
        ('These cuties turned out to be "Chhota packet, Bada dhamaka." Don\'t stop answering!', "assets/sounds/3.wav"),
        ("Not again...Will they be able to cross the bridge?? Answer to find out.", "assets/sounds/4.wav"),
        ("Wow!! They crossed the bridge by using their brains and not power. Continue applying your brains to solve this last question.", "assets/sounds/5.wav")
    ]
    current_problem = 0
    user_answer = ''
    current_story_index = 0
    video_played = False
    audio_played = [False] * len(story)

    video_segments = [
        ("assets/videos/bridge.mp4", 0, 44), 
        ("assets/videos/bridge.mp4", 44, 82), 
        ("assets/videos/bridge.mp4", 82, 106), 
        ("assets/videos/bridge.mp4", 106, 128),
        ("assets/videos/bridge.mp4", 128, 139)
    ]

    def display_story_and_problem():
        screen.fill((255, 255, 255))  # Clear the screen with a white color
        
        if current_story_index < len(story):
            draw_text(screen, story[current_story_index][0], (50, 50), font, color=(139, 69, 19)) 
        
        if current_problem < len(problems):
            a, b, operation, _ = problems[current_problem]
            question = f"{a} {operation} {b} = ?"
            draw_text(screen, question, (50, 250), font, color=(0, 0, 128)) 
            draw_text(screen, user_answer, (50, 350), font, color=(0, 0, 128))  

        # Draw Back button
        back_button = pygame.Rect(680, 10, 100, 50)
        draw_button(screen, "Back", back_button, font, color=(255, 0, 0))
        
        pygame.display.flip()

    def play_current_video_segment():
        nonlocal video_played
        if not video_played and current_story_index < len(video_segments):
            video_path, start_time, end_time = video_segments[current_story_index]
            play_background_music("assets/sounds/background_music.mp3")
            play_video_in_popup(video_path, start_time, end_time, screen)
            video_played = True

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_sound()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = event.pos
                    # Check if Back button is clicked
                    if pygame.Rect(680, 10, 100, 50).collidepoint(mouse_pos):
                        stop_sound()
                        return "back_to_menu"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    _, _, _, correct_answer = problems[current_problem]
                    if user_answer == str(correct_answer):
                        current_problem += 1
                        current_story_index += 1
                        user_answer = ''
                        video_played = False
                        if current_problem >= len(problems):
                            current_problem = 0
                            running = False
                    else:
                        user_answer = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_answer = user_answer[:-1]
                else:
                    user_answer += event.unicode

        display_story_and_problem()
        
        if not video_played:
            play_current_video_segment()
        elif video_played and not audio_played[current_story_index]:
            stop_sound()
            play_sound(story[current_story_index][1])
            audio_played[current_story_index] = True

    stop_sound()  # Ensure any sound effects are stopped
    play_background_music("assets/sounds/background_music.mp3")
    return "back_to_menu"

