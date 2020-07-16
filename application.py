import tkinter
import getFiles
import random


def guess_song(guess, song, window, guesses=[0]):
    if guess.lower() == song.lower():
        window.delete('guessText')
        window.create_text(25, 150, text='Correct! You Win!', font=('TkDefaultFont', 10), anchor='w')
    elif guesses[0] == 1:
        window.delete('guessText')
        window.create_text(25, 150, text='Incorrect! Game Over!', font=('TkDefaultFont', 10), anchor='w')
    else:
        window.delete('guessText')
        guesses[0] += 1
        print(guesses)
        window.create_text(25, 150, text='Incorrect! Guess ' + str(guesses[0]) + ' Of 2!', font=('TkDefaultFont', 10), anchor='w', tag='guessText')


def application(username):
    app_window = tkinter.Tk()
    screen_canvas = tkinter.Canvas(app_window, width=1700, height=900, bd=0, highlightthickness=0, relief='ridge')
    screen_canvas.pack()
    app_window.title('MusicGame')

    songs = getFiles.getsongs()
    chosen_song = list(songs['Songs'])[random.randint(0, len(list(songs['Songs']))-1)]  # Converts to list to find a random song as dicts are not searchable by int (lists are)
    screen_canvas.create_text(25, 25, text='Guess the Song:', font=('TkDefaultFont', 10), anchor='w')
    screen_canvas.create_text(25, 50, text='Artist: ' + songs['Songs'][chosen_song]['artist'], font=('TkDefaultFont', 10), anchor='w')
    screen_canvas.create_text(25, 75, text='Song: ' + chosen_song[0] + (len(chosen_song)-1)*' _', font=('TkDefaultFont', 10), anchor='w')
    submit_field = tkinter.Entry(screen_canvas)
    screen_canvas.create_window(25, 100, window=submit_field, anchor='w', width=250)
    submit_button = tkinter.Button(screen_canvas, text='Submit Guess', command=lambda: guess_song(submit_field.get(), chosen_song, screen_canvas))
    screen_canvas.create_window(300, 100, window=submit_button, anchor='w')
    submit_field.bind('<Return>', lambda x: guess_song(submit_field.get(), chosen_song, screen_canvas))

    app_window.mainloop()
