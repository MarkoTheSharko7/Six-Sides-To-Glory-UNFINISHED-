import pygame, math

class HexTile:
    def __init__(self, q, r, size, terrain="land"):
        self.q = q  # column index
        self.r = r  # row index
        self.size = size
        self.terrain = terrain

        # Default terrain colours
        if terrain == "land":
            self.colour = (34, 139, 34)  # green
            self.claimable = True
        elif terrain == "water":
            self.colour = (30, 144, 255)  # blue
            self.claimable = False
        elif terrain == "border":
            self.colour = (80, 80, 80)  # dark grey
            self.claimable = False
        else:
            self.colour = (200, 200, 200)  # fallback neutral
            self.claimable = True

        self.owner = None       # country that owns this tile (None = neutral)
        self.selected = False   # for highlighting

        # Calculate pixel position (using odd-q vertical layout)
        self.x = size * (3/2 * q)
        self.y = size * (math.sqrt(3) * (r + 0.5 * (q % 2)))


    def get_corners(self):
        corners = []
        for i in range(6):
            angle = math.pi / 3 * i
            cx = self.x + self.size * math.cos(angle)
            cy = self.y + self.size * math.sin(angle)
            corners.append((cx, cy))
        return corners

    def draw(self, screen):
        base_colour = self.colour  # terrain base (e.g. land = green, water = blue)

        if self.owner:  # Apply translucent overlay for owner colour
            shape = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            pygame.draw.polygon(shape, (*self.owner.colour, 120), self.get_corners())  
            screen.blit(shape, (0,0))

# Draw terrain and border on top
        pygame.draw.polygon(screen, base_colour, self.get_corners())
        pygame.draw.polygon(screen, (0, 0, 0), self.get_corners(), 2)

        if self.selected:
            pygame.draw.polygon(screen, (255, 255, 0), self.get_corners(), 3)


    def was_clicked(self, pos):
        x, y = pos
        corners = self.get_corners()
        inside = False

        j = len(corners) - 1
        for i in range(len(corners)):
            xi, yi = corners[i]
            xj, yj = corners[j]
            if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi + 1e-9) + xi):
                inside = not inside
            j = i

        return inside