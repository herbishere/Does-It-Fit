from classStats import ClassStats
from statistics import mean
from classCourse import Course


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
            course = ClassStats(self.file, course)
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
        hours = 0
        for course in self.classes:
            if minMax == "min":
                hours += course.timeMinMean
            elif minMax == "max":
                hours += course.timeMaxMean
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
        return mean([self.maximumHours, self.maximumHours])

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
