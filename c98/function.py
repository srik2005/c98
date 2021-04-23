def count():
    f = input("Enter File Path:")
    file = open(f,"r")
    nwords = 0
    for line in file:
        words = line.split()
        nwords = nwords + len(words)
    print("No of words in the file is "+ str(nwords))

count()

