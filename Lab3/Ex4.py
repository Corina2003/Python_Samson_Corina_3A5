#Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start position (integer). The function will return the song composed by going though the musical notes beginning with the start position and following the moves given as parameter.
def compose(notes, moves, start_position):
    song = [None] * (len(moves) + 1)
    position = start_position
    song[0] = notes[position]

    for i in range(len(moves)):
        position = (position + moves[i]) % len(notes)
        song[i + 1] = notes[position]

    return song

musical_notes = ["do", "re", "mi", "fa", "sol"]
song_moves = [1, -3, 4, 2]
start_position = 2
result = compose(musical_notes, song_moves, start_position)
print(result)
