import random
import tkinter

import getFiles


def song_guesses(guess, username, song, window, guesses=None):
    if guesses is None:
        guesses = [0]
    if guess.lower() == song.lower():
        window.delete('guessText')
        scores = getFiles.get_scores()
        if guesses[0] == 0:
            scores['Scores'][username] = 1000
            window.create_text(25, 150, text='Correct! You Win! Score: 1000', font=('TkDefaultFont', 10), anchor='w',
                               tag='winText')
        else:
            if username in scores['Scores']:
                window.create_text(25, 150, text='Correct! You Win! Score: 500', font=('TkDefaultFont', 10),
                                   anchor='w', tag='winText')
                pass
            else:
                scores['Scores'][username] = 500
                window.create_text(25, 150, text='Correct! You Win! Score: 500', font=('TkDefaultFont', 10), anchor='w',
                                   tag='winText')
        getFiles.write_scores(scores)
    elif guesses[0] == 1:
        window.delete('winText')
        window.delete('guessText')
        window.create_text(25, 150, text='Incorrect! Game Over!', font=('TkDefaultFont', 10), anchor='w')
    else:
        window.delete('winText')
        window.delete('guessText')
        guesses[0] += 1
        window.create_text(25, 150, text='Incorrect! Guess ' + str(guesses[0]) + ' Of 2!', font=('TkDefaultFont', 10),
                           anchor='w', tag='guessText')


def guess_song(username, screen_canvas, app_window):
    screen_canvas.delete('all')
    songs = getFiles.get_songs()
    chosen_song = list(songs['Songs'])[random.randint(0, len(list(
        songs['Songs'])) - 1)]  # Converts to list to find a random song as dicts
    # are not searchable by int (lists are)
    screen_canvas.create_text(25, 25, text='Guess the Song:', font=('TkDefaultFont', 10), anchor='w')
    screen_canvas.create_text(25, 50, text='Artist: ' + songs['Songs'][chosen_song]['artist'],
                              font=('TkDefaultFont', 10), anchor='w')
    screen_canvas.create_text(25, 75, text='Song: ' + chosen_song[0] + (len(chosen_song) - 1) * ' _',
                              font=('TkDefaultFont', 10), anchor='w')
    submit_field = tkinter.Entry(screen_canvas)
    screen_canvas.create_window(25, 100, window=submit_field, anchor='w', width=250)
    submit_button = tkinter.Button(screen_canvas, text='Submit Guess',
                                   command=lambda: song_guesses(submit_field.get(), username, chosen_song,
                                                                screen_canvas))
    screen_canvas.create_window(300, 100, window=submit_button, anchor='w')
    submit_field.bind('<Return>', lambda x: song_guesses(submit_field.get(), username, chosen_song, screen_canvas))
    back_button = tkinter.Button(screen_canvas, text="Back", command=lambda: return_to_menu(username, app_window))
    screen_canvas.create_window(25, 200, window=back_button, anchor='w')


def show_songs(screen_canvas, username, app_window):
    screen_canvas.delete('all')
    songs = getFiles.get_songs()
    screen_canvas.create_text(25, 20, text='Song', font=('TkDefaultFont', 12), anchor='w')
    screen_canvas.create_text(200, 20, text='Artist', font=('TkDefaultFont', 12), anchor='w')
    screen_canvas.create_text(300, 20, text='Album', font=('TkDefaultFont', 12), anchor='w')
    for i in range(len(songs['Songs'])):
        screen_canvas.create_text(25, (i * 25) + 50, text=list(songs['Songs'])[i], anchor='w')
        screen_canvas.create_text(200, (i * 25) + 50, text=songs['Songs'][list(songs['Songs'])[i]]['artist'],
                                  anchor='w')  # It looks horrible but it works, ok?
        screen_canvas.create_text(300, (i * 25) + 50, text=songs['Songs'][list(songs['Songs'])[i]]['album'], anchor='w')
    back_button = tkinter.Button(screen_canvas, text="Back", command=lambda: return_to_menu(username, app_window))
    screen_canvas.create_window(25, (i * 25) + 100, window=back_button, anchor='w')


def show_high_scores(screen_canvas, username, app_window):
    screen_canvas.delete('all')
    scores = getFiles.get_scores()
    screen_canvas.create_text(25, 20, text='User', font=('TkDefaultFont', 12), anchor='w')
    screen_canvas.create_text(100, 20, text='Score', font=('TkDefaultFont', 12), anchor='w')
    for i in range(len(scores['Scores'])):

        if scores['Scores'][list(scores['Scores'])[i]] == 1000:
            screen_canvas.create_text(25, (i * 25) + 50, text=list(scores['Scores'])[i], anchor='w')
            screen_canvas.create_text(100, (i * 25) + 50, text=scores['Scores'][list(scores['Scores'])[i]], anchor='w')
    back_button = tkinter.Button(screen_canvas, text="Back", command=lambda: return_to_menu(username, app_window))
    screen_canvas.create_window(25, (i * 25) + 100, window=back_button, anchor='w')


def menu(username):
    app_window = tkinter.Tk()
    screen_canvas = tkinter.Canvas(app_window, width=1700, height=900, bd=0, highlightthickness=0, relief='ridge')
    screen_canvas.pack()
    app_window.title('MusicGame')
    screen_canvas.create_text(25, 25, text='Select Your Option', font=('TkDefaultFont', 12), anchor='w')
    show_song_button = tkinter.Button(screen_canvas, text='Show Songs', command=lambda: show_songs(screen_canvas,
                                                                                                   username,
                                                                                                   app_window))
    screen_canvas.create_window(25, 50, window=show_song_button, anchor='w')
    guess_song_button = tkinter.Button(screen_canvas, text='Guess Songs',
                                       command=lambda: guess_song(username, screen_canvas, app_window))
    screen_canvas.create_window(120, 50, window=guess_song_button, anchor='w')
    high_score_button = tkinter.Button(screen_canvas, text='Show Highscores',
                                       command=lambda: show_high_scores(screen_canvas, username, app_window))
    screen_canvas.create_window(200, 50, window=high_score_button, anchor='w')

    app_window.mainloop()


def return_to_menu(username, app_window):
    app_window.destroy()
    menu(username)
