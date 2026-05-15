def student_details(name,roll_no,marks):
    print(f"student: {name}")
    print(f"roll_number: {roll_no}")
    total=sum(marks)
    average=total/5
    print(f"toatl: {total} Average: {average} ")
    if average>=90:
          grade='A'
  
    elif average>=75:
        grade='B'
    elif average>=60:
        grade='C'
    elif average>=40:
        grade='D'
    else:
        grade='FAIL'
    print("subject below 40: ")
    for i in range(len(marks)):
        if marks[i]<=40:
            print(f"subject: {i+1}")
        
student_details("shilpa",141,[90,67,58,40,98])
        
   

    


  
