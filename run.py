import numpy as np
import cv2

import winsound
import threading
import ctypes
import wave
import contextlib
import turtle
import random
import time

# Step 1: define the dictionary dict
d = dict()
with open("dictionary.txt",'r') as f:
        for line in f:
           (key, val) = line.split(',')
           d[key] = int(val)



#step 2: Define to following functions

#play music
def playSong(fileName):
    winsound.PlaySound(fileName, winsound.SND_FILENAME)

    
#display image - not used currently
def displayImage(fileName):
    img = cv2.imread(fileName)
    cv2.imshow("Kinect", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
            

#finds the emotional value of the paragraph by checking dictionary
def emotional_val( j, i) :
    c = 0
    val = 0
    with open("lyrics.txt", "r") as f:
        for line in f:
            c= c+1
            if c < j : continue
            else :
                line = line.split(" ")
                line_t = tuple(line)
                
                for key in line_t:

                    key = key.lower()
                    val = val + d.get(key,0)

            if c == i : break
    
    return val


#function to clear by quadrant using different styles
def clear_quad(quad):

    #set the X and Y co-ordinates based on the quadrant passed
    if(quad == 2):
        X = -150
        Y = 0

    elif(quad == 1):
        X = 150
        Y = 0

    elif( quad == 3):
        X = -150
        Y = -250

    elif(quad == 4):
        X = 150
        Y = -250
        
    pen.setpos(X,Y)
    pen.pensize(50)
    

    select = random.randint(1,3) #choose a way to clear randomly

    if select == 1: #circular clearing
        pen.pendown()
        pen.begin_fill()
        radius = 140
        pen.circle(radius)
        pen.end_fill()
        pen.penup()
        #pen.home()
    elif select == 2: #zig-zag clearing
        pen.pendown()
        pen.speed(10)
        pen.left(15)
        pen.forward(100)
        for i in range (1,6):
                  pen.left(165)
                  pen.forward(210)
                  pen.right(165)
                  pen.forward(210)
        pen.penup()
        #pen.home()
    
    elif select == 3: #rectangular clearing
        pen.pendown()
        pen.speed(5)
        pen.left(20)
        pen.begin_fill()
        pen.forward(120)
        pen.left(90)
        pen.forward(250)
        pen.left(90)
        pen.forward(250)
        pen.left(90)
        pen.forward(250)
        pen.left(90)
        pen.forward(130)
        pen.end_fill()
        pen.penup()
        #pen.home()
        


#function to draw happy pictures
def happy_sketches(quad):
    #randomly choose a picture
    select = random.randint(1,5)

    #clear the quandrant
    clear_quad(quad)
    
    #set quadrants X and Y values
    

    if quad == 1:
        X = 150
        Y = 200
    elif quad ==2:
        X = -150
        Y = 200
    elif quad == 3:
        X = -150
        Y = -100
    elif quad == 4:
        X = 150
        Y = -100
    pen.pensize(20)
    pen.speed(10)

    
    #Two hearts beside each other, diff colours
    if select == 1 :
        pen.color("red")
        Y -= 130
        pen.setpos(X,Y)
        pen.left(10)
        pen.pendown()
        pen.begin_fill()
        for i in range(1,10): #first half of heart
            pen.forward(15)
            pen.left(5)
        pen.circle(50,180)
        pen.right(140)
        pen.circle(50,180)
        for i in range(1,10): #second half of the heart
            pen.forward(15)
            pen.left(5)
        pen.end_fill()
        pen.penup()
        pen.home()
        pen.setpos(X,Y)
        pen.color("IndianRed2")
        pen.pendown()
        pen.begin_fill()
        pen.left(80)
        for i in range (1,10):
            pen.forward(15)
            pen.left(5)
        pen.circle(50,180)
        pen.right(140)
        pen.circle(50,180)
        for i in range(1,10):
            pen.forward(15)
            pen.left(5)
        pen.end_fill()
        pen.penup()
        pen.home()


    #Leaves different colors
    elif select == 2:
        X -=130
        Y -=50
        select = random.randint(1,2)
        if select == 1: pen.color("SeaGreen4")
        else : pen.color("LimeGreen")
        pen.setpos(X,Y)
        pen.pensize(10)
        pen.right(15)
        pen.pendown()
        pen.begin_fill()
        for i in range(1,15):
            pen.forward(20)
            pen.right(9)
            pen.forward(10)
            pen.backward(10)
            pen.left(16)
        pen.forward(10)
        pen.penup()
        pen.right(4)
        pen.setpos(X,Y)
        pen.pendown()
        for i in range(1,15):
            pen.forward(20)
            pen.left(9)
            pen.forward(10)
            pen.backward(10)
            pen.right(16)
        pen.forward(10)
        pen.end_fill()
        pen.penup()
        select = random.randint(1,2)
        if select == 1 : pen.color("OliveDrab3")
        if select == 2 : pen.color("ForestGreen")
        pen.setpos(X+40,Y-40)
        pen.pensize(10)
        pen.right(30)
        pen.pendown()
        pen.begin_fill()
        for i in range(1,15):
            pen.forward(20)
            pen.right(9)
            pen.forward(10)
            pen.backward(10)
            pen.left(16)
        pen.penup()
        pen.right(5)
        pen.setpos(X+40,Y-40)
        pen.pendown()
        for i in range(1,15):
            pen.forward(20)
            pen.left(9)
            pen.forward(10)
            pen.backward(10)
            pen.right(16)
        pen.forward(10)
        pen.end_fill()
        pen.penup()
        pen.home()       
        
    
    
    #Orange sun and a flying bird :)
    elif select ==3 :
        Y = Y-100
        pen.setpos(X,Y-20)
        
        pen.pendown()
        pen.color("Orange")
        pen.begin_fill()
        pen.circle(50)
        pen.end_fill()
        pen.penup()
        pen.home()
        pen.setpos(X,Y)
        pen.color("OrangeRed4")
        pen.pendown()
        for i in range(1,5):
            pen.left(90)
            for j in range(1,10-i):
                pen.left(15+2*i)
                pen.forward(20)
            pen.penup()
            pen.home()
            pen.setpos(X,Y)
            pen.pendown()
        for i in range(1,5):
            pen.left(90)
            for j in range(1,10-i):
                pen.left(15+2*i)
                pen.forward(20)
            pen.penup()
            pen.home()
            pen.setpos(X,Y)
            pen.pendown()
        
        for i in range(1,5):
            pen.left(90)
            for j in range(1,10-i):
                pen.right(15+2*i)
                pen.forward(20)
            pen.penup()
            pen.home()
            pen.setpos(X,Y)
            pen.pendown()
        pen.penup()
        pen.home()
            
    #Tulip
    elif select == 4 :
        Y = Y-70
        pen.setpos(X,Y)
        pen.left(50)
        select = random.randint(1,2)
        if select == 1 : pen.color("yellow2")
        else : pen.color("lightsalmon")
        pen.pendown()
        
        pen.begin_fill()
        pen.circle(100,90)
        pen.left(90)
        pen.circle(100,90)
        pen.end_fill()
        pen.penup()
        pen.left(50)
        pen.pendown()
        pen.begin_fill()
        pen.circle(100,90)
        pen.left(90)
        pen.circle(100,90)
        pen.end_fill()
        pen.penup()
        pen.left(70)
        pen.pendown()
        pen.begin_fill()
        pen.circle(100,90)
        pen.left(90)
        pen.circle(100,90)
        pen.end_fill()
        pen.penup()
        pen.color("OliveDrab4")
        pen.pendown()
        pen.circle(200, 50)
        pen.penup()
        pen.home()


    #spirals! :D    
    elif select == 5 :  #spirals! :D
       pen.color("darkseagreen")
       select = random.randint(1,4)
       if select == 1 : pen.color("lightsalmon")
       if select == 2 : pen.color("gold")
       if select == 3 : pen.color("slateblue")
       pen.setpos(X-10,Y-130)
       pen.pendown()      
       for i in range (1,16):
           pen.circle(90-5*i,70)
           pen.right(20)       
       pen.penup()
       pen.home()
        
         
        
    #tree with red, blue, orange flowers
    #side view of a girl
    #beer 



#function to draw sad pictures
def sad_sketches(quad):

    #clear the quadrant and select picture

    select = random.randint(1,5)

    clear_quad(quad)

    #set quadrants X and Y values    
    if quad == 1:
        X = 150
        Y = 200
    elif quad ==2:
        X = -150
        Y = 200
    elif quad == 3:
        X = -150
        Y = -100
    elif quad == 4:
        X = 150
        Y = -100
    pen.pensize(20)
    pen.speed(10)

    
    #clouds clouding the sun
    if select ==1 :
       Y = Y-100
       pen.setpos(X,Y)
       pen.color("Orange")
       pen.pendown()
       pen.begin_fill()
       pen.circle(50)
       pen.end_fill()
       pen.penup() #end of sun

       pen.color("darkgrey")
       pen.setpos(X-30,Y-50)
       pen.pendown()
       pen.begin_fill()
       for i in range (1,12):
           pen.circle(60,80-i*i)
           pen.right(20)
       pen.end_fill()
       pen.penup()
       pen.home()


    #sad eye
    elif select == 2 :
        Y = Y - 50
        X = X - 30
        pen.home()
        pen.setpos(X-30,Y)
        pen.color("black")
        pen.right(45)
        pen.pensize(10)
        pen.pendown()
        for i in range (1,10): #lower eye
            pen.left(10)
            pen.forward(20)
        pen.penup()
        pen.home()
        pen.setpos(X-30,Y)
        pen.left(50)
        pen.pensize(20)
        pen.pendown()
        for i in range(1,10): #upper eye
            pen.right(8)
            pen.forward(22)
        pen.penup()
        pen.home()
        pen.setpos(X+25,Y+10)
        pen.right(90)
        pen.pendown()
        pen.circle(23,360) #eye ball
        pen.penup()
        pen.home()
        pen.setpos(X-35,Y-30)
        pen.pensize(5)
        pen.begin_fill() #tear drop
        pen.pendown()
        pen.right(110)
        pen.forward(15)
        pen.circle(10,250)
        pen.forward(10)
        pen.end_fill()
        pen.penup()
        pen.home()
        

        #broken heart
    elif select == 3 :
        pen.color("red")
        Y -= 130
        pen.setpos(X,Y)
        pen.left(10)
        pen.pendown()
        pen.begin_fill()
        for i in range(1,10): #first half of heart
            pen.forward(15)
            pen.left(5)
        pen.circle(50,180)
        (x,y) = pen.position()
        pen.left(50)
        pen.forward(40)
        pen.left(90)
        pen.backward(20)
        pen.setpos(X,Y)
        pen.penup()
        pen.setpos(x-50,y+30)
        pen.pendown()
        pen.left(80)  #second half of the heart
        pen.circle(50,180)
        for i in range(1,10): 
            pen.forward(15)
            pen.left(5)
        pen.right(60)
        pen.backward(100)
        pen.left(70)
        pen.forward(25)
        pen.setpos(x-50,y+30)

        pen.end_fill()
        pen.penup()
        pen.home()

    #flower thats hanging face down,pale colored closed with withering leaves(brown)

    elif select == 4 :
        pen.setpos(X,Y)
        pen.left(50)
        select = random.randint(1,2)
        if select == 1 : pen.color("yellow2")
        else : pen.color("lightsalmon")
        pen.pendown()
        
        pen.begin_fill()#flower
        pen.right(120)
        pen.circle(100,90)
        pen.left(90)
        pen.circle(100,90)
        pen.end_fill()
        pen.penup()
        pen.left(50)
        pen.pendown()
        pen.begin_fill()
        pen.circle(100,90)
        pen.left(90)
        pen.circle(100,90)
        pen.end_fill()
        pen.penup()
        pen.left(70)
        pen.pendown()
        pen.begin_fill()
        pen.circle(100,90)
        pen.left(90)
        pen.circle(100,90)
        pen.end_fill()
        pen.penup()
        pen.color("OliveDrab4") #stem
        pen.pendown()
        pen.circle(70, 50)
        pen.left(40)
        pen.circle(200,50)
        pen.penup()
        pen.home()


    #Dried up tree
    elif select == 5 :
       Y -= 150
       pen.setpos(X,Y)
       pen.left(75)
       pen.color("sienna")
       for i in range (1,4): #mid trunk
          pen.pensize(40-4*i)
          (x,y) = pen.position()
          pen.pendown()
          pen.forward(50)
          h = pen.heading()
          pen.right(70)
          pen.pensize(20)
          for j in range(1,4): #right branch
              pen.forward(20-2*i)
              pen.left(10)
          pen.penup()
          pen.home()
          pen.setpos(x,y)
          pen.left(h)
          pen.pendown()
          pen.forward(50)
          pen.left(70)
          (x,y) = pen.position()
          #pen.pendown()
          for j in range(1,4): #left branch
              pen.forward(20-3*i)
              pen.right(10)
          pen.penup()
          pen.home()
          pen.setpos(x,y)
          pen.left(h)
          pen.right(2)
          pen.pendown()
          pen.forward(5)
          pen.penup()

       pen.pendown()
       pen.forward(20)
       pen.penup()
       pen.home()
       
    

        
#function to draw as per mood
def draw(mood_val):
    
    k = 0
    timeout = time.time() + time_slice - 6   # execute for time_slice seconds from now
    while time.time() < timeout :
        k = (k+1)
        if k == 5 : k = 1
        pen.color("LemonChiffon1")
        bg_color = random.randint(1,4)
        if bg_color == 2 : pen.color("PowderBlue")
        if bg_color == 3 : pen.color("khaki")
        if bg_color == 4 : pen.color("Thistle")
        
        if mood_val > 1 :
           happy_sketches(k)
        elif mood_val < -1 :
           sad_sketches(k)
        else :
            if k%2 == 1 :
                happy_sketches(k)
            else:
                sad_sketches(k)



#multithreaded class Song to play song in separate thread
class Song (threading.Thread):
    def __init__(self, threadID, fileName):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.file = fileName
        
    def run(self):
        print "Starting Song "
        playSong(self.file)

#Not used multithreaded class Video2 to display sequence of images in separate thread
class Video2 (threading.Thread):
    def _init_(self,threadID, fileName):
        threading.Thread._init_(self)
        self.threadID = threadID
        self.file = fileName

    def run(self):
        print "starting Video "
        displayCollage(self.file)


#step 3: find the play time of the song
duration = 0
fname = 'sound.wav'
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    

#step 4: find number of paragraphs in the song
num = sum(1 for line in open('lyrics.txt','r'))
num_lines = sum(1 for line in open('lyrics.txt','r') if line.rstrip())
para_count = num - num_lines

time_slice = duration / para_count

#step 5: Play the song in a parallel thread
# Create new thread to run the song
thread1 = Song(1,"sound.wav")
# Start the song
thread1.start()

#step 6: set up the canvas to draw in
wn = turtle.Screen()
wn.bgcolor("aquamarine3")
pen = turtle.Pen()#by default in the center of the screen 0,0
pen.hideturtle()
pen.penup()


#step 7: for every paragraph in the text, find mood and draw

f = open('lyrics.txt','r')
i =1
j =1

for line in open('lyrics.txt', 'r'):
    
    if line =='\n' :
        val = emotional_val(j,i-1)
        print val #see the screen for the values being displayed
        draw(val)
        j = i+1        
    i = i+1
val = emotional_val(j,i-1) #final paragraph won't be covered in the loop, so out here
draw(val)
                     





#Let the drawing begin!

print "Exiting main thread"







