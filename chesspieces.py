import pygame

# Every piece in chess extends this class
class piece:
    pos = (0, 0)
    board = None
    team = -1
    spritesheet = (pygame.image.load("chesspieces.png"), 70) # 70 is the size of squares
    spriteIndex = (0, 0)
    canRender = True
    hadLastMove = False
    hasMoved = False
    validMoves = []
    threat = []
    semiThreat = []
    char = ["?"]

    # First init
    def __init__(self, board, pos, team):
        self.pos = pos
        self.team = team
        self.board = board
        self.hasMoved = False
        self.threat = []
        self.validMoves = []
        self.semiThreat = []
        self.hadLastMove = False
        self.canRender = True

    def render(self, surface):
        if(self.canRender):
            s = self.spritesheet
            surface.blit(s[0], (self.pos[0] * s[1], self.pos[1] * s[1]), ((self.spriteIndex[self.team]%6) * s[1], math.floor(self.spriteIndex[self.team]/6) * s[1], s[1], s[1]))

    def moveTo(self, pos):
        if(self.canMoveTo(pos)):
            self.hasMoved = True
            p2 = self.board.getPieceAt(pos)
            self.board.setPieceAt(pos, self)
            self.board.setPieceAt(self.pos, None)
            self.pos = pos
            if(p2):
                p2.kill()
                return True, True
            return True, False
        return False, False

    def canMoveTo(self, pos):
        return pos in self.validMoves

    def kill(self):
        pass

    def update(self):
        self.validMoves = []
        for i in self.threat:
            s = self.board.getPieceAt(i)
            if((not s) or (s and s.team != self.team)):
                self.validMoves.append(i)

    def afterUpdate(self):
        pass
    def __str__(self):
        return self.char[self.team%2]
