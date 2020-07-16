import tkinter

import getFiles


def signup():
    signup_window = tkinter.Tk()

    signup_canvas = tkinter.Canvas(signup_window, width=400, height=150, bd=0, highlightthickness=0, relief='ridge')
    signup_canvas.pack()

    signup_window.title('Sign Up for MusicGame')

    label_email = tkinter.Label(signup_canvas, text='Email:')
    signup_canvas.create_window(60, 12, window=label_email)

    label_username = tkinter.Label(signup_canvas, text='Username:')
    signup_canvas.create_window(60, 33, window=label_username)

    label_password = tkinter.Label(signup_canvas, text='Password:')
    signup_canvas.create_window(60, 54, window=label_password)

    label_reenter_password = tkinter.Label(signup_canvas, text='Confirm Password:')
    signup_canvas.create_window(60, 75, window=label_reenter_password)

    entry_email = tkinter.Entry(signup_canvas, width=40)
    signup_canvas.create_window(260, 12, window=entry_email)

    entry_username = tkinter.Entry(signup_canvas, width=40)
    signup_canvas.create_window(260, 33, window=entry_username)

    entry_password = tkinter.Entry(signup_canvas, show='•', width=40)
    signup_canvas.create_window(260, 54, window=entry_password)

    entry_reenter_password = tkinter.Entry(signup_canvas, show='•', width=40)
    signup_canvas.create_window(260, 75, window=entry_reenter_password)

    button_signup = tkinter.Button(signup_canvas, text='Sign Up', command=lambda: signupcode(entry_email.get(), entry_username.get(), entry_password.get(),  entry_reenter_password.get(), signup_window))

    signup_canvas.create_window(200, 110, window=button_signup)

    entry_reenter_password.bind('<Return>', lambda x: signupcode(entry_email.get(), entry_username.get(), entry_password.get(), entry_reenter_password.get(), signup_window))


def signupcode(email, username, password, confirmpassword, window):
    if password == confirmpassword:
        users = getFiles.getuserfile()
        new_user_dict = {'email': email, 'password':  password}
        users['Users'][username] = new_user_dict
        getFiles.makeuserfile(users)

        window.destroy()
    else:
        tkinter.Label(window, text='Please ensure your passwords match.').pack()
