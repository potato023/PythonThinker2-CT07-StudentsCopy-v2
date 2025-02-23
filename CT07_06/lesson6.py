print("Hello from lesson 6")

# You are about to graduate and would like to create a database
# to keep all your friend's contact details using a 2d list.

contacts = []
contact1 = ["John", 98453126, "john@gmail.com"]
contact2 = ["Adam", 93029102, "adam@gmail.com"]
contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]

# 1. append contact1, contact2, and contact3 into contacts
# 2. Write a nested loop to loop through each contact and print
#    the details for each contact

contacts.append(contact1)
contacts.append(contact2)
contacts.append(contact3)
print (contacts)



# You have been given a 2d list of students from a class
# consisting each student's name and their gender:


students = [
    ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
    ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],
    ["Sophia", "F"], ["Lucas", "M"], ["Mia", "F"],
    ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
    ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
]


### the above is a nested list. Study and discuss it before we
### move on.

# 1. Write a for loop to print out the names of each student and
#    the gender beside.
   
#    e.g. Olivia F
#         Noah M
girl = []
boy = []
for student in students:
    name, gender = student

if gender == 'f':
    girl.append

print ('gender of ' + (name) + ':' +(gender)) 