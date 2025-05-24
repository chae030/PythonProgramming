import pygame
import math

WindowSize = WindowWidth, WindowHeight = (400, 600)
Blue = (0, 0, 255)
Green = (0, 255, 0)
BorderWidth = 2
LargeSpace = True

def gray(val, min, max):
    val = max if val > max else min if val < min else val
    g = math.floor((val - min) / (max - min) * 255)
    return (g, g, g)

def extraInputPos(idx):
    Rows = [20, 3, 8]
    col = idx
    for row in range(len(Rows)):
        if col - Rows[row] < 0:
            return row, col
        col -= Rows[row]
    return len(Rows), col

class Display:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.window = pygame.display.set_mode(WindowSize)

    def update(self, inputs, outputs):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise Exception("Display window closed by user.")

        self.window.fill(Green)
        y = self.drawInputs(inputs)
        #y = self.drawState(state, y)  # ← 이 줄을 다시 추가
        self.drawOutputs(outputs, y)
        pygame.display.flip()

    def drawInputs(self, inputs):
        NumTiles = self.screen_width * self.screen_height
        TileSize = 15
        self.window.fill(Blue, (5-BorderWidth, 5-BorderWidth,
                                self.screen_width * TileSize + BorderWidth*2,
                                self.screen_height * TileSize + BorderWidth*2))
        for tileX in range(self.screen_width):
            for tileY in range(self.screen_height):
                self.window.fill(
                    gray(inputs[tileY * self.screen_width + tileX], -2, 2),
                    (5 + tileX * TileSize, 5 + tileY * TileSize, TileSize, TileSize)
                )

        y = self.screen_height * TileSize + 10
        maxRow = maxCol = 0
        for i in range(NumTiles, len(inputs)):
            row, col = extraInputPos(i - NumTiles)
            maxRow = max(row, maxRow)
            maxCol = max(col, maxCol)

        self.window.fill(Blue, (5-BorderWidth, y-BorderWidth,
                                (maxCol+1)*TileSize + BorderWidth*2,
                                (maxRow+1)*TileSize + BorderWidth*2))
        for i in range(NumTiles, len(inputs)):
            row, col = extraInputPos(i - NumTiles)
            self.window.fill(
                gray(inputs[i], 0, 1),
                (5 + col*TileSize, y + row*TileSize, TileSize, TileSize)
            )

        y += (maxRow + 1) * TileSize
        y += 30 if LargeSpace else 10
        return y

    def drawOutputs(self, outputs, y):
        positions = [
            (6, 1), (5, 2), (5, 0), (4, 1),
            (1, 0), (1, 2), (0, 1), (2, 1),
        ]
        OutputSize = 15
        self.window.fill(Blue, (5-BorderWidth, y-BorderWidth,
                                7 * OutputSize + BorderWidth * 2,
                                3 * OutputSize + BorderWidth * 2))
        for i in range(len(outputs)):
            px, py = positions[i]
            px *= OutputSize
            py *= OutputSize
            self.window.fill(
                gray(outputs[i], 0, 1),
                (5 + px, y + py, OutputSize, OutputSize)
            )

    def close(self):
        pygame.display.quit()
