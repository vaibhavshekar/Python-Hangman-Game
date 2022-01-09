import random
print('')
print('_______________________________________________________________________________________________________________')
print('                                            HANGMAN GAME')

# line 68 onwards code for the game structure

#for drawing the hangman structure
def hangman_no_chances():
    print('_______')
    print('|      ')      
    print('|')       
    print('|')      
    print('|')   
    print('|')       
    print('-')      

def hangman_1_wrong():    #for drawing the hangman structure
    print('________')
    print('       O')       
    print(' ')   
    print('')    

def hangman_2_wrong():     #for drawing the hangman structure
    print('________')                                             
    print('       O')       
    print('       | ')
    print('')               
    print('')

def hangman_3_wrong():     #for drawing the hangman structure
    print('________')      
    print('       O')       
    print('     / | ')
    print('')               
    print('') 

def hangman_4_wrong():    #for drawing the hangman structure
    print('________')      
    print('       O')       
    print('     / | \\')               
    print('')     
    

def hangman_5_wrong():       #for drawing the hangman structure
    print('________')      
    print('       O')       
    print('     / | \\')
    print('      / ')         
    print('')
    print('')

def hangman_6_wrong():       #for drawing the hangman structure
    print('________')      
    print('       O')       
    print('     / | \\')
    print('      / \\')        
    print(' ')
    print('') 

# making the word list and hints
words=['indigo','vistara','goair','emirates','delta','lufthansa',
       'them','mathematics', 'school', 'english','economics','chips','pizza','burger',
       'sandwhich','Joey','christmas','friends','apartments','apparently','star',
       'hollywood','brooklyn','antelope','hotel','sacraemento','clock','painting','infernal',
       'immortal','tata','ford','mercedes','hyundai','skoda','volkswagan','mahindra']

w= random.choice(words).upper()

def play():
    cw='-'*len(w)                       #to take unguessed letters as - initially
    guessed = False
    g_letters = []
    g_words = []
    for_replacing = [cw]
    chances = 6
    print('')
    print('GAME BEGINS')
    print('')
    print('')
    print('INSTRUCTION: When all your guessed letters fit in the blanks, press any letter, when you are asked to guess, to finish the game')
    print('')
    if chances == 6:
        print(hangman_no_chances())
    else:
        pass
    print('')
    print(cw)

    def printing_hangman():
        if chances == 0:                 #for drawing the hangman structure
            print(hangman_6_wrong())
        elif chances == 1:
            print(hangman_5_wrong())
        elif chances == 2:
            print(hangman_4_wrong())
        elif chances == 3:
            print(hangman_3_wrong())
        elif chances == 4:
            print(hangman_2_wrong())
        elif chances == 5:
            print(hangman_1_wrong())

    while not guessed and chances >0:
        a = input('your guess (letter/word): ').upper()         
        
        def replacing():              # to replace the - by correct guessed letters
            us = for_replacing[-1]
            n = w.find(a)
            p = w.rfind(a)
            y = us[0:n] + a + us[n+1:]
            us = y
            for_replacing.append(us)
            if p != -1:
                us = us[0:p] + a + us[p+1:] 
                q = us
                for_replacing.append(q)             
            else:
                us = y
                for_replacing.append(us)
        
        replacing
        # setting the conditions if the user guessed a letter, or a word, or something else    
        if len(a) == 1 and type(a) == str and w not in for_replacing :
            if a in g_letters:
                print('already guessed this letter ')
                print(for_replacing[-1])
                print(' __________________')            #checking if the letter has already been guessed is there in the word or not there in the word  

            elif a not in w:  
                print('incorrect guess')
                chances = chances - 1
                print(chances,'chances remaining')
                printing_hangman()
                print(for_replacing[-1])
                g_letters.append(a)                      # to store in the list of letters that are stored
                print(' ________________ ')
       
            else:
                print(a, 'is a correct guess')
                printing_hangman()
                replacing()
                print(for_replacing[-1])
                g_letters.append(a)   
                print(' ________________ ')

        elif len(a) == len(w) and type(a) == str and w not in for_replacing:
            if a in g_words:
                print('word already guessed')
                printing_hangman()
                print(for_replacing[-1])
                print(' ___________________ ')
            elif a != w:
                print(a,'not the word')
                chances = chances - 1
                print(chances,'chances remaining')
                printing_hangman()
                print(for_replacing[-1])
                g_words.append(a)
                print(' ________________ ')

            else:
                print('')
                print(a,'is a correct guess')
                printing_hangman()
                print('GAMEOVER')
                guessed= True
               
        elif w in for_replacing:
            print('GAMEOVER!')
            break
        else:
            print('incorrect guess')
            print(for_replacing[-1])
            print(chances,'chances remaining') 



    if chances == 0:
        print('All chances over')
        print('GAMEOVER!')
        print('the word was: ',w)

    
# running the game 
def gameplay():  
    play()

print(gameplay())

