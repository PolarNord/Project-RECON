import engine
from raylib import *
from os.path import join
from json import load
from importlib import import_module

class GameLoader:
    def loadGame(directory):
        with open(join(directory, "config.json")) as conf_file:
            conf_data = load(conf_file)

            SetTargetFPS(60)
            SetConfigFlags(FLAG_WINDOW_RESIZABLE)
            InitWindow(conf_data["win_size"][0], conf_data["win_size"][1], conf_data["title"].encode())
            SetExitKey(0)
        
        engine.GAME_NAME = directory
        engine.gameComponents = import_module(f"{directory}.components")
    
    def runGame():
        while not WindowShouldClose():
            engine.tree.engineUpdate()
            BeginDrawing()
            ClearBackground((16, 49, 120))
            EndDrawing()
        
        CloseWindow()
