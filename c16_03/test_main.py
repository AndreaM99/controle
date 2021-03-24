from .main import Note

note = Note('xx','yy','zzz')
print(note)

def test_ajout():
  Note.vider()
  assert len(Note.instances) == 0
  Note(eleve = 'eleve1', matiere='math', valeur = 12) # quand on commence des mots clés, on les continu !! + Note pas Node.
  assert len(Note.instances) == 1
  Note.moyenne()
  Note.moyennebis()


# pip install pytest-cov
# pytest --cov .abs
# toute la couverture de code car tout le fichier est parcouru.