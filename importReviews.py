# IMPORT PACKAGES AND MODULES
import csv
from classReview import ClassReview


class ImportReviews:
    def __init__(self, file):
        self.file = file
        self.reviewList = self.csvToArray()

    def _getIndices(self, headerList, matchString):
        indices = []
        index = 0
        for cell in headerList:
            if cell == matchString:
                indices.append(index)
            index += 1
        return indices

    def _getCourseNameIndices(self, headerList):
        COURSENAME_HEADER = "What Course Did You Take?"
        return self._getIndices(headerList, COURSENAME_HEADER)

    def _getHoursIndices(self, headerList):
        HOURS_HEADER = "How much time did you spend on average (per week) for this class?"
        return self._getIndices(headerList, HOURS_HEADER)

    def _getDifficultyIndices(self, headerList):
        DIFFICULTY_HEADER = "How hard was this class?"
        return self._getIndices(headerList, DIFFICULTY_HEADER)

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
