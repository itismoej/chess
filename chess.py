import pygame

pygame.init()

# Set colors constant
WHITE, BLACK = (237, 215, 192), (185, 82, 44)

# Set display
gameDisplay = pygame.display.set_mode((560, 560))

# Window caption
pygame.display.set_caption("ChessBoard")

# Size of squares
size = 70

# board length, must be 8
boardLength = 8
gameDisplay.fill(WHITE)

# Draw background sqaures (The Chessboard)
counter = 0
for horizontal_counter in range(0, boardLength):
    for vertical_counter in range(0, boardLength):
        # check if current loop value is even
        if counter % 2 == 0:
            pygame.draw.rect(gameDisplay, WHITE, [size * vertical_counter, size * horizontal_counter, size, size])
        else:
            pygame.draw.rect(gameDisplay, BLACK, [size * vertical_counter, size * horizontal_counter, size, size])
        counter += 1

    # since theres 8 number of squares go next line and change color
    counter -= 1

# Add a nice boarder
pygame.draw.rect(gameDisplay, BLACK, [0, 0, boardLength * size, boardLength * size], 1)

pygame.display.update()

img = pygame.image.load("img/chesspieces.png")
width, height = img.get_width() / 6, img.get_height() / 2

# White Pieces
# Rook WhiteTeam -Black
gameDisplay.blit(img,
                 (0 * width, 7 * height),
                 pygame.Rect((4 * width, 0 * height), (width, height)))
# Rook WhiteTeam -White
gameDisplay.blit(img,
                 (7 * width, 7 * height),
                 pygame.Rect((4 * width, 0 * height), (width, height)))

# Knight WhiteTeam -White
gameDisplay.blit(img,
                 (1 * width, 7 * height),
                 pygame.Rect((3 * width, 0 * height), (width, height)))
# Knight WhiteTeam -Black
gameDisplay.blit(img,
                 (6 * width, 7 * height),
                 pygame.Rect((3 * width, 0 * height), (width, height)))

# Bishop WhiteTeam -Black
gameDisplay.blit(img,
                 (2 * width, 7 * height),
                 pygame.Rect((2 * width, 0 * height), (width, height)))
# Bishop WhiteTeam -White
gameDisplay.blit(img,
                 (5 * width, 7 * height),
                 pygame.Rect((2 * width, 0 * height), (width, height)))

# King WhiteTeam
gameDisplay.blit(img,
                 (4 * width, 7 * height),
                 pygame.Rect((0 * width, 0 * height), (width, height)))

# Queen WhiteTeam
gameDisplay.blit(img,
                 (3 * width, 7 * height),
                 pygame.Rect((1 * width, 0 * height), (width, height)))

# Pawns of WhiteTeam
for i in range(8):
    gameDisplay.blit(img,
                     (i * width, 6 * height),
                     pygame.Rect((5 * width, 0 * height), (width, height)))


# Black Pieces
# Rook BlackTeam -Black
gameDisplay.blit(img,
                 (7 * width, 0 * height),
                 pygame.Rect((4 * width, height), (width, height)))
# Rook BlackTeam -White
gameDisplay.blit(img,
                 (0 * width, 0 * height),
                 pygame.Rect((4 * width, height), (width, height)))

# Knight BlackTeam -Black
gameDisplay.blit(img,
                 (1 * width, 0 * height),
                 pygame.Rect((3 * width, height), (width, height)))
# Knight BlackTeam -White
gameDisplay.blit(img,
                 (6 * width, 0 * height),
                 pygame.Rect((3 * width, height), (width, height)))

# Bishop BlackTeam -White
gameDisplay.blit(img,
                 (2 * width, 0 * height),
                 pygame.Rect((2 * width, height), (width, height)))
# Bishop BlackTeam -Black
gameDisplay.blit(img,
                 (5 * width, 0 * height),
                 pygame.Rect((2 * width, height), (width, height)))

# King BlackTeam
gameDisplay.blit(img,
                 (4 * width, 0 * height),
                 pygame.Rect((0 * width, height), (width, height)))

# Queen BlackTeam
gameDisplay.blit(img,
                 (3 * width, 0 * height),
                 pygame.Rect((1 * width, height), (width, height)))

# Pawns of BlackTeam
for i in range(8):
    gameDisplay.blit(img,
                     (i * width, 1 * height),
                     pygame.Rect((5 * width, height), (width, height)))

# Appearing images after adding them
pygame.display.update()

# Running the application till it's exited
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
