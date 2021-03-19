# pour exectuer on fait python main.py

note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

print("-- Question 4 a) --")
notes_elv1 = [note for note in notes if note[0] == 'eleve1']
print(notes_elv1)
print(sum(note[2] for note in notes_elv1)/len(notes_elv1))

print("-- Question 4 b) --")
notes_elv1_maths = [n for n in notes_elv1 if n[1] == 'math']
print(notes_elv1_maths)
print(sum(n[2] for n in notes_elv1_maths)/len(notes_elv1_maths))

