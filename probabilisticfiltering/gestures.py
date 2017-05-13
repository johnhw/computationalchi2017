from Tkinter import *
import numpy as np
import json

class GestureData(object):
    def __init__(self, jsonfile):
        with open(jsonfile, "r") as f:
            gestures_json = json.load(f)
        self.screen_size = max(gestures_json["width"], gestures_json["height"])
        self.gestures = [np.array(path) for path in gestures_json["gestures"]]
        self.n_gestures = len(self.gestures)
        
    def get_template(self, i, t):
        if 0<i<self.n_gestures:
            gesture = self.n_gestures[i]
            t = np.floor(np.clip(gesture,0,len(gesture)-1))
            x, y = gesture[t]
            return [x,y,1]
        
    def get_speed(self):
        return 1

class Gesture(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.master = Tk()
        self.master.call('wm', 'attributes', '.', '-topmost', True)
        self.w = Canvas(self.master, width=300, height=300)
        self.w.pack()
        self.gesture = None
        self.gestures = []
        self.w.bind('<Motion>', self.motion)
        self.w.bind('<Button-1>', self.click)        
        self.master.bind('<Escape>', self.exit)        
        
        self.ox, self.oy = None, None    
        
    def exit(self, event):
        if self.gesture is not None:
            self.click()
            
        with open("gestures.txt", "w") as f:
            f.write(self.json())
        print "%d gestures recorded to gestures.txt" % (len(self.gestures))
        self.master.destroy()
        
        
    def redraw(self):        
        w.move(line_id, 0, 1)    
        master.after(50, redraw)
        
    def click(self, event):
        if self.gesture is None:
            self.gesture = []
        else:
            self.gestures.append(self.gesture)
            self.gesture = None
            self.w.delete("all")
    
    def motion(self,event):
        if self.gesture is not None:
            x, y = event.x, self.height - event.y
            self.gesture.append([x,y])
            self.w.create_line(self.ox, self.oy, x,y)
        self.ox, self.oy = x,y
        
    def json(self):
        return json.dumps({"width":self.width, "height":self.height, "gestures":self.gestures})

def record_gestures():
    gesture = Gesture(400,400)
    
    
        
    
