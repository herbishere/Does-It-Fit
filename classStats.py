from classReview import ClassReview
from importReviews import ImportReviews
from statistics import mean, median
from collections import Counter


class ClassStats:
    def __init__(self, file, courseName):
        self.courseName = courseName
        self.reviewListAll = ImportReviews(file).list
        self.courseReviews = self.courseReviewList()
        # self.hoursMinMean =
        # self.hoursMinMedian =
        # self.hoursMaxMean =
        # self.hoursMaxMedian =
        # self.hoursTotalMean =
        # self.hoursMostCommon =
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


# SET DATA DIRECTORY
DIR = './data'
FILE = '/Course Reviews (Responses) - Form Responses 1.csv'
file = '{}{}'.format(DIR, FILE)

courseName = "CS 271 - Computer Architecture & Assembly Language"

CS271 = ClassStats(file, courseName)

print(CS271.difficultyScores)
print(CS271.difficultyMean)
print(CS271.difficultyMedian)
