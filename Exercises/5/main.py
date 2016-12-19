
print("Part 1")
print("")
print_me = 10
for i in range(9):
    string = ""
    for j in range(i+1):
        string += str(print_me) + " "
        print_me += 1
    print(string)

print("")
print("Part 2")
print("")
n = int(input("How large of a box? "))
border = 'o'*2*n
inner = 'o' + ' '*(2*n-2) + 'o'
print(border)
for i in range(n-2):
    print(inner)
print(border)
print("")

print("Part 3")
print("")
n = int(input("How large of a box? "))
available = [(2*i)+1 for i in range(n)]
#available.extend(available[::-1])
for i in range(n):
    string = ""
    indices = range(n)[i::]
    spaces = range(2*n)[:2*i:]
    for j in indices:
        string += str(available[j]) + ' '
    for j in spaces:
        string += '  '
    for j in indices[::-1]:
        string += str(available[j]) + ' '
    print(string)
        
for i in range(n)[::-1]:
    string = ""
    indices = range(n)[i::]
    spaces = range(2*n)[:2*i:]
    for j in indices:
        string += str(available[j]) + ' '
    for j in spaces:
        string += '  '
    for j in indices[::-1]:
        string += str(available[j]) + ' '
    print(string)
print("")

"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
WIDTH = 700
HEIGHT = 500
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    
    for x in range(WIDTH)[::16]:
        for y in range(HEIGHT)[::16]:
            pygame.draw.rect(screen, GREEN, [x, y, 8, 8], 0)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
