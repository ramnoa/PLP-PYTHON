# creating new file
file = open('week4assgnment.pdf', 'w')
# writing content to the file
file.write("This is a sample text for week 4 assignment.\n")
# closing the file
file.close()
# This code handles the case where the file does not exist
try:
    file = open('week4assgnment.pdf', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file 'week4assgnment.pdf' does not exist. Please check the file name and try again.")
    
