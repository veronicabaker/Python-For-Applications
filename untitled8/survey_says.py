import list_utils

with open("survey-results.csv", "r") as f:
    skill_list = []
    pace_list = []
    for line in f.readlines():
        line = line.split(",")
        if line[0] == "Student":
            continue
        else:
            skill_list.append(line[2].strip())
            pace_list.append(line[1].strip())

print("SURVEY RESULTS")
print("Skills")
print("~~~~~~")

for x, y in enumerate(skill_list):
    print(str(x + 1) + ": " + str(y))

print("Average: " + str(list_utils.mean(skill_list)))
print("Standard Deviation: " + str(list_utils.std_dev(skill_list)))
print("Median: " + str(list_utils.median(skill_list)))

print("/nPaces")
print("~~~~~~")

for x, y in enumerate(pace_list):
    print(str(x + 1) + ": " + str(y))

print("Average: " + str(list_utils.mean(pace_list)))
print("Standard Deviation: " + str(list_utils.std_dev(pace_list)))
print("Median: " + str(list_utils.median(pace_list)))