"""
Music. Giorno's Theme (Il vento di oro)
Name: Ana Karen López Baltazar - A01707750
Date: 17/09/2021
"""

from music21 import note, stream

# Notas de la canción
Giorno1 = ['F#', 'D', 'D', 'E', 'F', 'E', 'D', 'C#', 'D', 'E']
Giorno2 = ['F#', 'F#', 'B', 'C#', 'D', 'E', 'D', 'C#', 'A', 'G']
Giorno3 = ['F#', 'F#', 'B', 'B', 'C#', 'D', 'G', 'F#', 'F', 'A#']
Giorno4 = ['F#', 'F#', 'B', 'B', 'C#', 'D', 'E', 'D', 'F#']

st = stream.Stream()

# Ciclo for para la repetición de notas
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

# Descarga del archivo mid
st.write('midi', fp="Ej3.mid")
# files.download("Ej3.mid")
