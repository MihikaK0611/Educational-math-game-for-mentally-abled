import pygame
import random
from utils import draw_text, play_sound, load_image, draw_button, play_background_music

def generate_questions(num_questions=20):
    operations = ['+', '-', '*', '/']
    questions = []
    while len(questions) < num_questions:  # Generate exactly num_questions unique questions
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(operations)
        if operation == '+':
            answer = num1 + num2
        elif operation == '-':
            answer = num1 - num2
        elif operation == '*':
            answer = num1 * num2
        elif operation == '/':
            num1 = num1 * num2  # Ensure division is exact
            answer = num1 / num2
        question_text = f"What is {num1} {operation} {num2}?"
        answer_choices = [answer, answer + random.randint(1, 5), answer - random.randint(1, 5)]
        random.shuffle(answer_choices)
        question = (question_text, list(map(str, answer_choices)), str(answer))
        if question not in questions:  # Ensure uniqueness
            questions.append(question)
    return questions

def run_test_section(screen, font):
    quiz_questions = generate_questions(20)  # Generate exactly 20 questions
    random.shuffle(quiz_questions)  # Shuffle the questions for random order
    current_question = 0
    score = 0

    test_background = load_image("assets/images/background.jpg", 800, 600)
    star_image = load_image("assets/images/star.png", 50, 50)  # Decorative stars

    feedback_start_time = None
    feedback_duration = 5000  # Duration to show feedback (in milliseconds)
    is_correct_feedback = False
    feedback_playing = False

    def display_question(question, score):
        screen.blit(test_background, (0, 0))
        question_text = font.render(question[0], True, (0, 100, 0))
        screen.blit(question_text, (150, 100))
        button_1 = pygame.Rect(275, 200, 250, 75)
        button_2 = pygame.Rect(275, 300, 250, 75)
        button_3 = pygame.Rect(275, 400, 250, 75)
        draw_button(screen, f"1. {question[1][0]}", button_1, font, color=(0, 100, 0))
        draw_button(screen, f"2. {question[1][1]}", button_2, font, color=(0, 100, 0))
        draw_button(screen, f"3. {question[1][2]}", button_3, font, color=(0, 100, 0))
        score_text = font.render(f"Score: {score}", True, (0, 0, 255))
        screen.blit(score_text, (350, 50))

        # Draw "Back to Main Menu" button
        back_button = pygame.Rect(650, 10, 140, 50)
        draw_button(screen, "Back", back_button, font, color=(255, 0, 0))
        
        pygame.display.flip()
        return [button_1, button_2, button_3, back_button]

    def display_final_score(score):
        play_background_music("assets/sounds/background_music.mp3")
        screen.blit(test_background, (0, 0))
        final_message = f"Congratulations! You scored {score} points out of 20!"
        draw_text(screen, final_message, (100, 250), font, color=(0, 100, 0))

        # Draw 5 decorative stars below the final message in a horizontal line
        text_rect = font.render(final_message, True, (0, 100, 0)).get_rect(center=(400, 300))
        star_y_position = text_rect.bottom + 20  # 20 pixels below the text
        star_positions = [
            (text_rect.centerx - 2.5 * star_image.get_width(), star_y_position),
            (text_rect.centerx - 1.5 * star_image.get_width(), star_y_position),
            (text_rect.centerx - 0.5 * star_image.get_width(), star_y_position),
            (text_rect.centerx + 0.5 * star_image.get_width(), star_y_position),
            (text_rect.centerx + 1.5 * star_image.get_width(), star_y_position),
        ]
        for pos in star_positions:
            screen.blit(star_image, pos)
        
        pygame.display.flip()
        pygame.time.wait(5000)  # Wait for 5 seconds before exiting

    def animate_feedback(is_correct, correct_answer=None):
        nonlocal feedback_start_time, feedback_playing, is_correct_feedback
        feedback_start_time = pygame.time.get_ticks()
        feedback_playing = True
        is_correct_feedback = is_correct
        if not is_correct:
            display_correct_answer(correct_answer)

    def display_correct_answer(answer):
        correct_text = f"The correct answer is: {answer}"
        draw_text(screen, correct_text, (150, 500), font, color=(54, 32, 4))  # Dark brown
        pygame.display.flip()
        pygame.time.wait(5000)  # Wait for 5 seconds to display the correct answer

    def check_for_button_clicks(mouse_pos):
        nonlocal current_question, score
        if buttons[0].collidepoint(mouse_pos):
            answer = quiz_questions[current_question][1][0]
        elif buttons[1].collidepoint(mouse_pos):
            answer = quiz_questions[current_question][1][1]
        elif buttons[2].collidepoint(mouse_pos):
            answer = quiz_questions[current_question][1][2]
        elif buttons[3].collidepoint(mouse_pos):  # Back to Main Menu button
            return "back_to_menu"
        else:
            return None

        if answer == quiz_questions[current_question][2]:
            play_sound("assets/sounds/correct.wav")
            animate_feedback(True)
        else:
            play_sound("assets/sounds/incorrect.wav")
            animate_feedback(False, quiz_questions[current_question][2])
        return None

    buttons = display_question(quiz_questions[current_question], score)

    running = True
    while running:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not feedback_playing:  # Left mouse button and not playing feedback
                    mouse_pos = event.pos
                    result = check_for_button_clicks(mouse_pos)
                    if result == "back_to_menu":
                        return "back_to_menu"  # Signal to return to main menu

        if feedback_playing and feedback_start_time and current_time - feedback_start_time >= feedback_duration:
            feedback_playing = False
            feedback_start_time = None
            if current_question < len(quiz_questions) - 1:
                current_question += 1
                if is_correct_feedback:
                    score += 1
                buttons = display_question(quiz_questions[current_question], score)
            else:
                display_final_score(score)
                running = False

        pygame.time.delay(10)  # Small delay to limit CPU usage

    return "completed"  # Indicate that the test section was completed
