from tkinter import *
import random

def movecar(event):    #Keypress and move the car
    print(event)
    global disable_a
    global disable_d
    global disable_j
    global disable_l
    if event.char == 'a':
        if disable_a is False:
            canvas.move(image1, -170, 0)
            disable_a = True
            disable_d = False
    elif event.char == 'd':
        if disable_d is False:
            canvas.move(image1, 170, 0)
            disable_a = False
            disable_d = True
    elif event.char == 'j':
        if disable_j is False:
            canvas.move(image2, -170, 0)
            disable_l = False
            disable_j = True
    elif event.char == 'l':
        if disable_l is False:
            canvas.move(image2, 170, 0)
            disable_l = True
            disable_j = False

def obstacle():
    obstacle = canvas.create_rectangle(70, 20, 90, 50)
    obstacleX = random.randint(0)




window = Tk() #create window
window.title("2 cars")
window.configure(background='black') #full black background when we stretch the window
# photo1 = PhotoImage(file = "road.png")

canvas = Canvas(window, width = 700, height = 700, bg= 'gray')
canvas.pack()

img = PhotoImage(file = "carplayer.png")
img2 = PhotoImage(file = "carplayer2.png")
image1 = canvas.create_image(60, 520, anchor=NW, image=img)
image2 = canvas.create_image(410, 520, anchor=NW, image=img2)
# Label(window, image = photo1, bg= 'Black').grid(row = 0, column = 0, sticky = W) #bg=Black is for the border, stick to the left hand-side

#Yellow line Left
line = canvas.create_rectangle(178, 10, 188, 100, fill='white')
line = canvas.create_rectangle(178, 130, 188, 220, fill='white')
line = canvas.create_rectangle(178, 250, 188, 340, fill='white')
line = canvas.create_rectangle(178, 370, 188, 460, fill='white')
line = canvas.create_rectangle(178, 490, 188, 580, fill='white')
line = canvas.create_rectangle(178, 610, 188, 670, fill='white')

#Yellow line Right
line = canvas.create_rectangle(528, 10, 538, 100, fill='white')
line = canvas.create_rectangle(528, 130, 538, 220, fill='white')
line = canvas.create_rectangle(528, 250, 538, 340, fill='white')
line = canvas.create_rectangle(528, 370, 538, 460, fill='white')
line = canvas.create_rectangle(528, 490, 538, 580, fill='white')
line = canvas.create_rectangle(528, 610, 538, 670, fill='white')

#middle line
line = canvas.create_rectangle(338, 0, 348, 700, fill='white')
line = canvas.create_rectangle(352, 0, 362, 700, fill='white')

#Restrict the moving of the keys, can't accross to another road
disable_a = True
disable_d = False
disable_j = True
disable_l = False
window.bind("<Key>", movecar)

#Score
score=0
txt = "Score:" + str(score)
scoreText = canvas.create_text( 650 , 18 , fill="white" , font="Times 20 italic bold", text=txt)
canvas.itemconfig(scoreText, text = txt)

window.mainloop()