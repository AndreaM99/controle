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

print("-- Question 4 c) --")
def moyenne_tuple(notes, eleve, matiere):
  notes_elv = [note for note in notes if note[0] == eleve]
  notes_elv_matiere = [n for n in notes_elv if n[1] == matiere]
  return sum([n[2] for n in notes_elv_matiere])/len(notes_elv_matiere)

print(moyenne_tuple(notes,'eleve1','math'))

def moyenne_tuplealt(notes, eleve = None, matiere = None):
  notes_elv = [note for note in notes if note[0] == eleve] if eleve is not None else notes
  notes_elv_matiere = [n for n in notes_elv if n[1] == matiere] if matiere is not None else notes_elv

  return sum([n[2] for n in notes_elv_matiere])/len(notes_elv_matiere)

print(moyenne_tuplealt(notes)) # moyenne totale
print(moyenne_tuplealt(notes, 'eleve1', 'math'))

print("-- Question 5 --")
class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur


  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)


onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)

onote.afficher()

onotes = [Note(a,b,c) for a,b,c in notes]
print(onotes) # c'est moche...
print('--')
for onote in onotes:
  print(onote) # toujours moche 

for onote in onotes:
  onote.afficher() # beaucoup plus jolie ! merci afficher() 

print("-- Question 6 --")
class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur


  def __str__(self):
    return f"{self.__class__.__name__}('{self.eleve}','{self.matiere}','{self.valeur}')"

onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
print(onote)

print("-- Question 7 --")
notes_enregistrees = []

class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur
    notes_enregistrees.append(self) 


  def __str__(self):
    return f"{self.__class__.__name__}('{self.eleve}','{self.matiere}','{self.valeur}')"

print(notes_enregistrees)
onote = Note('eleve1', 'math', 13)
print(onote)
print(notes_enregistrees)

print("-- Question 8 --")
def moyenne_notes(notes, eleve = None, matiere = None):
  notes_elv = [note for note in notes if note.eleve == eleve] if eleve is not None else notes
  notes_elv_matiere = [n for n in notes_elv if n.matiere == matiere] if matiere is not None else notes_elv

  return sum([n.valeur for n in notes_elv_matiere])/len(notes_elv_matiere)

onotes = [Note(a,b,c) for a,b,c in notes]
print(moyenne_notes(onotes))
print(moyenne_notes(onotes, 'eleve1', 'math'))

print("-- Question 9 --")
class Demo:
  classattr = 'defaut'
  def __init__(self, a):
    self.a = a


demo1 = Demo(1)
demo2 = Demo(2)

print(demo1.a)
print(demo2.a)
print(Demo.classattr)
print(demo1.classattr)
print(demo2.classattr)

Demo.classattr = 23

print(demo1.classattr)
print(demo2.classattr)

demo1.classattr = -1

print(Demo.classattr)
print(demo1.classattr)
print(demo2.classattr)

Demo.classattr = 14

print(Demo.classattr)
print(demo1.classattr) # aïe toujours -1 :(
print(demo2.classattr)

class Note:
  instances = []
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur
    
    self.instances.append(self) 

  def __str__(self):
    return f"{self.__class__.__name__}('{self.eleve}','{self.matiere}','{self.valeur}')"

  @classmethod #attention !
  def default_len(cls):
    return len(cls.instances)

print(Note.default_len()) # 0

onotes = [Note(a,b,c) for a,b,c in notes]

print(Note.default_len()) # 8 notes différentes