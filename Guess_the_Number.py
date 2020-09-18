from tkinter import*
import random
#import simplegui
import math

num_range=100
secret_number=0
count=0

# helper function to start and restart the game

def new_game():
    global secret_number,num_range,count
    secret_number=random.randrange(0,num_range)
    #print (secret_number)
    count=int(math.ceil(math.log((num_range-0)+1,2)))
    print('New Game.Range is from 0 to',num_range)
    print('Number of remaining guesses is',count)
    
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range=100
    new_game()
    
    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range=1000
    new_game()
    
    

   
def input_guess(guess):
    # main game logic goes here


    l1=Label(root,text=e.get())
    l1.pack()
    guess=float(guess)
    print('')
    print ('Guess was',guess)
    global secret_number,count,num_py
    count-=1
    print ('Number of remaining guesses is',count)
    if count>0:
        if guess>secret_number:
            print('Lower')
        elif guess<secret_number:
            print('Higher')
        elif guess==secret_number:
            print('Correct')
            print('')
            new_game()
     
    elif guess==secret_number:
        print('Correct')
        print('')
        new_game()
    else:
        print('You are out of guesses.The number was',secret_number)
        print('')
        new_game()
     
#create frame
root=Tk()
root.title('Guess the Number')
l=Label(root,text='Guess the Number').pack()
e=Entry(root)
e.pack()
b1=Button(root,text='Enter your Guess',command=lambda:input_guess(e.get()))
b1.pack()
b2=Button(root,text='Range is from O to 100',command=range100)
b2.pack()
b3=Button(root,text='Range is from O to 1000',command=range1000)
b3.pack()

root.mainloop()
