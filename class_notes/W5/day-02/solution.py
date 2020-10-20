import os
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 08:59:01 2020

@author: platf
"""

class Grades:

    def __init__(self, file_name):
        self.file_name = file_name


    def fd(self):

        data = {}

        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, self.file_name)

        file = open(file_path, "r")

        for line in file:
            line = line.rstrip("\n")
            column = line.split(',')

            # create a dictonary with the student id as the key and the
            # remaining items as a list
            data[column[0]] = column[1:len(column)]

        for key in data.keys():
            student_list = data[key]
            data[key] = self.find_grade_list(student_list)

        for key in data.keys():
            student_list = data[key]
            data[key] = self.get_gpa(student_list)

        print(data)


        file.close()

        # print(data)


    def find_grade_list(self, students_list):


        # [' Rubble', ' Test_3', '  80', ' Test_4 ', ' 80', ' quiz ', ' 90']
        # [' Bunny', ' Test_2', ' 100', ' Test_1', ' 100', 'Test_3   ', ' 100 ', 'Test_4 ', ' 100']
        # [' Duck', ' Test_1', ' 86', ' Test_5   ', ' 100 ', ' Test_2 ', '93 ', 'Test_4', ' 94']



        test_1 = 0
        test_2 = 0
        test_3 = 0
        test_4 = 0
        for index, grades in enumerate(students_list):
            if grades.strip() == 'Test_1':
                test_1 = students_list[index + 1]
            if grades.strip() == 'Test_2':
                test_2 = students_list[index + 1]
            if grades.strip() == 'Test_3':
                test_3 = students_list[index + 1]
            if grades.strip() == 'Test_4':
                test_4 = students_list[index + 1]

        return[students_list[0], int(test_1), int(test_2), int(test_3), int(test_4)]


    def get_gpa(self, student_list):
        grade_total = 0
        for index, value in enumerate(student_list):
            if type(value) != str:
                grade_total += value
        total_grades = len(student_list) - 1
        gpa = grade_total/total_grades
        student_list.append(gpa)
        return student_list


student_data = Grades("grades.txt")
student_data.fd()



