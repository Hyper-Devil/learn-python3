# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def print_score(std):
        print('%s: %s' % (std.name, std.score))
        
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
			
bart = Student('Bart Simpson', 59)

print(bart.name)
#print(bart.score)	
bart.print_score()
print(bart.get_grade())
