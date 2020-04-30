import os
Class_Schedule = ["", "","", "", "", "", ""]
Student_Name = 0
Class_1_Index = 1
Class_2_Index = 2
Class_3_Index = 3
Class_4_Index = 4
Class_5_Index = 5
Class_6_Index = 6
Class_Schedule[Student_Name] = raw_input("What is the name of the student this schedule is for?")
Class_Schedule[Class_1_Index] = raw_input("You can have a total of six classes. What is your first one?")
More_Classes = raw_input("Do you want more classes?")
if More_Classes == ("Yes") or ("yes"):
    Class_Schedule[Class_2_Index] = raw_input("What is your second one?")
    More_Classes = raw_input("Do you want more classes?")
    if More_Classes == ("Yes") or ("yes"):
        Class_Schedule[Class_3_Index] = raw_input("What is your third one?")
        More_Classes = raw_input("Do you want more classes?")
        if More_Classes == ("Yes") or ("yes"):
            Class_Schedule[Class_4_Index] = raw_input("What is your fourth one?")
            More_Classes = raw_input("Do you want more classes?")
            if More_Classes == ("Yes") or ("yes"):
                Class_Schedule[Class_5_Index] = raw_input("What is your fifth one?")
                More_Classes = raw_input("Do you want more classes?")
                if More_Classes == ("Yes") or ("yes"):
                    Class_Schedule[Class_6_Index] = raw_input("This is your final class. What is your sixth one?")
                    Schedule = raw_input("Do you want to see your class schedule?")
                    if Schedule == ("Yes") or ("yes"):
                        print Class_Schedule
                        f= open(str(Class_Schedule[Student_Name]),"w+")
                        f.write(str(Class_Schedule))
                        f.close() 
                else:
                    os.system('python Welcome.py')
            else:
                os.system('python Welcome.py')
        else:
            os.system('python Welcome.py')
    else:
        os.system('python Welcome.py') 
else:
    os.system('python Welcome.py')   

