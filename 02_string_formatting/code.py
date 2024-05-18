name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)



longer_pphrase = "Hello, {}.Today is {}"
formatted = longer_pphrase.format("Rolf", "Monday")
print(formatted)