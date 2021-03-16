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

# Question 4 a)
from statistics import mean
x = (13,13,15,12,13,12)
print("Moyenne est ",mean(x))

notes_elv1 = [note for note in notes if note[0] == 'eleve1']

# Question 4 b)
y = (13,13,12)
print("Moyenne en maths est ",round(mean(y),2))

# Question 4 c)
def moyenne_tuplestest(notes,eleve,matiere):
  s = 0
  i = 0
  for x in notes:
    if x[0] == eleve and x[1]== matiere:
      s = s + x[2]
      i = i + 1
      print(i)
  moy = s / i
  return round(moy,2)

print(moyenne_tuplestest(notes,'eleve1','math'))

def moyenne_tuples (liste_note,eleve = None,matiere = None):
  if matiere != None :
    notes = [ liste_note[i][2] for i in range(len(liste_note)) if liste_note[i][0] == eleve and liste_note[i][1] == matiere]
    moyenne = sum(notes)/len(notes)
    return moyenne
  else :
    notes = [ liste_note[i][2] for i in range(len(liste_note)) if liste_note[i][0] == eleve ]
    moyenne = sum(notes)/len(notes)
    return moyenne
 
#test
print("le résultat de la fonction : " , moyenne_tuples(notes,"eleve2","math"))


print("")
##########
class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve # eleve defini dans le init
    self.matiere = matiere
    self.valeur = valeur


  def afficher(self):
    print('eleve :', self.eleve, 'matiere :', self.matiere, 'note :', self.valeur)


onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)

print("")
##########

# Question 5)
eleve = [notes[i][0] for i in range(len(notes))]
print(eleve)

onotes = Note("eleve1", 'maths',13)
Note.afficher(onotes)