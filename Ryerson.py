import bisect
from typing import *

# Define the grade cutoffs and corresponding letter grades
# gloabal_variable | localVariable for easy identification
grade_cutoffs = [0, 50, 53, 57, 60, 63, 67, 70, 73, 77, 80, 85, 90]

letter_grades = ["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"]

def errorCheck(value):
# Check for data type
	if not isinstance(value, (int, float)):
		raise Exception("input must be a int or float")
# Check for valid value
	if not 0 <= value <= 100:
	    raise Exception("score must be between 0 and 100")
		    
def ryersonScaleList (score:List[float]) ->str:
	gradeList = []
	for i in score:
		errorCheck(i)
	# Get grade index and assign grade value to list
		gradeIndex = bisect.bisect_left(grade_cutoffs, i)
		gradeList.append(letter_grades[gradeIndex -1])
	return gradeList

def ryersonScale(score: float) -> str:
	errorCheck(score)
	# Get grade index and assign grade value to variable
	gradeIndex = bisect.bisect_left(grade_cutoffs, score)
	grade = letter_grades[gradeIndex - 1]
	return grade

def main ():
	# Score list to grade
	score = [12, 43.5, 56, 25.4, 80.3, 78.9, 90.6, 75.1, 99]
	
	print(ryersonScaleList(score))
	print(ryersonScale(96))
	
main()
