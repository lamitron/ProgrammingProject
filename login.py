import tkinter
import getFiles
import application


def login(root):
    login_window = tkinter.Toplevel(root)

    login_canvas = tkinter.Canvas(login_window, width=300, height=100, bd=0, highlightthickness=0, relief='ridge')
    login_canvas.pack()

    login_window.title('Please Login to MusicGame')

    label_username = tkinter.Label(login_canvas, text='Username:')
    login_canvas.create_window(40, 12, window=label_username)

    label_password = tkinter.Label(login_canvas, text='Password:')
    login_canvas.create_window(40, 33, window=label_password)

    username = tkinter.Entry(login_canvas)
    login_canvas.create_window(190, 12, window=username, width=200)

    password = tkinter.Entry(login_canvas, show='•')
    login_canvas.create_window(190, 33, window=password, width=200)

    login_button = tkinter.Button(login_canvas, text='Login', command=lambda: loginproc(username.get(), password.get(), login_window, root))
    login_canvas.create_window(150, 60, window=login_button)

    password.bind('<Return>', lambda x: loginproc(username.get(), password.get(), login_window, root))

    login_window.mainloop()


def loginproc(username, password, window, root):
    users = getFiles.get_user_file()
    if username in users['Users']:
        if password == users['Users'][username]['password']:
            window.destroy()
            root.destroy()
            application.menu(username)
