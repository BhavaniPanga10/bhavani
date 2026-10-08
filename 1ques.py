def calculate_result(student_name,*marks,**details):
    print("student Name:",student_name)
    print("total_marks:",sum(marks))
    print("average_marks:",sum(marks)/len(marks))
    for key,value in details.items():
        print(key,":",value)

calculate_result("Bhavani",20,25,25,grade="A",clg="TKR",city="Hyd")


