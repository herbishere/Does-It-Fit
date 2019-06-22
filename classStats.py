'''
    File name: classStats.py
    Author: Herbert Diaz
    Date created: 6/21/2019
    Last modified: 6/22/2019
    Python Version: 3.7.3

    Overview:
        This class object is first initalized with the location of the course review data
        and the specific name of the course. The class than calculates various statistical
        aspects of the course based on the spreadsheet.
        Datamembers includes:
            > courseName = A string of the name of the course.
            > reviewListAll = A list of all the course reviews
            > courseReviews = The reviews of a specific course
            > timeMinValues = A list of the minimum estimated times for a course
            > timeMaxValues = A list of the maximum estimated times for a course
            > timeMinMean = The mean of the minimum esimated times
            > timeMaxMean = The mean of the maximum estimated times
            > timeMinMedian = The median of the minimum estimated times
            > timeMaxMedian = The median of the maximum estimated times
            > timeTotalMean = The mean of the maximum and minimum means
            > timeMostCommon = The most common time string
            > difficultyScores = A list of the difficulty scores of the course
            > difficultyMean = The mean of the difficulty scores
            > difficultyMedian = The median of the difficulty scores
'''

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
        self.timeMostCommon = self.getMostCommonTimeString()
        self.difficultyScores = self.getScores()
        self.difficultyMean = mean(self.difficultyScores)
        self.difficultyMedian = median(self.difficultyScores)

    # courseReviewList(self)
    # Purpose: Get all the courseReviews for the specific course
    # Entry: none
    # Exit: A list of all the course's reviews (classReview objects)
    def courseReviewList(self):
        courseReviews = []
        for review in self.reviewListAll:
            if review.courseName == self.courseName:
                courseReviews.append(review)
        return courseReviews

    # getScores(self)
    # Purpose: Get all the difficulty scores of a specific course
    # Entry: none
    # Exit: A list of all the course's difficulty scores
    def getScores(self):
        difficultyScoreList = []
        for review in self.courseReviews:
            difficultyScoreList.append(int(review.difficulty))
        return difficultyScoreList

    # getTime(self, quantityDescriptor)
    # Purpose: Get a list of all the estimated time devoted to a course
    # Entry: "min" = examine minimum times, "max" = examine maximum times
    # Exit: A list of all the minimum or maximum times for a course
    def getTime(self, quantityDescriptor):
        numList = []
        for review in self.courseReviews:
            if quantityDescriptor == "min":
                numList.append(int(review.timeMin))
            elif quantityDescriptor == "max":
                numList.append(int(review.timeMax))
        return numList

    # getTimeStrings(self)
    # Purpose: Get a list of all the strings estimating the time devoted to a course
    # Entry: none
    # Exit: A list of all the time strings
    def getTimeStrings(self):
        timeCommittments = []
        for review in self.courseReviews:
            timeCommittments.append(review.time)
        return timeCommittments

    # getMostCommonTimeString(self)
    # Purpose: Get the most common time string
    # Entry: none
    # Exit: A string that holds the most common estimated time
    def getMostCommonTimeString(self):
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

# print(CS271.getMostCommonTimeString())
