## controller.py
# Controller File

controller = {
    "up": False,
    "down": False,
    "left": False,
    "right": False
}

# DEFINE FUNCTIONS
def on_press(key):
    if key == keyboard.Key.up:
        controller["up"]= True
        
    if key == keyboard.Key.down:
        controller["down"]= True

    if key == keyboard.Key.right:
        controller["right"]= True

    if key == keyboard.Key.left:
        controller["left"]= True

def on_release(key):
    if key == keyboard.Key.up:
        controller["up"]= False
        
    if key == keyboard.Key.down:
        controller["down"]= False

    if key == keyboard.Key.right:
        controller["right"]= False

    if key == keyboard.Key.left:
        controller["left"]= False

def init():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    )
    listener.start()
