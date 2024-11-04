class Robot:
    def __init__(self):
        self.ycord = 0
        self.xcord = 0
        self.direction = "North"
    
    def turnLeft(self):
        if self.direction == "North":
            self.direction = "West"
        elif self.direction == "West":
            self.direction = "South"
        elif self.direction == "South":
            self.direction = "East"
        else: 
            self.direction = "North"

    def forward(self, n):
        if self.direction == "North":
            self.ycord = self.ycord + n
        elif self.direction == "South":
            self.ycord = self.ycord - n
        elif self.direction == "West":
            self.xcord = self.xcord - n
        else: 
            self.xcord = self.xcord + n




r = Robot()
r.turnLeft()
r.forward(10)