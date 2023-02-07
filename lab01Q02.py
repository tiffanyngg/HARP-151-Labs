import random
sowpods = "sowpods.txt"

#sourced from powerpoint slides 1/30
def word_generator():
  filename = sowpods
  f = open(filename, "r", encoding = "utf8")
  words = f.readlines()
  f.close
  return random.choice(words).strip().lower()

def main():
  #appends 7 words from sowpods.txt
  list = ["apple", "chestnut", "gargoyle", "pandas", "sheep", "raptor"]
  for i in range(7):
    list.append(word_generator())
  print(list)

  #find longest string in list
  longest = 0
  index = 0
  for i in range(len(list)):
    characters = len(list[i])
    if characters > longest:
      longest = characters
      index = i
  print()
  print("The longest word is:", list[index])
  print("Number of characters:", longest)
main()



