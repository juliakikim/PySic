# PySic (Python + Music)
# Created by KyungIn Kim
# 03/09/2019 
# Run this in JEM (Jython Environment for Music)

from music import *



def sorts(x):
   if x == ('a'):
      return A4
   elif x == ('b'):
      return B4
   elif x == ('n'):
      return G4
   else:
      return C4
   
lists = ['b', 'a', 'n', 'a', 'n', 'a']

song = []
for i in range(len(lists)):
   n = sorts(lists[i])
   song.append(n)

phrase = Phrase(0,0)
for pitch in song:
   n = Note(pitch, HN)
   phrase.addNote(n)

Play.midi(phrase)
