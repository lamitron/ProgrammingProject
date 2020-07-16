import tkinter


def main(login, signup):
    home_window = tkinter.Tk()
    screen_canvas = tkinter.Canvas(home_window, width=600, height=400, bd=0, highlightthickness=0, relief='ridge')
    screen_canvas.pack()

    home_window.title('Please login to MusicGame')

    button_signup = tkinter.Button(screen_canvas, text='Sign Up', command=lambda: signup())
    screen_canvas.create_window(300, 325, window=button_signup)

    button_login = tkinter.Button(screen_canvas, text='Log In', command=lambda: login(home_window))
    screen_canvas.create_window(300, 365, window=button_login)

    home_window.mainloop()
