"""
Code Academy - Python Course -  Exam Statistics example 
Feb 2016, gulsedaunal
"""
#grades of a class, can be later modified for user input or read from a file
grades = [100,30,40,50,60,100,90,80,75]

#prints the grades list
def print_grades(grades):
    for num in grades:
        print str(num) + '\n'

print_grades(grades)

#calculates the sum of all grades - to be used in average calculation
def grades_sum(scores):
    result = 0
    for num in scores:
        result += num
    return result

#print grades_sum(grades)

#calculates the average of all grades
def grades_average(grades):
    return grades_sum(grades)/float(len(grades))

#print grades_average(grades)

#calculates the variance (over all grades wrt the average)
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / float(len(scores))
  
#print grades_variance(grades)

#calculates the standard deviation
def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)
print grades_std_deviation(variance)

#eof
