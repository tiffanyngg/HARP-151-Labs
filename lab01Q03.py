edp = { "138A" : "TesserTheFlexer",
      "138B" : "KnitGurlKel",
      "138C" : "Moi",
      "138D" : "Kimiorawr",
      "113" : "CreepyCandy"
}

#removes the element with key-value 113 & prints the changed edp dictionary
edp.pop("113")
print(edp)
print()

#prints all items in edp dictionary
print(edp.items())
print()

#adds key-value to the end of the dictionary
edp.update({"138" : "O'Connor"})
print(edp)
print()

#clears the edp dictionary
edp.clear()
print(edp)

