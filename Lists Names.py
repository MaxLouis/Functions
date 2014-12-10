#Lists
def output(names):
    count = 1
    for each in names:
        print(count,each)
        count += 1

def name_change(names):
    change = int(input("Which name would you like to change?"))
    change -= 1
    print()
    return change

def name_input(names):
    student_num = 0
    for each in names:
        names[student_num] = input("Please enter student {}:".format(student_num + 1))
        student_num += 1
    
# Main
names = ["","","","","","","","",""]
name_input(names)
output(names)
change = name_change(names)

print(names[change])
names[change] = input("Please enter the change.")
print()
output(names)
