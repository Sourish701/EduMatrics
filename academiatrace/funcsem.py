# Function to input and store marks for multiple semesters and calculate averages
from funcvalidmark import get_valid_marks
from funcvalidname import get_valid_names
from funcvalidnum import get_valid_num_students 
def sem_marks():
    s=[]
    i={}
    k=0
    stud_names=[]
    n=get_valid_num_students()
    #For 1st Sem
    for x in range(n):
        print(f"--- Entering marks for (1st Sem) ---")
        names=get_valid_names()
        stud_names.append(names)
        b=get_valid_marks("physics: ")
        c=get_valid_marks("chemistry: ")
        d=get_valid_marks("maths: ")
        e=get_valid_marks("computer: ")
        f=get_valid_marks("biology: ")
        s.append(b)
        s.append(c)
        s.append(d)
        s.append(e)
        s.append(f)
        i[names]=s[k:k+5: ]
        k=k+5
    print(i)
    g=0
    # Average for 1st Sem
    d = input("Whose average marks do you want to find?: ")
    if d not in i:
        from functime import flash_and_input
        
        d = flash_and_input("Invalid student name!", "Enter name again: ")
    if d in i:
        g = 0
        l = i.get(d)
        for j in l:
            g = g + j
        h = g / 5
        print(f"Average marks for 1st sem of {d} is {h}")
    else:
        print(f"Sorry, {d} could not be found even on the second attempt.")
#For 2nd Sem
    s1=[]
    i1={}
    k1=0
    student_names = list(i.keys())
    for name in student_names:
        print(f"--- Entering marks for {name} (2nd Sem) ---")
        b1=get_valid_marks("physics: ")
        c1=get_valid_marks("chemistry: ")
        d1=get_valid_marks("maths: ")
        e1=get_valid_marks("computer: ")
        f1=get_valid_marks("biology: ")
        s1.append(b1)
        s1.append(c1)
        s1.append(d1)
        s1.append(e1)
        s1.append(f1)
        i1[name]=s1[k1:k1+5: ]
        k1=k1+5
    print(i1)
    #Average for 2nd Sem
    choice = input("Do you want to find average for 2nd sem?(y/n): ")
    if choice=='y' or choice=='Y':
        search_name = input("Do you want to find the same student's average?(y/n): ")
        if search_name=='y' or search_name=='Y':
            search_name=d
            g1=0
            l1=i1.get(d)
            for j1 in l1:
                g1=g1+j1
                h1=g1/5
            print(f"Average marks for 2nd sem of {d} is {h1}")
        else:
            search_name=input("Enter the student's name: ")
            g1=0
            l1=i1.get(search_name)
            for j1 in l1:
                g1=g1+j1
                h1=g1/5
            print(f"Average marks for 2nd sem of {search_name} is {h1}")
    #For 3rd Sem
    s2=[]
    i2={}
    k2=0
    student_names = list(i.keys())
    for name in student_names:
        print(f"--- Entering marks for {name} (3rd Sem) ---")
        b2=get_valid_marks("physics: ")
        c2=get_valid_marks("chemistry: ")
        d2=get_valid_marks("maths: ")
        e2=get_valid_marks("computer: ")
        f2=get_valid_marks("biology: ")
        s2.append(b2)
        s2.append(c2)
        s2.append(d2)
        s2.append(e2)
        s2.append(f2)
        i2[name]=s2[k2:k2+5: ]
        k2=k2+5
    print(i2)
    #Average for 3rd Sem
    choice1 = input("Do you want to find average for 3rd sem?(y/n): ")
    if choice1=='y' or choice1=='Y':
        search_name1 = input("Do you want to find the same student's average?(y/n): ")
        if search_name1=='y' or search_name1=='Y':
            search_name=d
            g2=0
            l2=i2.get(d)
            for j2 in l2:
                g2=g2+j2
                h2=g2/5
            print(f"Average marks for 2nd sem of {d} is {h2}")
        else:
            search_name1=input("Enter the student's name: ")
            g2=0
            l2=i2.get(search_name1)
            for j2 in l2:
                g2=g2+j2
                h2=g2/5
            print(f"Average marks for 2nd sem of {search_name1} is {h2}")
    #For 4th Sem
    s3=[]
    i3={}
    k3=0
    student_names = list(i.keys())
    for name in student_names:
        print(f"--- Entering marks for {name} (4th Sem) ---")
        b3=get_valid_marks("physics: ")
        c3=get_valid_marks("chemistry: ")
        d3=get_valid_marks("maths: ")
        e3=get_valid_marks("computer: ")
        f3=get_valid_marks("biology: ")
        s3.append(b3)
        s3.append(c3)
        s3.append(d3)
        s3.append(e3)
        s3.append(f3)
        i3[name]=s3[k3:k3+5: ]
        k3=k3+5
    print(i3)
    #Average for 4th Sem
    choice2 = input("Do you want to find average for 4th sem?(y/n): ")
    if choice2=='y' or choice2=='Y':
        search_name2 = input("Do you want to find the same student's average?(y/n): ")
        if search_name2=='y' or search_name2=='Y':
            search_name=d
            g3=0
            l3=i3.get(d)
            for j3 in l3:
                g3=g3+j3
                h3=g3/5
            print(f"Average marks for 4th sem of {d} is {h3}")
        else:
            search_name2=input("Enter the student's name: ")
            g3=0
            l3=i3.get(search_name2)
            for j3 in l3:
                g3=g3+j3
                h3=g3/5
            print(f"Average marks for 4th sem of {search_name2} is {h3}")
    
    return i,i1,i2,i3
    

