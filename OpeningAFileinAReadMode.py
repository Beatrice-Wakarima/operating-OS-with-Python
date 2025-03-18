"""This line opens the file spider.txt in read mode. The open() function returns a file object which is assigned to the variable file."""
file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()