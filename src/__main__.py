import tkinter as tk
import src.getUser


users = {"lamitron": {"highscore": 15000}, "NullPtr": {"highscore": 24360}}

src.getUser.makeJSON(users)
