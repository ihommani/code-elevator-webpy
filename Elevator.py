from collections import deque

class elevator:
    def __init__(self, lastFloor=5):
        self._current_floor = 0
        self._next_floor = 0
        self._isClosed = True
        self._passengersNumber = 0
        self._upperLimit = lastFloor
        self._nextCommandQueue = deque()
        
    def isGroundFloor(self):
        return

    def call(self, floor):
        self._computeCall(int(floor))

    def go(self, floor):
        self._computeCall(int(floor))

    def getNextMove(self):
        if len(self._nextCommandQueue):
            return self._nextCommandQueue.popleft()
        else:
            return "NOTHING"
    
    def _computeCall(self, floorToGo):
        if not self.isWithinLimits(floorToGo):
            self._nextCommandQueue.append("NOTHING")  
        elif floorToGo is self._current_floor:
            self.openDoor()
        else:
            while not(self._current_floor is floorToGo): 
                if not self._isClosed:
                    self.closeDoor()
                elif self._current_floor < floorToGo:
                    self.goUp()
                else:
                    self.goDown()
            self.openDoor()

    def userEntrance(self):
        self._passengersNumber += 1
        return self._passengersNumber

    def userExit(self):
        if self._passengersNumber > 0:
            self._passengersNumber -= 1
            return self._passengersNumber
        else:
            return self._passengersNumber

    def isClosed(self):
        return self._isClosed

    def getCurrentFloor(self):
        return self._current_floor

    def isOpen(self):
        return not self.isClosed()

    def goUp(self):
        if self.isWithinLimits(self._current_floor):
            self._nextCommandQueue.append("UP")
            self._current_floor += 1
    
    def goDown(self):
        if self.isWithinLimits(self._current_floor):
            self._nextCommandQueue.append("DOWN")
            self._current_floor -= 1

    def isWithinLimits(self, floor):
        return floor >= 0 and floor <= self._upperLimit

    def closeDoor(self):
        if not self._isClosed:
            self._nextCommandQueue.append("CLOSE")
        self._isClosed = True
        return

    def openDoor(self):
        if self._isClosed:
            self._nextCommandQueue.append("OPEN")
        self._isClosed = False
        return

    def reset(self):
        self.__init__(5)
