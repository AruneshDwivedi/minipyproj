#Based on data provided by user this project is used to calculate time remaining to complete a particular task 
from datetime import datetime

data =input("please enter your goal and deadline date\n")
input_data=data.split(":")

goal=input_data[0]
deadline=input_data[1]


deadline_data=datetime.strptime(deadline,"%d/%m/%Y")
today_data=datetime.today()

time_left=deadline_data-today_data

print(f"number of days remaining to complete your goal {goal} is {time_left.days} days.")
