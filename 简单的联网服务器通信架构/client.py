import pygame
import socket
import threading
import pickle

# 配置客户端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

# 初始化Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("联网小游戏")

clock = pygame.time.Clock()
player_pos = [400, 300]
positions = {}

def receive_positions():
    global positions
    while True:
        try:
            data = client.recv(1024)
            positions = pickle.loads(data)
        except Exception as e:
            print(f"[错误] 接收数据出错: {e}")
            client.close()
            break

threading.Thread(target=receive_positions).start()

def send_position():
    try:
        client.send(pickle.dumps(player_pos))
    except Exception as e:
        print(f"[错误] 发送数据出错: {e}")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5

    send_position()

    screen.fill((0, 0, 0))
    for pos in positions.values():
        pygame.draw.circle(screen, (0, 255, 0), pos, 10)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
client.close()
