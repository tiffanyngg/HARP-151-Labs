list = ["apple", "chestnut", "gargoyle", "pandas", "sheep", "raptor"]
longest = 0
index = 0
for i in range(len(list)):
  characters = len(list[i])
  if characters > longest:
    longest = characters
    index = i
print("The longest word is:", list[index])
print("Number of characters:", longest)
