# Devin Theriault
# 06/19/2026
# P4HW1
# Grading Program which includes for and while loops

'''
Ask users how many scores they would like to enter.
Creates empty list of scores.
If scores are not between 0 and 100, prints invalid score, tells the user the number must be between 0 and 100, asks the user to enter score again.
Adds valid scores to the list.
Removes lowest score.
Averages remaining scores.
Selects letter grade.
Displays Text

'''



# Ask for total number of scores
total_scores = int(input("How many scores do you want to enter? "))

scores_list = []
current_count = 1

# Collect scores from user
while current_count <= total_scores:
    score = float(input(f"Enter score #{current_count}: "))

    # Make sure the score is between 0 and 100
    while score < 0 or score > 100:
        print ("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{current_count} again: "))

    scores_list.append(score)
    current_count += 1

# Find the lowest score
lowest_score = min(scores_list)

# Create modified list by removing lowest score
modified_list = scores_list[:]
modified_list.remove(lowest_score)

#Calculate average of remaining scores
scores_average = sum(modified_list) / len(modified_list)


# determine letter grade for average

if scores_average >= 90:
    grade = 'A'
elif scores_average >= 80:
    grade = 'B'
elif scores_average >= 70:
    grade = 'C'
elif scores_average >= 60:
    grade = 'D'
else:
    grade = 'f'

#Display results
print("\n------------Results------------")
print(f'{"Lowest Score:":<18} {lowest_score}')
print(f'{"Modofied List:":<18} {modified_list}')
print(f'{"Scores Average:":<18} {scores_average}')
print(f'{"Grade":<18} {grade}')
print("-" * 35)
