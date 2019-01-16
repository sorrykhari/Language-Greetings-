
#Language Program
#by Keary Mobley

import pygame
from graphics import *
#=====================================

    
#-------------------------------------
def LanGreet(a):
    if a == 'ENGL':
        b = "Hello"
        c = 'hello.wav'
        return b,c
    elif a == 'SPAN':
        b = "Hola"
        c = 'hola.wav'
        return b,c
        
    elif a == 'RUSS':
        b = "Привет! (Privet!)"
        c = 'privet.wav'
        return b,c
    elif a == 'ARAB':
        b = "السلام عليكم (as-salām 'alaykum)"
        c = 'assalam alaykum.wav'
        return b,c
    elif a == 'KORE':
        b = "안녕하세요 (Annyeonghaseyo)"
        c = 'annyoung.wav'
        return b,c
    elif a == 'JAPA':
        b = "今日は (Konnichiwa)"
        c = 'konnichiwa.wav'
        return b,c
    elif a == 'CHIN':
        b = "你好 (Ni Hao)"
        c = 'nihao.wav'
        return b,c
    else:
        print("Either the spelling is incorrect")
        print("Or the language is not supported at this time.")
        

#-------------------------------------
def PrintIntro():
    p1 = print("This is program displays hello in many different languages.")
    p2 = print("Also provided is an audio clip to help with pronunciation.")
    p3 = print("Languages can be accessed by inputing the correct abbreviations")
    p4 = print("The correct abbreviation is the first four letters of the language.")
    p5 = print("For example Russian would be  RUSS.")
    return p1,p2,p3,p4,p5
    
#-------------------------------------
def main():
    PrintIntro()
    
    win = GraphWin("Language Greetings", 800, 600)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    
    # Draw the interface
    Text(Point(1,3), "   Language:").draw(win)
    Text(Point(1,1), "Hello:").draw(win)
    input1 = Entry(Point(2,3), 5)
    input1.setText("LANG")
    input1.draw(win)
    output = Text(Point(2,1),"")
    output.draw(win)
    button = Text(Point(1.5,2.0),"Translate")
    button.draw(win)
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)
    

    # wait for a mouse click
    win.getMouse()

    # evaluate user input
    uinput = input1.getText()
    txtfile, wavfile = LanGreet(uinput)
    

    # display output and change button
    output.setText(txtfile)
    winsound.PlaySound(wavfile,winsound.SND_FILENAME)
    button.setText("Quit")

    # wait for click and then quit
    win.getMouse()
    win.close()
    
    

main()
