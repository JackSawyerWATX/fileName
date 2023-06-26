fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

with open(fname, "r") as file:
    for line in file:
        if line.startswith('From ') and not line.startswith('From:'):
            words = line.split()
            email = words[1]
            print(email)
            count += 1

print("There were", count, "lines in the file with From as the first word")



#
# # Open the file
# file_path = "mbox-short.txt"  # Replace with the actual file path
#
# # Initialize variables
# count = 0
#
# # Read the file line by line
# with open(file_path, "r") as file:
#     for line in file:
#         # Check for lines starting with 'From ' but not 'From:'
#         if line.startswith('From ') and not line.startswith('From:'):
#             words = line.split()
#             email = words[1]
#             print(email)
#             count += 1
#
# # Print the count
# print("Count:", count)
