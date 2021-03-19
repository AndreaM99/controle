from .main import Note

note = Note('xx','yy','zzz')
print(note)

def test_ajout():
  Note.vider()
  # assert
  Note(eleve = 'eleve1', matiere='math', valeur = 12)
  # assert