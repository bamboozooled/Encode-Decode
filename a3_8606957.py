#Name: Oluwatimi Owoturo
#Student Number: 8606957
#Assignment 3
#Partners name: Orion Kemp
#Partners student Number: 8788626

def runLength_Encode(f1,output):
    file1L = f1.read()
    f1.close()
    
    same = 0
    letter = 0
    sameL = []
    previous = []
    counter2=0
    keepT = 1
    keepT2 = 1
    Encoded = ''


    for i in range(len(file1L)-1):
        if file1L[i] == file1L[i+1]:
            keepT2 = 1
            if keepT != 1:
                keepT = 1    #Keeping track of spaces
            same = same+1

            #sameL.append(same)
            #sameL.append(file1L[i])

        if file1L[i] != file1L[i+1]:
            if keepT == 1:
                same = same+1
                sameL.append(str(same)) #Appending the number of elements that are the same(determined by the counter)
                sameL.append(file1L[i-1]) #Appending previous to list.
                same = 0
                keepT = keepT - 1

            if keepT2 == 0:
                counter2 = counter2 + 1
                sameL.append(str(counter2))
                sameL.append(file1L[i])
                counter2 = 0

            if keepT2 == 1:
                keepT2 = keepT2 - 1

    print("Encoding in progress......")

    import string

    j = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    k = j + '\t' + '\r\x0b\x0c'

    for i in range(len(k)):
        if (k[i] in sameL): #Checking for unsupported characters 
            print("Unsupported characters")
            print("Restarting program")
            return main() #Restarting program main()

    else:
        for v in range(len(sameL)):
            Encoded = Encoded + sameL[v] #Adding elements of list to a string Encoded

        print("Encoding completed! ")
        compression = len(file1L) / len(Encoded) #Calculating compression ratio

        print("Compression ratio: " + str(compression))

        output.write(Encoded) #Outputting to file
        output.close()
            
def decode(file,output):
    file1L = file.read()
    file.close()
    h = []
    decoded = ""
    num = ""
    j = 0

    for i in range(len(file1L)-1):
        if file1L[i].isdigit() and file1L[i+1].isalpha() or file1L[i+1].isspace(): #Checking if element is a digit, alphabet or a space
            h.append(int(file1L[i])*file1L[i+1]) #Only happens if a one digit number
        elif file1L[i].isdigit() and file1L[i+1].isdigit():
            h.append(int(file1L[i] + file1L[i+1])*file1L[i+2]) #Happens if a 2 digit number

    print("Decoding in progress.............")

    j = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    k = j + '\t' + '\r\x0b\x0c'

    for i in range(len(k)):
        if (k[i] in h): #Checking for unsupported characters
            print("Wrong encoded format")
            print("Restarting program")
            return main()

    print("Decoding completed")
    
    for i in range(len(h)):
        decoded = decoded + h[i] #Adding elements of list to a string decoded

    output.write(decoded) #Outputting the decode to a file
    output.close()
        
def menu(userSelect):
    try:
        #Checking for user selection and input.
        #Also checking if file exists by using try and except
        if userSelect == "1":
            file = input("Input Source File Name: ").strip()
            file1 = open(file,'r')

            outfile = input("Input Destination File Name: ").strip()
            fileo = open(outfile,'w')

            runLength_Encode(file1,fileo)
        if userSelect == "2":
            file = input("Input Source File Name: ").strip()
            file1 = open(file,'r')

            outfile = input("Input Destination File Name: ").strip()
            fileo = open(outfile,'w')
            decode(file1,fileo)

        if userSelect == "3":
            quit
            
    except FileNotFoundError:
        print("Input file not found")
        return main()

def main(): #Main program(Program handler) and menu
    print("Make your selection(Type 1,2 or 3): ")
    print("1. Encode a File")
    print("2. Decode a File")
    print("3. Exit")
    userSelect = (input("Your selection: ")).strip()

    menu(userSelect)

#main
main()
