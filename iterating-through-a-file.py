'''iterating through a file.'''
with open("spider.txt") as file:
    for line in file:
        print(line.upper())