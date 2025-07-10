from code5functions import avg_cal,grade_cal
name=input("Enter Student name: ")
marks=list(map(int,input("Enter marks seperated by space: ").split()))
print("Student: ",name)
average=avg_cal(marks)
print("Average: ",average)
print("Grade: ",grade_cal(average))
