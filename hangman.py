import random
def hangman():
    list_of_words=["computer","Hangman","Bluesky","PinkA"]
    word=random.choice(list_of_words)
    turns=10
    guessemade=' '
    valid_entery=set("abcdefghijklmnopqrstuvwxyz")
    while len(word)>0:
        main_word=' '
        missed =0   
        for letter in word:
            if letter in guessemade:
                main_word+=letter
            else:
                main_word+="_ "
        if main_word==word:
            print(main_word)
            print("You won!!!")
            break
        print("guess the word",main_word)
        guess= input()
        if guess in valid_entery:
            guessemade+=guess
        else:
            print("enter the valid character")
            guess=input()
        if guess not in word:
            turns-=1

            if turns==9:
                print("9 turns left!!!")
                print(".........................")
            if turns==8:
                print("8 turns left!!!")
                print(".........................")
                print("            o            ")
            if turns==7:
                print("7 turns left!!!")
                print(".........................")
                print("            o            ")
                print("            |            ")
            if turns==6:
                print("6 turns left!!!")
                print(".........................")
                print("            o            ")
                print("            |            ")
                print("           /             ")
            if turns==5:
                print("5 turns left!!!")
                print(".........................")
                print("            o            ")
                print("            |            ")
                print("           / \           ")
            if turns==4:
                print("4 turns left!!!")
                print(".........................")
                print("           \o            ")
                print("            |            ")
                print("           / \           ")
            if turns==3:
                print("3 turns left!!!")
                print(".........................")
                print("           \o/            ")
                print("            |           ")
                print("           / \           ")
            if turns ==2:
                print("2 turns left!!!")
                print(".........................")
                print("           \o/  |          ")
                print("            |           ")
                print("           / \           ")
            if turns ==1:
                print("only 1 turns left!! hangman on his last breath")
                print(".........................")
                print("           \o/__|          ")
                print("            |           ")
                print("           / \           ")
            if turns==0:
                print("You loose")
                print("You let a good mab die")
name=input("ENTER YOUR NAME->")
print("welcome",name,"!")
print("....................")
print("Try to guess the word in lessthan 10 atempts")
hangman()