from classStats import ClassStats
from statistics import mean
from classCourse import Course
import datetime


class Schedule:
    def __init__(self, file):
        self.file = file
        self.classes = []
        self.minimumHours = 0
        self.maximumHours = 0
        self.meanHours = 0
        self.difficulty = 0
        self.hoursAvailable = 0

    def _noDuplications(self, inputClass):
        for course in self.classes:
            if inputClass == course.courseName:
                return False
        return True

    def addClass(self, courseName):
        if self._noDuplications(courseName):
            course = ClassStats(self.file, courseName)
            self.classes.append(course)
            self.recalculateData()
            return True
        return False

    def removeClass(self, courseName):
        for course in self.classes:
            if courseName == course.courseName:
                self.classes.remove(course)
                self.recalculateData()
            return True
        return False

    def clearClasses(self):
        del self.classes[:]
        self.classes = []
        self.minimumHours = 0
        self.maximumHours = 0
        self.meanHours = 0
        self.difficulty = 0

    def _calcHours(self, minMax):
        SUMMERMULTIPLIER = 1.25
        hours = 0
        for course in self.classes:
            if minMax == "min":
                hours += course.timeMinMean
            elif minMax == "max":
                hours += course.timeMaxMean
        if self.isSummer == True:
            hours *= SUMMERMULTIPLIER
        return hours

    def _calcMinHours(self):
        return self._calcHours("min")

    def _setMinHours(self):
        self.minimumHours = self._calcMinHours()

    def _calcMaxHours(self):
        return self._calcHours("max")

    def _setMaxHours(self):
        self.maximumHours = self._calcMaxHours()

    def _calcMeanHours(self):
        return mean([self.minimumHours, self.maximumHours])

    def _setMeanHours(self):
        self.meanHours = self._calcMeanHours()

    def _calcMeanDifficulty(self):
        difficulties = []
        for course in self.classes:
            difficulties.append(course.difficultyMean)
        return mean(difficulties)

    def _setMeanDifficulty(self):
        self.difficulty = self._calcMeanDifficulty()

    def recalculateData(self):
        self._setMinHours()
        self._setMaxHours()
        self._setMeanHours()
        self._setMeanDifficulty()

    def setHoursAvailable(self, hours):
        self.hoursAvailable = hours

    def isScheduleOK(self):
        YES = "You WILL sleep. You should be able to handle this schedule!"
        MAYBE_YES = "Some weeks might be a rough, but it should be manageable."
        MAYBE_NO = "This WILL be rough. Consider changing your schedule."
        NO = "You WILL NOT sleep. Change your schedule."
        if self.hoursAvailable >= self.maximumHours:
            return YES
        elif self.hoursAvailable >= self.meanHours:
            return MAYBE_YES
        elif self.hoursAvailable >= self.minimumHours:
            return MAYBE_NO
        else:
            return NO
            
    def isSummer(self):
        curDate = datetime.datetime.now()
        minRange = datetime.datetime(day=1, month=4, year=1990)
        maxRange = datetime.datetime(day=30, month=7, year=1990)
        if (curDate.month >= minRange.month) and (curDate.month <= maxRange.month) :
            return True
        else:
            return False


# # TEST
# # SET DATA DIRECTORY
# DIR = './data'
# FILE = '/Course Reviews (Responses) - Form Responses 1.csv'
# file = '{}{}'.format(DIR, FILE)

# classes = Course()
# mySched = Schedule(file)
# mySched.addClass(classes.CS340)
# mySched.addClass(classes.CS325)
# mySched.setHoursAvailable(24)

# for course in mySched.classes:
#     print(course.courseName)
# print("minHours:", mySched.minimumHours)
# print("maxHours:", mySched.maximumHours)
# print("meanHours:", mySched.meanHours)
# print(mySched.isScheduleOK())
