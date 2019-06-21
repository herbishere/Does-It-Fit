class ClassReview:
    def __init__(self, courseName, time, difficulty):
        self.courseName = courseName
        self.time = time
        self.timeMin = self.getTimeMin()
        self.timeMax = self.getTimeMax()
        self.difficulty = difficulty

    def getTimeMin(self):
        timeState = self._convertTimeString()
        if timeState == "LO":
            return 0
        elif timeState == "MED":
            return 6
        elif timeState == "HI":
            return 13
        elif timeState == "VHI":
            return 19
        else:
            return -999

    def getTimeMax(self):
        timeState = self._convertTimeString()
        if timeState == "LO":
            return 5
        elif timeState == "MED":
            return 12
        elif timeState == "HI":
            return 18
        elif timeState == "VHI":
            return 30

    def _convertTimeString(self):
        LO = "0-5 hours"
        MED = "6-12 hours"
        HI = "13-18 hours"
        VHI = "18+ hours"
        timeString = self.time
        if timeString == LO:
            return "LO"
        elif timeString == MED:
            return "MED"
        elif timeString == HI:
            return "HI"
        elif timeString == VHI:
            return "VHI"
        else:
            return "ERROR: INVALID STRING"
