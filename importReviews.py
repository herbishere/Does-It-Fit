# IMPORT PACKAGES AND MODULES
import csv
from classReview import ClassReview

# SET DATA DIRECTORY
DIR = './data'
FILE = '/Course Reviews (Responses) - Form Responses 1.csv'
file = '{}{}'.format(DIR, FILE)


def _getIndices(headerList, matchString):
    indices = []
    index = 0
    for cell in headers:
        if cell == matchString:
            indices.append(index)
        index += 1
    return indices


def _getCourseNameIndices(headerList):
    COURSENAME_HEADER = "What Course Did You Take?"
    return _getIndices(headerList, COURSENAME_HEADER)


def _getHoursIndices(headerList):
    HOURS_HEADER = "How much time did you spend on average (per week) for this class?"
    return _getIndices(headerList, HOURS_HEADER)


def _getDifficultyIndices(headerList):
    DIFFICULTY_HEADER = "How hard was this class?"
    return _getIndices(headerList, DIFFICULTY_HEADER)


with open(file) as csvFile:
    readCSV = csv.reader(csvFile)
    headers = next(readCSV)

    # GET INDICES
    courseNameIndices = _getCourseNameIndices(headers)
    hoursIndices = _getHoursIndices(headers)
    difficultyIndices = _getDifficultyIndices(headers)

    reviews = []
    for line in readCSV:
        commonIndex = 0
        for index in courseNameIndices:
            if line[index]:
                courseName = line[index]
                hours = line[hoursIndices[commonIndex]]
                difficulty = line[difficultyIndices[commonIndex]]
                newReview = ClassReview(courseName, hours, difficulty)
                reviews.append(newReview)
                commonIndex += 1
            else:
                break

    for review in reviews:
        print(review.courseName, review.time, review.timeMin,
              review.timeMax, review.difficulty)
