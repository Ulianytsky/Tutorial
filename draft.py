work_experience = int(input("Enter your full work experience in years: "))

if work_experience >= 4:
    developer_type = "Middle"


elif work_experience <= 1:
    developer_type = "Junior"
else:
    developer_type = "Senior"
print(work_experience)
print(developer_type)