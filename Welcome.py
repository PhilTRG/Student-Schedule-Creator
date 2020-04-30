import os
Welcome_Prompt = raw_input("Hi! My name is 01100010 01101111 01100010, but you can call me Bob! Are you here to create a schedule or check a schedule?")
if Welcome_Prompt == ("Create"):
    os.system('python Schedule_Creator.py')
elif Welcome_Prompt == ("Check"):
    Student = raw_input("What is your name?")
    exists = os.path.isfile(str(Student))
    if exists:
        f= open(str(Student),"r")
        contents = f.read()
        print(contents)
    else:
        Prompt = raw_input("Sorry, there is no known schedule for " + Student + ". Do you want to create one?")
        if Prompt == ("Yes") or ("yes"):
            os.system('python Schedule Creator.py')
        else:
            exit()