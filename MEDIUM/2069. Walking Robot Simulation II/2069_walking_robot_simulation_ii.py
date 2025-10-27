class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        # I initialize the robot's position at (0, 0) and set its initial direction to "East".
        # I also precompute the sequence of moves that the robot will make along the perimeter
        # of the rectangle to optimize the step function.
        # The robot's movement is constrained to the perimeter of the rectangle, so I create a list 
        self.width = width
        self.height = height
        self.dx_dy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.dir_names = ["East", "North", "West", "South"]
        self.dir_idx = 0 
        self.x = 0
        self.y = 0

        self.perimeter_moves = []
        for i in range(self.width - 1):
            self.perimeter_moves.append((1, 0))
        for i in range(self.height - 1):
            self.perimeter_moves.append((0, 1))
        for i in range(self.width - 1):
            self.perimeter_moves.append((-1, 0))
        for i in range(self.height - 1):
            self.perimeter_moves.append((0, -1))
        self.perimeter_len = len(self.perimeter_moves)
        self.perimeter_pos = 0 

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Here, I move the robot along the perimeter of the rectangle
        # according to the number of steps specified by 'num'.
        # I update the robot's position and direction based on its current location
        # and the precomputed perimeter moves.

        if self.width == 1 or self.height == 1:
            return

        steps = num % self.perimeter_len
        for _ in range(steps):
            dx, dy = self.perimeter_moves[self.perimeter_pos]
            self.x += dx
            self.y += dy
            self.perimeter_pos = (self.perimeter_pos + 1) % self.perimeter_len
        
        if self.perimeter_len > 0:
            if self.perimeter_pos == 0:
                self.dir_idx = 3 
            elif self.perimeter_pos <= self.width - 1:
                self.dir_idx = 0
            elif self.perimeter_pos <= self.width - 1 + self.height - 1:
                self.dir_idx = 1
            elif self.perimeter_pos <= 2 * (self.width - 1) + self.height - 1:
                self.dir_idx = 2
            else:
                self.dir_idx = 3

    def getPos(self):
        """
        :rtype: List[int]
        """
        # I return the current position of the robot as a list [x, y].
        return [self.x, self.y]

    def getDir(self):
        """
        :rtype: str
        """
        # I return the current direction of the robot as a string.
        return self.dir_names[self.dir_idx]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()