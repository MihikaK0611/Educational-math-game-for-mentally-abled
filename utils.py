import pygame

def play_background_music(music_path, loops=-1):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(loops=loops)

def stop_background_music():
    pygame.mixer.music.stop()

def draw_text(screen, text, position, font, color=(0, 0, 0), max_width=750):
    words = text.split(' ')
    lines = []
    current_line = []
    width, _ = position
    space_width, _ = font.size(' ')
    
    for word in words:
        word_surface = font.render(word, True, color)
        word_width, word_height = word_surface.get_size()
        
        if width + word_width >= max_width:
            lines.append((current_line, width))
            current_line = []
            width = position[0]
        
        current_line.append(word)
        width += word_width + space_width
    
    lines.append((current_line, width))
    
    y = position[1]
    for line, _ in lines:
        line_surface = font.render(' '.join(line), True, color)
        screen.blit(line_surface, (position[0], y))
        y += font.get_height()

def load_image(path, width=None, height=None):
    image = pygame.image.load(path)
    if width and height:
        image = pygame.transform.scale(image, (width, height))
    return image

def play_sound(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def stop_sound():
    pygame.mixer.music.stop()

def draw_button(screen, text, rect, font, color=(0, 0, 0), bg_color=(255, 255, 255)):
    pygame.draw.rect(screen, bg_color, rect)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)
