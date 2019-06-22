from classReview import ClassReview
from importReviews import ImportReviews
from statistics import mean, median
from collections import Counter


class ClassStats:
    def __init__(self, file, courseName):
        self.courseName = courseName
        self.reviewListAll = ImportReviews(file).list
        self.courseReviews = self.courseReviewList()
        self.timeMinValues = self.getTime("min")  # TODO: TEST
        self.timeMaxValues = self.getTime("max")  # TODO: TEST
        self.timeMinMean = mean(self.timeMinValues)  # TODO: TEST
        self.timeMinMedian = median(self.timeMinValues)  # TODO: TEST
        self.timeMaxMean = mean(self.timeMaxValues)  # TODO: TEST
        self.timeMaxMedian = median(self.timeMaxValues)  # TODO: TEST
        # self.timeTotalMean = #TODO: FINISH/IMPLEMENT
        # self.timeMostCommon = #TODO: FINISH/IMPLEMENT
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

    #TODO: TEST
    def getTime(self, quantityDescriptor):
        numList = []
        for review in self.courseReviews:
            if quantityDescriptor == "min":
                numList.append(int(review.timeMin))
            elif quantityDescriptor == "max":
                numList.append(int(review.timeMax))
        return numList


# SET DATA DIRECTORY
DIR = './data'
FILE = '/Course Reviews (Responses) - Form Responses 1.csv'
file = '{}{}'.format(DIR, FILE)

# courseName = "CS 271 - Computer Architecture & Assembly Language"

# CS271 = ClassStats(file, courseName)

# print(CS271.difficultyScores)
# print(CS271.difficultyMean)
# print(CS271.difficultyMedian)
