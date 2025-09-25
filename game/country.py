import pygame
#creating a class so we can create the countries easier
class country:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.hexes = []  # list of HexTile objects

        # Example stats
        self.population = 1000
        self.economy = 50
        self.power = 50
        self.stability = 50

    def add_hex(self, hex_tile):
        self.hexes.append(hex_tile)
        hex_tile.owner = self  # link tile to this country
        hex_tile.colour = self.colour  # colour the tile

    def remove_hex(self, hex_tile):
        if hex_tile in self.hexes:
            self.hexes.remove(hex_tile)
            hex_tile.owner = None
            hex_tile.colour = (150, 150, 150)  # neutral grey

    def __str__(self):
        return f"{self.name} (Pop: {self.population}, Econ: {self.economy}, Power: {self.power}, Stability: {self.stability})"
