from music21 import note, stream

Giorno1 = ['F#','D','D','E','F','E','D','C#','D','E']
Giorno2 = ['F#','F#','B','C#','D','E','D','C#','A','G']
Giorno3 = ['F#','F#','B','B','C#','D','G','F#','F','A#']
Giorno4 = ['F#','F#','B','B','C#','D','E','D','F#']

st = stream.Stream()
for i in range(10):
    G = Giorno1[i]
    N = note.Note(G)
    N.duration.quarterLength = 1
    st.append(N)
    
for i in range(10):
    G = Giorno2[i]
    N = note.Note(G)
    N.duration.quarterLength = 1
    st.append(N)

for i in range(10):
    G = Giorno1[i]
    N = note.Note(G)
    N.duration.quarterLength = 1
    st.append(N)

for i in range(10):
    G = Giorno3[i]
    N = note.Note(G)
    N.duration.quarterLength = 1
    st.append(N)

for i in range(10):
    G = Giorno1[i]
    N = note.Note(G)
    N.duration.quarterLength = 1
    st.append(N)

for i in range(9):
    G = Giorno4[i]
    N = note.Note(G)
    N.duration.quarterLength = 1
    st.append(N)

st.write('midi', fp="Ej3.mid")
files.download("Ej3.mid")