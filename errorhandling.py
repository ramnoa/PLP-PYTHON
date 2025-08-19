try:
    file = open('week4class.pdf', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file 'week4class.pdf' does not exist. Please check the file name and try again.")