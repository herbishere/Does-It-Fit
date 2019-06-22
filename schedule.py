from classStats import ClassStats
from statistics import mean
from classCourse import Course


class Schedule:
    def __init__(self):
        self.classes = []
        self.minimumHours = 0
        self.maximumHours = 0
        self.meanHours = 0
        self.difficulty = 0
        self.hoursAvailable = 0
        self.scheduleOK = False

    def _noDuplications(self, inputClass):
        for course in self.classes:
            if inputClass == course:
                return False
        return True

    def _calcMinimumHours(self):
        hours = 0
        for course in self.classes:
            hours += course.timeMinMean
        return hours

    def _setMinimumHours(self):
        self.minimumHours = self._calcMinimumHours()

    def setHoursAvailable(self, hours):
        self.hoursAvailable = hours
