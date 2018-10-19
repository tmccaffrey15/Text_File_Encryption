import random

def Keygen():
    letters = ['A','B','C','D','E','F','G','H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    key = []
    while len(letters) > 0:
        whichOne = random.randint(0,len(letters) -1)
        char = letters[whichOne]
        key.append(char)
        letters.remove(char)

    return key

def Encrypt(filename):
    mesg_outputFile = open(filename + '_coded' + '.txt', 'w')
    mesg_inputFile = open(filename + '.txt', 'r')
    key = Keygen() 
    letters = ['A','B','C','D','E','F','G','H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

    empty_str = ''
    line = mesg_inputFile.readline()
    while line != empty_str:
        list_line = list(line)
        for k in range(len(list_line)):
            currentChar = list_line[k]
            if currentChar != '\n' and currentChar != ' ':
                newChar = key[letters.index(currentChar)]
                list_line[k] = newChar
        str_line = ''.join(list_line)        
        mesg_outputFile.write(str_line)
        line = mesg_inputFile.readline()
        
    mesg_inputFile.close()
    mesg_outputFile.close()
    
    empty_str = ''
    str_key = empty_str.join(key)
    key_outputFile = open(filename + '_key' + '.txt', 'w')  
    key_outputFile.write(str_key)
    key_outputFile.close()
    
def Decrypt(filename):
    mesg_inputFile = open(filename + '_coded' + '.txt', 'r')
    mesg_outputFile = open(filename + '_decoded' + '.txt', 'w')
    
    key_inputFile = open(filename + '_key' + '.txt', 'r')
    key_str = key_inputFile.readline()
    key = list(key_str)
    letters = ['A','B','C','D','E','F','G','H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

    empty_str = ''
    coded = mesg_inputFile.readline()
    while coded != empty_str:
        list_coded = list(coded)
        for k in range(len(list_coded)):
            currentChar = list_coded[k]
            if currentChar != '\n' and currentChar != ' ':
                newChar = letters[key.index(currentChar)]
                list_coded[k] = newChar
        str_line = ''.join(list_coded)        
        mesg_outputFile.write(str_line)
        coded = mesg_inputFile.readline()

    mesg_inputFile.close()
    mesg_outputFile.close()

#main
filename = input('Enter filename: ')
choice = input('If encrypting, enter E, for decrypting enter D: ')

if choice == 'E':
    Encrypt(filename)
elif choice == 'D':
    Decrypt(filename)
