import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1100, 800
FPS = 60

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BUTTON_COLOR = (0, 150, 0)
BUTTON_TEXT_COLOR = WHITE

clock = pygame.time.Clock()
running = True
cookie_clicked = False

timer_active = False
timer_duration = 1.0
timer_countdown = timer_duration

score = 0
score_per_second = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Clicker")

background_image = pygame.image.load("background.png")
background_rect = background_image.get_rect()

cookie_images = {
    'normal': pygame.image.load("cookie.png"),
    'clicked': pygame.image.load("cookie1.png"),
}
cookie_rect = cookie_images['normal'].get_rect()
cookie_rect.center = (WIDTH // 2, HEIGHT // 2)

button_rect = pygame.Rect(10, HEIGHT // 2 - 30, 200, 60)
second_button_rect = pygame.Rect(10, HEIGHT // 2 + 40, 200, 60)
third_button_rect = pygame.Rect(10, HEIGHT // 2 + 110, 200, 60)
fourth_button_rect = pygame.Rect(10, HEIGHT // 2 + 180, 200, 60)
fifth_button_rect = pygame.Rect(10, HEIGHT // 2 + 250, 200, 60)

button_price = 10
second_button_price = 100
third_button_price = 1000
fourth_button_price = 10000
fifth_button_price = 100000

shrink_duration = 0.5
shrink_timer = 0

clock = pygame.time.Clock()
running = True
cookie_clicked = False

timer_active = False
timer_duration = 1.0
timer_countdown = timer_duration

score_per_second = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = event.pos
            if cookie_rect.collidepoint(click_x, click_y):
                cookie_clicked = True
                score += 1
                shrink_timer = shrink_duration
            elif button_rect.collidepoint(click_x, click_y) and score >= button_price:
                score -= button_price
                button_price += int(button_price * 0.2)
                timer_active = True
                score_per_second += 0.1
            elif second_button_rect.collidepoint(click_x, click_y) and score >= second_button_price:
                score -= second_button_price
                second_button_price += int(second_button_price * 0.2)
                timer_active = True
                score_per_second += 1
            elif third_button_rect.collidepoint(click_x, click_y) and score >= third_button_price:
                score -= third_button_price
                third_button_price += int(third_button_price * 0.2)
                timer_active = True
                score_per_second += 10
            elif fourth_button_rect.collidepoint(click_x, click_y) and score >= fourth_button_price:
                score -= fourth_button_price
                fourth_button_price += int(fourth_button_price * 0.2)
                timer_active = True
                score_per_second += 100
            elif fifth_button_rect.collidepoint(click_x, click_y) and score >= fifth_button_price:
                score -= fifth_button_price
                fifth_button_price += int(fifth_button_price * 0.2)
                timer_active = True
                score_per_second += 1000
        elif event.type == pygame.MOUSEBUTTONUP:
            cookie_clicked = False

    screen.fill(WHITE)
    screen.blit(background_image, background_rect)

    if shrink_timer > 0:
        cookie_rect.width -= 5
        cookie_rect.height -= 5
        shrink_timer -= 1 / FPS
    else:
        cookie_rect.width = cookie_images['normal'].get_width()
        cookie_rect.height = cookie_images['normal'].get_height()

    if timer_active:
        timer_countdown -= 1 / FPS
        if timer_countdown <= 0:
            score += score_per_second
            timer_countdown = timer_duration

    if cookie_clicked:
        screen.blit(cookie_images['clicked'], cookie_rect)
    else:
        screen.blit(cookie_images['normal'], cookie_rect)

    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {int(score)}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    score_per_second_text = font.render(f"Score per second: {round(score_per_second, 1)}", True, (255, 255, 255))
    screen.blit(score_per_second_text, (10, 50))

    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    pygame.draw.rect(screen, GREEN, button_rect, 3)
    button_text = font.render(f"Clicker\nPrice: {button_price}", True, BUTTON_TEXT_COLOR)
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

    pygame.draw.rect(screen, BUTTON_COLOR, second_button_rect)
    pygame.draw.rect(screen, GREEN, second_button_rect, 3)
    second_button_text = font.render(f"Farm\nPrice: {second_button_price}", True, BUTTON_TEXT_COLOR)
    second_text_rect = second_button_text.get_rect(center=second_button_rect.center)
    screen.blit(second_button_text, second_text_rect)

    pygame.draw.rect(screen, BUTTON_COLOR, third_button_rect)
    pygame.draw.rect(screen, GREEN, third_button_rect, 3)
    third_button_text = font.render(f"Mine\nPrice: {third_button_price}", True, BUTTON_TEXT_COLOR)
    third_text_rect = third_button_text.get_rect(center=third_button_rect.center)
    screen.blit(third_button_text, third_text_rect)

    pygame.draw.rect(screen, BUTTON_COLOR, fourth_button_rect)
    pygame.draw.rect(screen, GREEN, fourth_button_rect, 3)
    fourth_button_text = font.render(f"Factory\nPrice: {fourth_button_price}", True, BUTTON_TEXT_COLOR)
    fourth_text_rect = fourth_button_text.get_rect(center=fourth_button_rect.center)
    screen.blit(fourth_button_text, fourth_text_rect)

    pygame.draw.rect(screen, BUTTON_COLOR, fifth_button_rect)
    pygame.draw.rect(screen, GREEN, fifth_button_rect, 3)
    fifth_button_text = font.render(f"Bank\nPrice: {fifth_button_price}", True, BUTTON_TEXT_COLOR)
    fifth_text_rect = fifth_button_text.get_rect(center=fifth_button_rect.center)
    screen.blit(fifth_button_text, fifth_text_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
