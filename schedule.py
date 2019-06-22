from classStats import ClassStats
from statistics import mean


class Schedule:
    def __init__(self):
        self.classes = []
        self.minimumHours = 0
        self.maximumHours = 0
        self.meanHours = 0
        self.difficulty = 0
        self.hoursAvailable = 0
        self.scheduleOK = False

    def _calcMinimumHours(self):
        hours = 0
        for course in self.classes:
            hours += course.timeMinMean
        return hours

    def _setMinimumHours(self):
        self.minimumHours = self._calcMinimumHours()

    def setHoursAvailable(self, hours):
        self.hoursAvailable = hours
