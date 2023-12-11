from pynput import keyboard
from tkinter import *

# custom modules
import model
import controller

SWIDTH = 500
SHEIGHT = 400

frame = Tk()

canvas = Canvas(frame, width=SWIDTH, height=SHEIGHT, background="white")

def init():
    controller.init()

def render():
    x_string="x:"+str(model.world["x"])
    y_string="y:"+str(model.world["y"])
    canvas.delete("all")
    canvas.create_text(200, 200, text=x_string)
    canvas.create_text(200, 300, text=y_string)
    canvas.pack()
    canvas.create_rectangle(
        (model.world["x"]) - 50,
        (model.world["y"]),
        (model.world["x"]) + 50,
        (model.world["y"]) + 50,
        fill='pink'
    )
    
def process_input():
    if controller.controller["up"]:
       model.world ["y"] -= 25
    if controller.controller["down"]:
       model.world ["y"] += 25
    if controller.controller["left"]:
       model.world ["x"] -= 25
    if controller.controller ["right"]:
        model.world ["x"] += 25

def physics():
    return

def play():
    render()
    process_input()
    physics()
    frame.after(1000, play)
    print (model.world)
    print (controller.controller)


init()
frame.after(1000, play)
frame.mainloop()
print("after mainloop")
    
