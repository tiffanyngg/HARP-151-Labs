class Vocabulary:
  def __init__(self, inEnglish, inSpanish):
    self.inEnglish = inEnglish
    self.inSpanish = inSpanish

  def translateToEnglish(self,inSpanish):
    print(self.inEnglish)

  def translateToSpanish(self,inEnglish):
    print(self.inSpanish)
    
def main():
  vocab1 = Vocabulary("Hello", "Hola")
  vocab1.translateToEnglish("Hola")
  vocab1.translateToSpanish("Hello")
  
  vocab2 = Vocabulary("Good morning", "Buenos dias")
  vocab2.translateToEnglish("Buenos dias")
  vocab2.translateToSpanish("Good morning")

  vocab3 = Vocabulary("Good night", "Buenas noche")
  vocab3.translateToEnglish("Buenas noche")
  vocab3.translateToSpanish("Good night")
main()
  