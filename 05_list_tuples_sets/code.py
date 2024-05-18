l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne") # tuplas não podem ser modificadas
s = {"Bob", "Rolf", "Anne"} # sets não permite valores duplicados

l[0] = "Smith"
l.append("Richard")
l.remove("Smith")

s.add("Smith")
print(s)

#----------------------------------------------------------------

my_tuple = 15, # indica uma tupla de valor único