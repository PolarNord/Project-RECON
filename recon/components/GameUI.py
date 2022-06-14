from engine import *
from random import randint

class GameUI(UIComponent):
    def eventSetup(self, node):
        """Debug menu canvas
        * contains some useful monitors.
        """
        debug = self.addCanvas("debug", enabled=False, eventUpdate=self.updateDebug)
        debug.addTextLabel("fps", color=(240, 240, 240, 140), size=18)
        debug.addTextLabel("mouse_pos", color=(240, 240, 240, 140), size=18, pos=Vector2(0, 15))
        debug.addRect("bg", size=Vector2(235, 36), color=(0, 0, 0, 50))

        """Testing canvas"""
        assets.loadTexture("square", "recon/resources/square.png")
        test = self.addCanvas("test")
        test.addTexture(
            "texture", pos=Vector2(GetScreenWidth()/2, GetScreenHeight()/2),
            texture="square"
        )
        self.temp = False
        test.addCheckbox("checkbox", curve=0.15)
        
    def eventUpdate(self, node):
        self.toggleDebug()
        self.getCanvas("test").getElement("texture").rotation += 1
        print(self.getCanvas("test").getElement("checkbox").value)

    # Debug menu methods
    def toggleDebug(self):
        if not IsKeyPressed(KEY_F3):
            return
        debug = self.getCanvas("debug")
        debug.enabled = not debug.enabled

    def updateDebug(self, canvas):
        # Framerate
        fpsMonitor = canvas.getElement("fps")
        fpsMonitor.text = f"fps: {GetFPS()}"
        # Mouse Position
        mousePos = canvas.getElement("mouse_pos")
        mousePos.text = f"mouse x: {GetMouseX()} y: {GetMouseY()}"
