import pygame
import random

pygame.init()

# 1. 화면 설정
WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("바다를 지켜라! 오션 클리너 (Final Ver.)")

clock = pygame.time.Clock()

# 2. 이미지 로드
player_img = pygame.image.load("diver.png") 
player_img = pygame.transform.scale(player_img, (90, 60)) 

enemy_img = pygame.image.load("shark.png")
enemy_img = pygame.transform.scale(enemy_img, (130, 80))
enemy_img = pygame.transform.flip(enemy_img, True, False) 

item_img = pygame.image.load("trash.png")
item_img = pygame.transform.scale(item_img, (55, 55))

heart_img = pygame.image.load("heart.png")
heart_img = pygame.transform.scale(heart_img, (40, 40)) 

# 3. 함수 및 클래스

#플레이어의 남은 목숨 개수 만큼 하트 이미지 그리기 
def draw_hearts(surf, lives):
    for i in range(lives):
        x = WIDTH - 50 - (i * 45)
        y = 20
        surf.blit(heart_img, (x, y))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT // 2)
        self.speed = 6
        
        self.is_invincible = False
        self.invincible_timer = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]: self.rect.y -= self.speed
        if keys[pygame.K_DOWN]: self.rect.y += self.speed
        
        self.rect.clamp_ip(screen.get_rect())

        # 플레이어가 상어랑 충돌했을 때
        # 목숨 1개 줄이고 잠깐 깜빡거리게 해서 무적 상태로 만듦
        if self.is_invincible:
            self.invincible_timer -= 1 
            if self.invincible_timer <= 0:
                self.is_invincible = False
                self.image.set_alpha(255) 
            else:
                if self.invincible_timer % 10 < 5:
                    self.image.set_alpha(100)
                else:
                    self.image.set_alpha(255)
    # 무적 상태 확인하기 
    def get_hit(self):
        if self.is_invincible:
            return False
        self.is_invincible = True
        self.invincible_timer = 90 
        return True

#바닷속처럼 보이게 물방울 만들기 
class Bubble:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = HEIGHT + random.randint(0, 100)
        self.speed = random.randint(1, 3)
        self.size = random.randint(3, 8)
    
    def move(self):
        self.y -= self.speed
        if self.y < 0: 
            self.y = HEIGHT + 10
            self.x = random.randint(0, WIDTH)
    
    def draw(self, surface):
        s = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)
        pygame.draw.circle(s, (255, 255, 255, 100), (self.size, self.size), self.size)
        surface.blit(s, (self.x, self.y))

# 4. 초기화
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

enemies = []      
trash_list = []   
bubbles = [Bubble() for _ in range(20)] 

spawn_timer = 0
SPAWN_INTERVAL = 50 

score = 0 
lives = 3         
running = True
game_over = False
game_won = False #이겼는지 졌는지 기억하는 변수 

hit_message_timer = 0
hit_font = pygame.font.SysFont(None, 60) # 조금 큰 폰트

#속도 증가 경고 메시지용 변수 
speed_message_timer = 0
warning_font = pygame.font.SysFont(None, 70)

def spawn_objects():
    spawn_y = random.randint(0, HEIGHT - 80)
    level_speed = score // 5 
    
    if random.random() < 0.4: 
        rect = pygame.Rect(WIDTH, spawn_y, 55, 55)
        speed = random.randint(4, 6) + level_speed
        trash_list.append({"rect": rect, "speed": speed})
    else: 
        rect = pygame.Rect(WIDTH, spawn_y, 130, 80)
        speed = random.randint(6, 9) + level_speed
        enemies.append({"rect": rect, "speed": speed})

# 5. 메인 루프
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #게임 오버 상태이고 엔터키를 눌렀다면 재시작
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_RETURN:
                game_over = False
                game_won = False
                score = 0
                lives = 3          
                enemies.clear()
                trash_list.clear()
                player.rect.center = (100, HEIGHT // 2)
                player.is_invincible = False
                player.image.set_alpha(255)
                hit_message_timer = 0 # 재시작 시 ouch 메시지도 안뜨게 초기화
                speed_message_timer = 0
    if not game_over:
        all_sprites.update()
        
        for b in bubbles:
            b.move()

        spawn_timer += 1
        #점수가 높을수록 생성 간격을 줄여서 더 빨리 나오게 함 
        # 원래는 50 프레임마다 쓰레기/상어 하나를 생성했음 
        # 점수 5점마다 1씩 증가시켜 50에서 뺌으로써 간격을 줄임
        # 간격이 음수가 되는 걸 막기 위해 최소 20으로 제한
        current_interval = max(20, SPAWN_INTERVAL - (score // 5))
        
        if spawn_timer >= current_interval:
            spawn_timer = 0
            spawn_objects()

        # --- 상어 이동 ---
        new_enemies = []
        for enemy in enemies:
            rect = enemy["rect"]
            rect.x -= enemy["speed"]

            if player.rect.colliderect(rect):
                if player.get_hit(): 
                    lives -= 1
                    hit_message_timer = 60 #ouch 메시지 타이머 1초 설정 
                    print(f"충돌! 남은 목숨: {lives}")
                    if lives <= 0:
                        game_over = True
                        game_won = False #이기고 있는 상태 
            
            if rect.right > 0:
                new_enemies.append(enemy)
        enemies = new_enemies

        # --- 쓰레기 이동 ---
        new_trash = []
        for trash in trash_list:
            rect = trash["rect"]
            rect.x -= trash["speed"]

            if player.rect.colliderect(rect):
                score += 1 
                if score % 5 == 0 and score != 30:
                    speed_message_timer = 120 #2초 동안 띄우기
                if score >= 30:
                    game_over = True
                    game_won = True
                continue  # 부딪힌 쓰레기는 다시 안 넣음(먹음)

            if rect.right > 0:
                new_trash.append(trash)
        trash_list = new_trash

    # --- 화면 그리기 ---
    screen.fill((50, 150, 200)) 
    
    for b in bubbles:
        b.draw(screen)

    all_sprites.draw(screen)

    for enemy in enemies:
        screen.blit(enemy_img, enemy["rect"])

    for trash in trash_list:
        screen.blit(item_img, trash["rect"])

    # UI 표시
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Cleaned: {score} / 30", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))
    
    draw_hearts(screen, lives)

    # 피격 메시지 그리기 (게임 오버가 아닐 때만)
    if not game_over and hit_message_timer > 0:
        hit_text = hit_font.render("OUCH! -1 LIFE", True, (255, 50, 50))
        # 화면 정중앙에 배치
        text_rect = hit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(hit_text, text_rect)
        hit_message_timer -= 1 # 타이머 감소
    if not game_over and speed_message_timer > 0:
        warn_text = warning_font.render("WARNING : SPEED UP !", True, (255, 140, 0))
        warn_rect = warn_text.get_rect(center=(WIDTH//2, HEIGHT//2-50))
        screen.blit(warn_text, warn_rect)
        speed_message_timer -= 1
    # 게임 오버 화면
    if game_over:
        s = pygame.Surface((WIDTH, HEIGHT))
        s.set_alpha(128)
        s.fill((0,0,0))
        screen.blit(s, (0,0))

        over_font = pygame.font.SysFont(None, 80)
        if game_won:
            over_text = over_font.render("MISSION CLEAR!", True, (100,255,100))
        else:
            over_text = over_font.render("GAME OVER", True, (255, 50, 50))
        
        info_font = pygame.font.SysFont(None, 40)
        score_result = info_font.render(f"Total Trash Collected: {score}", True, (255, 255, 255))
        restart_text = info_font.render("Press Enter to Try Again", True, (255, 255, 0))
        
        screen.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//2 - 60))
        screen.blit(score_result, (WIDTH//2 - score_result.get_width()//2, HEIGHT//2 + 10))
        screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()