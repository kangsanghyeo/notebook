import pygame
import sys
import random

# 파이게임 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Combined Game Example")

# 색깔 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# 원 초기 설정
circle_radius = 100
circle_color = black
circle_center = (screen_width // 2, screen_height // 2)



# 동그라미 초기 설정
circle_radius_2 = 20
circle_color_2 = blue
circle_position = [circle_center[0], circle_center[1]]

# 타이머 설정
timer_font = pygame.font.Font(None, 36)
start_time = pygame.time.get_ticks()
time_limit = 3 * 60 * 1000  # 3분 (밀리초 단위)
timer_expired = False
size_update_interval = 0.05 * 1000  # 30초 (밀리초 단위)
last_size_update_time = start_time

# 게임 루프
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 원 크기 조절
    current_time = pygame.time.get_ticks()
    if not timer_expired:
        elapsed_time = current_time - start_time
        if elapsed_time >= time_limit:
            timer_expired = True
        else:
            if current_time - last_size_update_time >= size_update_interval:
                last_size_update_time = current_time
                circle_radius = max(0, circle_radius - 0.5)  # 5씩 줄어듦


    # 화면 업데이트
    screen.fill(white)
    pygame.draw.circle(screen, circle_color, circle_center, circle_radius)
   

    # 타이머 표시
    if not timer_expired:
        remaining_time = max(0, (time_limit - elapsed_time) // 1000)
        timer_text = timer_font.render(f"Time: {remaining_time // 60:02}:{remaining_time % 60:02}", True, black)
        timer_rect = timer_text.get_rect(center=(screen_width // 2, 50))
        screen.blit(timer_text, timer_rect)

    pygame.display.flip()

    # 초당 프레임 설정
    clock.tick(60)

# 파이게임 종료
pygame.quit()
sys.exit()
