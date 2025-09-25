import pygame
import math
import random
from game.country import country  # make sure this matches the folder structure
from game.HexTileMap import HexTile


pygame.init()
width, height = 1400, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("World domination simulator")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 24)

# Hex settings
hex_size = 42
grid_width = width // int(hex_size * 1.5) + 2
grid_height = height // int(hex_size * math.sqrt(3)) + 1


hexes = []
for q in range(int(grid_width)):
    for r in range(int(grid_height)):
        if q == 0 or r == 0 or q == grid_width-1 or r == grid_height-1:
            terrain = "border"
        else:
            terrain = "land" if (q + r) % 10 else "water"
        hexes.append(HexTile(q, r, hex_size, terrain))
        
c1 = country("juju land", (200, 0, 0))
c2 = country("fluffonia", (0, 0, 200))

# Pick a random claimable land tile for each
claimable_hexes = [h for h in hexes if h.claimable]

c1.add_hex(random.choice(claimable_hexes))
c2.add_hex(random.choice([h for h in claimable_hexes if h.owner is None]))

countries = [c1, c2]
        


# Track which country is selected
selected_country = None

running = True
while running:
    screen.fill((30, 30, 30))  # Clear the screen

# --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for h in hexes:
                if h.was_clicked(pos):
                    if h.selected:                        # if already selected → unselect
                        h.selected = False
                        print(f"Deselected hex at {h.q}, {h.r}")
                    else:                        # deselect all others first
                        for other in hexes:
                            other.selected = False                        # then select this one
                        h.selected = True
                        print(f"Selected hex at {h.q}, {h.r}, terrain: {h.terrain}")
                    break


    for h in hexes:
        h.draw(screen)

# Draw stats panel if a country is selected
#if selected_country:
#selected_country.show_stats(screen, font)

#this is refrehsing the screen at 60 fps
    pygame.display.flip()
    clock.tick(60)

pygame.quit()    