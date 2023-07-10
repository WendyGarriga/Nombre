import pygame
import time

# Inicialización de pygame
pygame.init()

# Definición de los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Dimensiones de la ventana del juego
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Velocidad de actualización de la pantalla
fps = 15
clock = pygame.time.Clock()

# Tamaño de cada segmento de la serpiente y margen entre ellos
segment_size = 20
segment_margin = 2

# Velocidad inicial de la serpiente
x_change = segment_size + segment_margin
y_change = 0

# Inicialización de la serpiente
snake_segments = []
snake_length = 1

# Función para dibujar la serpiente en la pantalla
def draw_snake(snake_segments):
    for segment in snake_segments:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], segment_size, segment_size))

# Bucle principal del juego
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -(segment_size + segment_margin)
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = segment_size + segment_margin
                y_change = 0
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -(segment_size + segment_margin)
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = segment_size + segment_margin

    # Actualizar posición de la serpiente
# Actualizar posición de la serpiente
    if snake_segments:
        snake_head = []
        snake_head.append(snake_segments[0][1] + x_change)
        snake_head.append(snake_segments[0][1] + y_change)
        snake_segments.insert(0, snake_head)


    # Controlar la longitud de la serpiente
    if len(snake_segments) > snake_length:
        snake_segments.pop()

    # Dibujar el fondo y la serpiente
    screen.fill(BLACK)
    draw_snake(snake_segments)

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(fps)

# Cerrar el juego
pygame.quit()
