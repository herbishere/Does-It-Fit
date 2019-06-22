from classReview import ClassReview
from importReviews import ImportReviews
from statistics import mean, median
from collections import Counter


class ClassStats:
    def __init__(self, file, courseName):
        self.courseName = courseName
        self.reviewListAll = ImportReviews(file).list
        self.courseReviews = self.courseReviewList()
        self.timeMinValues = self.getTime("min")
        self.timeMaxValues = self.getTime("max")
        self.timeMinMean = mean(self.timeMinValues)
        self.timeMinMedian = median(self.timeMinValues)
        self.timeMaxMean = mean(self.timeMaxValues)
        self.timeMaxMedian = median(self.timeMaxValues)
        self.timeTotalMean = mean([self.timeMinMean, self.timeMaxMean])
        self.timeMostCommon = self.getMostCommonTimeStrings()
        self.difficultyScores = self.getScores()
        self.difficultyMean = mean(self.difficultyScores)
        self.difficultyMedian = median(self.difficultyScores)

    def courseReviewList(self):
        courseReviews = []
        for review in self.reviewListAll:
            if review.courseName == self.courseName:
                courseReviews.append(review)
        return courseReviews

    def getScores(self):
        difficultyScoreList = []
        for review in self.courseReviews:
            difficultyScoreList.append(int(review.difficulty))
        return difficultyScoreList

    def getTime(self, quantityDescriptor):
        numList = []
        for review in self.courseReviews:
            if quantityDescriptor == "min":
                numList.append(int(review.timeMin))
            elif quantityDescriptor == "max":
                numList.append(int(review.timeMax))
        return numList

    def getTimeStrings(self):
        timeCommittments = []
        for review in self.courseReviews:
            timeCommittments.append(review.time)
        return timeCommittments

    def getMostCommonTimeStrings(self):
        timeStrings = self.getTimeStrings()
        mostCommon = [word for word in Counter(timeStrings).most_common()]
        return mostCommon[0][0]

# # TEST
# # SET DATA DIRECTORY
# DIR = './data'
# FILE = '/Course Reviews (Responses) - Form Responses 1.csv'
# file = '{}{}'.format(DIR, FILE)

# courseName = "CS 271 - Computer Architecture & Assembly Language"

# CS271 = ClassStats(file, courseName)

# print(CS271.getMostCommonTimeStrings())
