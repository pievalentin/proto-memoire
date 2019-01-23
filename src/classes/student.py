
from classes.personality import *
from classes.graph import *

class Student:
  def __init__ (self, name, new, gui):
    self.name = name
    self.gui = gui
    for widget in self.gui.winfo_children():
      widget.destroy()
    if(new == True):
      self.graph = Graph(self.name)
      self.graph.createStudentGraph()
      self.personality = Personality(self)
      perso_result = self.personality.calculatePersonality(gui)
      print(perso_result)

  def readPersonality (self,scores):
    for widget in self.gui.winfo_children():
      widget.destroy()
    print (scores)
    print('jaime la pizza')
  # def askName(self):
  #   for widget in gui.winfo_children():
  #     widget.destroy()

if __name__ == "__main__":
  print('lol')