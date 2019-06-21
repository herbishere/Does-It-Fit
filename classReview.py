'''
    File name: classReview.py
    Author: Herbert Diaz
    Date created: 6/21/2019
    Last modified: 6/21/2019
    Python Version: 3.7.3

    Overview:
        This class object contains all the relevant variables for a single class review.
        This includes:
            > courseName = A string of the name of the course.
            > time = A string detailing the time required by the course.
            > timeMin = An int detailing the minimum time required by the course.
            > timeMax = An int detailing the maximum time required by the course.
            > difficulty = An int detailing the difficulty rating of the course (1 - 5)
'''


class ClassReview:
    def __init__(self, courseName, time, difficulty):
        self.courseName = courseName
        self.time = time
        self.timeMin = self.getTimeMin()
        self.timeMax = self.getTimeMax()
        self.difficulty = difficulty

    # getTimeMin(self)
    # Purpose: Get the minimum time by the course
    # Entry: none
    # Exit: the minimum number of hours required by the course
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

    # getTimeMax(self)
    # Purpose: Get the maxmum time by the course
    # Entry: none
    # Exit: the maximum number of hours required by the course
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
        else:
            return -999

    # _convertTimeString(self)
    # Purpose: Helper function to convert the time string into a smaller string
    # Entry: none
    # Exit: the time strings are converted into a smaller string
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
