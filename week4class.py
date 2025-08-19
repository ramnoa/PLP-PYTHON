'''''
file =open("week4class.pdf", "w")
file.write("This is a sample text for week 4 class.")


#appending to the file
file = open("week4class.pdf", "a")
file.write("\nRamzey noah cartel is a great guy.")

# reading the file
file = open("week4class.pdf", "r")
content = file.read()
print(content)

#reading the file line by line
file = open("week4class.pdf", "r")
content = file.readlines()
'''
#reading image file
file = open("2.jpg", "rb")
content = file.read()
print(content)
