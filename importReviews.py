'''
    File name: importReviews.py
    Author: Herbert Diaz
    Date created: 6/21/2019
    Last modified: 6/21/2019
    Python Version: 3.7.3

    Overview:
        This class takes the location of a csv file containing the course reviews and 
        puts the relevant values into a list of ClassReview objects.
        This includes:
            > file = A string of the location of the csv file
            > list = A unsorted list of ClassReview objects
'''

# IMPORT PACKAGES AND MODULES
import csv
from classReview import ClassReview


class ImportReviews:
    def __init__(self, file):
        self.file = file
        self.list = self.csvToArray()

    # _getIndices(self, headerList, matchString)
    # Purpose: Get the Indices of certain strings in a header and returning an array
    #   of the indices
    # Entry:    headerList = a list of column names
    #           matchString = the string of the column name to search for
    # Exit: An array of indices detailing the location of the matchString
    def _getIndices(self, headerList, matchString):
        indices = []
        index = 0
        for cell in headerList:
            if cell == matchString:
                indices.append(index)
            index += 1
        return indices

    # _getCourseNameIndices(self, headerList)
    # Purpose: Get the Indices of the course name columns and return an array
    #   of the course name indices
    # Entry:    headerList = a list of column names
    # Exit: An array of indices detailing the location of the course names
    def _getCourseNameIndices(self, headerList):
        COURSENAME_HEADER = "What Course Did You Take?"
        return self._getIndices(headerList, COURSENAME_HEADER)

    # _getHoursIndices(self, headerList)
    # Purpose: Get the Indices of the time columns and return an array
    #   of the time indices
    # Entry:    headerList = a list of column names
    # Exit: An array of indices detailing the location of the times
    def _getHoursIndices(self, headerList):
        HOURS_HEADER = "How much time did you spend on average (per week) for this class?"
        return self._getIndices(headerList, HOURS_HEADER)

    # _getDifficultyIndices(self, headerList)
    # Purpose: Get the Indices of the difficulty columns and return an array
    #   of the difficulty indices
    # Entry:    headerList = a list of column names
    # Exit: An array of indices detailing the location of the difficultys
    def _getDifficultyIndices(self, headerList):
        DIFFICULTY_HEADER = "How hard was this class?"
        return self._getIndices(headerList, DIFFICULTY_HEADER)

    # csvToArray(self)
    # Purpose: Take the location of the csv file and put all relevant information into a
    #   list, which is then returned
    # Entry: none
    # Exit: An array of the course reviews.
    def csvToArray(self):
        with open(self.file) as csvFile:
            readCSV = csv.reader(csvFile)

            # GET INDICES
            headers = next(readCSV)
            courseNameIndices = self._getCourseNameIndices(headers)
            hoursIndices = self._getHoursIndices(headers)
            difficultyIndices = self._getDifficultyIndices(headers)

            # ADD INFORMATION TO REVIEWS
            reviews = []
            for line in readCSV:
                commonIndex = 0
                # ADD VALUES UNTIL REACHING EMPTY CELL
                for index in courseNameIndices:
                    if line[index]:
                        courseName = line[courseNameIndices[commonIndex]]
                        hours = line[hoursIndices[commonIndex]]
                        difficulty = line[difficultyIndices[commonIndex]]
                        newReview = ClassReview(courseName, hours, difficulty)
                        reviews.append(newReview)
                        commonIndex += 1
                    else:
                        break

            return reviews


# # TEST
# # SET DATA DIRECTORY
# DIR = './data'
# FILE = '/Course Reviews (Responses) - Form Responses 1.csv'
# file = '{}{}'.format(DIR, FILE)

# test = ImportReviews(file)
# for review in test.reviewList:
#     print(review.courseName, review.difficulty, review.time)
