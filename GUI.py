import PySimpleGUI
from classStats import ClassStats
from classReview import ClassReview
from importReviews import ImportReviews
from statistics import mean, median
from collections import Counter

PySimpleGUI.ChangeLookAndFeel('SandyBeach')
# ------ Menu Definition ------ #
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'], ]

# ------ Column Definition ------ #
column1 = [[PySimpleGUI.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],
           [PySimpleGUI.Spin(values=('Spin Box 1', '2', '3'),
                             initial_value='Spin Box 1')],
           [PySimpleGUI.Spin(values=('Spin Box 1', '2', '3'),
                             initial_value='Spin Box 2')],
           [PySimpleGUI.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

layout = [
    [PySimpleGUI.Menu(menu_def, tearoff=True)],
    [PySimpleGUI.Text('Will I Sleep this Semester?', size=(
        30, 1), justification='center', font=("Helvetica", 25), relief=PySimpleGUI.RELIEF_RIDGE)],
    [PySimpleGUI.Text('Total Hours for Class Each Week:'),
     PySimpleGUI.InputText('0', key='userHours', size=(4, 1))],
    [PySimpleGUI.Checkbox('Summer Semester?', size=(
        20, 1), key='hasSummer'), PySimpleGUI.Text('', key='answer', size=(40, 4))],
    [PySimpleGUI.Text('Class 1:')], [PySimpleGUI.InputCombo(('CS 161 - Intro to Computer Science I', 'CS 162 - Intro to Computer Science II', 'CS 165 - Intro to Computer Science (Accelerated)', 'CS 225 - Discrete Structures in Computer Science', 'CS 261 - Data Structures', 'CS 271 - Computer Architecture & Assembly Language', 'CS 290 - Web Development', 'CS 325 - Analysis of Algorithms', 'CS 340 - Introduction to Databases', 'CS 344 - Operating Systems',
                                                             'CS 352 - Introduction to Usability Engineering', 'CS 361 - Software Engineering I', 'CS 362 - Software Engineering II', 'CS 372 - Intro to Computer Networks', 'CS 373 - Defense Against the Dark Arts', 'CS 464 - Open Source Software', 'CS 419/467 - Software Projects', 'CS 475 - Intro to Parallel Programming', 'CS 496 - Mobile and Cloud Software Development'), size=(20, 1), key='class1'), PySimpleGUI.Text('', key='class_uno', size=(40, 4))],
    [PySimpleGUI.Text('Class 2:')], [PySimpleGUI.InputCombo(('None', 'CS 161 - Intro to Computer Science I', 'CS 162 - Intro to Computer Science II', 'CS 165 - Intro to Computer Science (Accelerated)', 'CS 225 - Discrete Structures in Computer Science', 'CS 261 - Data Structures', 'CS 271 - Computer Architecture & Assembly Language', 'CS 290 - Web Development', 'CS 325 - Analysis of Algorithms', 'CS 340 - Introduction to Databases', 'CS 344 - Operating Systems',
                                                             'CS 352 - Introduction to Usability Engineering', 'CS 361 - Software Engineering I', 'CS 362 - Software Engineering II', 'CS 372 - Intro to Computer Networks', 'CS 373 - Defense Against the Dark Arts', 'CS 464 - Open Source Software', 'CS 419/467 - Software Projects', 'CS 475 - Intro to Parallel Programming', 'CS 496 - Mobile and Cloud Software Development'), size=(20, 1), key='class2'), PySimpleGUI.Text('', key='class_dos', size=(40, 4))],
    [PySimpleGUI.Text('Class 3:')], [PySimpleGUI.InputCombo(('None', 'CS 161 - Intro to Computer Science I', 'CS 162 - Intro to Computer Science II', 'CS 165 - Intro to Computer Science (Accelerated)', 'CS 225 - Discrete Structures in Computer Science', 'CS 261 - Data Structures', 'CS 271 - Computer Architecture & Assembly Language', 'CS 290 - Web Development', 'CS 325 - Analysis of Algorithms', 'CS 340 - Introduction to Databases', 'CS 344 - Operating Systems',
                                                             'CS 352 - Introduction to Usability Engineering', 'CS 361 - Software Engineering I', 'CS 362 - Software Engineering II', 'CS 372 - Intro to Computer Networks', 'CS 373 - Defense Against the Dark Arts', 'CS 464 - Open Source Software', 'CS 419/467 - Software Projects', 'CS 475 - Intro to Parallel Programming', 'CS 496 - Mobile and Cloud Software Development'), size=(20, 1), key='class3'), PySimpleGUI.Text('', key='class_tres', size=(40, 4))],
    [PySimpleGUI.Text('Class 4:')], [PySimpleGUI.InputCombo(('None', 'CS 161 - Intro to Computer Science I', 'CS 162 - Intro to Computer Science II', 'CS 165 - Intro to Computer Science (Accelerated)', 'CS 225 - Discrete Structures in Computer Science', 'CS 261 - Data Structures', 'CS 271 - Computer Architecture & Assembly Language', 'CS 290 - Web Development', 'CS 325 - Analysis of Algorithms', 'CS 340 - Introduction to Databases', 'CS 344 - Operating Systems',
                                                             'CS 352 - Introduction to Usability Engineering', 'CS 361 - Software Engineering I', 'CS 362 - Software Engineering II', 'CS 372 - Intro to Computer Networks', 'CS 373 - Defense Against the Dark Arts', 'CS 464 - Open Source Software', 'CS 419/467 - Software Projects', 'CS 475 - Intro to Parallel Programming', 'CS 496 - Mobile and Cloud Software Development'), size=(20, 1), key='class4'), PySimpleGUI.Text('', key='class_cuatro', size=(40, 4))],
    [PySimpleGUI.Text('_' * 80)],
    [PySimpleGUI.ReadButton('Calculate')]
]


window = PySimpleGUI.Window('Will I Sleep this Semester? ',
                            layout, default_element_size=(40, 1), grab_anywhere=False)

DIR = './data'
FILE = '/Course Reviews (Responses) - Form Responses 1.csv'
file = '{}{}'.format(DIR, FILE)


while True:
    button, values = window.Read()

    if button is None:
        break
    # logic for output
    #keys = userHours, hasSummer, class1, class2, class3, class4
    # TODO: case where <4 courses selected, disable button if same courses selected, bring in isSummer function for default value
    hoursAvailable = float(values['userHours'])
    exists1, exists2, exists3, exists4 = values['class1'], values['class2'], values['class3'], values['class4']
    #first_class = ClassStats(file, str(values['class1']))
    #second_class = ClassStats(file, values['class2'])
    #third_class = ClassStats(file, values['class3'])
    #fourth_class = ClassStats(file, values['class4'])
    summer_multiplier = 1.0
    class_total_mean = 0.0
    class_uno = ''
    class_dos = ''
    class_tres = ''
    class_cuatro = ''
    if (values['hasSummer'] == True):
        summer_multiplier = 1.75
    else:
        summer_multiplier = 1.0
    if (exists1 != 'None'):
        first_class = ClassStats(file, str(values['class1']))
        class_uno = (first_class.courseName + ': ' + '\nAverage Estimated Time Required: ' + str(int(first_class.timeTotalMean * summer_multiplier)) + '\xB1' + str(format(
            (first_class.timeTotalMean - first_class.timeMinMean)*summer_multiplier, '.1f')) + " hrs" + '\nAverage Expected Difficulty: ' + str(format(first_class.difficultyMean, '.1f')))
        class_total_mean += first_class.timeTotalMean
    if (exists2 != 'None'):
        second_class = ClassStats(file, values['class2'])
        class_dos = (second_class.courseName + ': ' + '\nAverage Estimated Time Required: ' + str(int(second_class.timeTotalMean * summer_multiplier)) + '\xB1' + str(format(
            (second_class.timeTotalMean - second_class.timeMinMean)*summer_multiplier, '.1f')) + " hrs" + '\nAverage Expected Difficulty: ' + str(format(second_class.difficultyMean, '.1f')))
        class_total_mean += second_class.timeTotalMean
    if (exists3 != 'None'):
        third_class = ClassStats(file, values['class3'])
        class_tres = (third_class.courseName + ': ' + '\nAverage Estimated Time Required: ' + str(int(third_class.timeTotalMean * summer_multiplier)) + '\xB1' + str(format(
            (third_class.timeTotalMean - third_class.timeMinMean)*summer_multiplier, '.1f')) + " hrs" + '\nAverage Expected Difficulty: ' + str(format(third_class.difficultyMean, '.1f')))
        class_total_mean += third_class.timeTotalMean
    if (exists4 != 'None'):
        fourth_class = ClassStats(file, values['class4'])
        class_cuatro = (fourth_class.courseName + ': ' + '\nAverage Estimated Time Required: ' + str(int(fourth_class.timeTotalMean * summer_multiplier)) + '\xB1' + str(format(
            (fourth_class.timeTotalMean - fourth_class.timeMinMean)*summer_multiplier, '.1f')) + " hrs" + '\nAverage Expected Difficulty: ' + str(format(fourth_class.difficultyMean, '.1f')))
        class_total_mean += fourth_class.timeTotalMean
    class_total_mean *= summer_multiplier
    time_difference = int(hoursAvailable - class_total_mean)
    if (time_difference >= 0):
        answer = 'You WILL get sleep this semester!' + ' You went ' + \
            str(time_difference) + ' hours under your free time.'
    else:
        answer = 'You will NOT get sleep this semester!' + '\nYou went ' + \
            str(time_difference * (-1)) + ' hours over your free time.'
    if (exists1 != 'None'):
        class_uno = (first_class.courseName + ': ' + '\nAverage Estimated Time Required: ' + str(int(first_class.timeTotalMean * summer_multiplier)) + '\xB1' + str(format(
            (first_class.timeTotalMean - first_class.timeMinMean)*summer_multiplier, '.1f')) + " hrs" + '\nAverage Expected Difficulty: ' + str(format(first_class.difficultyMean, '.1f')))
    window.FindElement('answer').Update(answer)
    window.FindElement('class_uno').Update(class_uno)
    window.FindElement('class_dos').Update(class_dos)
    window.FindElement('class_tres').Update(class_tres)
    window.FindElement('class_cuatro').Update(class_cuatro)
