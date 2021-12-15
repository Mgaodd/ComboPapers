import itertools
import mmap
import timeit
import math
import time


def load_words(filename):
    with open(filename, "r+") as f:
        return set(f.read().splitlines())


def getWordListLength(words, length):
    listed = []
    for word in words:
        if len(word) == length:
            listed.append(word)
    return listed

def crackWordWithLength(words, password, flag):
    for word in words:
        if(word == password):
            if(flag):
                print("Found the password:", password)
            return password


def crackWordNoLength(words, password, flag):
    for word in words:
        if password == word:
            if(flag):
                print("Found the password:", password)
            return password


def crackWordHint(words, password, flag):
    for word in words:
        if password == word:
            if(flag):
                print("Found the password:", password)
            return password

def getWordListHint(words, hint):
    listed = []
    for word in words:
        if(hint in word):
            listed.append(word)
    return listed


def checkifInList():
    print("\nWe're gonna try and crack your password. Make sure its lowercase and alphanumeric.")
    password = input("Type in your password: ")
    
    print("Checking the Million List")
    passwords = load_words("10-million-password-list-top-1000000.txt")
    passwords = lowerList(passwords)
    begin = time.time()
    for word in passwords:
        if(word == password):
            end = time.time()
            print("Found the password in the 10Mil list: ", password)
            print("Time taken:", end - begin)
            passwords = None
            if(input("Do you want to try another? (y/n)") == "y"):
                checkifInList()
            return
    
    print("Checking words list...")
    begin = time.time()
    words = load_words("words_alpha_num.txt")
    words = lowerList(words)
    for word in words:
        if(word == password):
            end = time.time()
            print("Found the password in the english list:", password)
            print("Time taken:", end - begin)
            words = None
            if(input("Do you want to try another? (y/n)") == "y"):
                checkifInList()
            return
    
    print("Checking combinatorics list...")
    
    if(len(password) > 6):
        print("\nPassword is too long, will take a while to check...")
        if(input("Continue? (y/n)") != 'y'):
            words = None
            if(input("Do you want to try another? (y/n)") == "y"):
                checkifInList()
            return
    
    words = itertools.product("abcdefghijklmnopqrstuvwxyz1234567890", repeat=len(password))
    begin = time.time()
    counter = 0;
    length = len(password)
    
    for word in words:
        if(counter % (length * 1000000) == 0):
            print(".", end="", flush=True)
            
        counter += 1
        if("".join(word) == password):
            print("\n")
            end = time.time()
            print("Found the password in the computed list:", password)
            print("Time taken:", end - begin)
            words = None
            if(input("Do you want to try another? (y/n)") == "y"):
                checkifInList()
            return
    

def lowerList(words):
    lower = []
    for word in words:
        lower.append(word.lower())
    return lower


def runTimingFunction():
    wordsName = "words_alpha_num.txt"
    passwordsName = "10-million-password-list-top-1000000.txt"
    
    
    saveName = "words_alpha_timeTaken.csv"
    
    saveFile = open(saveName, "w+", encoding='utf-8')
    
    
    passwords = load_words(passwordsName)
    words = load_words(wordsName)
    
    lower = []
    for word in words:
        lower.append(word.lower())
    words = lower
    
    lower = []
    for word in passwords:
        if(word.isalnum()):
            lower.append(word.lower())
    passwords = lower
    
    
    import itertools
    
    for x in range(10):
        
        wordsListforTimer = getWordListLength(words, x)
        passwordsListForTimer = getWordListLength(passwords, x)
        
        counter = 0
        wordsTimer = time.time()
        for word in wordsListforTimer:
            if(word == "three"):
                counter += 1
        wordsTimeTaken = time.time() - wordsTimer;
        
        passwordsTimer = time.time()
        for password in passwordsListForTimer:
            if(password == "three"):
                counter += 1
        passwordsTimeTaken = time.time() - passwordsTimer;
        
        me = itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=x)
        
        start = time.time()
        for z in me:
            if z == "zzzzzz":
                counter += 1
        end = time.time()
        print("starting", x)
        roundingNum = 12
        
            
        saveFile.write(str(x) + "," + str(round(end - start, roundingNum)) + ","  + str(round(wordsTimeTaken, roundingNum)) + "," + str(round(passwordsTimeTaken, roundingNum)) + "\n")
        saveFile.flush()



if __name__ == "__main__":
    import timeit

#     filename = "words_alpha.txt"
#     filename = "words.txt"
    
    
#     print("\nTesting words in the English alphabet")
#     words = load_words(filename)
    
#     lower = []
#     for word in words:
#         lower.append(word.lower())
    
#     words = lower
    
#     findMe = "three"
    
#     siftedList = getWordListLength(words, len(findMe))
#     t = timeit.Timer(lambda: crackWordWithLength(siftedList, findMe, False))
#     print("With length", t.timeit(number=100))

#     words = lower
#     t = timeit.Timer(lambda: crackWordNoLength(words, findMe, False))
#     print("Without length", t.timeit(number=100))
    
#     siftedList = getWordListHint(words, findMe[0:4])
#     t = timeit.Timer(lambda: crackWordHint(siftedList, findMe, False))
#     print("With hint", t.timeit(number=100))
    
    
#     print("\nTesting 10k most common passwords")
    
#     filename = "10k-most-common.txt"
#     words = load_words(filename)
    
#     lower = []
#     for word in words:
#         lower.append(word.lower())
    
#     words = lower
    
#     findMe = "three"
    
#     siftedList = getWordListLength(words, len(findMe))
#     t = timeit.Timer(lambda: crackWordWithLength(siftedList, findMe, False))
#     print("With length", t.timeit(number=100))

#     words = lower
#     t = timeit.Timer(lambda: crackWordNoLength(words, findMe, False))
#     print("Without length", t.timeit(number=100))
    
#     siftedList = getWordListHint(words, findMe[0:4])
#     t = timeit.Timer(lambda: crackWordHint(siftedList, findMe, False))
#     print("With hint", t.timeit(number=100))
    # runTimingFunction()
    checkifInList()
    
    


    
    