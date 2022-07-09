def countfileline ():
    filename = input('Enter a file name: ')
    numberofwords=0

    file= open(filename )
    print("hello")
    
    for line in file:
        print("bye")
        print(line)
        words=line.split()
        numberofwords = numberofwords+len(words)
        
    print("Number of words" , numberofwords)

countfileline()