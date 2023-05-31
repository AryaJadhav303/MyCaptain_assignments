# -*- coding: utf-8 -*-
"""
Created on Wed May 31 18:01:34 2023

@author: Arya
"""

import csv
def write_in_file(info_list):
    with open("student_info.csv","a+",newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name ","Roll No. ","Class ","Email id. "])
        writer.writerow(info_list)
if __name__ == "__main__":
    condition=1
    student=1
    while condition== 1:
        student_info=input("Enter student#{} details in format\n(Name, Roll No., Class, Email id.): ".format(student))
        student_info_list=student_info.split(",")
        print("\nEntered student#{} details are- \nName: {}\nRoll No.: {}\nClass: {}\nEmail id.: {}"
              .format(student,student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice=input("Would you like to make any changes?(Y/N): ")
        if choice.capitalize()=="N":
            write_in_file(student_info_list)
            student+=1
            condition_check=input("Would you like to enter another student's information?(Y/N) : ")
            if condition_check.capitalize()== "Y":
                condition=1
            else:
                condition=0
        elif choice.capitalize()=="N":
            print("Enter details")
